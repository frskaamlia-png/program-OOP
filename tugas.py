class Mahasiswa:
    universitas = "STITEK Bontang"

    # Constructor
    def __init__(self, nama, nim, jurusan, ipk=0.0):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan
        self.ipk = ipk

    def perkenalan_diri(self):
        return (f"Halo, saya {self.nama} dengan NIM {self.nim}, "
                f"jurusan {self.jurusan} di {Mahasiswa.universitas}. "
                f"IPK saya {self.ipk:.2f}")

    def update_ipk(self, ipk_baru):
        if 0.0 <= ipk_baru <= 4.0:
            self.ipk = ipk_baru
            return f"IPK {self.nama} berhasil diperbarui menjadi {self.ipk:.2f}"
        return "IPK tidak valid, harus antara 0.0 sampai 4.0"

    def predikat_kelulusan(self):
        if self.ipk >= 3.5:
            return "Cum Laude"
        elif self.ipk >= 3.0:
            return "Sangat Memuaskan"
        elif self.ipk >= 2.5:
            return "Memuaskan"
        elif self.ipk >= 2.0:
            return "Lulus"
        return "Tidak Lulus"



mhs1 = Mahasiswa("Budi Santoso", "TI001", "Teknik Informatika", 3.75)
mhs2 = Mahasiswa("Siti Aminah", "TI002", "Teknik Informatika", 3.20)
mhs3 = Mahasiswa("Andi Pratama", "TI003", "Teknik Informatika")  # ipk default 0.0


print("=== perkenalan_diri() ===")
for mhs in (mhs1, mhs2, mhs3):
    print(mhs.perkenalan_diri())

print("\n=== predikat_kelulusan() ===")
for mhs in (mhs1, mhs2, mhs3):
    print(f"{mhs.nama}: IPK {mhs.ipk:.2f} -> {mhs.predikat_kelulusan()}")

print("\n=== update_ipk() ===")
print(mhs3.update_ipk(2.60))
print(mhs2.update_ipk(2.10))
print(mhs1.update_ipk(4.5))  

print("\n=== Setelah update_ipk() ===")
for mhs in (mhs1, mhs2, mhs3):
    print(f"{mhs.nama}: IPK {mhs.ipk:.2f} -> {mhs.predikat_kelulusan()}")


print(f"\nUniversitas: {Mahasiswa.universitas}")