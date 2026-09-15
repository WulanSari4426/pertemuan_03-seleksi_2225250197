nilai = float(input("Masukkan nilai ujian: "))
kehadiran = int(input("Masukkan persentase kehadiran (%): "))
if kehadiran >= 75:
    if nilai >= 60:
        print("Status: Lulus")
    else:
        print("Status: Tidak Lulus (Nilai kurang)")
else:
    print("Status: Tidak Lulus (Kehadiran kurang dari 75%)")