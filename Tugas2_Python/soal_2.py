harga = int(input("Masukkan total belanja: "))
member = input("Apakah member(y/n): ")
if member == 'y':
  if harga <500000:
    diskon = 5 
  if harga >500000 and harga <=1000000:
    diskon = 7
  elif harga >1000000:
    diskon = 8
else: 
  if harga >500000 and harga <=1000000:
    diskon = 2
  elif harga >1000000:
    diskon = 3
  elif harga <500000:
    diskon = 0

print(f"Total diskon anda {diskon}%")