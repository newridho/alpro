# Sekarang jam (saat ini):(menit saat ini) WIB. Hari ini adalah hari (hari ini), tanggal (tanggal hari ini), bulan (bulan ini), tahun (tahun ini).
# from time import time
from datetime import datetime

sekarang = datetime.now()
jamSekarang = sekarang.hour
menitSekarang = sekarang.minute

hariIni = sekarang.strftime("%A")
tanggalSekarang = sekarang.day
bulanSekarang = sekarang.strftime("%B")
tahunIni = sekarang.year


print(f"Sekarang jam {jamSekarang}:{menitSekarang} WIB. Hari ini adalah hari {hariIni}, tanggal{tanggalSekarang}, bulan {bulanSekarang}, tahun {tahunIni}")