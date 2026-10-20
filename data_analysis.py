# Studi Kasus: Make Sense of Data with Analysis and AI

def simulate_data_preparation_and_analytics():
    print("=" * 65)
    print(" SIMULASI TAHAPAN DATA PREPARATION & ANALYTICS (CRISP-DM)")
    print(" Materi: Informatics Practitioner Lecture Series - Andria Arisal")
    print("=" * 65)
    
    raw_data = [
        {"id": 1, "kategori": "Elektronik", "penjualan": 1200000, "status": "Valid"},
        {"id": 2, "kategori": "Pakaian", "penjualan": None, "status": "Missing Value"}, # Data kosong
        {"id": 3, "kategori": "Elektronik", "penjualan": 1500000, "status": "Valid"},
        {"id": 4, "kategori": "Pakaian", "penjualan": 450000, "status": "Valid"}
    ]
    
    print("\n[Tahap 1: Data Understanding & Preparation]")
    print(f"Total Data Mentah Diterima : {len(raw_data)} baris")
    
    clean_data = []
    for item in raw_data:
        if item["penjualan"] is not None:
            clean_data.append(item)
            
    print(f"Data Setelah Dibersihkan   : {len(clean_data)} baris (Data kosong di-drop)\n")
    
    total_revenue = sum(item["penjualan"] for item in clean_data)
    print("[Tahap 2: Analytical Levels]")
    print(f" > Analisis Deskriptif   : Total Pendapatan Saat Ini = Rp {total_revenue:,}")
    
    avg_revenue = total_revenue / len(clean_data)
    projected_next_month = avg_revenue * 1.15
    print(f" > Analisis Prediktif    : Proyeksi Pendapatan Bulan Depan = Rp {projected_next_month:,.0f}")
    
    print("-" * 65)
    print("📌 KESIMPULAN: Proses data preparation yang akurat menghasilkan")
    print("   wawasan (insight) dan keputusan bisnis yang valid.")
    print("=" * 65)

if __name__ == "__main__":
    simulate_data_preparation_and_analytics()