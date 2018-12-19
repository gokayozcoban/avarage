

sayılar = 0
girilen_sayılar = []
for i in range(10):
    veri = int(input("{}. sayı: ".format(i+1)))
    sayılar += veri
    girilen_sayılar += [veri]
print("Girilen sayılar: ",*girilen_sayılar)
print("Ortalaması: ",sayılar/10)
