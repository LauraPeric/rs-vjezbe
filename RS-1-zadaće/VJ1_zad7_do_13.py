#zad7
def provjera_lozinke(lozinka):
  if not (8 <= len(lozinka) <= 15):
      return "Lozinka mora sadržavati između 8 i 15 znakova."

  ima_veliko_slovo = any(char.isupper() for char in lozinka)
  ima_broj = any(char.isdigit() for char in lozinka)
  if not (ima_veliko_slovo and ima_broj):
      return "Lozinka mora sadržavati barem jedno veliko slovo i jedan broj."

  lozinka_mala = lozinka.lower()
  if "password" in lozinka_mala or "lozinka" in lozinka_mala:
      return "Lozinka ne smije sadržavati riječi 'password' ili 'lozinka'."

  return "Lozinka je jaka!"

unos = input("Unesite lozinku: ")

print(provjera_lozinke(unos))

#zad8

def filtriraj_parne_brojeve(lista):
    parni_brojevi = [broj for broj in lista if broj % 2 == 0]
    return parni_brojevi

lista = [4, 12, 23, 44, 65, 68, 27, 81, 94, 210]
print(filtriraj_parne_brojeve(lista))

#zad9
def ukloni_duplikate(lista):
    #lista u skup-ne dozvoljava duplikate
    bez_duplikata = list(set(lista))
    return bez_duplikata

lista = [123, 242, 332, 434, 555, 123, 221, 332, 434, 555]
print(ukloni_duplikate(lista))

#zad10
def brojanje_riječi(tekst):
    # razmak kao separator
    riječi = tekst.split()
    brojač_riječi = {}

    for riječ in riječi:
        if riječ in brojač_riječi:
            brojač_riječi[riječ] += 1
        else:
            brojač_riječi[riječ] = 1

    return brojač_riječi

tekst = "Python je programski jezik koji je jednostavan za učenje i korištenje. Python je vrlo popularan."
print(brojanje_riječi(tekst))

#zad11

def grup_po_par(lista):
   rezultat = { 'parni': [], 'neparni': []}

   for broj in lista:
       if broj % 2 == 0:
         rezultat['parni'].append(broj) 
       else:
          rezultat['neparni'].append(broj)
    
   return rezultat

lista =[1, 23, 42, 35, 6, 22, 35, 64, 12, 11]
print(grup_po_par(lista))


#zad12

def obrnuti_r(rjecnik):
    return{ vrijednost: kljuc for kljuc, vrijednost in rjecnik.items()}
rjecnik = {"ime": "Ivan", "prezime": "Ivić", "dob": 25}
print(obrnuti_r(rjecnik))


#zad13

#a
def prvi_i_zadnji(lista):
    return (lista[0], lista[-1])
lista= [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
print(prvi_i_zadnji(lista))

#b
def maks_i_min(lista):
    maks = lista[0]
    min = lista[0]

    for broj in lista:
        if broj > maks:
            maks = broj
        if broj < min:
            min = broj

    return (maks, min)

lista = [5, 10, 20, 50, 100, 11, 250, 50, 80]
print(maks_i_min(lista))

#c
def presjek(skup_1, skup_2):
    return {element for element in skup_1 if element in skup_2}

skup_1 = {1, 2, 3, 4, 5}
skup_2 = {4, 5, 6, 7, 8}
print(presjek(skup_1, skup_2))

