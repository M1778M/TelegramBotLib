info = """
for set data in folder data to file Group&Channels.json
"""

def SetData(data:dict,Type:str):
    if Type == 'w' or Type == 'write':
        ln = 0
        nd = {}
        for d in data.values():
            nd[ln+1] = d
            ln+=1
        with open('..\\data\\Group&Channels.json','w') as f:
            f.write(json.dumps(nd))
        
    elif Type == 'a' or Type == 'append':
        OldDt = ReadGOC()
        ln = len(OldDt)
        nd = OldDt
        for d in data.values():
            nd[ln+1] = d
        
        with open('..\\data\\Group&Channels.json','w') as f:
            f.write(json.dumps(nd))
        
def GetData():
    with open('..\\data\\Group&Channels.json','r') as f:
        d = f.read()
        
    ToJson = json.loads(json.dumps(json.loads(d)))
    return ToJson


