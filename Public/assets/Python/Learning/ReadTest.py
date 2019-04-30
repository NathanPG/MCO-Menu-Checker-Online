# -*- coding:utf-8 -*-
import json

with open("read_json.json", 'r') as f:
  temp = json.loads(f.read())
  print(temp)
  print(temp['rule'])
  print(temp['rule']['namespace'])

test_dict = {'bigberg': [7600, {1: [['iPhone', 6300], ['Bike', 800], ['shirt', 300]]}]}
print(test_dict)
print(type(test_dict))
json_str = json.dumps(test_dict)
print(json_str)
print(type(json_str))

 new_dict = json.loads(json_str)
 print(new_dict)
 print(type(new_dict))

 with open("test.json","w") as f:
   json.dump(new_dict,f)
   print("write complete!")
   
with open("test.json",'r') as load_f:
  load_dict = json.load(load_f)
  print(load_dict)
load_dict['smallberg'] = [8200,{1:[['Python',81],['shirt',300]]}]
print(load_dict)

with open("test.json","w") as dump_f:
  json.dump(load_dict,dump_f)