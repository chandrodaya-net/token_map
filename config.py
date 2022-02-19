JUNO = {
    'source_ibc_token_file': "/home/dau/workspace/network/juno/junoswap-asset-list/ibc_assets.json",
    'source_cw20_token_file': "/home/dau/workspace/network/juno/junoswap-asset-list/token_list.json",
    'target_token_file': "/home/dau/workspace/chandrodaya-net/token_map/target/juno.json",
    'juno_token_json': {
      'id': 'juno',
      "sourceChainId": "juno-1",
      "sourceChain": "juno",
      'chainDenom': 'ujuno',
      'chainToViewConversionFactor': 1e-6,
      'viewDenom': 'JUNO',
      'type': 'STAKE',
      'icon': "coins/tokens/token-juno.svg",
    },
    'source_target_map' : {
                    'id': 'id',
                    'symbol' : 'viewDenom',
                     'juno_denom' : 'chainDenom', 
                     'decimals' :  'chainToViewConversionFactor',
                     'chain_id' :  'sourceChainId'
         },
    
    'source_target_cw20_map' : {
                    'token_address': 'id',
                    'symbol' : 'viewDenom',
                    'denom' : 'chainDenom', 
                    'decimals' :  'chainToViewConversionFactor',
                    'chain_id' :  'sourceChainId'
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
                     'dig': 'dig',
                     'secret': 'secret',
                     'bitcanna': 'bitcanna'
                     
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
            'bitcanna' : 'coins/ibc/ibc-bcna.png',
            'secret': 'coins/ibc/ibc-scrt.png',
            'neta': "coins/juno/cw20/neta.svg",
            'canlab': "coins/juno/cw20/custom/cannalabs.png",
            'tuck':  "coins/juno/cw20/custom/tuckermint.png",
            'hulc': "coins/juno/cw20/hulcat.png",  
        }
      
    }