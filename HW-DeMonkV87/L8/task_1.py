# Aceasta este tema pentru lecția 8 legată de loops

# Creați o listă de numere de la 1 la 10 folosind un for loop și funcția range().

# CODUL TĂU VINE MAI JOS:
lista = [h for h in range(1,11,1)]
print(lista)
# CODUL TĂU VINE MAI SUS:

# Folosind un for loop, parcurgeți lista creată și afișați numai numerele pare.

# CODUL TĂU VINE MAI JOS:
for numerepare in lista:
    if numerepare % 2 ==0:
        print(numerepare)
# CODUL TĂU VINE MAI SUS:

# Folosind un while loop, creați o variabilă 'i' inițializată cu 1 și incrementați-o până când ajunge la 5. Afișați valoarea 'i' la fiecare pas.

# CODUL TĂU VINE MAI JOS:
i = 1
while i <= 5:
    print(i)
    i += 1
# CODUL TĂU VINE MAI SUS:

# Creați un dicționar person cu cheile 'name', 'age' și 'city' și iterați prin dicționar afișând perechile de cheie-valoare.

# CODUL TĂU VINE MAI JOS:
Person = {"name": "x", "age": "x", "city":"x"}
for key in Person:
    print(key)
# CODUL TĂU VINE MAI SUS:

# Utilizați un for loop pentru a itera printr-o listă de liste (matrice) și afișați fiecare element.

# CODUL TĂU VINE MAI JOS:
matrice =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for element in matrice:
    for numar in element:
        print(f"element: {numar}")
# CODUL TĂU VINE MAI SUS:

# Creați o secvență de numere folosind funcția range() și apoi iterați prin această secvență folosind un for loop pentru a afișa numerele.

# CODUL TĂU VINE MAI JOS:
lista = list(range(5))
for i in lista:
     print(i)
# CODUL TĂU VINE MAI SUS:

# Folosiți funcția enumerate() pentru a itera printr-o listă și a afișa indexul fiecărui element alături de valoarea sa.

# CODUL TĂU VINE MAI JOS:
orase = ("Chisinau", "Iasi", "Bucuresti", "Brasov", "Frankfurt")
for i, orase in enumerate(orase):
     print(i,orase) # sau i+1 in caz ca dorim ca indexul sa se inceapa cu 1 nu cu 0
# CODUL TĂU VINE MAI SUS:

# Folosiți funcția zip() pentru a itera simultan prin două liste și a afișa elementele corespunzătoare.

# CODUL TĂU VINE MAI JOS:
brends = ["Xiaomi", "Apple", "Samsung", "LG", "Sharp", "Huawei"]
numar_telefoane = [3, 1, 2, 0, 1, 1]
for brends, numar_telefoane in zip(brends, numar_telefoane):
    print(brends, numar_telefoane)
# CODUL TĂU VINE MAI SUS:

# Creați o listă de numere de la 1 la 10 folosind un for loop și funcția range().

# CODUL TĂU VINE MAI JOS:
listaX = [x for x in range(1,11,1)]
print(listaX)
# CODUL TĂU VINE MAI SUS:

# Folosind un buclă while, dublează valorile listei până când primul element va deveni mai mare decât 50.

# CODUL TĂU VINE MAI JOS:
listaY = [1, 2, 3, 4, 5]
while max(listaY) <=50:
    listaY = [i*2 for i in listaY]
    print(listaY)
# CODUL TĂU VINE MAI SUS:

# Generează și printează o listă cu toate numerele pătrat perfect din intervalul [1, 100].

# CODUL TĂU VINE MAI JOS:
Patrate_perfecte = [i**2 for i in range(1,11,1)]
print(Patrate_perfecte)
# CODUL TĂU VINE MAI SUS:

# Folosind un buclă for , printează tabla înmulțirii pentru numărul 7.

# CODUL TĂU VINE MAI JOS:
tabel = {i for i in range(1,10,1)}
i = 1
while i<= 10:
     print("7 *",i ,"=", i*7)
     i+=1
# CODUL TĂU VINE MAI SUS:

# Creează o listă de liste, unde fiecare sub-listă conține perechi (i, j) pentru i și j de la 1 la 5. Printează această listă de perechi.

# CODUL TĂU VINE MAI JOS:
lista_de_liste = [[(i, j) for j in range(1, 6)] for i in range(1, 6)]

for sublist in lista_de_liste:
    print(sublist)
# CODUL TĂU VINE MAI SUS:

# Parcurge lista de la punctul anterior și printează doar perechile unde i < j .

# CODUL TĂU VINE MAI JOS:
for sublist in lista_de_liste:
    for pair in sublist:
        i, j = pair
        if i < j:
            print(pair)
# CODUL TĂU VINE MAI SUS:

# Folosind un buclă while , caută și printează prima valoare care este mai mare decât 10 dintr-o listă cu numere random creată de tine. Dacă nu există, printează "Nu există valori mai mari decât 10".

# CODUL TĂU VINE MAI JOS:
random_list = [1, 3, 5, 7, 9, 7, 10, 21]
num_de_comparatie = False
x = 0
while x < len(random_list):
    if random_list[x]> 10:
        print(random_list[x])
        num_de_comparatie = True
        break
    x +=1
else:
    print("Nu există valori mai mari decât 10 în lista generată.")
# CODUL TĂU VINE MAI SUS:

# Folosind loop-uri Creează un pătrat de stele ( * ) folosind bucle încadrate. Dimensiunea pătratului va fi citită de la utilizator.
# Exemplu pentru un pătrat de dimensiune 5:
# *****
# *****
# *****
# *****
# *****

# CODUL TĂU VINE MAI JOS:
patrat = ()
for i in range(1, 5+1):
    for j in range(1,5+1):
        print("*", end="")
    print()
# CODUL TĂU VINE MAI SUS:

# Folosind for sau while loops realizați afișările de mai jos

# Afișarea 1:
# 1
# 12
# 123
# 1234
# 12345
# 123456

# CODUL TĂU VINE MAI JOS:
lista_deltaUP = []
for i in range(7):
    for j in range(1, i+1):
        print(j, end="")
    print()
# CODUL TĂU VINE MAI SUS:

# Afișarea 2:

# 54321
# 5432
# 543
# 54
# 5

# CODUL TĂU VINE MAI JOS:
lista_deltaDown = []
for i in range(1,6):
    for j in range(5, i-1, -1):
        print(j, end="")
    print()
# CODUL TĂU VINE MAI SUS:

# Afișarea 3:

# abcdefg
# bcdefg
# cdefg
# defg
# efg
# fg
# g

# CODUL TĂU VINE MAI JOS:
lista_Alfabetica = ()
for i in range(1,i+1,1):
    a=97
    for j in range(7, i-1, -1):
        print("%c" %(a), end="")
        a += 1
    print() # mai trebuie ceva ca sa scoata fiecare litera cu index 1 din printare
# CODUL TĂU VINE MAI SUS:

# Afișarea 4:

# +-+-+-+-+-+-+-+-
# -+-+-+-+-+-+-+-+
# +-+-+-+-+-+-+-+-
# -+-+-+-+-+-+-+-+
# +-+-+-+-+-+-+-+-
# -+-+-+-+-+-+-+-+
# +-+-+-+-+-+-+-+-
# -+-+-+-+-+-+-+-+

# CODUL TĂU VINE MAI JOS:
PlusMinus  = ()
for i in range(1, 4+1):
    for j in range(1):
        print("+-+-+-+-+-+-+-+-" '\n' "-+-+-+-+-+-+-+-+", end="")
    print()
# CODUL TĂU VINE MAI SUS:

# Afișarea 5:

# 3
# 3 9
# 3 9 27
# 3 9 27 81
# 3 9 27 81 243
# 9 27 81 243
# 27 81 243
# 81 243
# 243

# CODUL TĂU VINE MAI JOS:
TreilaPutere  = [3**i for i in range(1,6,1)]
for i in range(len(TreilaPutere)):
    for j in range(i+1):
        print(TreilaPutere[j], end= " ")
    print()
#  mai e nevoie sa scriu pentru descrestere
# CODUL TĂU VINE MAI SUS:

# Completați sarcinile de mai sus pentru a exersa lucrul cu buclele în Python.