import time

f = [1, 2, 5, 4, 7, 5, 3,9,10,12,17,2,1]

start = time.time()
d = [i**2 for i in f if i % 2] #
print('Segundo: ', time.time() - start)

dic = {
    'uno': 12,
    'dos': 2.0,
     3: 543,
    'cuatro': 'ads',
     4: 'asdf'
    }

keys = ['uno', 'dos', 'cuatro']
new = {k: dic[k] for k in keys}
print(new)
print("hola")
