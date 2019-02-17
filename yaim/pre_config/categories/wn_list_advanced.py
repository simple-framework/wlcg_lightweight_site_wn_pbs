from models.parameter_category import ParameterCategory

def get(data):
    advanced_category = ParameterCategory("wn_list_advanced", data)
    dns_info = data['dns']
    hostnames = []
    for dns in dns_info:
        if dns['type'] == 'worker_node':
            hostnames.append(dns['hostname'])
            advanced_category.add(dns['hostname'] + "\n")
    return [advanced_category]