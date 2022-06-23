from hewan_air import HewanAir
from hewan_darat import HewanDarat

# sapi, kambing, burung merpati,ikan cupang, ikan hiu, ikan paus

sapi = HewanDarat(nama='Sapi', kaki=4, bersayap=False)
kambing = HewanDarat(nama='Kambing', kaki=4, bersayap=False)
burung_merpati = HewanDarat(nama='Burung Merpati', kaki=2, bersayap=True)
ikan_cupang = HewanAir(nama='Ikan Cupang', habitat="air tawar")
ikan_hiu = HewanAir(nama='Ikan Hiu', habitat="air laut")
ikan_paus = HewanAir(nama='Ikan Paus', habitat="air laut")

print(ikan_hiu.nama)
print(ikan_hiu.habitat)
ikan_hiu.bernafas()
ikan_hiu.makan()

print(sapi.bersayap)
