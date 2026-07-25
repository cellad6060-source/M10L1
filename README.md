# M10L1

2.Fikir: 
kulanıcının harcadığı enerjileri ve karbon ayak izini hesaplayarak. hafta sonuna bir özet veri çıkarması, kullanıcıyı bilgilendirmesi ve son olarak da ne yapması gerektiğini öneren bir site 


# 🌿 Karbon Ayak İzi & Sürdürülebilir Yaşam Asistanı

![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-2.x-000000?style=for-the-badge&logo=flask&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-Database-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white)

Bireysel günlük/haftalık tüketim alışkanlıklarını analiz ederek emisyon verilerini hesaplayan ve kullanıcıya **en yüksek salınım yaptığı alanlarda nokta atışı 9'ar adet aksiyon önerisi** sunan web tabanlı sürdürülebilirlik uygulaması.

---

## 🎯 Projenin Amacı ve Önemi

Günümüzde bireysel karbon salınımını takip etmek karmaşık ve zor görünebilir. Bu proje, kullanıcıların elektrik, ulaşım, ısınma ve beslenme verilerini kolayca girip emisyonlarını **somut verilerle (kg CO₂ ve ağaç karşılığı)** görmelerini sağlar. 

Uygulamanın ana amacı sadece durum tespiti yapmak değil, **akıllı öneri motoru** ile kullanıcıya sürdürülebilir yaşam alışkanlıkları kazandırmaktır.

---

## 🚀 Öne Çıkan Özellikler & İşlevler

* **📊 Dinamik Karbon Hesaplama:** Elektrik (kWh), ulaşım (km), doğalgaz ($m^3$) ve et tüketimi (porsiyon) verilerinden anlık emisyon hesabı.
* **🎯 Akıllı Öneri Motoru (Smart Recommendation Engine):** Kullanıcıyı bilgi kalabalığına boğmamak adına o gün/hafta **en yüksek salınıma sebep olan İLK 2 KATEGORİYİ** otomatik tespit eder ve yalnızca bu alanlarda detaylı rehberler sunar.
* **📈 Görsel Analiz & Grafikler:** `Chart.js` altyapısı ile son 7 günlük emisyon trendi ve kategori bazlı dağılım pasta grafiği.
* **🌲 Ağaç Telafi Sayacı:** Üretilen toplam CO₂ miktarını nötralize etmek için haftalık kaç ağaç dikilmesi gerektiğini hesaplar.
* **🗂️ Grid & Kart Mimarisi:** Tavsiyeleri okunabilirliği yüksek 3'lü modern kartlar ve numaralı rozetlerle sunar.

---

## 🖥️ Proje Ekran Görüntüleri & Çalışma Mantığı

> *Buraya projenin çalışırken çekilmiş ekran görüntülerini veya GIF'lerini ekleyebilirsin.*

| Veri Giriş Paneli | Analiz ve Öneri Paneli |
| :---: | :---: |
| `![Form Ekranı](görsel_linki_veya_dosya_yolu)` | `![Özet Ekranı](görsel_linki_veya_dosya_yolu)` |

---

## 🛠️ Kurulum ve Kullanım

Projeyi kendi yerel makinenizde çalıştırmak için aşağıdaki adımları takip edebilirsiniz:

1. **Repoyu klonlayın:**
   ```bash
   git clone [https://github.com/kullanici-adi/karbon-ayak-izi.git](https://github.com/kullanici-adi/karbon-ayak-izi.git)
   cd karbon-ayak-izi
