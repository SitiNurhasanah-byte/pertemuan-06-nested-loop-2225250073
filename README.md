# Pertemuan 06 Nested Loop Python

Nama: Siti Nurhasanah  
NIM: 2225250073  
Kelas: 3B  

## Tujuan
Menggunakan nested loop, pola, akumulasi, dan pencacahan.

## Cara Menjalankan
python3 tugas/tabel_perkalian_dan_statistik.py

## Algoritma Tugas 3
1. Baca n sebagai integer positif.  
2. Validasi n agar > 0.  
3. Loop luar (i): mengatur baris tabel perkalian dari 1 sampai n.  
4. Loop dalam (j): menghitung hasil = i * j.  
5. Akumulator total_semua: menambahkan semua hasil perkalian.  
6. Akumulator total_baris: menambahkan hasil perkalian per baris.  
7. Counter count_genap: menghitung berapa hasil perkalian yang genap.  
8. Tampilkan tabel, jumlah per baris, total keseluruhan, dan banyak hasil genap.  

---

## 📊 Hasil Pengujian

| Input (n) | Hasil Diharapkan       | Keluaran Aktual        | Status |
|-----------|------------------------|------------------------|--------|
| 1         | Total=1, Genap=0       | Total=1, Genap=0       | ✅ |
| 2         | Total=9, Genap=3       | Total=9, Genap=3       | ✅ |
| 3         | Total=36, Genap=5      | Total=36, Genap=5      | ✅ |

---

## ⚡ Analisis Efisiensi
Loop luar berjalan n kali.  
Loop dalam berjalan n kali untuk setiap iterasi loop luar.  
Total eksekusi badan loop dalam = n × n = n².  
Contoh: untuk n = 3, badan loop dalam berjalan 9 kali.  

---

## 🪞 Refleksi
Kesalahan nested loop yang pernah ditemukan adalah **lupa menginisialisasi ulang total_baris**.  
Akibatnya, jumlah baris menjadi akumulasi dari baris sebelumnya.  
Perbaikan dilakukan dengan menempatkan `total_baris = 0` di dalam loop luar.  
Dengan perbaikan ini, jumlah setiap baris dihitung secara mandiri.  

---