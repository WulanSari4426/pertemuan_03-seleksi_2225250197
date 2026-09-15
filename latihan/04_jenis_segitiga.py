s1 = float(input("Sisi 1: "))
s2 = float(input("Sisi 2: "))
s3 = float(input("Sisi 3: "))

if s1 == s2 and s2 == s3:
    print("Segitiga Sama Sisi")
elif s1 == s2 or s2 == s3 or s1 == s3:
    print("Segitiga Sama Kaki")
else:
    print("Segitiga Sembarang")