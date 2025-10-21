# 🎬 py_NetflixClone Uygulaması  

Bu proje, Netflix benzeri bir kullanıcı deneyimi sunmayı amaçlayan tam işlevli bir **film izleme platformu klonudur**.  
Kullanıcılar, profil oluşturabilir, tür veya kategoriye göre film arayabilir ve popüler içerikleri görüntüleyebilir.  
Proje, **Django** altyapısı kullanılarak geliştirilmiştir ve dinamik veri yönetimini destekler.  

---

## 🚀 Özellikler  

- 👤 **Kullanıcı Yönetimi:** Kullanıcı kaydı, girişi ve profil oluşturma.  
- 🎞️ **Film Yönetimi:** Filmler, kategoriler ve türlere göre filtreleme ve listeleme.  
- 🔍 **Akıllı Arama:** Film adı, tür veya kategoriye göre dinamik arama özelliği.  
- 🧩 **Bileşen Tabanlı Arayüz:** Navbar, footer, movie-card gibi modüler HTML bileşenleri.  
- 🖼️ **Modern Görseller:** Netflix tarzı arayüz ve özel tasarlanmış statik kaynaklar.  
- ⚙️ **Yönetici Paneli:** Django Admin üzerinden film, kullanıcı ve kategori yönetimi.  

---

## 🧩 Kullanılan Teknolojiler  

| Teknoloji | Rolü |
|------------|-----------|
| **Python 3 & Django** | Backend, veri yönetimi ve kullanıcı oturumları. |
| **HTML5 & Django Templates** | Sayfa yapısı ve dinamik veri gösterimi. |
| **CSS3** | Netflix tarzı modern arayüz. |
| **JavaScript (ES6)** | Dinamik etkileşimler ve kullanıcı deneyimi. |
| **SQLite3** | Varsayılan veritabanı olarak kullanılmıştır. |

---

## 📂 Proje Dosya Yapısı  

📁 py_NetflixClone  
├── 📁 movie  
│   ├── models.py  
│   ├── views.py  
│   ├── urls.py  
│   └── templates/  
├── 📁 user  
│   ├── models.py  
│   ├── forms.py  
│   ├── views.py  
│   └── urls.py  
├── 📁 templates  
│   ├── layout.html  
│   └── components/  
├── 📁 static  
│   ├── css/style.css  
│   ├── js/script.js  
│   └── img/ (film görselleri)  
├── db.sqlite3  
├── manage.py  
└── README.md  

---

## ⚙️ Kurulum ve Çalıştırma  

Projeyi yerel ortamda çalıştırmak için aşağıdaki adımları izleyin:  

1. Depoyu klonlayın:  
   ```bash
   git clone https://github.com/mhilmicicek07/py_NetflixClone.git
   cd py_NetflixClone
Gerekli paketleri yükleyin:


pip install -r requirements.txt
Veritabanı migrasyonlarını uygulayın:


python manage.py migrate
Geliştirme sunucusunu başlatın:


python manage.py runserver
Tarayıcıdan şu adrese gidin:

http://127.0.0.1:8000/
🧠 Teknik Açıklama
Arama sistemi, Q nesneleri kullanılarak film adı, tür ve kategori alanlarında aynı anda arama yapar.

distinct() ile yinelenen sonuçlar önlenir.

Template yapısı, her bileşenin ayrı HTML dosyasında tutulduğu modüler bir sistemdir.

Static dosyalar, static/ klasöründe organize edilmiştir ve Django’nun collectstatic komutu ile yönetilir.

👨‍💻 Geliştirici
Mehmet Hilmi Çiçek
💼 Full Stack Web Developer
📍 Geislingen an der Steige

“Basit ama tutarlı kod, karmaşık olandan her zaman üstündür.”

🪪 Lisans
Bu proje açık kaynaklıdır.
Kodlar incelenebilir, geliştirilebilir veya kişisel projelerde referans olarak kullanılabilir.