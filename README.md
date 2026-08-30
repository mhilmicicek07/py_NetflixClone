# py_NetflixClone

[TR: Türkçe](#türkçe) | [EN: English](#english) | [DE: Deutsch](#deutsch)

---

## Türkçe

Bu proje, Netflix benzeri bir kullanıcı deneyimi sunmayı amaçlayan **film izleme platformu klonudur**. Kullanıcılar kayıt olabilir, profil oluşturabilir, kategorilere ve türlere göre filmleri listeleyebilir, arama yapabilir ve içerikleri izleyebilir.

### Özellikler

- **Kimlik Doğrulama:** E-posta ile kayıt, giriş, çıkış ve şifre değiştirme.
- **Profil Yönetimi:** Her hesap için birden fazla profil oluşturma, düzenleme ve silme (profil resmi desteği ile).
- **Film Listeleme:** Kategoriye veya türe göre filtreleme.
- **Arama:** İsim, kategori veya türe göre film arama.
- **Video Oynatma:** Seçili filme ait video oynatma sayfası; her izlemede görüntülenme sayısı artar.
- **Yönetici Paneli:** Django Admin üzerinden tam içerik yönetimi.
- **Özel 404 Sayfası:** Doğru HTTP 404 durum kodu ile özelleştirilmiş hata sayfası.

### Teknolojiler

- **Backend:** Python 3 & Django 5.1
- **Frontend:** HTML5, CSS3, JavaScript
- **Veritabanı:** SQLite3
- **Bağımlılıklar:** django-autoslug (SEO uyumlu URL'ler), Pillow (görsel yükleme)

### Gereksinimler

- Python 3.10+
- pip

### Kurulum

1. Repoyu klonlayın:
   ```bash
   git clone https://github.com/mhilmicicek07/py_NetflixClone.git
   cd py_NetflixClone
   ```
2. (Önerilen) Sanal ortam oluşturun ve aktifleştirin:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Windows: .venv\Scripts\activate
   ```
3. Bağımlılıkları yükleyin:
   ```bash
   pip install -r requirements.txt
   ```
4. Veritabanı migrasyonlarını uygulayın:
   ```bash
   python manage.py migrate
   ```
5. (İsteğe bağlı) Yönetici kullanıcısı oluşturun:
   ```bash
   python manage.py createsuperuser
   ```
6. Geliştirme sunucusunu başlatın:
   ```bash
   python manage.py runserver
   ```

Uygulama `http://127.0.0.1:8000/` adresinde çalışır.

### Ortam Değişkenleri

ASGI/WSGI dağıtımlarında `DJANGO_SETTINGS_MODULE` değişkenini `py_NetflixClone.settings` olarak ayarlayın. `settings.py` içindeki `SECRET_KEY` üretim ortamında güvenli bir değerle değiştirilmelidir.

---

## English

This project is a **movie streaming platform clone** designed to provide a Netflix-like user experience. Users can register, create profiles, browse and search movies by category or genre, and watch content.

### Features

- **Authentication:** Register, log in, log out, and change password using email-based login.
- **Profile Management:** Create, edit, and delete multiple profiles per account (with profile image upload).
- **Movie Browsing:** Filter movies by category or genre.
- **Search:** Search movies by name, category, or genre.
- **Video Playback:** Dedicated video page per movie; view count increments on each watch.
- **Admin Panel:** Full content management via Django Admin.
- **Custom 404 Page:** Returns a proper HTTP 404 status code.

### Technologies

- **Backend:** Python 3 & Django 5.1
- **Frontend:** HTML5, CSS3, JavaScript
- **Database:** SQLite3
- **Dependencies:** django-autoslug (SEO-friendly slugs), Pillow (image uploads)

### Requirements

- Python 3.10+
- pip

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/mhilmicicek07/py_NetflixClone.git
   cd py_NetflixClone
   ```
2. (Recommended) Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Windows: .venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Apply database migrations:
   ```bash
   python manage.py migrate
   ```
5. (Optional) Create an admin user:
   ```bash
   python manage.py createsuperuser
   ```
6. Start the development server:
   ```bash
   python manage.py runserver
   ```

The application runs at `http://127.0.0.1:8000/`.

### Environment Variables

For ASGI/WSGI deployments, set `DJANGO_SETTINGS_MODULE` to `py_NetflixClone.settings`. The `SECRET_KEY` in `settings.py` must be replaced with a secure value in production.

---

## Deutsch

Dieses Projekt ist ein **Klon einer Film-Streaming-Plattform**, der ein Netflix-ähnliches Benutzererlebnis bietet. Benutzer können sich registrieren, Profile anlegen, Filme nach Kategorie oder Genre durchsuchen und Inhalte ansehen.

### Funktionen

- **Authentifizierung:** Registrierung, Anmeldung, Abmeldung und Passwortänderung per E-Mail-Login.
- **Profilverwaltung:** Mehrere Profile pro Konto erstellen, bearbeiten und löschen (mit Profilbild-Upload).
- **Film-Browsing:** Filme nach Kategorie oder Genre filtern.
- **Suche:** Filme nach Name, Kategorie oder Genre suchen.
- **Videowiedergabe:** Eigene Videoseite pro Film; Aufrufzähler wird bei jedem Aufruf erhöht.
- **Admin-Panel:** Vollständige Inhaltsverwaltung über Django Admin.
- **Benutzerdefinierte 404-Seite:** Gibt korrekt den HTTP-Statuscode 404 zurück.

### Technologien

- **Backend:** Python 3 & Django 5.1
- **Frontend:** HTML5, CSS3, JavaScript
- **Datenbank:** SQLite3
- **Abhängigkeiten:** django-autoslug (SEO-freundliche Slugs), Pillow (Bild-Uploads)

### Anforderungen

- Python 3.10+
- pip

### Installation

1. Repository klonen:
   ```bash
   git clone https://github.com/mhilmicicek07/py_NetflixClone.git
   cd py_NetflixClone
   ```
2. (Empfohlen) Virtuelle Umgebung anlegen und aktivieren:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Windows: .venv\Scripts\activate
   ```
3. Abhängigkeiten installieren:
   ```bash
   pip install -r requirements.txt
   ```
4. Datenbankmigrationen anwenden:
   ```bash
   python manage.py migrate
   ```
5. (Optional) Admin-Benutzer erstellen:
   ```bash
   python manage.py createsuperuser
   ```
6. Entwicklungsserver starten:
   ```bash
   python manage.py runserver
   ```

Die Anwendung läuft unter `http://127.0.0.1:8000/`.

### Umgebungsvariablen

Für ASGI/WSGI-Deployments muss `DJANGO_SETTINGS_MODULE` auf `py_NetflixClone.settings` gesetzt werden. Der `SECRET_KEY` in `settings.py` muss in der Produktion durch einen sicheren Wert ersetzt werden.

---

👨‍💻 **Geliştirici / Developer:** Mehmet Hilmi Çiçek
📍 **Location:** Geislingen an der Steige, Germany
