from models.parameter_category import ParameterCategory


def get(data):
    category = ParameterCategory("cream_info_static", data)
    category.add_key_value("wn_list", "/root/wn-list")
    category.add_key_value("users_conf", "/root/users_conf")
    category.add_key_value("ce_batch_sys", "pbs")
    category.add_key_value("ce_os", "ScientificCERNSLC")
    category.add_key_value("ce_os_release", "6.8")
    category.add_key_value("ce_os_version", "Carbon")
    category.add_key_value("ce_runtimeenv", "EMI-4")
    category.add_key_value("job_manager", "pbs")
    category.add_key_value("ce_batch_sys", "torque")
    category.add_key_value("batch_version", "2.5.13-1cri.9nik")

    return [category]
