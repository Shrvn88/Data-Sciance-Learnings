book = {}

book['john'] = {
    'name' : 'john',
    'address' : '1 red street, NY',
    'phone' : 48484848
}
book['tom'] = {
    'name' : 'tom',
    'address' : '19 blue street, NY',
    'phone' : 98989898
}

import json

s = json.dumps(book)

with open("D://Dec'24//DSCourse//data//book.txt","w") as f:
    f.write(s)
    
    
    
with open("D://Dec'24//DSCourse//data//book.txt","r") as f:
    d = f.read()
    
    d = json.loads(d)
    
print(d['tom']['phone'])