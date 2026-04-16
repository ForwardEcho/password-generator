# 🛡️ Professional Password Generator

![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)
![Type](https://img.shields.io/badge/category-Cybersecurity-red.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

Sebuah alat pembuat password berbasis CLI yang dirancang khusus untuk keperluan **Cybersecurity** dan **Penetration Testing**. Dilengkapi dengan analisis kekuatan password dan estimasi waktu brute-force secara real-time.

---

## ✨ Fitur Utama

*   🚀 **Custom Generation**: Kendali penuh atas jumlah huruf, angka, dan simbol.
*   📊 **Strength Analysis**: Menilai keamanan password berdasarkan kriteria standar industri.
*   ⏳ **Crack Time Estimation**: Menghitung berapa lama waktu yang dibutuhkan untuk membongkar password menggunakan hardware modern (GPU).
*   🎨 **Cyberpunk UI**: Antarmuka terminal dengan banner ASCII yang keren dan output berwarna.
*   📂 **Batch Output**: Simpan hasil generate langsung ke dalam file `.txt` untuk dijadikan wordlist.

---

## 🛠️ Instalasi

Pastikan Anda sudah menginstal Python di sistem Anda.

1. Clone repositori ini:
   ```bash
   git clone https://github.com/ForwardEcho/password-generator.git
   ```
2. Masuk ke direktori project:
   ```bash
   cd password-generator
   ```

---

## 🚀 Cara Penggunaan

Gunakan argumen berikut untuk menjalankan script:

```bash
python passgenerate.py -l [length] -n [number] -o [output_file] -s [symbol] -d [digit] -a [alphabet]
```

### Argumen:
| Flag | Nama | Deskripsi |
|---|---|---|
| `-l` | `--length` | Total panjang password yang diinginkan. |
| `-n` | `--number` | Jumlah password yang ingin dihasilkan. |
| `-o` | `--output` | Nama file hasil output (ex: `wordlist.txt`). |
| `-s` | `--special` | Jumlah minimal karakter spesial/simbol. |
| `-d` | `--digits` | Jumlah minimal angka. |
| `-a` | `--letters` | Jumlah minimal huruf. |

### Contoh:
Generate **10 password** dengan panjang **16 karakter**, minimal **4 angka** dan **2 simbol**:
```bash
python passgenerate.py -l 16 -n 10 -o wordlist.txt -s 2 -d 4 -a 4
```

---

## 📸 Preview Tampilan
Saat dijalankan, tool ini akan menampilkan analisis seperti ini:
```text
[#] Sample: 7H!pL0@d3r_X9
[#] Strength: Strong
[#] Crack Time: 1245.22 Centuries
[+] Successfully generated 10 passwords!
[+] Saved to: wordlist.txt
```

---

## ⚠️ Disclaimer
Penggunaan tool ini untuk tujuan ilegal adalah dilarang keras. Penulis tidak bertanggung jawab atas penyalahgunaan alat ini. Gunakan untuk keperluan edukasi, riset keamanan, dan pengujian penetrasi yang sah secara hukum.

---

## 👨‍💻 Credits
Created with ❤️ by **ForwardEcho**
