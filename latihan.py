def pertambahan(a, b):
    return f'Hasil Dari {a} + {b} Adalah {a + b}'

def pengurangan(a, b):
    return f'Hasil Dari {a} - {b} Adalah {a - b}'

def perkalian(a, b):
    return f'Hasil Dari {a} * {b} Adalah {a * b}'

def pembagian(a, b):
    return f'Hasil Dari {a} / {b} Adalah {a / b}'


def fungsi():
    inputan_user = input(f'''Pilih Menu :
1. Pertambahan
2. Penguranagan
3. Perkalian
4. Pembagian

Silahkan Pilih 1 - 4
''')
    a = int(input('Masukkan Angka Pertama : '))
    b = int(input('Masukkan Angka Kedua : '))
    if inputan_user == '1':
        print(pertambahan(a, b))
    elif inputan_user == '2':
        print(pengurangan(a, b))
    elif inputan_user == '3':
        print(perkalian(a, b))
    elif inputan_user == '4':
        print(pembagian(a, b))
    else:
        print('Masukkan Angka Yang Benar')
        fungsi()

while True:
    fungsi()
    lanjut = input('Mau Lanjut Apa Tidak : y/n : ')
    if lanjut != 'y':
        break

