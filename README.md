# RiiPedia
## First PBP Individual Project by
### Hadyan Fachri
### 2306245030
### PBP A

## Checkpoint
✔  Membuat sebuah proyek Django baru\
✔  Membuat aplikasi dengan nama main pada proyek tersebut\
✔  Melakukan routing pada proyek agar dapat menjalankan aplikasi main\
✔  Membuat model pada aplikasi main dengan nama Product dan memiliki atribut wajib sebagai berikut:\
&ensp; * name\
&ensp; * price\
&ensp; * quantity\
&ensp; * description\
✔  Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.\
✔  Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py\
✔  Melakukan deployment ke PWS terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.\
✔  Membuat sebuah README.md yang berisi tautan menuju aplikasi PWS yang sudah di-deploy, serta jawaban dari beberapa pertanyaan berikut.\

### 1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
jawab:\
    Sebelum membuat sebuah proyek Django baru, kita harus menginstalasi Django terlebih dahulu dan mengaktifkan *Virtual Environtment*. Fungsi *Virtual Environtment* sendiri adalah memungkinkan user untuk memiliki beberapa versi pake bahasa pemrograman dan pemrograman lain di komputer sama, sekaligus menjaga agar *package* dan *dependedncies* dari aplikasi tetap terisolasi sehingga tidak menimbulkan konflik.\
    \
    Pertama saya buka command prompt dan atur path menuju folder lokal yang sudah saya siapkan untuk menyimpan segala sesuatu *file* pemrograman proyek ini. Membuat *Virtual Environment* bisa dilakukan dengan menjalankan perintah `python -m venv env` lalu diaktifkan dengan perintah `env\Scripts\activate`. Jika baris input terminal sudah ditandai `(env)` maka *Virtual Environment* sudah aktif.\
    \
    Selanjutnya, saya membuat *dependencies* di *file* `requirements.txt` yang berisikan\
    > django\gunicorn\whitenoise\psycopg2-binary\requests\urllib3\
    setelah itu lakukan perintah `pip install -r requirements.txt` dan buat proyek Djano dengan perintah `django-admin startproject RiiPedia .`. Perintah `startproject` akan membuat *file* `manage.py` dan folder **RiiPedia** yang berisikan `__init__.py`,`settings.py`, `urls.py`, `asgi.py`, dan `wsgi.py`. *file* - *file* tersebut akan bergunan nanti untuk pengaturan proyek maupun aplikasi Django. Kemudian saya menambahkan dua string **"localhost", "127.0.0.1"** didalam variable list `ALLOWED_HOSTS` yang masih kosong yang ada di dalam `settings.py`. `ALLOWED HOST` berfungsi untuk mendaftarkan host untuk mengakses aplikasi web. jika ingin mengecek apakah aplikasi berjalan, jalankan perintah `python manage.py runserver` dan buka *http://localhost.8000* untuk melihat apakah aplikasi sudah berjalan atau belum.\
    \
    Untuk mengunggah proyek Django ke repository github, saya menambahkan *file* `.gitugnore` berfungsi sebagai konfigurasi yang digunakan dalam repositori Git untuk menentukan *file* dan direktori yang harus diabaikan oleh Git. Jika tidak ada `.gitignore` kemungkinan akan mengakibatkan error. Kemudian saya melakukan `add`, `commit`, dan `push` seperti biasa dari repositori lokal.\
    \
    Masuk ke tahap membuat aplikasi dengan nama main pada proyek **RiiPedia**. Jalankan perintah `python manage.py startapp main` untuk membuat folder `main` yang berfungsi untuk membuat aplikasi `main`. Kemudian ke *file* `settings.py` dan tambahkan string **"main"** pada variable list `INSTALLED_APPS`. Sekarang aplikasi `main` sudah terdaftar dalam proyek **RiiPedia**. Setelah itu, buatlah folder `template` yang ada di dalam folder `main` dan isi folder tersebut dengan file `main.html` yang berguna untuk menampilkan data program.\
    \
    Untuk `main.html` isi dan hias sesuka hati dengan model penting yang wajib di masukan seperti variable `ecommerce`, `name`, `npm`, `class`, `productname`, `price`, `quantity`, dan `description`. Setelah membuat model di dalam html, model tersebut hanya tampil di html saja dan belum terhubung ke Django. Maka dari itu saya membutuhkan mengedit models.py dan membuat sekaligus mengaplikasikan migrasi model.\
    \
    Pada file `models.py` saya membuat class yang berisikan variable yang berhubungan dengan model penting yang sudah ada di `main.html`. `models.py` kelas dasar yang digunakan untuk mendefinisikan model dalam Django. Dan bisa menambahkan function dibawah `@property` yang biasa untuk testing. Jangan lupa untuk migrasi model karena berfungsi untuk Django melacak perubahan pada model basis data. Jalankan `python manage.py makemigrations` dan `python manage.py migrate`. *makemigrations* untuk membuat perubahan model yang belum diaplikasikan ke basis data dan *migrate* untuk mengaplikasikan perubahan model yang tercantum dalam file migrasi ke basis data dengan menjalankan perintah sebelumnya.\
    \
    Setelah sudah membuat isi dari `models.py` dan melakukan migrasi model, sekarang waktunya menghubungkan antara `views.py` dan `template`. Di dalam file `views.py` saya menambahkan function dictionary untuk menyimpan produk yang akan saya tawarkan di dalam E-commerce tersebut. Nama function masi sama dengan tutorial yaitu `show_main` yang berisi keempat model yang sudah dibuat pada `models.py` dan `main.html` seperti `ecommerce`, `name`, `npm`, `class`, `productname`, `price`, `quantity`, dan `description`. Kemudian pergi kembali ke `main.html` untuk mengganti nama nama produk yang berhubungan dengan keempat model tersebut, contohnya seperti ini. **"price: Rp{{ price }}"**. {{ price }} ini adalah template variable yang didefinisikan didalam `contect`. Lalu edit `urls.py` dengan menambahkan app name dan url pattern-nya. `urls.py` bertanggung jawab untuk mengatur rute URL yang terkait dengan aplikasi `main` kemudian import `path` dari `django.urls` untuk mendefinisikan pola URL. Fungsi `show_main` sebagai tampilan saat URL diakses dan `app_name` untuk memberi nama unik pada pola URL.\
    \
    Terakhir edit `urls.py` yang ada dalam proyek RiiPedia, bukan didalam folder main. Tambahkan `path('', include('main.urls')),` untuk mengarahkan rute yang telah didefinisikan di `urls.py` yang ada di aplikasi `main`. Semua langkah sudah dilakukan dan hanya tinggal jalankan perintah `python manage.py runserver` dan buka http://localhost:8000/. Untuk tugas saya, saya sudah membuat file unit test namun belum sepenuhnya benar karena masih error saat menjalankannya.\
    \
    Karena tugas ini juga perlu di deployment melalui PWS jadi saya perlu menambahkan string **"http://hadyan-fachri-riipedia.pbp.cs.ui.ac.id/"** di `ALLOWED_HOSTS` yang ada di settings.py di dalam proyek RiiPedia. Kemudian `git remote add pws http://pbp.cs.ui.ac.id/hadyan.fachri/riipedia` lalu `git branch -M master`, dan `git push pws master`. Perintah tersebut akan melakukan push program ke PWS buka ke github. Namun sebaiknya add, commit dan push terlebih dahulu ke repository github sebelum di deploy di PWS. Jika ada perubahan, bisa jalankan perintah `git push pws main:master` untuk memperbaharui proyek ini.\
    
### 2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
jawab:\
    ![bagan django](https://github.com/user-attachments/assets/69a62625-cb79-4f12-8211-ae7f132bbad7)\
    penjelasan sudah ada di dalam bagan\
    \
### 3. Jelaskan fungsi git dalam pengembangan perangkat lunak!
jawab:\
    1. **Version Control System\
    Git memungkinkan pengembang untuk melacak perubahan pada kode sumber proyek dari waktu ke waktu. Setiap perubahan yang dilakukan dapat disimpan sebagai sebuah *"commit"*, yang dapat dilihat kembali atau diubah jika diperlukan. Ini membantu dalam menjaga riwayat perubahan yang jelas, serta mempermudah dalam menemukan dan memperbaiki bug.\
    \
    2. **Branching dan Merging**\
    Git mendukung pembuatan cabang untuk mengembangkan fitur-fitur baru atau memperbaiki bug tanpa mempengaruhi kode utama. Fitur ini memungkinkan pengembang untuk mengembangkan fitur baru secara paralel, yang kemudian bisa diuji dan digabungkan kembali dengan kode utama jika sudah siap.\
    \
    3. **Collaboration**\
    \
    Dalam proyek perangkat lunak besar, banyak pengembang yang bekerja bersama pada kode sumber yang sama. Git memungkinkan banyak pengembang untuk bekerja pada cabang (*branches*) yang berbeda tanpa mengganggu pekerjaan satu sama lain. Setelah pekerjaan selesai, cabang-cabang tersebut dapat digabungkan (*merge*) ke dalam cabang utama (`main`) atau cabang pengembangan lainnya.\
    \
    4. **Distributed Storage and Offline Work**\
    Git adalah sistem kontrol versi terdistribusi, yang berarti setiap pengembang memiliki salinan penuh dari repositori di komputer mereka. Ini memungkinkan mereka untuk bekerja secara offline dan melakukan commit lokal, dan kemudian menggabungkan pekerjaan mereka dengan server pusat (*remote repository*) ketika kembali online.\
    \
    5. **Backup and recovery**\
    Dengan Git, pengembang dapat dengan mudah mengembalikan proyek ke versi sebelumnya jika terjadi kesalahan atau bug setelah perubahan kode. Ini memberikan keamanan dan fleksibilitas untuk user dalam pengembangan perangkat lunak, karena setiap commit menyimpan *snapshot* atau alur commit kita dari kode proyek pada waktu tertentu.\
    \
    6. **Integration with CI/CD Tools**\
    Git biasanya terintegrasi dengan alat **CI/CD** (*Continuous Integration/Continuous Deployment*). Integrasi ini memungkinkan otomatis pengujian, build, dan deployment setiap kali ada perubahan kode yang di push ke repositori, meningkatkan efisiensi dan kualitas perangkat lunak.\
    \
    7. **Tracking**\
    Git menyediakan riwayat perubahan kode yang jelas, siapa yang membuat perubahan, kapan perubahan itu dibuat, dan mengapa perubahan tersebut dilakukan terlihat dari commit atau perintah yang kita jalankan. Ini sangat penting untuk mereview kode, dan pemeliharaan di masa depan atau jangka panjang.\
    \
### 4. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
jawab:\
    