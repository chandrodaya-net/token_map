import json 
import config





def get_juno_token():
    f = open(config.JUNO['source_token_file'])
    return json.load(f)['tokens']


def pretty_print(parsed_json):
    """ pretty_print(get_junot_token()[0])
    """
    print(json.dumps(parsed_json, indent=4, sort_keys=True))
    
def transform_json():
    source_target_map = config.JUNO['source_target_map']
    token_image_path_map = config.JUNO['token_image_path_map']
    chain_source_map = config.JUNO['chain_source_map']
    result_json = []
    for token_json in get_juno_token():
        new_token_json = {}
        for key in source_target_map:
            new_key = source_target_map[key]
            value = token_json[key]
            if key == 'decimals':
                value = "1e-{}".format(token_json[key])
            new_token_json[new_key] = value
        token_image_path = token_image_path_map.get(token_json['id'], 'None')
        new_token_json['icon'] = token_image_path
        new_token_json['chainSource'] = chain_source_map.get(token_json['id'], 'None')
        result_json.append(new_token_json)
    
    return sorted(result_json, key = lambda i: i['id'])
 
def dump_transform_json():
    result_json = transform_json()
    with open(config.JUNO['target_token_file'], 'w', encoding='utf-8') as f:
        json.dump(result_json, f, ensure_ascii=False, indent=4, sort_keys=True)
        
    
if __name__ == "__main__":
    # pretty_print(get_juno_token())
    pretty_print(transform_json())
    # dump_transform_json()
    



