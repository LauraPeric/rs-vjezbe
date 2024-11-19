'''
1. Definirajte klasu Automobil s atributima marka , model , godina_proizvodnje i kilometraža .
Dodajte metodu ispis koja će ispisivati sve atribute automobila.

Stvorite objekt klase Automobil s proizvoljnim vrijednostima atributa i pozovite metodu ispis .
Dodajte novu metodu starost koja će ispisivati koliko je automobil star u godinama, trenutnu
godine dohvatite pomoću datetime modula.
'''

class automobil:
    def __init__(self, marka, model, godina_proizvodnje, kilometraža):
        self.marka = marka
        self.model = model
        self.godina_proizvodnje = godina_proizvodnje
        self.kilometraža = kilometraža

    def ispis(self):
        return ( f"marka: {self.marka} "
                 f" model: {self.model} "
                 f"godina prizvodnje: {self.godina_proizvodnje} "
                 f"kilometraža {self.kilometraža} ")
        
automobil = automobil("VW", "Up", 2015, 70000)
print(automobil.ispis())



'''
2. Definirajte klasu Kalkulator s atributima a i b . Dodajte metode zbroj , oduzimanje , mnozenje ,
dijeljenje , potenciranje i korijen koje će izvršavati odgovarajuće operacije nad atributima a i
b .
'''
import math

class Kalkulator:
    def __init__(self, a, b):
        self.a = a
        self.b = b 
    
    def zbroj(self):
        return self.a+self.b
                
    def oduzimanje(self):
        return self.a-self.b
    
    def množenje(self):
        return self.a*self.b
    
    def dijeljenje(self):
        return self.a/self.b
    
    def potenciranje(self):
        return self.a**self.b
    
    def korijen(self):
        if self.a >= 0 and self.b >= 0:
            return math.sqrt(self.a), math.sqrt(self.b)
        else:
            return "Greška"

kalkulator = Kalkulator(5, 4)

# Pozivanje metoda
print("Zbroj:", kalkulator.zbroj())
print("Oduzimanje:", kalkulator.oduzimanje())
print("Množenje:", kalkulator.množenje())
print("Dijeljenje:", kalkulator.dijeljenje())
print("Potenciranje:", kalkulator.potenciranje())
print("Korijen:", kalkulator.korijen())
    


'''
3. Definirajte klasu Student s atributima ime , prezime , godine i ocjene .
Iterirajte kroz sljedeću listu studenata i za svakog studenta stvorite objekt klase Student i dodajte ga u
novu listu studenti_objekti :
Dodajte metodu prosjek koja će računati prosječnu ocjenu studenta.
U varijablu najbolji_student pohranite studenta s najvećim prosjekom ocjena iz liste
studenti_objekti . Implementirajte u jednoj liniji koda.
'''

class Student:
    def __init__(self,ime , prezime , godine, ocjene):
        self.ime = ime
        self.prezime = prezime
        self.godine = godine
        self.ocjene= ocjene

    def prosjek(self):
        return sum(self.ocjene) / len(self.ocjene) if self.ocjene else 0


studenti_podaci = [
    {"ime": "leon", "prezime": "leic", "godine": 24, "ocjene": [5, 4, 5, 5]},
    {"ime": "Antonela", "prezime": "Med", "godine": 22, "ocjene": [4, 2, 5, 5]},
    {"ime": "Matko", "prezime": "Maković", "godine": 21, "ocjene": [3, 2, 4, 3]},
    {"ime": "Petra", "prezime": "Perić", "godine": 23, "ocjene": [5, 3, 5, 5]},
]

studenti_objekti = [Student(stud["ime"], stud["prezime"], stud["godine"], stud["ocjene"]) for stud in studenti_podaci]

najbolji_student = max(studenti_objekti, key=lambda stud: stud.prosjek())

print(f"Najbolji student: {najbolji_student.ime} {najbolji_student.prezime}, Prosjek: {najbolji_student.prosjek():.2f}")


'''
4. Definirajte klasu Krug s atributom r . Dodajte metode opseg i povrsina koje će računati opseg i
površinu kruga.
Stvorite objekt klase Krug s proizvoljnim radijusom i ispišite opseg i površinu kruga.


 '''

class krug: 
    def __init__(self,r):
        self.r = r
    
    def opseg(self):
        opseg = 2 * math.pi * self.r
        return opseg
    
    def povrsina(self):
        povrsina = math.pi * self.r**2
        return povrsina
    
r = 6
moj_krug = krug(r)

opseg = moj_krug.opseg()
povrsina = moj_krug.povrsina()

print(f"Radijus: {r}")
print(f"Opseg kruga: {opseg:.2f}")
print(f"Površina kruga: {povrsina:.2f}")    

'''
5. Definirajte klasu Radnik s atributima ime , pozicija , placa . Dodajte metodu work koja će ispisivati
"Radim na poziciji {pozicija}".
Dodajte klasu Manager koja nasljeđuje klasu Radnik i definirajte joj atribut department . Dodajte
metodu work koja će ispisivati "Radim na poziciji {pozicija} u odjelu {department}".
U klasu Manager dodajte metodu give_raise koja prima parametre radnik i povecanje i
povećava plaću radnika ( Radnik ) za iznos povecanje .
Definirajte jednu instancu klase Radnik i jednu instancu klase Manager i pozovite metode work i
give_raise .'''


class Radnik:
    def __init__(self, ime , pozicija , placa):
        self.ime = ime
        self.pozicija = pozicija
        self.placa = placa

    def work(self):
        print(f"Radim na poziciji {self.pozicija}.")


class Manager(Radnik):
    def __init__(self,ime, pozicija, placa, department):
        super().__init__(ime, pozicija, placa)
        self.department = department

    def work(self):
        print (f"Radim na poziciji {self.pozicija} u odjelu {self.department}")
    
    def give_raise(self, radnik, povecanje):
        radnik.placa += povecanje
        print(f"{radnik.ime} sada ima plaću: {radnik.placa:.2f}.")
    

radnik1 = Radnik("Leon", "Programer", 5000)

manager1 = Manager("Antonela", "Menadžer", 7000, "IT")

radnik1.work()
manager1.work()

manager1.give_raise(radnik1, 500)