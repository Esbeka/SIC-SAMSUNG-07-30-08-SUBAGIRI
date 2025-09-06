def konversi_suhu(nilai, dari, ke):
    # Normalisasi input ke huruf kecil
    dari = dari.lower()
    ke = ke.lower()

    # Validasi satuan
    satuan_valid = ["c", "f", "k"]
    if dari not in satuan_valid or ke not in satuan_valid:
        return "Error: Satuan tidak valid. Gunakan 'C', 'F', atau 'K'."

    # Validasi nilai (khusus Kelvin)
    if dari == "k" and nilai < 0:
        return "Error: Suhu Kelvin tidak boleh negatif."

    # Jika satuan sama, langsung kembalikan nilai
    if dari == ke:
        return nilai

    # Konversi Celsius
    if dari == "c":
        if ke == "f":
            return (nilai * 9/5) + 32
        elif ke == "k":
            return nilai + 273.15

    # Konversi Fahrenheit
    if dari == "f":
        if ke == "c":
            return (nilai - 32) * 5/9
        elif ke == "k":
            return (nilai - 32) * 5/9 + 273.15

    # Konversi Kelvin
    if dari == "k":
        if ke == "c":
            return nilai - 273.15
        elif ke == "f":
            return (nilai - 273.15) * 9/5 + 32

    return "Error: Konversi tidak valid."
