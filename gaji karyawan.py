#menghitung penghasilan gaji

a = int(input("Masukkan Gaji Pokok : "))
b = int(input("Masukkan Lama Jam Lembur : "))
c = int(input("Masukkan Gaji Lembur /Jam : "))

gajiLembur = b *c
gajiBersih = a + gajiLembur
print(f"Gaji Anda : {gajiBersih}")