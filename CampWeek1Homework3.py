class Banka:
    def krediBasvur(self):
       print("Kredi başvurusu yapıldı.")

    def krediHesapla(self):
     print("Hesaplar yapıldı.")

banka=Banka()
banka.krediBasvur()

class Matematik:
    def __init__(self,sayi1,sayi2):
        self.s1=sayi1
        self.s2=sayi2
    def topla(self):
        return self.s1+self.s2
    def cikar(self):
        return self.s1-self.s2
    def bol(self):
        return self.s1/self.s2
    def carp(self):
        return self.s1*self.s2 

matematik=Matematik(14,7) 
sonuc=matematik.topla()
print("Sonuç : "+str(sonuc))

class Istatistik(Matematik):
    def __init__(self, sayi1, sayi2):
        super().__init__(sayi1, sayi2)
    def varyansHesapla(self):
        return self.s1*self.s2
    
istatistik=Istatistik(5,8)
istatistik.carp


class Person:
    def __init__(self,name,lastName):
        self.name=name
        self.lastName=lastName
musteri1=Person("Enes","Mentese")
print(musteri1.name)
