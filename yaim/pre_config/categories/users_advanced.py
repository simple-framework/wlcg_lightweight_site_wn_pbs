from models.parameter_category import ParameterCategory
from helpers.generic_helpers import get_voms_config, evaluate, get_component_section

def get(data, id):
    advanced_category = ParameterCategory("users_advanced", data)
    component_section = get_component_section(data, id)
    voms_config = get_voms_config(data, component_section)
    unique_pool_accounts = []
    for config in voms_config:
        if 'comment' in config:
            flag = config['comment']
        else:
            flag = ''
        for pool_account in config['pool_accounts']:
            unique = True
            for existing_pool_account in unique_pool_accounts:
                if existing_pool_account['pool_account']['initial_uid'] == pool_account['initial_uid']:
                    unique = False
                    break
            if unique:
                unique_pool_accounts.append({
                    'vo': config['vo'],
                    'pool_account': pool_account,
                    'flag': flag
                })

    for pool_account_info in unique_pool_accounts:
        pool_account = pool_account_info['pool_account']
        base_name = pool_account['base_name']
        initial_uid = pool_account['initial_uid']
        users_num = pool_account['users_num']

        primary_group = pool_account['primary_group']
        gid1 = primary_group['gid']
        primary_group_name = primary_group['name']

        vo = pool_account_info['vo']['name']
        flag = pool_account_info['flag']
        for user_num in list(range(0, users_num)):
            uid = initial_uid + user_num
            login_name = base_name + str(user_num + 1).zfill(3)
            user_entry = "{uid}:{login_name}:{gid1}".format(uid = uid, login_name = login_name, gid1 = gid1)
            if "secondary_groups" in pool_account and len(pool_account['secondary_groups']) >0:

                for secondary_group in pool_account['secondary_groups']:
                    user_entry += ",{gid}".format(gid = secondary_group['gid'])
                user_entry += ":{primary_group_name}".format(primary_group_name =primary_group_name)
                for secondary_group in pool_account['secondary_groups']:
                    user_entry += ",{group_name}".format(group_name=secondary_group['name'])
                user_entry += ":"
                user_entry += "{vo}:{flag}:".format(vo =vo, flag = flag)
            else:
                user_entry = "{uid}:{login_name}:{gid1}:{GROUP1}:{vo}:{flag}:".format(uid=uid, login_name=login_name, gid1=gid1, GROUP1 = primary_group_name, vo = vo, flag = flag)

            advanced_category.add(user_entry + "\n")

    return [advanced_category]