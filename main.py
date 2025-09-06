from utils import konversi_suhu

print("=== PROGRAM KONVERSI SUHU RUANGAN ===")
try:
    # Input dari user
    nilai = float(input("Masukkan nilai suhu: "))
    dari = input("Dari satuan (C/F/K): ").strip()
    ke = input("Ke satuan (C/F/K): ").strip()

    # Proses konversi
    hasil = konversi_suhu(nilai, dari, ke)

    # Output
    if isinstance(hasil, str):  # Jika error
        print(hasil)
    else:
        print(f"Hasil Konversi: {nilai}°{dari.upper()} = {hasil:.2f}°{ke.upper()}")

except ValueError:
    print("Error: Nilai suhu harus berupa angka.")
