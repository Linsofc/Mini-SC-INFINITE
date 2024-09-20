# Jenis Jenis Algoritma

## Sequence ( Sesuai Urutan ) ##
## Branches ( Bercabang ) ##
## Iteration ( Lopping / Pengulangan ) ##


## Sequence ( Sesuai Urutan )
print('ini urutan pertama')
print('ini urutan kedua')
print('ini urutan ketiga')


## Branches ( Bercabang ) ##
# if Statement
a = 10
if a == 10:
    print('a adalah 10')
elif a == 11:
    print('a adalah 11')

# else Statement
if a == 9:
    print('a adalah 9')
else:
    print('Data Bukan 9')

# Mengecek Inputan User Termasuk Bilangan Ganjil Atau Genap
bilangan = int(input('Masukkan Angka: ')) 
print(f"{bilangan} Adalah Bilangan Genap" if bilangan % 2 == 0 else f"{bilangan} Adalah Bilangan Ganjil") # Formated String 


## Iteration ( Lopping / Pengulangan ) ##
# statement break, continue dan pass
# Statement break ( Berhenti )
b = 1
while(b < 5) :
    print(f'Break : {b}')
    b += 1
    if b == 3:
        break

# Statement continue ( Berhenti Saat Perkondisian Dan Dilanjut Setelah Itu)
c = 0
while(c < 5):
    c += 1
    if c == 3:
        continue
    print(f'Continue : {c}')

# Statement pass ( hanya untuk placeholder untuk kode mendatang )
p = 0
while(p < 3):
    p += 1
    if p == 2:
        pass # tidak ada yang terjadi 
    print(f'pass : {p}')


# for i in rage(start, stop, step)

# Kondisi 1 Parameter
# start ( mengulangi nilai sebanayk yang ditentukan )
for i in range(3): # dimulai dari 0
    print('start :', i)

# Kondisi 2 Parameter
# stop ( mengurang 1 hasil dari stop 5 - 1 = 4 jadi stop di angka 4)
for i in range(1, 5):
    print('stop :', i)

# Kondisi 3 Parameter 
# step ( menambah nilai start 1 + 2 + 2 dst)
for i in range(1, 5, 2):
    print('step kondisi :', i)


data_satu = 1 # SNACK CASE
dataSatu = 1 # CAMEL CASE