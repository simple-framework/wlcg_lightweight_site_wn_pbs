from models.parameter_category import ParameterCategory

def get_component_section(data, id):
    return_value = None
    for component_section in data['lightweight_components']:
        if component_section['id'] is int(id):
            return_value = component_section
            break
    return return_value

def get(data, id):
    site_category = ParameterCategory("cream_info_queried", data)
    site_category.add_key_value_query("site_name", "$.site.name")
    site_category.add_key_value_query("site_email", "$.site.email")
    site_category.add_key_value_query("site_lat", "$.site.latitude")
    site_category.add_key_value_query("site_long", "$.site.latitude")
    site_category.add_key_value_query("site_desc", "$.site.description")
    site_category.add_key_value_query("site_loc", "$.site.location")
    site_category.add_key_value_query("site_web", "$.site.website")
    site_category.add_key_value_query("site_security_email", "$.site.security_email")
    site_category.add_key_value_query("site_support_email", "$.site.support_email")
    site_category.add_key_value_query("site_other_grid", "$.site.grid")
    site_category.add_key_value_query("bdii_host", "$.site.bdii_host")
    site_category.add_key_value_query("use_argus", "$.site.use_argus")

    component_section = get_component_section(data, id)
    component_category = ParameterCategory("cream_info_id_specific", component_section)
    component_category.add_key_value_query("ce_host", "$.deploy.node")
    component_category.add_key_value_query("ce_capability", "$.config.ce_capability")
    component_category.add_key_value_query("ce_cpu_model", "$.config.ce_cpu_model")
    component_category.add_key_value_query("ce_cpu_speed", "$.config.ce_cpu_speed")
    component_category.add_key_value_query("ce_cpu_vendor", "$.config.ce_cpu_vendor")
    component_category.add_key_value_query("ce_inboundip", "$.config.ce_inboundip")
    component_category.add_key_value_query("ce_logcpu", "$.config.ce_logcpu")
    component_category.add_key_value_query("ce_minphysmem", "$.config.ce_minphysmem")
    component_category.add_key_value_query("ce_minvirtmem", "$.config.ce_minvirtmem")
    component_category.add_key_value_query("ce_minvirtmem", "$.config.ce_minvirtmem")
    component_category.add_key_value_query("ce_os_arch", "$.config.ce_os_arch")
    component_category.add_key_value_query("ce_os_arch", "$.config.ce_os_arch")
    component_category.add_key_value_query("ce_otherdescr", "$.config.ce_otherdescr")
    component_category.add_key_value_query("ce_outboundip", "$.config.ce_outboundip") #caps
    component_category.add_key_value_query("ce_physcpu", "$.config.ce_physcpu")
    component_category.add_key_value_query("ce_rubtimeenv", "$.config.ce_physcpu")
    component_category.add_key_value_query("ce_sf00", "$.config.ce_sf00")
    component_category.add_key_value_query("ce_si00", "$.config.ce_si00")
    component_category.add_key_value_query("ce_smpsize", "$.config.ce_smpsize")
    component_category.add_key_value_query("batch_server", "$.deploy.node") #ce_host
    component_category.add_key_value_query("batch_log_dir", "$.config.batch_log_dir")
    component_category.add_key_value_query("blparser_with_updater_notifier", "$.config.blparser_with_updater_notifier")
    component_category.add_key_value_query("blparser_host", "$.deploy.node")
    component_category.add_key_value_query("cemon_host", "$.deploy.node")
    component_category.add_key_value_query("cream_db_user", "$.config.cream_db_user")
    component_category.add_key_value_query("cream_db_password", "$.config.cream_db_password")
    component_category.add_key_value_query("apel_mysql_host", "$.config.apel_mysql_host")
    component_category.add_key_value_query("apel_db_password", "$.config.apel_db_password")
    component_category.add_key_value_query("ce_close_se", "$.config.ce_close_se")
    component_category.add_key_value_query("ce_close_se3_access_point", "$.config.ce_close_se3_access_point") #additional
    component_category.add_key_value_query("ce_close_se3_host", "$.config.ce_close_se3_host") #additional
    component_category.add_key_value_query("se_list", "$.config.se_list") #list
    component_category.add_key_value_query("se_mount_info_list", "$.config.se_mount_info_list") #additional
    component_category.add_key_value_query("vo_sw_dir", "$.config.vo_sw_dir") #additional
    component_category.add_key_value_query("queues", "$.config.queues") #additional


    return [site_category, component_category]