from models.parameter_category import ParameterCategory

def get(data):
    category = ParameterCategory("wn_info_static", data)

    category.add_key_value("wn_list", "/root/wn-list.conf")
    category.add_key_value("users_conf", "/root/users.conf")
    category.add_key_value("groups_conf", "/root/groups.conf")
    category.add_key_value("vo_sw_dir", "/opt/exp_soft")
    return [category]