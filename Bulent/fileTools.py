class fileTool:
    ext = ".cvs"
    def __init__(self,adres,alanlar):
        self.adres = adres + fileTool.ext
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
            i += 1


    def girisYap(self):
        liste = []
        for item in self.alanlar:
            liste.append(input(f"{item}"))
        return ";".join(liste) + "\n" 