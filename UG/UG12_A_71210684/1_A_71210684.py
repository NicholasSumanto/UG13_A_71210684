deret = input("Masukan deret angka :")
deret = deret.split(",")
jumlah = 0
jenis = ""
Total = ""
for angka in deret:
    if angka != ",":
      if ((int(angka))%2) ==0:
        jumlah = jumlah + int(angka)
        jenis = " + "+angka
      else:
        jumlah = jumlah - int(angka)
        jenis = " - "+angka
      Total = Total + jenis

print("Total :",Total)
print("Hasil perhitungan diatas ialah",jumlah)








