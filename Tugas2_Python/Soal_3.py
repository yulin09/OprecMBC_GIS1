print("Warna Seragam Telkom University")
print("-------------------------------")

Hari = str(input("Masukan Hari(Dengan awalan kapital):"))
if Hari=="Senin":
    print("Memakai seragam merah")
elif Hari=="Kamis" or Hari=="Sabtu":
    print("Memakai seragam bebas")
elif Hari=="Selasa" or Hari=="Rabu":
    print("Memakai seragam putih")
elif Hari=="Jumat":
    print("Memakai seragam batik")
else:
    print("Seragam tidak ada")