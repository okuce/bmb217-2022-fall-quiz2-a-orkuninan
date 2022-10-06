class Otobus:
    otobusler: str = ""
    satislar: int = ""
    iadeler: int = ""
    kalkis: str = ""
    varis: str = ""
    dolu_koltik = 0
    plaka: str = ""
  def bilet_sat(self):
     Otobus.dolu_koltik += 1
 def bilet_iade(self):
     Otobus.dolu_koltik -= 1
 def durum_yaz(self):
      return f"{self.kalkis},{self.varis},{self.plaka},{self.dolu_koltik}"
