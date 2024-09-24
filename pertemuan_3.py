# Fungsi => Block Code Yang Bisa Digunakan Kembali Saat Dibutuhkan Tanpa Menulis Ulang Code.

# 1. Parameter / Argument
# 2. Return Value
# 3. Fungsi Rekursif
# 4. variable local & global

# () Parenthesis
# Casting => perubahan tipe data
# distractering ( pembongkaran )

# 1. Parameter / Argument
def function(Parameter):
    print(f'Ini Adalah {Parameter}') 

function('Argument')

# 2. Return Value
def operasi_matematika(a , b):
    tambah = a + b
    kurang = a - b
    kali = a * b
    bagi = a / b
    return tambah, kurang, kali, bagi

angka1 = 10
angka2 = 7
tambah, kurang, kali, bagi = operasi_matematika(angka1, angka2)
print(f'Hasil Dari {angka1} + {angka2} = {tambah}')

# 3. Fungsi Rekursif
def Rekursif(n):
    if n == 0:
        return 1
    
    return n * Rekursif(n - 1) # Memanggil Function Kembali ( Lopping )

print(f'Ini Adalah Hasil Dari Rekursif : {Rekursif(4)}')

# 4. variable local & global
a = 10 # Global => Dapat dilihat oleh local tetapi tidak bisa melihat lokal

def lokal():
    a = 5 # Local => Tidak dapat dilihat oleh global tetapi bisa melihat global
    return a
print(f'Ini Adalah Variable Lokal : {lokal()}') # Output 5


# LATIHAN 1 MEMBUAT KALKULATOR SEDERHANA
def pertambahan(a, b):
    return f'Hasil Dari {a} + {b} Adalah {a + b}'

def pengurangan(a, b):
    return f'Hasil Dari {a} - {b} Adalah {a - b}'

def perkalian(a, b):
    return f'Hasil Dari {a} * {b} Adalah {a * b}'

def pembagian(a, b):
    return f'Hasil Dari {a} / {b} Adalah {a / b}'

def masukkanAngka():
    a = int(input('Masukkan Angka Pertama : '))
    b = int(input('Masukkan Angka Kedua : '))
    return a, b

def fungsi():
    inputan_user = input(f'''
=== SELAMAT DATANG DI KALKULATOR SEDERHANA ===
Pilih Menu :
1. Pertambahan
2. Penguranagan
3. Perkalian
4. Pembagian

Silahkan Pilih 1 - 4 : ''')
    if inputan_user == '1':
        a, b = masukkanAngka()
        print(pertambahan(a, b))
    elif inputan_user == '2':
        a, b = masukkanAngka()
        print(pengurangan(a, b))
    elif inputan_user == '3':
        a, b = masukkanAngka()
        print(perkalian(a, b))
    elif inputan_user == '4':
        a, b = masukkanAngka()
        print(pembagian(a, b))
    else:
        kondisi = input(f'Masukkan Angka Yang Benar\nApakah Ingin Mengulangi ? (y/n) : ')
        if kondisi != 'y':
            exit()
        fungsi()

while True:
    fungsi()
    lanjut = input('\nMau Lanjut Apa Tidak : y/n : ')
    if lanjut != 'y':
        break



