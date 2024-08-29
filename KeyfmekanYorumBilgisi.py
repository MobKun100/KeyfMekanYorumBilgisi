from flask import Flask,jsonify
from selenium import webdriver  # Web tarayıcısını otomatik olarak kontrol etmek için Selenium kullanılırfrom
from selenium.webdriver.common.by import By  # Selenium'un By modülü, web elementlerini bulmak için kullanılır
from selenium.webdriver.chrome.options import Options  # Chrome tarayıcısının seçeneklerini ayarlamak için Options kullanılır
from time import sleep  # Zaman gecikmesi eklemek için sleep fonksiyonu kullanılır
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
app=Flask(__name__)
# Chrome seçeneklerini ayarlar



# Otelin birkaç yorumunu çeker
#puan_Bilgisi = tarayici.find_element(By.XPATH,'//*[@id="hotelDetailApp"]/div[2]/div[4]/div[3]/div/div[2]/div[1]/div/div/span').text   #   Girilen Sitenin Dosyalarının İçerisinde Bulunan XPath Verilerini
#yorum_Bilgisi = tarayici.find_element(By.XPATH,'//*[@id="user-reviewsContainer"]/div[2]/div/div[1]/div[2]/ul/li[2]').text           # Siteden Alınması Ve Bu Verilerin Değişkenlerle Depolanması Aynı 
#yorum_Bilgisi1 = tarayici.find_element(By.XPATH,'//*[@id="user-reviewsContainer"]/div[2]/div/div[2]/div[2]/ul/li[2]/p').text          # Zamanda Bir Süre İçerisinde Güncellenme OLasılığı Olduğu İçin 
#yorum_Bilgisi2 = tarayici.find_element(By.XPATH,'//*[@id="user-reviewsContainer"]/div[2]/div/div[3]/div[2]/ul/li[2]/p').text          # While True Döngüsüne Alınmıştır
#yorum_Bilgisi3 = tarayici.find_element(By.XPATH,'//*[@id="user-reviewsContainer"]/div[2]/div/div[4]/div[2]/ul/li[2]/p').text      //*[@id="user-reviewsContainer"]/div[2]/div/div[2]    #   Sonrasında Sleep() Komutu Kullanılarak Bunun Belirli Saniyeler
#//*[@id="more-show-review"]        # İçerisinde Tekrarlanması Sağlanmıştır.

@app.route('/')
def index():
    chrome_options = Options()
    # Tarayıcıyı başlatır
    chrome_options.add_argument("--headless")
    tarayici = webdriver.Chrome(options=chrome_options)
    # Veri çekmek istediğimiz siteye nasıl girileceği hakkında yazılıma bilgi verir
    tarayici.get("https://otelpuan.com/Hera-Hotel-Kas")
    # Kullanıcıya aranan otel adını söylediğini bildirir
    # Otelin puan bilgisini çeker
    
    sleep(2)

    try:
        try:
            yorum_Bilgisi = tarayici.find_element(By.XPATH,'/html/body/div[3]/div[11]/div/div/div[2]/div[1]/div[1]/div[2]/div[2]/div/div[2]').text
        except:
            yorum_Bilgisi = tarayici.find_element(By.XPATH,'/html/body/div[3]/div[11]/div/div/div[2]/div[1]/div[1]/div[2]/div[2]/div[2]/div[2]').text
        try:
            puan_Bilgisi = tarayici.find_element(By.XPATH,'/html/body/div[3]/div[11]/div/div/div[2]/div[1]/div[1]/div[2]/div[1]/div/div').text
        except:
            puan_Bilgisi = "???"

            
    
        try:
            yorum_Bilgisi1 = tarayici.find_element(By.XPATH,'/html/body/div[3]/div[11]/div/div/div[2]/div[1]/div[2]/div[2]/div[2]/div/div[2]').text
        except:
            yorum_Bilgisi1 = tarayici.find_element(By.XPATH,'/html/body/div[3]/div[11]/div/div/div[2]/div[1]/div[2]/div[2]/div[2]/div[2]/div[2]').text
        try:
            puan_Bilgisi1 = tarayici.find_element(By.XPATH,'/html/body/div[3]/div[11]/div/div/div[2]/div[1]/div[2]/div[2]/div[1]/div/div').text
        except:
            puan_Bilgisi1 = "???"




        try:
            yorum_Bilgisi2 = tarayici.find_element(By.XPATH,'/html/body/div[3]/div[11]/div/div/div[2]/div[1]/div[3]/div[2]/div[2]/div/div[2]').text
        except:
            yorum_Bilgisi2 = tarayici.find_element(By.XPATH,'/html/body/div[3]/div[11]/div/div/div[2]/div[1]/div[3]/div[2]/div[2]/div[2]/div[2]').text
        try:
            puan_Bilgisi2 = tarayici.find_element(By.XPATH,'/html/body/div[3]/div[11]/div/div/div[2]/div[1]/div[3]/div[2]/div[1]/div/div').text
        except:
            puan_Bilgisi2 = "???"

            

        try:    
            yorum_Bilgisi3 = tarayici.find_element(By.XPATH,'/html/body/div[3]/div[11]/div/div/div[2]/div[1]/div[4]/div[2]/div[2]/div/div[2]').text
        except:
            yorum_Bilgisi3 = tarayici.find_element(By.XPATH,'/html/body/div[3]/div[11]/div/div/div[2]/div[1]/div[4]/div[2]/div[2]/div[2]/div[2]').text
        try:
            puan_Bilgisi3 = tarayici.find_element(By.XPATH,'/html/body/div[3]/div[11]/div/div/div[2]/div[1]/div[4]/div[2]/div[1]/div/div').text
        except:
            puan_Bilgisi3 = "???"

            

        try:
            yorum_Bilgisi4 = tarayici.find_element(By.XPATH,'/html/body/div[3]/div[11]/div/div/div[2]/div[1]/div[5]/div[2]/div[2]/div/div[2]').text
        except:
            yorum_Bilgisi4 = tarayici.find_element(By.XPATH,'/html/body/div[3]/div[11]/div/div/div[2]/div[1]/div[5]/div[2]/div[2]/div[2]/div[2]').text
        try:
            puan_Bilgisi4 = tarayici.find_element(By.XPATH,'/html/body/div[3]/div[11]/div/div/div[2]/div[1]/div[5]/div[2]/div[1]/div/div').text
        except:
            puan_Bilgisi4 = "???"
    except:
        print("Otelin Yorumu Yok")
        yorum_Bilgisi = "Otelin Yorumu Yok"
        yorum_Bilgisi1 = "Otelin Yorumu Yok"
        yorum_Bilgisi2 = "Otelin Yorumu Yok"
        yorum_Bilgisi3 = "Otelin Yorumu Yok"
        yorum_Bilgisi4= "Otelin Yorumu Yok"
    tarayici.quit()

    
    return jsonify({
    "yorum_Bilgisi":yorum_Bilgisi, "yorum_Bilgisi1":yorum_Bilgisi1, "yorum_Bilgisi2":yorum_Bilgisi2, "yorum_Bilgisi3":yorum_Bilgisi3, "yorum_Bilgisi4":yorum_Bilgisi4, "puan_Bilgisi":puan_Bilgisi, "puan_Bilgisi1":puan_Bilgisi1, "puan_Bilgisi2":puan_Bilgisi2, "puan_Bilgisi3":puan_Bilgisi3, "puan_Bilgisi4":puan_Bilgisi4
})

if __name__ == '__main__':
    app.run(debug=True)
