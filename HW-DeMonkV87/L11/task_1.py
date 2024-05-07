from sigmoid_check.python_odyssey.lesson_11.lesson_11 import Lesson11

# Această temă pentru acasă necesită instalarea librăriei `sigmoid_check` cu versiunea cel puțin 0.0.4
# Pentru a instala această librărie, rulați următorul cod în terminal:
# pip install sigmoid_check==0.0.4

# VERIFICATION PROCESS
session = Lesson11()
# VERIFICATION PROCESS

"""
Task: Creați o funcție cu numele `task_1` care poate primi un număr variabil de argumente și returnează suma acestora.
Exemplu: task_1(1, 2, 3) ➞ 6
"""

# CODUL TĂU VINE MAI JOS:
def task_1(*n):
    suma = 0
    for i in n:
        suma += i
    return (suma)
# CODUL TĂU VINE MAI SUS:

# VERIFICATION PROCESS
print(session.check_task_1(task_1))
# VERIFICATION PROCESS


"""
Task: Creați o funcție cu numele `task_2` care primește un număr variabil de argumente și returnează o listă cu argumentele care sunt numere întregi.
Exemplu: task_2(1, 2, 'a', 'b') ➞ [1, 2]
"""

# CODUL TĂU VINE MAI JOS:
def task_2(*n):
    return [i for i in n if isinstance(i,int)]
print(task_2(1, 2, 'a', 'b','8')) #nu returneaza valorile de genu '8'
# CODUL TĂU VINE MAI SUS:

# VERIFICATION PROCESS
print(session.check_task_2(task_2))
# VERIFICATION PROCESS

"""
Task: Creați o funcție cu numele `task_3` care poate primi un număr variabil de argumente și va returna produsul acesora.
Exemplu: task_3(1, 4, 5) ➞ 20
"""

# CODUL TĂU VINE MAI JOS:
def task_3(*n):
    produsul = 1
    for i in n:
        produsul *= i
    return (produsul)
print(task_3(1, 0, 5))
# CODUL TĂU VINE MAI SUS:

# VERIFICATION PROCESS
print(session.check_task_3(task_3))
# VERIFICATION PROCESS

"""
Task: Creați o funcție cu numele `task_4` care primește un număr arbitrar de perechi cheie-valoare și returnează un string care conține toate cheile și valorile concatenate separate de un spațiu.
Exemplu: task_4(a=1, b=2, c=3) ➞ 'a 1 b 2 c 3'
"""

# CODUL TĂU VINE MAI JOS:
def task_4(**n):
    rezultat = ""
    for key, value in n.items():
        rezultat += f"{key} {value} "
    return rezultat.strip()
print(task_4(a=1, b=2, c=3))
# CODUL TĂU VINE MAI SUS:

# VERIFICATION PROCESS
print(session.check_task_4(task_4))
# VERIFICATION PROCESS

"""
Task: Creați o funcție cu numele `task_5` care primește un număr variabil de argumente și returnează două liste separate.
Prima listă conține toate argumentele de tip întreg sortate în ordine crescătoare, iar a doua listă conține denumirea tuturor argumentelor keyword care sunt de tip string sortate în ordine alfabetică.
Exemplu: task_5(3, 1, 2, a=10, b=20) ➞ [1, 2, 3], []
Exemplu: task_5(3, 1, 2, a=10, b=20, c='a') ➞ [1, 2, 3], ['c']
Exemplu: task_5(3, 1, 2, a=10, b=20, c='a', d='b') ➞ [1, 2, 3], ['c', 'd']
"""

# CODUL TĂU VINE MAI JOS:
def task_5(*n, **m):
    integer=sorted(i for i in n if isinstance(i, int))
    string=sorted(i for i in m.keys() if isinstance(m[i], str))
    # for i in n:
    #     if isinstance(i, int):
    #         integer.append(i)
    # for k in m.keys():
    #     if isinstance(k, str):
    #         string.append(k)
    return integer , string
print(task_5(3, 1, 2, a=10, b=20, c='a', d='b'))
# CODUL TĂU VINE MAI SUS:

# VERIFICATION PROCESS
print(session.check_task_5(task_5))
# VERIFICATION PROCESS

"""
Task: Creați o funcție cu numele `task_6` care primește un număr variabil de argumente și returnează un dicționar care conține toate argumentele keyword ca key și valoarea acestora ca value.
Exemplu: task_6(a=1, b=2, c=3) ➞ {'a': 1, 'b': 2, 'c': 3}
"""

# CODUL TĂU VINE MAI JOS:
def task_6(**n):
    rezultat = {}
    for key, value in n.items():
        rezultat [key] = value
    return rezultat
print(task_6(a=1, b=2, c=3))
# CODUL TĂU VINE MAI SUS:

# VERIFICATION PROCESS
print(session.check_task_6(task_6))
# VERIFICATION PROCESS

"""
Task: Creați o funcție cu numele `task_7` care poate primi un număr nedeterminat de argumente atât string-uri cât și numere și va returna un dicționar cu două chei: `str` și `int`.
Cheia `str` va avea o listă cu toate string-urile primite ca argumente, iar cheia `int` va avea o listă cu toate numerele primite ca argumente.
Exemplu: task_7(1, 'a', 2, 'b') ➞ {'str': ['a', 'b'], 'int': [1, 2]}
"""

# CODUL TĂU VINE MAI JOS:
def task_7(*n):
    Valori_int = [i for i in n if isinstance(i,int)]
    Valori_str = [i for i in n if isinstance(i,str)]
    return {'str':Valori_str, 'int':Valori_int}

print(task_7(1, 'a', 2, 'b'))

# CODUL TĂU VINE MAI SUS:

# VERIFICATION PROCESS
print(session.check_task_7(task_7))
# VERIFICATION PROCESS

"""
Task: Creați o funcție cu numele `task_8` care primește un număr variabil de argumente și returnează un dicționar cu două chei: `palindrom` și `non_palindrom`.
Cheia `palindrom` va avea o listă cu toate argumentele care sunt palindroame, iar cheia `non_palindrom` va avea o listă cu toate argumentele care nu sunt palindroame.
Exemplu: task_8('madam', 'hello', 'level', 'world') ➞ {'palindrom': ['madam', 'level'], 'non_palindrom': ['hello', 'world']}
"""

# CODUL TĂU VINE MAI JOS:
def task_8(*n):
    palindrom = []
    non_palindrom = []
    for i in n:
        if i == i[::-1]:
            palindrom.append(i)
        else:
            non_palindrom.append(i)
    return {'palindrom':palindrom, 'non_palindrom':non_palindrom}

print(task_8('madam', 'hello', 'level', 'world'))
# CODUL TĂU VINE MAI SUS:

# VERIFICATION PROCESS
print(session.check_task_8(task_8))
# VERIFICATION PROCESS

"""
Task: Creați o funcție cu numele `task_9` care primește un număr variabil de argumente de tip integer și un argument `number` de tip integer.
Funcția va returna toate argumentele care sunt multipli ai lui `number`.
Exemplu: task_9(1, 2, 3, 4, 5, number=2) ➞ [2, 4]
"""

# CODUL TĂU VINE MAI JOS:
def task_9(*n, number = None):
    lista_multipli = [] 
    for i in n:
        if number is not None and i % number == 0:
            lista_multipli.append(i)
    return lista_multipli
print(task_9(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, number=2))
# CODUL TĂU VINE MAI SUS:

# VERIFICATION PROCESS
print(session.check_task_9(task_9))
# VERIFICATION PROCESS

"""
Task: Creați o funcție cu numele `task_10` care primește un număr variabil de argumente de tip integer și un argument `number` de tip integer.
Funcția va returna toate argumentele care sunt divizibile cu `number`.
Exemplu: task_10(1, 2, 3, 4, 5, number=2) ➞ [2, 4]
"""

# CODUL TĂU VINE MAI JOS:
def task_10(*n, number = None):
    lista_div = []
    for i in n:
        if number is not None and number % i == 0:
            lista_div.append(i)
    return lista_div
print(task_10(1, 2, 3, 4, 5, 6, 7, 8, number=4))
# CODUL TĂU VINE MAI SUS:

# VERIFICATION PROCESS
print(session.check_task_10(task_10))
# VERIFICATION PROCESS

"""
Task: Creați o funcție cu numele `task_11` care primește un număr variabil de argumente de tip integer care reprezintă șirul Fibonacci.
Funcția va returna valoarea True dacă șirul Fibonacci este corect și False în caz contrar.
Exemplu: task_11(1, 1, 2, 3, 5, 8) ➞ True
Exemplu: task_11(1, 1, 2, 3, 5, 9) ➞ False
"""

# CODUL TĂU VINE MAI JOS:
def task_11(*n): # n trebuie sa se inceapa cu 0 nu cu 1 !!!
    fibonacci = [0, 1] # aici trebuie sa sie al doilea si al treilea numar din sirul fibonacci - adica [1,1]
    while len(fibonacci) < len(n):
         fibonacci.append(fibonacci[-1] + fibonacci[-2])
    return list(n) == fibonacci[:len(n)]

print(task_11(0, 1, 1, 2, 3, 5, 8)) # se genereaza insa nu se i-a in calcul la %
# CODUL TĂU VINE MAI SUS:

# VERIFICATION PROCESS
print(session.check_task_11(task_11))
# VERIFICATION PROCESS

"""
Task: Creați o funcție cu numele `task_12` care primește un număr variabil de argumente de tip integer.
Funcția va returna True dacă toate argumentele sunt numere prime și False în caz contrar.
Exemplu: task_12(2, 3, 5, 7) ➞ True
Exemplu: task_12(1, 2, 3, 4) ➞ False
"""

# CODUL TĂU VINE MAI JOS:
def task_12(*n):
    for i in n:
        if i<=1:
            return False
    for num in n:
        for i in range(2,int(num**0.5)+1):
            if num%i == 0:
                return False
    else:
        return True

print(task_12(2, 3, 5, 7))
# CODUL TĂU VINE MAI SUS:

# VERIFICATION PROCESS
print(session.check_task_12(task_12))
# VERIFICATION PROCESS

"""
Task: Creați o funcție cu numele `task_13` care primește obligatoriu un argument de tip string și un număr variabil de argumente de tip string.
Funcția va returna True dacă toate argumentele sunt anagrame și False în caz contrar.
Exemplu: task_13('listen', 'silent') ➞ True
Exemplu: task_13('hello', 'world') ➞ False
"""

# CODUL TĂU VINE MAI JOS:
def task_13(a,*n):
    cuvint_comparatie = sorted(a)
    for i in n:
        litere_comparatie = sorted(i)
        if litere_comparatie == cuvint_comparatie:
            return True
    return False
print(task_13('listen', 'silent', 'hello', 'world'))
# CODUL TĂU VINE MAI SUS:

# VERIFICATION PROCESS
print(session.check_task_13(task_13))
# VERIFICATION PROCESS

"""
Task: Creați o funcție cu numele `task_14` care primește un argument `sub_string` de tip string și un număr variabil de argumente de tip string.
Funcția va returna o listă cu toate argumentele care conțin `sub_string`.
Exemplu: task_14('home', 'same', 'meme', sub_string="me") ➞ ['home', 'meme', 'same']
"""

# CODUL TĂU VINE MAI JOS:
def task_14(*n, sub_string="me"):
    raspuns = []
    if sub_string == "me":
        for i in n:
            if sub_string in i:
                raspuns.append(i)
    return raspuns
print(task_14('home', 'same', 'meme', sub_string="me"))
# CODUL TĂU VINE MAI SUS:

# VERIFICATION PROCESS
print(session.check_task_14(task_14))
# VERIFICATION PROCESS

"""
Task: Creați o funcție cu numele `task_15` care primește un argument `sub_string` de tip string și un număr variabil de argumente de tip string.
Funcția va returna un dicționar cu două chei: `contains` și `not_contains`.
Cheia `contains` va avea o listă cu toate argumentele care conțin `sub_string`, iar cheia `not_contains` va avea o listă cu toate argumentele care nu conțin `sub_string`.
Exemplu: task_15('home', 'same', 'meme', sub_string = 'me') ➞ {'contains': ['home', 'same', 'meme'], 'not_contains': []}
"""

# CODUL TĂU VINE MAI JOS:
def task_15(*n, sub_string = 'me'):
    contains = []
    not_contains = []
    for i in n:
        if sub_string == "me":
            if sub_string in i:
                contains.append(i)
            else:
                not_contains.append(i)
    dictionar = {'contains': contains,'not_contains': not_contains}
    return dictionar
print(task_15('home', 'same', 'meme', sub_string="me"))
# CODUL TĂU VINE MAI SUS:

# VERIFICATION PROCESS
print(session.check_task_15(task_15))
# VERIFICATION PROCESS

"""
Task: Creați o funcție cu numele `task_16` care va primi un număr variabil de argumente de tip integer și un argument `ooperation` de tip string.
Funcția va returna rezultatul operației specificate de argumentul `operation` aplicată tuturor argumentelor.
Operațiile posibile sunt: `add`, `sub`, `mul`, `div`.
Exemplu: task_16(2, 3, 4, 5, operation='add') ➞ 14
Exemplu: task_16(2, 3, 4, 5, operation='sub') ➞ -10
Exemplu: task_16(2, 3, 4, 5, operation='mul') ➞ 120
Exemplu: task_16(2, 3, 4, 5, operation='div') ➞ 0.008333333333333333
"""

# CODUL TĂU VINE MAI JOS:
def task_16(*n, operation=None):
    if operation == 'add':
        return sum(n)
    elif operation == 'sub':
        result = n[0]
        for num in n[1:]:
            result -= num
        return result
    elif operation == 'mul':
        result = 1
        for num in n:
            result *= num
        return result
    elif operation == 'div':
        result = n[0]
        for num in n[1:]:
            result /= num
        return result
    else:
        return "Eroare operatie"
# CODUL MEU PE CARE L-AM SCRIS INITIAL LUCREAZA DAR NU SE SOCOATE CA CORECT
# def task_16(*n, operation=None):
#     if operation == 'add':
#         return sum(n)
#     elif operation == 'sub':
#         sub=n[0] 
#         for i in range(1,len(n)):
#             sub -= n[i]
#         return sub
#     elif operation == 'mul':
#         mul=(1)
#         for i in range(0,len(n)):
#             mul *= n[i]
#         return mul
#     elif operation == 'div':
#         div=(1)
#         for i in range(0,len(n)):
#             div /= n[i]
#         return div
#     else:
#         return "Operatia este difinita incorect"
# CODUL TĂU VINE MAI SUS:

# VERIFICATION PROCESS
print(session.check_task_16(task_16))
# VERIFICATION PROCESS

"""
Task: Creați o funcție cu numele `task_17` care primește un argument `number` după putea primi diferite argumente keyword precum `add`, `sub`, `mul`, `div` care vor fi liste cu numere.
Funcția va returna rezultatul operației specificate de argumentul `operation` aplicată tuturor argumentelor. Mai multe operații pot fi aplicate. Ordinea operațiilor va fi în ordinea în care sunt specificate.
Operațiile posibile sunt: `add`, `sub`, `mul`, `div`.
Exemplu: task_17(2, add=[3, 4, 5]) ➞ 14
Exemplu: task_17(2, sub=[3, 4, 5]) ➞ -10
Exemplu: task_17(2, mul=[3, 4, 5]) ➞ 120
Exemplu: task_17(2, div=[3, 4, 5]) ➞ 0.008333333333333333
Exemplu: task_17(2, add=[3, 4, 5], sub=[1, 2]) ➞ 11
"""

# CODUL TĂU VINE MAI JOS:
def task_17():
    pass
# CODUL TĂU VINE MAI SUS:

# VERIFICATION PROCESS
print(session.check_task_17(task_17))
# VERIFICATION PROCESS

"""
Task: Creați o funcție cu numele `task_18` care primește un număr variabil de argumente de tip string și va returna un dicționar în care cheile vor fi caracterele întâlnite în argumentele primite, iar valorile vor fi numărul de apariții ale caracterelor.
Exemplu: task_18('hello', 'world') ➞ {'h': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1}
"""

# CODUL TĂU VINE MAI JOS:
def task_18(*n):
    counter = {}
    for i in n:
        for j in i:
            if j in counter:
                counter[j]+=1
            else:
                counter[j]=1
    return counter
print(task_18('hello', 'world'))
# CODUL TĂU VINE MAI SUS:

# VERIFICATION PROCESS
print(session.check_task_18(task_18))
# VERIFICATION PROCESS

"""
Task: Creați o funcție cu numele `task_19` care primește un număr variabil de argumente de tip integer și va returna un dicționar în care cheile vor fi numerele prime întâlnite în argumentele primite, iar valorile vor fi numărul de apariții ale numerelor prime.
Exemplu: task_19(1, 2, 3, 4, 5, 6, 7, 8, 9) ➞ {2: 1, 3: 1, 5: 1, 7: 1}
"""

# CODUL TĂU VINE MAI JOS:
def numere_prime(n):
    if n<=1:
        return False
    for i in range(2, (int(n**0.5)+1)):
        if n%i == 0:
            return False
    else:
        return True
def task_19(*n):
    lista_numere_prime = {}
    for i in n:
        if numere_prime(i):
            if i in lista_numere_prime:
                lista_numere_prime[i] += 1
            else:
                lista_numere_prime[i] = 1
    return lista_numere_prime
print(task_19(0, 2, 3, 4, 5, 6, 7, 8, 9))
# CODUL TĂU VINE MAI SUS:

# VERIFICATION PROCESS
print(session.check_task_19(task_19))
# VERIFICATION PROCESS

"""
Task: Creați o funcție cu numele `task_20` care primește un număr variabil de argumente de tip string și va returna un dicționar în care cheile vor fi lungimile cuvintelor întâlnite în argumentele primite, iar valorile vor fi numărul de apariții ale lungimilor cuvintelor.
Exemplu: task_20('hello', 'world') ➞ {5: 2}
Exemplu: task_20('hello', 'world', 'python') ➞ {5: 2, 6: 1}
"""

# CODUL TĂU VINE MAI JOS:
def task_20(*n):
    numaratoarea_lit = {}
    for i in n:
        j = i.split()
        for k in j:
            lungime = len(k)
            if lungime in numaratoarea_lit:
                numaratoarea_lit[lungime] += 1
            else:
                numaratoarea_lit[lungime] = 1
    return numaratoarea_lit
print(task_20('hello', 'world'))
# CODUL TĂU VINE MAI SUS:

# VERIFICATION PROCESS
print(session.check_task_20(task_20))
print(session.get_completion_percentage())
# VERIFICATION PROCESS

