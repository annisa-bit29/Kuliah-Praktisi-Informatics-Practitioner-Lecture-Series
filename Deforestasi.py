import os
import random

# Studi Kasus: Simulasi Dataset Kategori Deforestasi 
CATEGORIES = [
    "Forest (Hutan Sehat)",
    "Small-Scale Agriculture (Pertanian Skala Kecil)",
    "Large-Scale Agriculture (Pertanian Skala Besar)",
    "Infrastructure/Road (Pengembangan Jalan)",
    "Mining (Pertambangan)",
    "Wildfire/Fire (Kebakaran Hutan)"
]

def simulate_image_feature_extraction():
    """
    Simulasi ekstraksi fitur dari Citra Satelit (Sentinel-2 & Sentinel-1).
    Mengembalikan nilai vegetasi (NDVI) dan variansi struktur (Radar Backscatter).
    """
    ndvi_index = round(random.uniform(-0.1, 0.9), 2)  
    radar_backscatter = round(random.uniform(-20.0, -5.0), 2) 
    return ndvi_index, radar_backscatter

def classify_deforestation_driver(ndvi, radar):
    """
    Model aturan/klasifikasi sederhana untuk menentukan driver deforestasi.
    """
    if ndvi > 0.6:
        return "Forest (Hutan Sehat)"
    elif ndvi < 0.2 and radar > -10.0:
        return "Mining (Pertambangan) / Infrastructure"
    elif ndvi < 0.3 and radar <= -10.0:
        return "Wildfire/Fire (Kebakaran Hutan)"
    else:
        return "Small-Scale / Large-Scale Agriculture"

def main():
    print("=" * 60)
    print("SIMULASI ATRIBUSI DRIVER DEFORESTASI DARI CITRA SATELIT")
    print("Materi: Informatics Practitioner Lecture Series - Dr. Bart Slachter")
    print("=" * 60)
    
    for i in range(1, 6):
        ndvi, radar = simulate_image_feature_extraction()
        prediction = classify_deforestation_driver(ndvi, radar)
        
        print(f"\n[Sampel Citra Satelit #{i}]")
        print(f"  > Sentinel-2 NDVI Index       : {ndvi}")
        print(f"  > Sentinel-1 Radar Backscatter : {radar} dB")
        print(f"  > Hasil Klasifikasi AI         : {prediction}")

if __name__ == "__main__":
    main()