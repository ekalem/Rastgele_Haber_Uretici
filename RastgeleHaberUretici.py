import random # random içeri alınır.

class Uretici: # Uretici isimli bir sınıf oluşturulur.

    """ 
        Generates random news entry 
        Usage:
            generator = Generator()
            print(generator.generate())
    """
# Yardımda gözükmesi için yukarıdaki gibi bir açıklama yazılır. ve Usage yani Kullanımı anlatılır.

    def uret_isim(self):
        isimler = [
         "Tarık",
         "Kemal",
         "Leyla",
         "Micheal",
         "Robert",
         "Ali",
         "Şener",
         "Nicole",
         "Tayfun",
         "Deniz",
        ]
        return random.choice(isimler)

    def uret_soyisim(self):
        soyisimler = [
            "Demir",
            "Taş",
            "Burton",
            "Farrell",
            "Taş",
            "Güler",
            "Kaya",
            "Toprak",
            "Akın",
            "Akpınar",
        ]
        return random.choice(soyisimler)

    def uret(self):
        haberler = [
            "KPSS'de tüm soruları gözü kapalı çözen {} {} sadece {} doğru yaptı.",
            "{} {} tatildeyken {} hayranını konserine davet etti.",
            "Yazın yeni albüm çıkaran {} {} müzik listelerinde {} . sıraya yükseldi.",
            "Kod yazmaya başlayan lise öğrencisi {} {}, {} programlama dili öğrendi",
            "{} {} konuk olarak katıldığı programda diğer {} 3 konuk hiç konuşamadı.",
            "Türkiye'ye yeni gelen ünlü futbolcu {} {} , {} yüzbin TL'ye bir takımla anlaştı.",
            "{2} yıllık bölümde okuyan {0} {1} yine mezun olamadı.", #
        ]
        
        return random.choice(haberler).format(
            self.uret_isim(),
            self.uret_soyisim(),
            random.randint(0,100)
        )

print(Uretici().uret())
