from models.parameter_category import ParameterCategory
from helpers.generic_helpers import get_voms_config, evaluate, get_component_section

def append_vo_data(advanced_category, component_section, data):
    try:
        supported_vos = component_section['config']['vos']
    except KeyError:
        supported_vos = evaluate(data, "$.supported_virtual_organizations")

    vos = []
    for vo in supported_vos:
        vo_name = vo['name']
        vo_name_split = vo_name.split('.')
        vo_name_param = vo_name
        if len(vo_name_split) > 0:
            vo_name_param = '_'.join(vo_name_split)

        vos.append(vo_name)
        voms_servers = []
        vomses = []
        ca_dns = []
        for server in vo['servers']:
            voms_servers.append("'vomss://" + server['server'] + ":8443" + "/voms/" + vo_name + "?/" + vo_name + "'")
            vomses.append("{vo_name} {server} {port} \ \n{dn} {vo_name} 24".format(vo_name=vo_name, server=server['server'], port=server['port'], dn=server['dn']))
            ca_dns.append("{ca_dn}".format(ca_dn=server['ca_dn']))
        advanced_category.add_key_value("vo_" + vo_name_param + "_default_se", vo['default_se'])
        advanced_category.add_key_value("vo_" + vo_name_param + "_sw_dir", vo['sw_dir'])
        advanced_category.add_key_value("vo_" + vo_name_param + "_storage_dir", vo['storage_dir'])
        advanced_category.add_key_value("vo_" + vo_name_param + "_voms_servers",
                                        "\\ \n{0} \\ \n".format(" \\ \n".join(voms_servers)))
        advanced_category.add_key_value("vo_" + vo_name_param + "_vomses", "\\ \n{0} \\ \n".format(" \\ \n".join(vomses)))
        advanced_category.add_key_value("vo_" + vo_name_param + "_voms_ca_dn", "\\ \n{0} \\ \n".format(" \\ \n".join(ca_dns)))
    advanced_category.add_key_value("vos", ' '.join(vos))
    return advanced_category


def append_queue_info(advanced_category, component_section, data):
    #check if user defined queues in repo_config. If not, check if user defined voms_config section. If not, create a default voms_config section for each supported vo.
    queues = {}
    try:
        queues = component_section['config']['queues']
    except KeyError:
        voms_config = get_voms_config(data, component_section)
        #generate queues from voms_config
        for config in voms_config:
            key = config['vo']['name']
            if key in queues:
                queues[key].append(config)
            else:
                queues[key] = [config]

    for queue in queues:
        voms_configs = queues[queue]
        groups_enable_key = "{queue}_group_enable".format(queue = queue)
        groups_enable_value = [queue] #MUST BE VO NAME
        for voms_config in voms_configs:
            groups_enable_value.append(voms_config['voms_fqan'])
        advanced_category.add_key_value(groups_enable_key, ' '.join(groups_enable_value))

    return advanced_category


def get(data, id):
    component_section = get_component_section(data, id)
    advanced_category = ParameterCategory("wn_info_advanced", data)
    advanced_category = append_vo_data(advanced_category,component_section, data)
    advanced_category = append_queue_info(advanced_category, component_section, data)
    return [advanced_category]
