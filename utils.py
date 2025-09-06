def konversi_suhu(nilai, dari, ke):
    dari = dari.lower()
    ke = ke.lower()
    if dari not in ["c", "f", "k"] or ke not in ["c", "f", "k"]:
        return "Error: satuan tidak valid. Gunakan 'C', 'F', atau 'K'."
    if dari == "k" and nilai < 0:
        return "Error: Suhu Kelvin tidak boleh negatif."
    if dari == "c":
        c = nilai
    elif dari == "f":
        c = (nilai - 32) * 5/9
    elif dari == "k":
        c = nilai - 273.15
    if ke == "c":
        hasil = c
    elif ke == "f":
        hasil = (c * 9/5) + 32
    elif ke == "k":
        hasil = c + 273.15
    return hasil