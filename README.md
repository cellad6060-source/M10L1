# 🌿 Karbon Ayak İzi & Sürdürülebilir Yaşam Asistanı

![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-2.x-000000?style=for-the-badge&logo=flask&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-Database-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white)
![Responsive](https://img.shields.io/badge/Mobile-PC_Compatible-brightgreen?style=for-the-badge)

Bireysel günlük/haftalık tüketim alışkanlıklarını analiz ederek emisyon verilerini hesaplayan ve kullanıcıya **en yüksek salınım yaptığı ilk 2 alanda nokta atışı 9'ar adet aksiyon önerisi** sunan web tabanlı sürdürülebilirlik uygulaması.

---

## 🎯 Projenin Amacı ve Önemi

Günümüzde bireysel karbon salınımını takip etmek karmaşık ve zor görünebilir. Bu proje, kullanıcıların elektrik, ulaşım, ısınma ve beslenme verilerini kolayca girip emisyonlarını **somut verilerle (kg CO₂ ve ağaç karşılığı)** görmelerini sağlar. 

Uygulamanın ana amacı sadece durum tespiti yapmak değil, **akıllı öneri motoru ve interaktif görev kartları** ile kullanıcıya sürdürülebilir yaşam alışkanlıkları kazandırmaktır.

---

## 🚀 Öne Çıkan Özellikler & İşlevler

* **📊 Dinamik Karbon Hesaplama:** Elektrik (kWh), ulaşım (km), doğalgaz ($m^3$) ve et tüketimi (porsiyon) verilerinden anlık emisyon hesabı.
* **🎯 Akıllı Öneri Motoru (Smart Recommendation Engine):** Kullanıcıyı bilgi kalabalığına boğmamak adına o gün/hafta **en yüksek salınıma sebep olan İLK 2 KATEGORİYİ** otomatik tespit eder ve yalnızca bu alanlarda 9'ar maddelik detaylı rehber sunar.
* **📱 %100 Mobil & PC Uyumlu (Fully Responsive):** Tüm cihaz ekranlarına göre otomatik şekil alan esnek Bootstrap 5 ve CSS Grid mimarisi.
* **✅ İnteraktif Görev Kartları:** Kullanıcının uyguladığı tavsiyeleri işaretleyebileceği (checkbox) ve durumunu anlık takip edebileceği kart tasarımı.
* **🎨 Dinamik Tema & Süslemeler:** 
  * Emisyon seviyesine göre anlık renk değiştiren durum kartları (🟢 Yeşil / 🟡 Turuncu / 🔴 Kırmızı).
  * Hesaplanan ağaç sayısı kadar ekrana basılan canlı 🌲 emojileri.
  * Düşük emisyon yakalandığında çalışan doğa dostu **JS Konfeti (Confetti)** efekti.
* **📈 Görsel Analiz & Grafikler:** `Chart.js` altyapısı ile son 7 günlük emisyon trendi ve kategori bazlı dağılım pasta grafiği.

---

## 🖥️ Proje Ekran Görüntüleri & Çalışma Mantığı

| Veri Giriş Paneli | Analiz ve Öneri Paneli |
| :---: | :---: |
| <img src="https://github.com/user-attachments/assets/f89b36c0-777a-4b4e-b695-117f979251a5" width="400"> | <img src="https://github.com/user-attachments/assets/d9cd8ac4-eab2-4c5c-b9af-7eca82877efd" width="400"> |

---

## 🛠️ Kurulum ve Kullanım

Projeyi kendi yerel makinenizde çalıştırmak için aşağıdaki adımları takip edebilirsiniz:

1. **Repoyu klonlayın:**
   ```bash
   git clone https://github.com/cellad6060-source/M10L1.git
   cd M10L1
