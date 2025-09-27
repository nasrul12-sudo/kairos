# apps/leaf/utils/disease_data.py

DISEASE_ANALYSIS = {
    "bercak_daun": {
        "nama": "Bercak Daun",
        "deskripsi": "Penyakit bercak daun disebabkan jamur (Cercospora, Alternaria).",
        "gejala": [
            "Bercak bulat/kecoklatan pada daun",
            "Kadang ada lingkaran konsentris",
            "Daun rontok lebih cepat"
        ],
        "penanganan": [
            "Gunakan fungisida (mankozeb, klorotalonil, tembaga hidroksida)",
            "Buang daun yang terinfeksi berat",
            "Kurangi kelembaban dan perbaiki sirkulasi udara",
            "Lakukan rotasi tanaman dengan non-inang"
        ]
    },
    "sehat": {
        "nama": "Tanaman Sehat",
        "deskripsi": "Tanaman sehat, daun hijau segar tanpa gejala penyakit.",
        "gejala": ["Daun normal hijau segar", "Pertumbuhan optimal", "Tidak ada bercak/keriting"],
        "penanganan": [
            "Pertahankan pemupukan seimbang",
            "Jaga kelembaban ideal",
            "Monitoring rutin",
            "Gunakan pestisida/fungisida preventif bila perlu"
        ]
    },
    "thrips": {
        "nama": "Hama Thrips",
        "deskripsi": "Thrips menyerang daun dengan menghisap cairan tanaman.",
        "gejala": [
            "Daun mengeriting",
            "Belang keperakan",
            "Pertumbuhan terganggu",
            "Bunga rontok"
        ],
        "penanganan": [
            "Gunakan insektisida selektif (spinosad, abamectin, emamectin benzoate)",
            "Pasang perangkap biru berlem",
            "Gunakan agen hayati (Beauveria bassiana, Metarhizium anisopliae)",
            "Hindari pestisida berlebihan yang mematikan musuh alami"
        ]
    },
    "virus_kuning": {
        "nama": "Virus Kuning",
        "deskripsi": "Virus kuning disebabkan Begomovirus yang ditularkan oleh kutu kebul.",
        "gejala": [
            "Daun menguning dan melengkung",
            "Tanaman kerdil",
            "Produksi buah menurun drastis"
        ],
        "penanganan": [
            "Kendalikan kutu kebul dengan insektisida (imidacloprid, thiamethoxam, abamectin)",
            "Pasang perangkap kuning berlem",
            "Gunakan insect net pada persemaian",
            "Cabut tanaman parah agar tidak menular",
            "Rotasi tanaman non-inang (jagung, padi)"
        ]
    }
}
