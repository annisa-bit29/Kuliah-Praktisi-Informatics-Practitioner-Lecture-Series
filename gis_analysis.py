# Studi Kasus: Career and Competition in Industrial Era with GIS

import random

def simulate_gis_spatial_analysis():
    """
    Simulasi Pemrosesan Data Spasial Sederhana (Konsep GeoPandas / QGIS)
    Menganalisis koordinat lokasi aset untuk mendeteksi aset di dalam area bahaya/risiko.
    """
    print("=" * 65)
    print(" SIMULASI ANALISIS SPASIAL ASET KOTA BERBASIS GEOSPASIAL (GIS)")
    print(" Materi: Informatics Practitioner Lecture Series - Widi Primadepa")
    print("=" * 65)
    
    hazard_zone = {"lat_min": -3.80, "lat_max": -3.75, "lon_min": 102.25, "lon_max": 102.30}
    
    print(f"\n[Batas Geografis Area Bahaya Banjir]:")
    print(f"Latitude: {hazard_zone['lat_min']} s/d {hazard_zone['lat_max']} | Longitude: {hazard_zone['lon_min']} s/d {hazard_zone['lon_max']}\n")
    
    assets = [
        {"id": "AST-001", "nama": "Pompa Air Utama", "lat": -3.77, "lon": 102.27},
        {"id": "AST-002", "nama": "Gardu Induk B", "lat": -3.85, "lon": 102.20},
        {"id": "AST-003", "nama": "Sensor Cuaca A", "lat": -3.78, "lon": 102.29},
        {"id": "AST-004", "nama": "Fasilitas Server C", "lat": -3.70, "lon": 102.35}
    ]
    
    print("Hasil Spatial Overlay / Filtering Status Aset:")
    print("-" * 65)
    
    for asset in assets:
        in_lat = hazard_zone["lat_min"] <= asset["lat"] <= hazard_zone["lat_max"]
        in_lon = hazard_zone["lon_min"] <= asset["lon"] <= hazard_zone["lon_max"]
        
        if in_lat and in_lon:
            status = "⚠️ RISIKO TINGGI (Dalam Zona Bahaya)"
        else:
            status = "✅ AMAN (Luar Zona Bahaya)"
            
        print(f"ID: {asset['id']} | Aset: {asset['nama']:<18} | Lat: {asset['lat']}, Lon: {asset['lon']} -> {status}")

if __name__ == "__main__":
    simulate_gis_spatial_analysis()