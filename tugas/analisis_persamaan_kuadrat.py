print("Analisis Persamaan Kuadrat")
a = float(input("Koefisien a: "))
b = float(input("Koefisien b: "))
c = float(input("Koefisien c: "))

if a == 0:
    print("Bukan persamaan kuadrat.")
else:
    D = (b ** 2) - (4 * a * c)
    print(f"Diskriminan = {D:.2f}")

    if D > 0:
        x1 = (-b + D ** 0.5) / (2 * a)
        x2 = (-b - D ** 0.5) / (2 * a)
        print(f"D > 0, hitung dan tampilkan dua akar real berbeda: x1 = {x1:.2f} dan x2 = {x2:.2f}")
    elif D == 0:
        x = -b / (2 * a)
        print(f"D = 0, hitung dan tampilkan satu akar real kembar: x = {x:.2f}")
    else:
        print("D < 0, hitung dan tampilkan bahwa tidak ada akar real.")