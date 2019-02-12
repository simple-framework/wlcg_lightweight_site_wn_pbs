from models.parameter_category import ParameterCategory

def get(data):
    category = ParameterCategory("wn_info_static", data)
    category.add_key_value("wn_list", "/root/wn-list.conf")
    return [category]