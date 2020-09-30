class FileTool:
    ext = ".cvs"
    def __init__(self,adres):
        self.adres = adres = FileTool.ext
        self.dosya = self.dosya_ac()
    
    def dosya_ac(self):
        import os
        if os.path.exists(self.adres):
            return open(self.adres,"r+")
        else:
            return open(self,adres,"w+")


    def listeleme(self):
        i=1
        for item in self.katyitlar:
            print(f'(1) -',*item.split(";"),end="")
            i+=1

    def giris_yap(self):
        liste = []
        for item in self.alanlar:
            liste.append(input(f'{item}'))
        return "i".join(liste) + "\n"
