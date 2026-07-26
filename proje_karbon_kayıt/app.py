from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///karbon_detayli.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Veri(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tarih = db.Column(db.Date, default=datetime.utcnow)
    
    # Detaylı Tüketimler
    ev_elektrik = db.Column(db.Float, default=0.0)      # kWh
    sehir_ici_arac = db.Column(db.Float, default=0.0)   # km (Benzin/Dizel)
    toplu_tasima = db.Column(db.Float, default=0.0)     # km (Otobüs/Metro)
    ucak_mesafe = db.Column(db.Float, default=0.0)      # km
    dogalgaz = db.Column(db.Float, default=0.0)         # m3
    et_tuketimi = db.Column(db.Float, default=0.0)      # Porsiyon/Öğün
    
    # Hesaplanan Karbon Salınımları (kg CO2)
    karbon_elektrik = db.Column(db.Float, default=0.0)
    karbon_ulasim = db.Column(db.Float, default=0.0)
    karbon_isinma = db.Column(db.Float, default=0.0)
    karbon_beslenme = db.Column(db.Float, default=0.0)
    toplam_karbon = db.Column(db.Float, default=0.0)

with app.app_context():
    db.create_all()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Form Verilerini Al
        ev_el = float(request.form.get('ev_elektrik', 0))
        arac = float(request.form.get('sehir_ici_arac', 0))
        toplu = float(request.form.get('toplu_tasima', 0))
        ucak = float(request.form.get('ucak_mesafe', 0))
        gaz = float(request.form.get('dogalgaz', 0))
        et = float(request.form.get('et_tuketimi', 0))

        # Detaylı Karbon Hesaplamaları (kg CO2)
        c_el = round(ev_el * 0.45, 2)
        c_ul = round((arac * 0.19) + (toplu * 0.05) + (ucak * 0.25), 2)
        c_is = round(gaz * 2.0, 2)
        c_bes = round(et * 2.5, 2)
        
        c_toplam = round(c_el + c_ul + c_is + c_bes, 2)

        yeni_veri = Veri(
            ev_elektrik=ev_el, sehir_ici_arac=arac, toplu_tasima=toplu,
            ucak_mesafe=ucak, dogalgaz=gaz, et_tuketimi=et,
            karbon_elektrik=c_el, karbon_ulasim=c_ul,
            karbon_isinma=c_is, karbon_beslenme=c_bes,
            toplam_karbon=c_toplam
        )
        db.session.add(yeni_veri)
        db.session.commit()
        return redirect(url_for('ozet'))

    return render_template('index.html')

@app.route('/ozet')
def ozet():
    veriler = Veri.query.order_by(Veri.id.desc()).limit(7).all()
    veriler.reverse()

    tarihler = [v.tarih.strftime('%d/%m') for v in veriler]
    toplam_karbonlar = [v.toplam_karbon for v in veriler]

    # Kategori Bazlı Toplamlar (Tüm Verilerin Toplamı)
    tot_el = sum(v.karbon_elektrik for v in veriler)
    tot_ul = sum(v.karbon_ulasim for v in veriler)
    tot_is = sum(v.karbon_isinma for v in veriler)
    tot_bes = sum(v.karbon_beslenme for v in veriler)
    genel_toplam = sum(v.toplam_karbon for v in veriler)

    agac_sayisi = round(genel_toplam / 0.42, 1)

    # --- TÜM TAVSİYE HAVUZU ---
    tum_havuz = {
        "ulasim": {
            "kategori": "Ulaşım & Mobilite",
            "ikon": "bi-car-front-fill",
            "renk": "primary",
            "baslik": "Ulaşım Kaynaklı Emisyonu Azaltma Rehberi",
            "neden": "Ulaşım harcamaların emisyonunda en yüksek paya sahip alanlardan biri.",
            "aksiyonlar": [
                "**Toplu Taşıma / Bisiklet:** Haftada 2 gün hususi araç yerine toplu taşıma kullanmak emisyonunu yılda yaklaşık 400 kg CO₂ azaltır.",
                "**Eko-Sürüş Teknikleri:** Ani fren ve sert hızlanmalardan kaçınarak yakıt tüketimini %15 oranında düşürebilirsin.",
                "**Lastik Basıncı Kontrolü:** Araç lastiklerinin basıncını ideal seviyede tutmak yakıt verimliliğini %3 artırır.",
                "**Yol Paylaşımı (Carpooling):** İş veya okul rotalarında yakın arkadaşlarınla araç paylaşarak kişi başı düşen emisyonu yarıya indir.",
                "**Gereksiz Ağırlıkları Boşalt:** Araç bagajında taşınan her fazladan 50 kg yakıt tüketimini artırır.",
                "**Kısa Mesafelerde Yürüme:** 1-2 km arası kısa mesafelerde araç çalıştırmak yerine yürümeyi tercih et.",
                "**Rölantide Çalıştırmayı Önle:** 10 saniyeden uzun beklemelerde motoru kapatmak gereksiz yakıt harcamasının önüne geçer.",
                "**Uçuş Sayılarını Optimize Et:** Kısa mesafe seyahatlerde uçak yerine hızlı tren veya otobüs alternatiflerini değerlendir.",
                "**Düzenli Araç Bakımı:** Motor yağı ve hava filtresini zamanında değiştirmek aracın yakıt verimliliğini maksimumda tutar."
            ]
        },
        "elektrik": {
            "kategori": "Ev & Enerji Verimliliği",
            "ikon": "bi-lightning-charge-fill",
            "renk": "warning",
            "baslik": "Elektrik Tüketimini Optimize Etme Rehberi",
            "neden": "Elektrik kullanımın toplam karbon ayak izinin büyük bir kısmını oluşturuyor.",
            "aksiyonlar": [
                "**Vampir Yükleri Kesin:** Bekleme (stand-by) modundaki cihazlar ev elektriğinin %10'unu harcar. Anahtarlı priz kullanarak tamamen kapatın.",
                "**LED Dönüşümü:** Akkor ampulleri LED ampullerle değiştirmek aydınlatma enerjisinden %80 tasarruf sağlar.",
                "**Doğal Işıktan Faydalanın:** Gün içi çalışma alanlarınızı pencere kenarlarına kaydırarak yapay aydınlatma ihtiyacını azaltın.",
                "**A+++ Beyaz Eşya Kullanımı:** Yeni beyaz eşya alırken yüksek enerji sınıfı seçmek uzun vadede tüketimi yarı yarıya düşürür.",
                "**Çamaşırları Düşük Isıda Yıkayın:** Çamaşır makinesini 60°C yerine 30°C'de çalıştırmak enerji kullanımını %50 azaltır.",
                "**Buzdolabı Derecesi:** Buzdolabını +4°C, dondurucuyu -18°C ideal seviyesinde tutarak fazla yüklenmeyi önleyin.",
                "**Kurutma Makinesi Yerine Doğal Kurutma:** Çamaşırları imkan dahilinde asarak kurutmak ciddi bir elektrik tasarrufu sağlar.",
                "**Şarj Aletlerini Prizde Bırakmayın:** Cihaz bağlı olmasa dahi prizde kalan şarj aletleri elektrik çekmeye devam eder.",
                "**Bulaşık Makinesini Tam Doldurun:** Bulaşık makinesini tam dolmadan çalıştırmayarak hem su hem elektrik israfını engelleyin."
            ]
        },
        "beslenme": {
            "kategori": "Beslenme & Tüketim",
            "ikon": "bi-egg-fried",
            "renk": "danger",
            "baslik": "Sürdürülebilir Beslenme Alışkanlıkları Rehberi",
            "neden": "Beslenme tercihin yüksek emisyon üreten ana faktörler arasında yer alıyor.",
            "aksiyonlar": [
                "**Haftada 1 Gün Bitkisel Beslenme:** Et tüketimini haftada 1 gün durdurmak, yılda 1000 km araç sürmemeye denk emisyon tasarrufu sağlar.",
                "**Yerel ve Mevsimsel Gıda:** İthal veya seralarda yetiştirilen gıdalar yerine yerel pazarlardan alışveriş yaparak lojistik emisyonunu sıfırlayın.",
                "**Gıda İsrafını Önleyin:** Alışveriş listesi yapıp gıda israfının önüne geçmek üretim aşamasında heba olan enerjiyi korur.",
                "**Kırmızı Et Yerine Alternatifler:** Kırmızı et yerine tavuk, balık veya baklagil tercih etmek beslenme emisyonunu büyük oranda düşürür.",
                "**Kompost Yapımı:** Organik mutfak atıklarını kompost yaparak çöplüklerde metan gazı oluşumunu engelleyin.",
                "**Ambalajsız / Dökme Ürünler:** Aşırı plastik ambalajlı ürünler yerine dökme veya cam kavanozdaki gıdaları tercih edin.",
                "**Kendi Mataranı Kullan:** Plastik şişe suyu yerine cam veya çelik matara kullanarak ambalaj emisyonunu engelleyin.",
                "**Evde Yemek Pişirme:** Dışarıdan paket servis sipariş etmek yerine evde yemek pişirmek ambalaj ve kurye emisyonunu azaltır.",
                "**Porsiyon Kontrolü:** Yiyeceğin kadar tabağına alarak yemek atığı oluşumunu doğrudan engelleyin."
            ]
        },
        "isinma": {
            "kategori": "Isınma & İklimlendirme",
            "ikon": "bi-fire",
            "renk": "secondary",
            "baslik": "Doğal Gaz ve Isı Yönetimi Rehberi",
            "neden": "Isınma kaynaklı karbon salınımın bugün oldukça yüksek seviyede.",
            "aksiyonlar": [
                "**Termostat Ayarı:** Ev termostatını sadece 1°C düşürmek yıllık doğal gaz faturasını ve emisyonunu %7 azaltır.",
                "**Radyatör Arkası Yalıtım:** Radyatörlerin arkasına yansıtıcı levha koyarak ısının dış duvardan kaçmasını önleyin.",
                "**Pencerelerde Isı Yalıtım Bandı:** Pencere ve kapı kenarlarına yalıtım bandı çekerek soğuk hava sızıntılarını kapatın.",
                "**Radyatörlerin Önünü Açın:** Peteklerin önüne koltuk, perde veya mobilya koymayarak ısı yayılımını engellemeyin.",
                "**Kombi Bakımı:** Kombi ve petek temizliğini yılda bir kez yaptırmak ısı transfer verimini artırır.",
                "**Geceleri Panjur / Perde Kullanımı:** Geceleri kalın perdeleri kapatmak pencerelerden olan ısı kaybını %10 azaltır.",
                "**Güneş Işığından Faydalanın:** Gün boyunca pencereleri açarak güneş ısısının içeri girmesini sağlayın.",
                "**Programlanabilir Termostat:** Evde olunmayan saatlerde ısınmayı otomatik olarak düşük seviyeye getirin.",
                "**Oda Kapılarını Kapalı Tutun:** Kullanılmayan odaların kapılarını kapalı tutarak ısınan alanı daraltın."
            ]
        }
    }

    # --- EN YÜKSEK 2 KATEGORİYİ TESPİT ETME ---
    # Son girilen veriye (güncel veri) veya toplam verilere göre sıralama yapılır:
    kategori_skorlari = [
        ('elektrik', tot_el),
        ('ulasim', tot_ul),
        ('isinma', tot_is),
        ('beslenme', tot_bes)
    ]
    
    # Emisyon miktarına göre büyükten küçüğe sırala
    kategori_skorlari.sort(key=lambda x: x[1], reverse=True)

    # Sıfırdan büyük olan EN YÜKSEK İKİ kategoriyi al
    detayli_oneriler = []
    for kat_anahtar, skor in kategori_skorlari[:2]: # İlk 2 eleman
        if skor > 0:
            detayli_oneriler.append(tum_havuz[kat_anahtar])

    return render_template(
        'ozet.html',
        tarihler=tarihler,
        toplam_karbonlar=toplam_karbonlar,
        tot_el=tot_el, tot_ul=tot_ul, tot_is=tot_is, tot_bes=tot_bes,
        genel_toplam=genel_toplam,
        agac_sayisi=agac_sayisi,
        detayli_oneriler=detayli_oneriler
    )

if __name__ == '__main__':
    app.run(debug=True)