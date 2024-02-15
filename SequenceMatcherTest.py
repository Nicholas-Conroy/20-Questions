from difflib import SequenceMatcher

def similar (a, b):
    return SequenceMatcher(None, a, b).ratio()

a = [1,0,0,0,1]
b = [1,0,0,0,1]



result = similar(a,b)
print(result)