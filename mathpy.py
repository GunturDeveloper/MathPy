# mathpy.py

def pi():
    return 3.141592653589793

def luas_persegi(sisi):
    hasil = sisi ** 2
    print(f"Luas Persegi: {hasil}")
    return hasil

def keliling_persegi(sisi):
    hasil = 4 * sisi
    print(f"Keliling Persegi: {hasil}")
    return hasil

def luas_persegi_panjang(panjang, lebar):
    hasil = panjang * lebar
    print(f"Luas Persegi Panjang: {hasil}")
    return hasil

def keliling_persegi_panjang(panjang, lebar):
    hasil = 2 * (panjang + lebar)
    print(f"Keliling Persegi Panjang: {hasil}")
    return hasil

def luas_segitiga(alas, tinggi):
    hasil = 0.5 * alas * tinggi
    print(f"Luas Segitiga: {hasil}")
    return hasil

def keliling_segitiga(sisi1, sisi2, sisi3):
    hasil = sisi1 + sisi2 + sisi3
    print(f"Keliling Segitiga: {hasil}")
    return hasil

def luas_lingkaran(jari_jari):
    hasil = pi() * jari_jari ** 2
    print(f"Luas Lingkaran: {hasil}")
    return hasil

def keliling_lingkaran(jari_jari):
    hasil = 2 * pi() * jari_jari
    print(f"Keliling Lingkaran: {hasil}")
    return hasil

def luas_jajar_genjang(alas, tinggi):
    hasil = alas * tinggi
    print(f"Luas Jajar Genjang: {hasil}")
    return hasil

def keliling_jajar_genjang(alas, sisi_miring):
    hasil = 2 * (alas + sisi_miring)
    print(f"Keliling Jajar Genjang: {hasil}")
    return hasil

def luas_trapesium(sisi_a, sisi_b, tinggi):
    hasil = 0.5 * (sisi_a + sisi_b) * tinggi
    print(f"Luas Trapesium: {hasil}")
    return hasil

def keliling_trapesium(sisi_a, sisi_b, sisi_c, sisi_d):
    hasil = sisi_a + sisi_b + sisi_c + sisi_d
    print(f"Keliling Trapesium: {hasil}")
    return hasil

def luas_belah_ketupat(diagonal1, diagonal2):
    hasil = 0.5 * diagonal1 * diagonal2
    print(f"Luas Belah Ketupat: {hasil}")
    return hasil

def keliling_belah_ketupat(sisi):
    hasil = 4 * sisi
    print(f"Keliling Belah Ketupat: {hasil}")
    return hasil

def luas_layang_layang(diagonal1, diagonal2):
    hasil = 0.5 * diagonal1 * diagonal2
    print(f"Luas Layang-layang: {hasil}")
    return hasil

def keliling_layang_layang(sisi1, sisi2):
    hasil = 2 * (sisi1 + sisi2)
    print(f"Keliling Layang-layang: {hasil}")
    return hasil

def luas_permukaan_kubus(sisi):
    hasil = 6 * (sisi ** 2)
    print(f"Luas Permukaan Kubus: {hasil}")
    return hasil

def volume_kubus(sisi):
    hasil = sisi ** 3
    print(f"Volume Kubus: {hasil}")
    return hasil

def luas_permukaan_balok(panjang, lebar, tinggi):
    hasil = 2 * (panjang * lebar + panjang * tinggi + lebar * tinggi)
    print(f"Luas Permukaan Balok: {hasil}")
    return hasil

def volume_balok(panjang, lebar, tinggi):
    hasil = panjang * lebar * tinggi
    print(f"Volume Balok: {hasil}")
    return hasil

def luas_permukaan_tabung(jari_jari, tinggi):
    hasil = 2 * pi() * jari_jari * (jari_jari + tinggi)
    print(f"Luas Permukaan Tabung: {hasil}")
    return hasil

def volume_tabung(jari_jari, tinggi):
    hasil = pi() * jari_jari ** 2 * tinggi
    print(f"Volume Tabung: {hasil}")
    return hasil

def luas_permukaan_bola(jari_jari):
    hasil = 4 * pi() * jari_jari ** 2
    print(f"Luas Permukaan Bola: {hasil}")
    return hasil

def volume_bola(jari_jari):
    hasil = 4/3 * pi() * jari_jari ** 3
    print(f"Volume Bola: {hasil}")
    return hasil

def luas_permukaan_kerucut(jari_jari, tinggi):
    s = (jari_jari ** 2 + tinggi ** 2) ** 0.5  
    hasil = pi() * jari_jari * (jari_jari + s)
    print(f"Luas Permukaan Kerucut: {hasil}")
    return hasil

def volume_kerucut(jari_jari, tinggi):
    hasil = 1/3 * pi() * jari_jari ** 2 * tinggi
    print(f"Volume Kerucut: {hasil}")
    return hasil

def aritmatika_nth_term(a, d, n):
    hasil = a + (n - 1) * d
    print(f"Barisan Aritmatika suku ke-{n}: {hasil}")
    return hasil

def aritmatika_sum(a, d, n):
    hasil = n * (a + aritmatika_nth_term(a, d, n)) / 2
    print(f"Jumlah {n} suku pertama barisan aritmatika: {hasil}")
    return hasil

def geometri_nth_term(a, r, n):
    hasil = a * (r ** (n - 1))
    print(f"Barisan Geometri suku ke-{n}: {hasil}")
    return hasil

def geometri_sum(a, r, n):
    if r == 1:
        hasil = a * n
    else:
        hasil = a * (1 - r ** n) / (1 - r)
    print(f"Jumlah {n} suku pertama barisan geometri: {hasil}")
    return hasil

def peluang(kasus, ruang_sampel):
    if ruang_sampel == 0:
        raise ValueError("Ruang sampel tidak boleh nol")
    hasil = kasus / ruang_sampel
    print(f"Peluang: {hasil}")
    return hasil
