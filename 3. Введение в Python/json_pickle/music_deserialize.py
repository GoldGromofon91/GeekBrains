import pickle
import json
import music_serialize

with open('group.pickle','rb') as f:
    bresult = pickle.load(f)
print(bresult)
print(type(bresult))
with open('group.json','r',encoding='utf-8') as fi:
    jresult = json.load(fi)
print(jresult)
print(type(jresult))