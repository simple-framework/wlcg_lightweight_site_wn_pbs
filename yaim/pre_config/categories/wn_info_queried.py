from models.parameter_category import ParameterCategory
from helpers.generic_helpers import get_component_section

def get(data, execution_id):
    category = ParameterCategory("wn_info_queried", data)
    category.add_key_value_query("site_name", "$.site.name")
    category.add_key_value_query("site_email", "$.site.email")
    category.add_key_value_query("bdii_host", "$.site.bdii_host")

    component_section = get_component_section(data, execution_id)
    component_category = ParameterCategory("wn_info_component_queried", component_section)
    component_category.add_key_value_query("px_host", "$.config.px_host")
    component_category.add_key_value_query("ce_host", "$.config.ce_host")
    component_category.add_key_value_query("ce_smpsize", "$.config.ce_smpsize")
    component_category.add_key_value_query("batch_server", "$.config.batch_server")
    component_category.add_key_value_query("ce_close_se", "$.config.ce_close_se")
    component_category.add_key_value_query("ce_close_se3_access_point", "$.config.ce_close_se3_access_point")
    component_category.add_key_value_query("ce_close_se3_host", "$.config.ce_close_se3_host")
    component_category.add_key_value_query("se_list", "$.config.se_list")
    component_category.add_key_value_query("se_mount_info_list", "$.config.se_mount_info_list")

    return [category, component_category]
