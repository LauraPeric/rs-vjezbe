#zadatak1 LAMBDA IZRAZI
#1. Kvadriranje broja:
def kvadriraj(x):
 return x ** 2

kvadriraj = lambda x: x**2
print(kvadriraj(2))


#2. Zbroji pa kvadriraj:
def zbroji_pa_kvadriraj(a, b):
 return (a + b) ** 2

zbroji_pa_kvadriraj = lambda a,b: (a + b) ** 2
print(zbroji_pa_kvadriraj(2,3))

#3. Kvadriraj duljinu niza:
def kvadriraj_duljinu(niz):
 return len(niz) ** 2

kvadriraj_duljinu = lambda niz: (niz) ** 2
print(kvadriraj_duljinu(2))


#4. Pomnoži vrijednost s 5 pa potenciraj na x:
def pomnozi_i_potenciraj(x, y):
 return (y * 5) ** x

pomnozi_i_potenciraj = lambda x,y: (y * 5) ** x
print(pomnozi_i_potenciraj(2,3))


#5. Vrati True ako je broj paran, inače vrati None:
def paran_broj(x):
  if x % 2 == 0:
    return True
  else:
    return None

paran_broj= lambda x: True if x % 2 == 0 else None
print(paran_broj(3))

