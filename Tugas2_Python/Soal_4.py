num = int(input("Masukkan nilai n: "))

for i in range(num): #baris
    for j in range(num): #kolom
        if i==0 or i==num-1 or j==0 or j==num-1:
            print("*",end="")
        else:
            print("#",end="")
    print("")