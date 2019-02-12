from models.parameter_category import ParameterCategory

import yaql


engine = yaql.YaqlFactory().create()


def evaluate(data, query):
    expression = engine(query)
    return expression.evaluate(data)

def get_component_section(data, id):
    for component in data['lightweight_components']:
        if component['id'] is int(id):
            return component

def get_yaml_sections(data, id):
    sections = {}
    site_section = "$.site"
    return sections

def globus_tcp_port_range(component_section):
    return "ram gopal verma ki aag"

def vos(component_section, data):
    result = ""
    vos = evaluate(data, "$.supported_virtual_organizations")
    print(vos)
    return "yolo"

def get(data, id):
    component_section = get_component_section(data, id)
    advanced_category = ParameterCategory("cream_info_advanced", data)
    advanced_category.add_key_value("globus_tcp_port_range", globus_tcp_port_range(component_section))
    advanced_category.add_key_value("vos", vos(component_section, data)) #additional
    return [advanced_category]