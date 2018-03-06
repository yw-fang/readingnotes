########################################################
# This script is an example to show IO with json       #
# python version: v2.7                                 #
# Yue-Wen FANG at Kyoto University                     #
# Created in March 6th, 2018                           #
########################################################

from pprint import pprint
import json
#with open('ltc.json','w') as f:
#    json.dump({},f)
newdata={
        'name': 'ACEM',
        'shares': 100,
        'xyz': 'xyz',
        'pop': 10000
        }
print(type(newdata))
with open('ltc.json') as f:
    data = json.load(f)
print(type(data))
data.update(newdata)
with open('ltc.json','w') as f:
    json.dump(data,f)
    print(json.dumps(data, sort_keys=True, indent=4))
