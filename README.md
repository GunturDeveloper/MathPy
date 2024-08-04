# MathPy Module

Selamat datang di **MathPy Module** oleh **Guntur Developer**. Modul ini dirancang untuk menyediakan berbagai fungsi matematika dasar yang dapat digunakan dalam pemrograman Python.

## Deskripsi

Modul ini mencakup fungsi-fungsi untuk menghitung luas dan keliling bangun datar, luas permukaan dan volume bangun ruang, deret aritmatika dan geometri, serta perhitungan peluang. Semua fungsi dalam modul ini mencetak hasil secara otomatis.

## Instalasi

1. Clone repositori ini atau unduh file `mathpy.py` dari repositori ini.
2. Simpan file `mathpy.py` di direktori proyek Anda.

## Penggunaan

Anda dapat mengimpor modul ini dengan nama alias pilihan Anda dan menggunakan fungsi-fungsinya seperti contoh berikut:

```python
import mathpy as mp

# Contoh penggunaan fungsi
mp.luas_persegi(4)          # Menghitung luas persegi dengan sisi 4
mp.keliling_lingkaran(7)    # Menghitung keliling lingkaran dengan jari-jari 7
mp.volume_bola(5)           # Menghitung volume bola dengan jari-jari 5
mp.aritmatika_sum(1, 2, 5)  # Menghitung jumlah 5 suku pertama deret aritmatika dengan suku awal 1 dan beda 2
mp.peluang(3, 10)           # Menghitung peluang dengan kasus 3 dari ruang sampel 10
```

## Daftar Fungsi

### Bangun Datar
- `luas_persegi(sisi)`
- `keliling_persegi(sisi)`
- `luas_persegi_panjang(panjang, lebar)`
- `keliling_persegi_panjang(panjang, lebar)`
- `luas_segitiga(alas, tinggi)`
- `keliling_segitiga(sisi1, sisi2, sisi3)`
- `luas_lingkaran(jari_jari)`
- `keliling_lingkaran(jari_jari)`
- `luas_jajar_genjang(alas, tinggi)`
- `keliling_jajar_genjang(alas, sisi_miring)`
- `luas_trapesium(sisi_a, sisi_b, tinggi)`
- `keliling_trapesium(sisi_a, sisi_b, sisi_c, sisi_d)`
- `luas_belah_ketupat(diagonal1, diagonal2)`
- `keliling_belah_ketupat(sisi)`
- `luas_layang_layang(diagonal1, diagonal2)`
- `keliling_layang_layang(sisi1, sisi2)`

### Bangun Ruang
- `luas_permukaan_kubus(sisi)`
- `volume_kubus(sisi)`
- `luas_permukaan_balok(panjang, lebar, tinggi)`
- `volume_balok(panjang, lebar, tinggi)`
- `luas_permukaan_tabung(jari_jari, tinggi)`
- `volume_tabung(jari_jari, tinggi)`
- `luas_permukaan_bola(jari_jari)`
- `volume_bola(jari_jari)`
- `luas_permukaan_kerucut(jari_jari, tinggi)`
- `volume_kerucut(jari_jari, tinggi)`

### Barisan Deret
- `aritmatika_nth_term(a, d, n)`
- `aritmatika_sum(a, d, n)`
- `geometri_nth_term(a, r, n)`
- `geometri_sum(a, r, n)`

### Peluang
- `peluang(kasus, ruang_sampel)`

## Penulis

Modul ini dikembangkan oleh **Guntur Developer**, siswa SMK-SMTI Yogyakarta.

## Lisensi

Modul ini dilisensikan di bawah [MIT License](LICENSE).
