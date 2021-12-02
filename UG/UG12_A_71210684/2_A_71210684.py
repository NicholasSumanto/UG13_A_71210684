A = []
B = []

while (True):
    nama = input("Masukkan nama: ")
    if nama == "STOP":
        break
    kursi = int(input("Masukkan nomor kursi " + nama + ": "))

    if kursi in B:
        print("Mohon maaf kursi tersebut telah terisi!")
        if kursi in B:
            continue
    if kursi not in A:
        A.append(nama)
        B.append(kursi)

print()
print("List kursi yang telah terisi : ")


for a in range(0, len(A), 1):
    print("Kursi nomor", B[a], "telah diisi oleh", A[a])





