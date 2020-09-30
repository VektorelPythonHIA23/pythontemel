class FileTool:
    ext = ".csv"
    def __init__(self,adres,alanlar):
        self.adres = adres + FileTool.ext
        self.dosya = self.dosyaAc()
        self.kayitlar = self.dosya.readlines()
        self.alanlar = alanlar
    def dosyaAc(self):
        import os
        if os.path.exists(self.adres):
            return open(self.adres,"r+")
        else:
            return open(self.adres,"w+")
    

    def listeleme(self):
        i = 1
        for item in self.kayitlar:
            print(f"{i} -",*item.split[";"],end="")
            i+=1
    
    def girisYap(self):
        liste = []
        for item in self.alanlar:
            liste.append(input(f"{item}"))
        return ";".join(liste) + "\n"

    def ekleme(self):
        self.kayitlar.append(self.girisYap())

    def silme(self):
        self.listeleme()
        del self.kayitlar[int(input("Silmek istediğiniz kaydı seçiniz"))-1] 

    def guncelle(self):
        self.listeleme()
        self.kayitlar[int(input("Güncellemek istediğiniz\
         kaydı seçiniz:"))-1] = self.girisYap()

    def menu(self):
        menu = """
        1-Ekleme
        2-Güncelleme
        3-Silme
        4-Listeleme
        5-Çıkış
        İşlem Seçiniz:
        """
        fonkListesi=["",self.ekleme,self.guncelle,self.silme,self.listeleme]
        anahtar = 1
        while anahtar == 1:
            islem = int(input(menu))
            if islem != 5:
                fonkListesi[islem]()
            else:
                anahtar = 0
        else:
            self.dosya.seek(0)
            self.dosya.truncate()
            self.dosya.writelines(self.kayitlar)
            self.dosya.flush()


    def __del__(self):
        print("RIP")
        self.dosya.seek(0)
        self.dosya.truncate()
        self.dosya.writelines(self.kayitlar)
        self.dosya.close()

nesne = FileTool("defter",["Adı","Soyadı","Tel"])
nesne.menu()