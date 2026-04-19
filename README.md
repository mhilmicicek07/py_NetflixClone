# 🎬 py_NetflixClone

[TR: Türkçe](#türkçe) | [EN: English](#english) | [DE: Deutsch](#deutsch)

---

## Türkçe

Bu proje, Netflix benzeri bir kullanıcı deneyimi sunmayı amaçlayan tam işlevli bir **film izleme platformu klonudur**. Kullanıcılar profil oluşturabilir, kategorilere göre filmleri listeleyebilir ve içerikleri izleyebilir.

### 🚀 Özellikler
- 👤 **Çoklu Profil Yönetimi:** Her kullanıcı için ayrı profiller oluşturma ve yönetme.
- 🎞️ **Gelişmiş Film Yönetimi:** Kategoriler ve türler arası ilişkilendirme.
- 🔍 **Dinamik Arama:** İsim, tür veya kategoriye göre hızlı arama.
- 📺 **Video Oynatma:** Dahili video oynatıcı desteği.
- ⚙️ **Yönetici Paneli:** Django Admin üzerinden tam kontrol.

### 🛠️ Teknolojiler
- **Backend:** Python 3 & Django
- **Frontend:** HTML5, CSS3 (Modern Flexbox/Grid), JavaScript
- **Veritabanı:** SQLite3
- **Ekstra:** Django Autoslug (SEO uyumlu URL'ler)

### 🧰 Gereksinimler
- Python 3.12+
- `pip` ile kurulabilen paketler: Django 5.1.15, django-autoslug 1.9.9, Pillow 12.1.1 (tümü `requirements.txt` içinde listelenir)

### 📂 Kurulum
1. Repoyu klonlayın: `git clone https://github.com/mhilmicicek07/py_NetflixClone.git`
2. (Önerilen) Sanal ortam kurun ve aktifleştirin: `python -m venv .venv && source .venv/bin/activate`
3. Gereksinimleri yükleyin: `pip install -r requirements.txt`
4. Migrasyonları çalıştırın: `python manage.py migrate`
5. Sunucuyu başlatın: `python manage.py runserver`
6. Doğrulama için mevcut testleri çalıştırın: `python manage.py test`
7. **Önemli düzeltmeler:** `DJANGO_SETTINGS_MODULE` artık `py_NetflixClone.settings` değerini kullanır; ASGI/WSGI dağıtımlarında bu değeri ortam değişkeni olarak ayarlayın. Özel 404 sayfası doğru 404 durum koduyla döner.

---

## English

This project is a fully functional **movie streaming platform clone** designed to provide a Netflix-like user experience. Users can create profiles, browse movies by category, and watch content.

### 🚀 Features
- 👤 **Multi-Profile Management:** Create and manage separate profiles for each user account.
- 🎞️ **Advanced Movie Management:** Relationships between categories and genres.
- 🔍 **Dynamic Search:** Fast search by name, genre, or category.
- 📺 **Video Playback:** Integrated video player support.
- ⚙️ **Admin Panel:** Full control via Django Admin.

### 🛠️ Technologies
- **Backend:** Python 3 & Django
- **Frontend:** HTML5, CSS3, JavaScript
- **Database:** SQLite3
- **Extras:** Django Autoslug (SEO-friendly URLs)

### 🧰 Requirements
- Python 3.12+
- Installable via `pip`: Django 5.1.15, django-autoslug 1.9.9, Pillow 12.1.1 (see `requirements.txt`)

### 📂 Installation
1. Clone the repo: `git clone https://github.com/mhilmicicek07/py_NetflixClone.git`
2. (Recommended) Create & activate a virtual env: `python -m venv .venv && source .venv/bin/activate`
3. Install requirements: `pip install -r requirements.txt`
4. Run migrations: `python manage.py migrate`
5. Start server: `python manage.py runserver`
6. Run existing tests for verification: `python manage.py test`
7. **Important fixes:** `DJANGO_SETTINGS_MODULE` now points to `py_NetflixClone.settings`; set this value for ASGI/WSGI deployments. The custom 404 page now returns a proper 404 status code.

---

## Deutsch

Dieses Projekt ist ein voll funktionsfähiger **Klon einer Film-Streaming-Plattform**, der ein Netflix-ähnliches Benutzererlebnis bietet. Benutzer können Profile erstellen, Filme nach Kategorien durchsuchen und Inhalte ansehen.

### 🚀 Funktionen
- 👤 **Multi-Profil-Verwaltung:** Erstellen und Verwalten separater Profile für jedes Benutzerkonto.
- 🎞️ **Erweiterte Filmverwaltung:** Verknüpfungen zwischen Kategorien und Genres.
- 🔍 **Dynamische Suche:** Schnelle Suche nach Name, Genre oder Kategorie.
- 📺 **Videowiedergabe:** Integrierte Videoplayer-Unterstützung.
- ⚙️ **Admin-Panel:** Volle Kontrolle über Django Admin.

### 🛠️ Technologien
- **Backend:** Python 3 & Django
- **Frontend:** HTML5, CSS3, JavaScript
- **Datenbank:** SQLite3
- **Extras:** Django Autoslug (SEO-freundliche URLs)

### 🧰 Anforderungen
- Python 3.12+
- Über `pip` installierbar: Django 5.1.15, django-autoslug 1.9.9, Pillow 12.1.1 (siehe `requirements.txt`)

### 📂 Installation
1. Repository klonen: `git clone https://github.com/mhilmicicek07/py_NetflixClone.git`
2. (Empfohlen) Virtuelle Umgebung anlegen & aktivieren: `python -m venv .venv && source .venv/bin/activate`
3. Anforderungen installieren: `pip install -r requirements.txt`
4. Migrationen ausführen: `python manage.py migrate`
5. Server starten: `python manage.py runserver`
6. Vorhandene Tests ausführen: `python manage.py test`
7. **Wichtige Korrekturen:** `DJANGO_SETTINGS_MODULE` verweist nun auf `py_NetflixClone.settings`; setzen Sie diesen Wert für ASGI/WSGI-Bereitstellungen. Die benutzerdefinierte 404-Seite liefert jetzt korrekt den Statuscode 404.

---
👨‍💻 **Geliştirici / Developer:** Mehmet Hilmi Çiçek  
📍 **Location:** Geislingen an der Steige, Germany
