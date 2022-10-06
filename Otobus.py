class Otobus:
    kalkis: str = ""
    varis: str = ""
    koltuk_sayi = 0
    dolu_koltik = 0
    plaka: str = ""
 def _init_(self, plaka, kalkis, varis, koltuk_sayi):
        self.plaka= plaka
        self.kalkis = kalkis
        self.varis = varis
        self.koltuk_sayi = koltuk_sayi
 def bilet_sat(self):
     Otobus.dolu_koltik += 1
 def bilet_iade(self):
     Otobus.dolu_koltik -= 1
 def durum_yaz(self):
     return f"{self.kalkis},{self.varis},{self.plaka},{self.dolu_koltik}"
