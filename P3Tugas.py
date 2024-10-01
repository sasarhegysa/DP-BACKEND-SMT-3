# Define the function to calculate salary
def hitung_gaji(golongan, jam_kerja):
    upah_per_jam = {
        'a': 5000,
        'b': 7000,
        'c': 8000,
        'd': 10000
    }

    if golongan in upah_per_jam:
        upah = upah_per_jam[golongan] * jam_kerja
    else:
        return "Golongan tidak valid!"

    lembur = 0
    if jam_kerja > 48:
        lembur = (jam_kerja - 48) * 4000

    total_gaji = upah + lembur
    return total_gaji

nama = input("Masukkan nama: ")
golongan = input("Masukkan golongan (a/b/c/d): ")
jamkerja = int(input("Masukkan Jam Kerja: "))
gaji = hitung_gaji(golongan.lower(), jamkerja)

print(f"{nama} menerima upah: Rp. {gaji}")