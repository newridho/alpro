from datetime import timedelta
import datetime

sekarang = datetime.datetime.now()
tanggalPinjam = sekarang.date()
setelah7Hari = sekarang + timedelta(days = 7)

print("===STRUK PINJAM BUKU===")
print("Nama : Siti")
print("Buku : Novel Laskar Pelangi")
print("Tanggal Pinjam : ", sekarang.date())
print("Max Tanggal Kembali : ", setelah7Hari.date())
print("===TERIMA KASIH===")