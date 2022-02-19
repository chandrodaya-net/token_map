import json 
import config

def get_juno_ibc_token():
    f = open(config.JUNO['source_ibc_token_file'])
    return json.load(f)['tokens']


def get_juno_cw20_token():
    f = open(config.JUNO['source_cw20_token_file'])
    cw20 =[t for t in json.load(f)['tokens'] if "cw20" in t['tags'] ]
    return cw20 

def pretty_print(parsed_json):
    """ pretty_print(get_junot_token()[0])
    """
    print(json.dumps(parsed_json, indent=4, sort_keys=True))
    
def transform_json():
    source_target_map = config.JUNO['source_target_map']
    source_target_cw20_map = config.JUNO['source_target_cw20_map']          
    token_image_path_map = config.JUNO['token_image_path_map']
    chain_source_map = config.JUNO['chain_source_map']
    juno_token_json = config.JUNO['juno_token_json']
    result_json = []
    
    # IBC token
    for token_json in get_juno_ibc_token():
        new_token_json = {}
        for key in source_target_map:
            new_key = source_target_map[key]
            value = token_json[key]
            if key == 'decimals':
                value =  float("1e-{}".format(token_json[key]))
            new_token_json[new_key] = value
        token_image_path = token_image_path_map.get(token_json['id'], 'None')
        new_token_json['icon'] = token_image_path
        new_token_json['sourceChain'] = chain_source_map.get(token_json['id'], 'None')
        new_token_json['type'] = 'IBC'
        result_json.append(new_token_json)
        
    # cw token
    for cw_token_json in get_juno_cw20_token():
        new_token_json = {}
        for key in source_target_cw20_map:
            new_key = source_target_cw20_map[key]
            value = cw_token_json[key]
            if key == 'decimals':
                value =  float("1e-{}".format(cw_token_json[key]))
            new_token_json[new_key] = value
        token_image_path = token_image_path_map.get(cw_token_json['denom'], 'None')
        new_token_json['icon'] = token_image_path
        new_token_json['sourceChain'] = 'juno'
        new_token_json['type'] = 'CW20'
        result_json.append(new_token_json)

    result_json.append(juno_token_json)
    return sorted(result_json, key = lambda i: (i['type'], i['id']))
 
def dump_transform_json():
    result_json = transform_json()
    with open(config.JUNO['target_token_file'], 'w', encoding='utf-8') as f:
        json.dump(result_json, f, ensure_ascii=False, indent=4, sort_keys=True)
        
    
if __name__ == "__main__":
    # pretty_print(get_juno_ibc_token())
    # pretty_print(transform_json())
    dump_transform_json()
    # pretty_print(get_juno_cw20_token())
    



