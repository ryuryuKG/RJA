import re
import json
import sys

json_open = open('catalog.json', 'r')
json_load = json.load(json_open)

l=[ v['price'] for v in json_load if re.match("jacket",v['name'])]

print(max(l))
print(min(l))
print(len(l))


# count=0
# max=0
# min=sys.maxsize
# json_open = open('catalog.json', 'r')
# json_load = json.load(json_open)
# for v in json_load:
#     if re.match("jacket",v['name']):
#         count=count+1
#         if min > v['price']:
#             min=v['price']
#         if max<v['price']:
#             max=v['price']
# print(count)
# print(min)
# print(max)
