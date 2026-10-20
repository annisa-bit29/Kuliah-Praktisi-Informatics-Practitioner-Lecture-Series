import os
# Studi Kasus: Human-Computer Interaction & Data Visualization
def display_ascii_dashboard():
    """
    Simulasi Visualisasi Data / Dashboard Interaktif Sederhana
    Menerapkan prinsip Human-Computer Interaction (HCI) & Data Visualization:
    - Minim Chartjunk
    - High Data-Ink Ratio
    - Clear Visual Hierarchy
    """
    print("=" * 60)
    print("       DASHBOARD ANALISIS INTERAKSI PENGGUNA & VISUALISASI DATA       ")
    print("       Studi Kasus: Informatics Practitioner Lecture Series - BRIN        ")
    print("=" * 60)
    print("\n[ VISUALISASI TREN BEBAN KOGNITIF PENGGUNA (Cognitive Load) ]")
    print("Hukum Gestalt & Principles: Recognition over Recall\n")
    
    metrics = {
        "Sistem A (Tanpa UCD)": 78,
        "Sistem B (Dengan UCD)": 35,
        "Sistem C (Desain Iteratif)": 15
    }
    
    for system, load_score in metrics.items():
        bar = "█" * (load_score // 2)
        print(f"{system:<28} | {bar} ({load_score}% Extraneous Load)")
        
    print("\n" + "-" * 60)
    print("📌 KESIMPULAN DASHBOARD:")
    print("   Penerapan User-Centered Design (UCD) berhasil menurunkan")
    print("   extraneous load pengguna hingga 63%.")
    print("-" * 60)

if __name__ == "__main__":
    display_ascii_dashboard()