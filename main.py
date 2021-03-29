#Zad1
'''class Material:
    rodzaj = "0"
    dlugosc = 0
    szerokosc = 0

    def __init__(self,r,d,s):
        self.rodzaj = r
        self.dlugosc = d
        self.szerokosc = s

    def wyswietl_nazwe(self):
        pass

class Ubrania(Material):
    rozmiar = " "
    kolor = " "
    dla_kogo = " "

    def wyswietl_dane(self):
        print("rozmiar: ", self.rozmiar)
        print("kolor: ", self.kolor)
        print("dla_kogo: ", self.dla_kogo)

class Sweter(Ubrania):
    rodzaj_swetra = " "

    def wyswietl_dane(self):
        print("rodzaj swetra: ",self.rodzaj_swetra)

print("bawełna")
bawelna = Material("bawełna", 124, 68)
print("koszulka")
koszulka = Ubrania("polo", 110, 75)
print("golf")
golf = Sweter("golf", 120, 85)

bawelna.wyswietl_nazwe()
koszulka.wyswietl_dane()
golf.wyswietl_dane()'''
#Zad2
'''class Kwadrat:
    bok = 5


    def __add__(self):
        self.bok = self.bok*5
        return self

    def wyswietl_dane(self, kwadrat):
        return kwadrat.bok
#kwad = Kwadrat()
#print(kwad.wyswietl_dane(kwad.__add__()))

#Zad3
    def __le__(self, wartos2):
        if(self.bok <= wartos2.bok):
            return True
        else:
            return False

    def __lt__(self, wartos2):
        if(self.bok < wartos2.bok):
            return True
        else:
            return False
    def __ge__(self, wartos2):
        if(self.bok >= wartos2.bok):
            return True
        else:
            return False
    def __gt__(self, wartos2):
        if(self.bok > wartos2.bok):
            return True
        else:
            return False

kwad = Kwadrat()
print(kwad.__gt__(kwad))'''
#Zad4
'''class Point:
    counter = 0

    def __init__(self, c):
        self.counter = c

    def __le__(self, wartos2):
        if (self.counter <= wartos2.counter):
            return True
        else:
            return False

    def __lt__(self, wartos2):
        if (self.counter < wartos2.counter):
            return True
        else:
            return False

    def __ge__(self, wartos2):
        if (self.counter >= wartos2.counter):
            return True
        else:
            return False

    def __gt__(self, wartos2):
        if (self.counter > wartos2.counter):
            return True
        else:
            return False

point1 = Point(5)
point2 = Point(3)
point3 = Point(8)
point4 = Point(3)

print(point1.__gt__(point1))
print(point1.__ge__(point2))
print(point1.__lt__(point3))
print(point1.__le__(point4))'''
#Zad5
'''class Osoba:
    pass
class Pracownik(Osoba):
    pass
class Menadzer(Pracownik):
    pass

ludz = Osoba()
pracownik = Pracownik()
jurek = Menadzer()
print(isinstance(jurek, Osoba))
print(issubclass(ludz.__class__,Menadzer))'''
#Zad6
'''class Wspak:
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]

obiekt = Wspak("Monsterek")
print(obiekt.__next__())
print(obiekt.__next__())
print(obiekt.__next__())
print(obiekt.__next__())
obiekt2 = Wspak([1,2,3,4,5])
print(obiekt2.__next__())
print(obiekt2.__next__())
print(obiekt2.__next__())'''
#Zad7
'''class Parzyste:
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        if(self.data[self.index] % 2 == 0):
            return self.data[self.index]

obiekt = Parzyste([1,2,3,4,5])
print(obiekt.__next__())
print(obiekt.__next__())
print(obiekt.__next__())'''
#Zad8
'''class Samogloski:
    def __init__(self, data):
        if(isinstance(data, str)):
            self.data = data
            self.index = len(data)
        else:
            print("Podana zmienna nie jest typu string")

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        if self.data[self.index] == "a" or self.data[self.index] == "e" or self.data[self.index] == "i" or self.data[self.index] == "o" or self.data[self.index] == "u" or self.data[self.index] == "y":
            return self.data[self.index]
obiekt1 = Samogloski(123)
obiekt2 = Samogloski("Monsterek")
print(obiekt2.__next__())
print(obiekt2.__next__())
print(obiekt2.__next__())
print(obiekt2.__next__())'''
#Zad9
'''def parzyste(data):
    for index in range(len(data)-1, -1, -1):
        if data[index] % 2 == 0:
            yield data[index]

data = [6,5,4,3,2,1]
gen = parzyste(data)
print(gen.__next__())
print(gen.__next__())
print(gen.__next__())'''
#Zad10
'''ciag = (x+x for x in range(1, 100)) #r=2
print(next(ciag))
print(next(ciag))
print(next(ciag))
print(next(ciag))
print(next(ciag))
print(next(ciag))
print(next(ciag))
print(next(ciag))
print(next(ciag))
print(next(ciag))
print(next(ciag))
print(next(ciag))'''