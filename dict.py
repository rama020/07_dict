'''
DATE:30TH NOV 2022
DAY: WEDNESDAY
TOPIC: DICTIONARY
AUTHOR: RAMA BHARGAVI
'''
foods={1:'magie',2:'pasta',3:'panipuri',4:'fied rice'}
print(foods[2])
#print(foods[5])
h={}
print(type(h))
f={1:'good',2:'bad',3:7,4:6.2,5:[1,4],6:(4,3)}
print(f.keys())
print(f.values())
print(f.items())
f.clear()
print(f)
b=[10,20,30,40,50,60]
print(dict.fromkeys(b,25))
c={1:"",2:"kiran",3:7,4:5.2}
print(c.get(3))
print(c.get(2))
c.pop(4)
print(c)
c.popitem()
print(c)
k={1:"",2:"pooja",3:5,4:3.2}
k.update({3:"kiran"})
print(k)
k.update({6:"bhargavi"})
print(k)
l={1:'rama',2:'pooja',3:5,4:5.2}
l.setdefault(4,'sravani')
print(l)
l.setdefault(5,'sravani')
print(l)

