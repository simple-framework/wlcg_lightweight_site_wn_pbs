from models.parameter_category import ParameterCategory

def get(data, execution_id):
    category = ParameterCategory("wn_info_queried", data)
    category.add_key_value_query("site_name", "$.site.name")
    return [category]
