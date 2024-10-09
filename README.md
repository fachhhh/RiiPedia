# RiiPedia
## First PBP Individual Project by
### Hadyan Fachri
### 2306245030
### PBP A

## PWS
[RiiPedia](http://hadyan-fachri-riipedia.pbp.cs.ui.ac.id/)

## Wiki for README.md Archieve
- [Tugas Individu 2](https://github.com/fachhhh/RiiPedia/wiki/Archieve-Tugas-Individu-2-PBP)
- [Tugas Individu 3](https://github.com/fachhhh/RiiPedia/wiki/Archieve-Tugas-Individu-3-PBP)
- [Tugas Individu 4](https://github.com/fachhhh/RiiPedia/wiki/Archieve-Tugas-Individu-4-PBP)
- [Tugas Individu 5](https://github.com/fachhhh/RiiPedia/wiki/Archieve-Tugas-Individu-5-PBP)

## Checkpoint Tugas Individu 6
✔ Mengubah tugas 5 yang telah dibuat sebelumnya menjadi menggunakan AJAX.
- AJAX GET
    - Ubahlah kode cards data mood agar dapat mendukung AJAX GET.
    - Lakukan pengambilan data mood menggunakan AJAX GET. Pastikan bahwa data yang diambil hanyalah data milik pengguna yang logged-in.
- AJAX POST
    - Buatlah sebuah tombol yang membuka sebuah modal dengan form untuk menambahkan mood.
    - Buatlah fungsi view baru untuk menambahkan mood baru ke dalam basis data.
    - Buatlah path /create-ajax/ yang mengarah ke fungsi view yang baru kamu buat.
    - Hubungkan form yang telah kamu buat di dalam modal kamu ke path /create-ajax/.
    - Lakukan refresh pada halaman utama secara asinkronus untuk menampilkan daftar mood terbaru tanpa reload halaman utama secara keseluruhan.\
✔ Menjawab beberapa pertanyaan berikut pada README.md pada root folder (silakan modifikasi README.md yang telah kamu buat sebelumnya; tambahkan subjudul untuk setiap tugas).

### 1. Jelaskan manfaat dari penggunaan JavaScript dalam pengembangan aplikasi web!
Jawab:\
JavaScript mempunyai beberapa manfaat dalam pengembangan aplikasi web.\

1. **Interaktif dan Responsif**\
JavaScript memungkinkan developer untuk membuat elemen antarmuka user (UI) yang interaktif dan pastinya responsif. Yang mana bermanfaat untuk para user mendapatkan pengalaman yang terbaik saat mengunjungi website tsb.

2. **Client-Side Processing**\
Ketika JavaScript berjalan di sebuah browser, pengolahan data bisa dilakukan tanpa harus mengirim permintaan ke server yang mana dapat mengurangi beban server dan meningkatkan kecepatan aplikasi.\

3. **Integrasi dengan HTML dan CSS**\
Sangat udah untuk mengintegrasikan JavaScript dengan HTML dan CSS yang mana memudahkan developer untuk memanipulasi elemen DOM secara langsung dan mengubah tampilan secara dinamis.\

4. **Framework dan Library yang kuat**\
Terdapat banyak framework dan library JavaScript yang dapat membantu developer mengembangkan aplikasi seperti React, Angular, Vue.js, dan jQuery. Framework tsb menyediakan struktur dan komponen yang reusable untuk membangun aplikasi web yang kompleks.\

5. **Kompatibilitas Cross-Browser**\
JavaScript didukung oleh hampir semua browser modern, sehingga aplikasi web berbasis JavaScript dapat berjalan di berbagai platform tanpa banyak perubahan.\

6. **Pengembangan Aplikasi Front-End dan Back-End**\
Node.js dapat digunakan untuk back-end dari sebuah JavaScript dan memungkinkan developer untuk menggunakan satu bahasa dalam dua fungsi yaitu back-end dan front-end.

7. **Real-time Interaction**\
Javascript sangat mendukung interaksi real-time dengan server menggunakan teknologi seperti AJAX. AJAX dapat membuat aplikasi seperti chat, notifikasi, atau update secara real-time dan tanpa reload halaman.\

8. **Dukungan Komunitas dan Ekosistem yang Besar**\
JavaScript mempunyai komunitas yang besar dan aktif. Yang mana sangat bermanfaat untuk developer baru karena mempunyai tempat belajar yang sangat luas.

### 2.  Jelaskan fungsi dari penggunaan await ketika kita menggunakan fetch()! Apa yang akan terjadi jika kita tidak menggunakan await?
Jawab:\
Await dalam Javascript digunakan untuk menangani operasi asynchronous. Contohnya `fetch()`. Ada dua fungsi await dalam `fetch()`:\
1. **Menunggu Hasil `fetch()`**\
`fetch()` adalah operasi asynchronous yang mana akan mengembalikan sebuah promise. Ketika `fetch()` bekerja, await akan menunggu pekerjaan `fetch()` selesai sebelum lanjut ke baris selanjutnya.

```
const response = await fetch('https://api.example.com/data');
const data = await response.json();
console.log(data);
```

2. **Menghindari Callback Hell**\
Await membuat penanganan kode asynchronous menjadi lebih mudah ditulis dan dibaca. Hanya dengan `.then()` dan `.catch()` bisa menghemat banyak callback.\
\
Jika tidak menggunakan await dalam operasi `fetch()` maka tidak akan menunggu response. Misal operasi `fetch()` dilakukan membutuhkan waktu yang lama. Jika tidak ada await, program akan mengeksekusi tanpa menunggu operasi `fetch()` selesai. Kemudian jika tidak ada await, kita harus menggunakan `.then()` yang mana harus menangani promise dari await jika ingin mendapatkan hasil dari operasi `fetch()`.

```
fetch('https://api.example.com/data')
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error('Error:', error));
```

### 3. Mengapa kita perlu menggunakan decorator csrf_exempt pada view yang akan digunakan untuk AJAX POST?
Jawab:\
Decorator csrf_exempt membuat Django tidak perlu mengecek keberadaan csrf_token pada POST request yang dikirimkan ke fungsi ini. Secara default, Django menerapkan perlindungan CSRF untuk semua permintaan POST, yang bertujuan untuk melindungi aplikasi web dari serangan CSRF. Namun, dalam kasus tertentu, terutama saat menangani AJAX requests, kita mungkin perlu mengecualikan view dari perlindungan ini menggunakan `@csrf_exempt`.

### 4. Pada tutorial PBP minggu ini, pembersihan data input pengguna dilakukan di belakang (backend) juga. Mengapa hal tersebut tidak dilakukan di frontend saja?
Jawab:\
Ada beberapa alasan mengapa pembersihan data di backend perlu dilakukan.
1. **Frontend Tidak Dapat Dipercaya Sepenuhnya**
Validasi di frontend, meskipun penting untuk pengalaman user, tidak dapat diandalkan untuk keamanan. User atau hacker bisa dengan mudah memanipulasi kode JavaScript di browser mereka atau menggunakan alat seperti Postman untuk mengirim data langsung ke server, melewati frontend sepenuhnya. Oleh karena itu, pembersihan data di backend adalah langkah penting untuk melindungi aplikasi dari input berbahaya.\

2. **Mencegah Serangan Keamanan (Security Attacks)**\
Tanpa pembersihan data di backend, aplikasi rentan terhadap berbagai serangan, seperti SQL Injection, XSS maupun Remote Code Execution.\

3. **Memastikan Konsistensi Validasi**\
Validasi di backend memastikan konsistensi. Semua input akan diproses dan dibersihkan dengan cara yang sama.\

4. **Multi-Client Environment**\
Jika pembersihan hanya dilakukan di frontend, maka input dari sumber lain yang tidak melalui validasi frontend bisa mengandung data berbahaya. Dengan pembersihan di backend, semua data yang masuk dari berbagai sumber akan diperlakukan dengan sama aman.\

5. **Kepatuhan Terhadap Standar Keamanan**\
Banyak standar keamanan dan praktik terbaik yang direkomendasikan oleh industri, seperti OWASP (Open Web Application Security Project), yang menekankan bahwa validasi dan sanitasi data harus dilakukan di backend, karena hanya backend yang bisa sepenuhnya dikontrol dan diamankan oleh developer.

### 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!
Jawab:\
Karena tugas 6 mengganti add form normal yang sebelumnya memakai page create product entry. yang mana kita perlu menuju page lain dan reload setelah input produk baru. Kali ini memakai AJAX (Asynchronous JavaScript And XML).\
\
Konsep AJAX dalam menggantikan form normal seperti pada tugas yang Anda kerjakan untuk create product entry adalah untuk meningkatkan pengalaman pengguna (user experience) dengan menghindari page reload dan mempercepat proses input data. Pada implementasi sebelumnya, pengguna harus diarahkan ke halaman lain (form page) untuk menambahkan produk baru, dan setelah mengirim form, halaman perlu di-reload atau pengguna harus kembali ke halaman sebelumnya. 
Memory updated
Konsep AJAX dalam menggantikan form normal seperti pada tugas yang Anda kerjakan untuk create product entry adalah untuk meningkatkan pengalaman pengguna (user experience) dengan menghindari page reload dan mempercepat proses input data. Pada implementasi sebelumnya, pengguna harus diarahkan ke halaman lain (form page) untuk menambahkan produk baru, dan setelah mengirim form, halaman perlu di-reload atau pengguna harus kembali ke halaman sebelumnya. Dengan menggunakan AJAX dan modal, konsepnya adalah sebagai berikut\
1. **Pengguna Tetap di Halaman yang Sama**
2. **Asynchronous Request (AJAX)**
3. **Feedback Instan**
4. **Pengalaman Pengguna yang Lebih Baik**\
\
Yang pertama kali saya lakukan adalah membuat function add product entry ajax dengan sedikit modifikasi validasi input.
```
@csrf_exempt
@require_POST
def add_product_entry_ajax(request):
    try:
        name = request.POST.get("name")
        price = request.POST.get("price")
        quantity = request.POST.get("quantity")
        description = request.POST.get("description")
        
        # Validasi input
        if not all([name, price, quantity, description]):
            return JsonResponse({
                "status": False,
                "message": "Semua field harus diisi!"
            }, status=400)
        
        # Konversi price dan quantity ke integer
        try:
            price = int(price)
            quantity = int(quantity)
        except ValueError:
            return JsonResponse({
                "status": False,
                "message": "Price dan quantity harus berupa angka!"
            }, status=400)

        # Buat produk baru
        new_product = Ecommerce.objects.create(
            user=request.user,
            name=name,
            price=price,
            quantity=quantity,
            description=description
        )

        # Serialize produk untuk response
        return JsonResponse({
            "status": True,
            "message": "Product berhasil ditambahkan!",
            "product": {
                "id": str(new_product.id),
                "name": new_product.name,
                "price": new_product.price,
                "quantity": new_product.quantity,
                "description": new_product.description,
            }
        }, status=201)

    except Exception as e:
        return JsonResponse({
            "status": False,
            "message": str(e)
        }, status=500)
```
Setelah itu modifikasi sedikit di bagian show_main dan show_json sekaligus show_xml untuk memfilter sesuai id primary key dan set url add_product_entry_ajax di urls.py\
\
Kemudian karena AJAX membutuhkan modal maka modifikasi html dan css pada main.html dan membuat fungsi dengan `getProductEntries()`, `refreshProductEntries()`, `openModal(id)`, `closeModal(id)` dan `addProductEntry(event)`.

## Terima Kasih