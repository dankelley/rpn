import json
with open('dan3.json', 'r') as file:
    d = json.load(file)
print(d)
#print(f'g:{d["_g"]}, _h:{d["_h"]}')
g = d["_g"]
print(g)
h = d["_h"]
print(h)
try:
    nothing = d["_nothing"]
except:
    print("_nothing not in dictionary")
