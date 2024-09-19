# TIPE DATA 
integer = 11 # DATA INTEGER
float_data = 12.5 # DATA FLOAT
string = 'hello world' # DATA STRING
data_benar = True # False # DATA BOOLEAN

print(f'''Integer : {type(integer)}
Float : {type(float_data)}
String : {type(string)}
Boolean : {type(data_benar)}
''')

# OPERATOR DAN OPERAND
# a, b, c, d, e, f Adalah Variable
# Tetapi jika di operatorkan a - f adalah Operand
a = 10 
b = 20
c = 30
d = 40
e = 34
f = 5

# Operator Aritmatik
penjumlahan = a + b # Output = 30
pengurangan = c - a # Output = 20
pembagian = d / a # Output = 4
perkalian = c * a # Output = 300
modulus = d % c # Output = 10
pangkat = c ** f # Output = 24300000
floor_devision = e // f  # yang mendekati hasil. Output = 6
print(f'''Penjumlahan {a} + {b} = {penjumlahan}
Pengurangan {c} - {a} = {pengurangan}
Pembagian {d} / {a} = {pembagian}
Perkalian {c} * {a} = {perkalian}
Modulus {d} % {c} = {modulus}
Pangkat {c} ** {f} = {pangkat}
Floor Devision {e} // {f} = {floor_devision}
''')

bilangan =  16
# Menentukan Bilangan Bulat atau Ganjil
print(f"{bilangan} Adalah Bilangan Genap" if bilangan % 2 == 0 else f"{bilangan} Adalah Bilangan Ganjil")

# Operator Relasi
sama_dengan = a == a # True
lebih_dari = a > b # False
lebih_sama_dengan =  d >= b # True
kurang_dari = a < b # True
kurang_sama_dengan = d < a # False
tidak_sama_dengan = c !=  a # True

# Operator Logika
print(f'''
Operator And : True && False = {True and False}
Operator Or : True || False = {True or False}
Operator Not : !True = {not True}
''')