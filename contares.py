from collections import Counter
l = [1, 1, 2, 3, 3, 2, 2]
c = Counter(l)
print(c)
Counter({1:4, 2:2, 3:1 })
Counter('palabras')
Counter({'a': 3, 'r' : 2, 's': 1, 'p': 1, })
c = Counter('palabras')
print(c)
animales = 'gato perro canario perro canario perro'
Counter(animales.split())
Counter({'gato': 3, 'perro': 2, 'canario':1})


animales = 'gato perro canario perro canario perro'
Counter(animales.split())
print(c.most_common(1))
print(c.most_common(2))
print(c.most_common())

[('perro', 3)]
[('perro', 3), ('canario', 2)]
[('perro', 3), ('canario', 2), ('gato', 1)]
l = [10,20,30,40,10,20,30,10,20,10]
c = Counter(l)

print(c.items())        
print(c.keys())         
print(c.values())       

print(sum(c.values()))  

print(list(c))          
print(dict(c))          
print(set(c))           
#dict_items([(40, 1), (10, 4), (20, 3), (30, 2)])
#dict_keys([40, 10, 20, 30])
#dict_values([1, 4, 3, 2])



