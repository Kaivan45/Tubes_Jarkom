# Tubes_Jarkom

# 📡 Panduan Menjalankan Program Client-Server

Ikuti langkah-langkah berikut untuk menjalankan program ini dengan benar:

1. **Atur Alamat IP Komputer**

   Buka Control Panel → Pengaturan Network → Ubah IP Address menjadi `192.168.4.43`.

2. **Jalankan Server**

   Buka terminal, masuk ke direktori proyek, lalu jalankan:

   ```bash
   py server.py

3. **Jalankan Client**
   Buka terminal baru, lalu jalankan perintah:
    ```bash
   py client.py <server_host> <server_port> <filename>
   contoh:
     ```bash
   py client.py 192.168.4.43 8000 index.html
