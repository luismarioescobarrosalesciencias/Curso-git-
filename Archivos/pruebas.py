import time
print("Probando merge Union ")
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


def palindromo(cadenas):
    for i, c in enumerate(cadenas):
        cadena_min = c.lower().replace(' ', '')
        if cadena_min == cadena_min[::-1]:
            return i

def conjunto(lista):
    return set(lista)

def duplicados(nums):
    set1=set()
    for i in range(0,len(nums)):
        if nums[i] not in set1:
            set1.add(nums[i])
        else:
            return False
    return True


def anagrama_valido(t,s):
    if len(s)!=len(t):
                return False
    dic={}
    for i in range(0,len(s)):
        if s[i]  in dic:
            dic[s[i]]+=1

        else:
            dic[s[i]]=1

    for st  in t:
        if st not in dic:
            return False
        else:
            dic[st]-=1

    for key in dic:
        if dic[key]!=0:
            return False
    return True

print("Pruebas stage")

cadenas = ['Hola como estas',
           'Lista de cadenas',
           'Anita lava la tina',
           'AJDSHFGDSHF']
palindromo(cadenas)

print("prueba merge fast-forward")
print ("stages ")
