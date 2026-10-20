# Studi Kasus: Introduction to Machine Learning

import random

def simulate_supervised_classification():
    """
    Simulasi Supervised Learning: Klasifikasi (Misal: Prediksi Kelayakan Pinjaman / Spam Email)
    Model belajar dari data berlabel (Fitur -> Label Target).
    """
    print("=" * 60)
    print(" 1. SIMULASI SUPERVISED LEARNING (CLASSIFICATION)")
    print("=" * 60)
    
    dataset = [
        {"pendapatan": 5000, "skor": 750, "target": "Disetujui"},
        {"pendapatan": 2000, "skor": 500, "target": "Ditolak"},
        {"pendapatan": 8000, "skor": 800, "target": "Disetujui"},
        {"pendapatan": 1500, "skor": 450, "target": "Ditolak"}
    ]
    
    for i, data in enumerate(dataset, 1):
        prediksi = "Disetujui" if data["pendapatan"] >= 4000 and data["skor"] >= 650 else "Ditolak"
        print(f"Data #{i} -> Pendapatan: ${data['pendapatan']}, Skor: {data['skor']} | Aktual: {data['target']} | Prediksi Model: {prediksi}")

def simulate_unsupervised_clustering():
    """
    Simulasi Unsupervised Learning: Clustering (Misal: K-Means Pengelompokan Pelanggan)
    Model mencari pola tersembunyi dari data tanpa label target.
    """
    print("\n" + "=" * 60)
    print(" 2. SIMULASI UNSUPERVISED LEARNING (CLUSTERING)")
    print("=" * 60)
    
    for i in range(1, 4):
        total_belanja = random.randint(100, 5000)
        cluster = "Cluster Premium (High Spender)" if total_belanja > 2500 else "Cluster Reguler (Standard Spender)"
        print(f"Pelanggan #{i} -> Total Belanja: ${total_belanja} -> Masuk ke: {cluster}")

if __name__ == "__main__":
    simulate_supervised_classification()
    simulate_unsupervised_clustering()
    print("\n[INFO] Alur kerja ML: Data Collection -> Preprocessing -> Training -> Evaluation selesai.")