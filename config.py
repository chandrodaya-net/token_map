JUNO = {
    'source_token_file': "/home/dau/workspace/network/juno/junoswap-asset-list/ibc_assets.json",
    'target_token_file': "/home/dau/workspace/dauTT/token_map/target/juno.json",
    'source_target_map' : {
                    'id': 'id',
                    'symbol' : 'viewDenom',
                     'juno_denom' : 'chainDenom', 
                     'decimals' :  'chainToViewConversionFactor',
                     'chain_id' :  'chainIdSource'
         },
    'chain_source_map' : {
                    'cosmos': 'cosmos',
                    'terra-luna' : 'terra',
                     'terrausd' : 'terra', 
                     'bitsong' :  'bitsong',
                     'osmosis' :  'osmosis',
                     'stargaze' : 'stargaze',
                     'chihuahua-token': 'chihuahua',
                     'akash-network': 'akash',
                     'persistence' : 'persistence',
                     'comdex': 'comdex',
                     'dig': 'dig'
                     
         },
    'token_image_path_map' : {
            'cosmos': 'coins/ibc/ibc-atom.png',
            'terra-luna': 'coins/ibc/ibc-luna.png',
            'terrausd': 'coins/ibc/ibc-ust.png',
            'bitsong': 'coins/ibc/ibc-btsg.png',
            'osmosis': 'coins/ibc/ibc-osmo.png',
            'stargaze': 'coins/ibc/ibc-stars.png',
            'chihuahua-token': 'coins/ibc/ibc-huahua.png',
            'akash-network': 'coins/ibc/ibc-akt.png',
            'persistence': 'coins/ibc/ibc-xprt.png',
            'comdex': 'coins/ibc/ibc-cmdx.png',
            'dig': 'coins/ibc/ibc-dig.png',
        }
      
    }