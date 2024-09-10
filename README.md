# RiiPedia
## First PBP Individual Project by
### Hadyan Fachri
### 2306245030
### PBP A

Checkpoint\
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
\
    1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).\
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
    Masuk ke tahap membuat aplikasi dengan nama main pada proyek **RiiPedia**. 
