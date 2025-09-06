def konversi_suhu(nilai, dari, ke):
    # Normalize input ke lowercase
    dari = dari.lower()
    ke = ke.lower()

    # Validasi satuan
    if dari not in ["c", "f", "k"] or ke not in ["c", "f", "k"]:
        return "Error: Satuan tidak valid. Gunakan 'C', 'F', atau 'K'."

    # Validasi nilai (Kelvin tidak boleh negatif)
    if dari == "k" and nilai < 0:
        return "Error: Suhu Kelvin tidak boleh negatif."

    # Jika satuan asal dan tujuan sama
    if dari == ke:
        return nilai

    # Konversi dari Celsius
    if dari == "c":
        if ke == "f":
            return (nilai * 9/5) + 32
        elif ke == "k":
            return nilai + 273.15

    # Konversi dari Fahrenheit
    if dari == "f":
        if ke == "c":
            return (nilai - 32) * 5/9
        elif ke == "k":
            return (nilai - 32) * 5/9 + 273.15

    # Konversi dari Kelvin
    if dari == "k":
        if ke == "c":
            return nilai - 273.15
        elif ke == "f":
            return (nilai - 273.15) * 9/5 + 32

    return "Error: Konversi tidak valid."
