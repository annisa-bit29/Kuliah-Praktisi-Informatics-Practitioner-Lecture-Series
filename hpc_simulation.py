# Studi Kasus: Bridging Global Infrastructure to Address Local Challenge with HPC

import time

def simulate_heavy_computation(data_id):
    """
    Mensimulasikan pemrosesan data berat (misal: simulasi cuaca/iklim atau analisis molekuler)
    yang biasanya dijalankan secara paralel menggunakan infrastruktur HPC.
    """
    start_time = time.time()
    total = sum(i * i for i in range(1000000))
    duration = time.time() - start_time
    return data_id, round(duration, 4)

def simulate_hpc_parallel_processing():
    print("=" * 65)
    print(" SIMULASI PEMROSESAN DATA SKALA BESAR BERBASIS HPC")
    print(" Materi: Informatics Practitioner Lecture Series - Dr. Warawan")
    print("=" * 65)
    print("\n[INFO] Menjalankan simulasi simulasi lingkungan/iklim paralel...")
    
    datasets = ["Dataset_Cuaca_Wilayah_A", "Dataset_Kualitas_Udara_B", "Dataset_Mitigasi_Bencana_C"]
    
    start_total = time.time()
    for ds in datasets:
        ds_id, durasi = simulate_heavy_computation(ds)
        print(f" > Memproses {ds_id:<28} | Waktu Eksekusi: {durasi} detik")
        
    total_duration = round(time.time() - start_total, 4)
    print("-" * 65)
    print(f"📌 Total Waktu Pemrosesan Paralel HPC : {total_duration} detik")
    print("   Pemanfaatan arsitektur superkomputer mempercepat penyelesaian")
    print("   simulasi lingkungan lokal secara signifikan.")
    print("=" * 65)

if __name__ == "__main__":
    simulate_hpc_parallel_processing()