n = int(input("n: "))
for i in range(1, n + 1):      # baris ke-i
    for j in range(i):         # jumlah bintang sesuai nomor baris
        print("*", end=" ")
    print()                    # pindah baris
