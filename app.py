"""
#Introdução às Generator functions
#generator = (n for n in range(100))
def generator(n=0):
    yield 1 #Pausar
    print('Continuando...')
    yield 2
    print('Mais uma ...')
    yield 3
    return "CABO"

#gen = generator(n=0)
def generator2(n=0, maximum=1):
    while True:
        yield n
        n+=1
        if n >= maximum:
            return
gen = generator2(maximum=10)
for n in gen:
    print(n)
"""

""""""
#Yiel from em generator functions
def gen1():
    yield 1
    yield 2
    yield 3
    yield 4
    print('Fim gen1')
def gen3():
    yield 8
    yield 9
    yield 0
    print('Fim gen3')
def gen2(gen):
    yield from gen()
    yield 5
    yield 6
    yield 7
    print('Fim gen2')

g1 = gen2(gen1)
g2 = gen2(gen3)
for numero in g1:
    print(numero)
for numero in g2:
    print(numero)