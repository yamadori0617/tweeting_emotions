# -*- coding: utf-8 -*-
import json

PATH = 'wago.121808.pn'
with open(PATH, encoding="UTF-8") as fd:
    wago_dict = {}
    for line in fd:
        try:
            polarity, word = line.rstrip().split('\t')
            word = word.replace(' だ', '').replace(' と', '').replace(' の', '').replace(' です', '')
            if word.endswith(' ある') or word.endswith(' あり') or word.endswith(' ない') or word.endswith(' なし'):
                continue
        except:
            continue
        wago_dict[word] = polarity
json.dump(wago_dict, open('pn_wago.json', 'w'))
