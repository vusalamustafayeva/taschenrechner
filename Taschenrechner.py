# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""



#Istifadeciden bir eded al ve bir riyazi emel secdir
def taschenrechner():
    # İki eded al
    eded1 = float(input("Birinci ededi yazin: "))
    eded2 = float(input("İkinci ededi yazin: "))
    
    # Riyazi emelleri gösterek
    print("Lütfen etmek istediyiniz emeli seçin:")
    print("1. Toplama")
    print("2. Çıxama")
    print("3. Vurma")
    print("4. Bölme")
    
    # Istifadecidan birini seçmesini iste
    secim = input("Seçiminiz (1/2/3/4): ")
    
    # Seçime göre ededi hesablayaq ve ekrana yazdıraq
    if secim == "1":
        netice = eded1 + eded2
        print(f"{eded1} + {eded2} = {netice}")
    elif secim == "2":
        netice = eded1 - eded2
        print(f"{eded1} - {eded2} = {netice}")
    elif secim == "3":
        netice = eded1 * eded2
        print(f"{eded1} * {eded2} = {netice}")
    elif secim == "4":
        netice = eded1 / eded2
        print(f"{eded1} / {eded2} = {netice}")
    else:
        print("Düzgün seçim etmediniz.")
        
# Fonksiyonu çağıraq
taschenrechner()
