from models.parameter_category import ParameterCategory
from helpers.generic_helpers import get_voms_config, evaluate, get_component_section

def get(data, id):
    advanced_category = ParameterCategory("users_advanced", data)
    component_section = get_component_section(data, id)
    voms_config = get_voms_config(data, component_section)
    for config in voms_config:
        voms_fqan = config['voms_fqan']
        flag = config['comment'] if 'comment' in config else ''
        groups_string = "\"{voms_fqan}\":::{flag}:".format(voms_fqan=voms_fqan, flag=flag)
        advanced_category.add(groups_string + "\n")
    return [advanced_category]