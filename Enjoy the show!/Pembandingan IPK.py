
# Imports, biarin ae wkwk
import numpy as np
"""
Daftar ipk dari kakak, kalo mau coba bikin tanpa make fungsi ipk_teman()
Kalo ga pake ipk_teman() berarti kesulitannya adalah bintang 3 ya (ipk_teman() itu sendiri 1 bintang wkwk)
"""
daftar_ipk = [2.8766969084366676, 3.5501030859378884, 3.7998245337441334, 3.8996071331873563, 3.5950592163442026, 3.362567990299601,
              3.538809951200334, 3.948128740862157, 3.9715933785472766, 2.8344887203511457]
def hitung_ipk():
    """
    Memasukkan IPKmu dan temanmu kedalam daftar ipk.\n
    Masukkan huruf apapun untuk menghentikan proses input. \n
    Output method ini adalah: \n
    IPK saya lebih tinggi/rendah dari teman-teman saya.
    """
    ipkku = input("Masukkan ipkmu: ")
    daftar_ipk.append(ipkku)
    ipk_teman() # Opsional pake ini aja
    # Lengkapin ini ya
    
    # Output ini diedit ya wkwk
    print("IPK saya lebih tinggi/rendah dari teman-teman saya.")
    
    
def ipk_teman():
    """
    Memasukkan ipk teman kedalam daftar ipk.\n
    Masukkan huruf apapun untuk menghentikan proses input.
    """
    daftar_ipk.clear()
    # Lengkapin ini yak


def hitung_posisi_ipk(ipk_ku):
    """
    Menghitung rata-rata IPK semua orang dan mereturn posisi IPKmu(diatas rata-rata atau dibawahnya)
    """
    # lengkapin ini ya
    posisi = "Belum tahu"    
    
    # Ini outputnya
    return posisi


def avg_ipk(df = daftar_ipk):
    """ Mereturn rata-rata dari semua ipk didalam daftar"""
    return np.mean(df)