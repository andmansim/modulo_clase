from collections import defaultdict
from collections import OrderedDict
from collections import namedtuple

d = defaultdict(float)  
print(d['algo'])
print(d)

defaultdict(float, {'algo': 0.0})
d = defaultdict(str)  
print(d['algo'])
print(d)


n = OrderedDict()
n['uno'] = 'one'
n['dos'] = 'two'
n['tres'] = 'three'

print(n)
OrderedDict([('uno', 'one'), ('dos', 'two'), ('tres', 'three')])

n1 = {}
n1['uno'] = 'one'
n1['dos'] = 'two'

n2 = {}
n2['dos'] = 'two'
n2['uno'] = 'one'

print(n1 == n2)




Persona = namedtuple('Persona','nombre apellido edad')
p = Persona(nombre="Hector",apellido="Costa",edad=27)

print(p)
print(p.nombre)
print(p.edad)

print(p[0])
print(p[-1])
Persona(nombre='Hector', apellido='Costa', edad=27)
