<p align="right">
بِسْــــــــــــــمِ اللَّهِ الرَّحْمَنِ الرَّحِيم 
</p>

# Website portofolio with Flask

Simple website using Python Flask.

## Installation

Buat virtualenv terlebih dahulu
```bash
virtualenv {nama_virtual}
virtualenv -p python3 {nama_virtual} (untuk python3, ubuntu biasanya menggunakan ini)
```
Masuk kedalam virtual
```bash
source {nama_virtual}/Scripts/activate

kalo pake Ubuntu
cd {nama_virtual}
source bin/activate
```
Install Flask menggunakan [pip](https://pip.pypa.io/en/stable/).
```bash
pip install -r requirements.txt

kalo pake python3 (biasanya dipakeubuntu)
pip3 install -r requirements.txt
```
Jalankan dengan perintah
```bash
python main.py

kalo pake python3 (biasanya dipakeubuntu)
python3 main.py

```
## Demo
Silahkan kunjungi [website profil](https://afrizalmy.com) saya.
### Endpoint URL
[root](https://afrizalmy.com) default <br>
[root/mahasiswaif17](https://afrizalmy.com/mahasiswaif17) List mahasiswa angkatan 2017 <br>
[root/mahasiswaif17/{npm}](https://afrizalmy.com/mahasiswaif17/17081010092) Detail mahasiswa angkatan 2017


### Note
Untuk mengupload ke shared hosting [Silahkan baca panduannya](https://www.domainesia.com/panduan/cara-menjalankan-flask-python-di-hosting/)

## Releases
Tagging untuk belajar tiap partnya. <br>
-> [Layouting Sederhana](https://github.com/afrizal423/flask-myportofolio/releases/tag/v1) <br>
-> Get data from MySQLDB dalam bentuk json. (belum release karena belum ada error handling jika npm tidak ada)

