""" KULLANILAN UYGULAMALAR
Python , Kivy , MySql ve Pycharm ile oluşturulan uygulama
email:ayapimim.muh@gmail.com, mesaproje34@gmail.com
tarih: 17.04.2022
"""
#----------------   KÜTÜPHANE -------------------------#
#------------------------------------------------------#
from kivy.app import App
from kivy.lang import Builder
import mysql.connector
import time
from datetime import datetime
from kivy.uix.screenmanager import ScreenManager, Screen

#----------------   ANA MENÜ  OLUŞTURULMASI --------------#
#---------------------------------------------------------#

#----------------   CARİ MENÜ OLUŞTURULMASI --------------#
#---------------------------------------------------------#

#-------------  CARİ HAREKET MENÜ OLUŞTURULMASI ----------#
#---------------------------------------------------------#


#----------------   PENCERELER ARASI GEÇİŞ ---------------#
#---------------------------------------------------------#

Builder.load_file('Cari.kv')
#Builder.load_file('Hareket.kv')

class CariPenceresi(Screen):
    pass
class HareketPenceresi(Screen):
    pass

screen_manager = ScreenManager()

screen_manager.add_widget(CariPenceresi(name="screen_one"))
screen_manager.add_widget(HareketPenceresi(name="screen_two"))


#-----------   UYGULAMA YAPIMI VE  ADI   ---------------------#
#-------------------------------------------------------------#

class Cari(App):
    def build(self):

# -----------   VERİBAĞLANTILARI  YAPIMI  ---------------------#
# -------------------------------------------------------------#

        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1234",
            database="akce_db",)

        # Create A Cursor
        c = mydb.cursor()

        c.execute("CREATE DATABASE IF NOT EXISTS akce_db")
         #Check to see if database was created
        #c.execute("SHOW DATABASES")
        #for db in c:
        #    print(db)

        c.execute("CREATE TABLE if not exists cari \
                            (c_id integer primary key AUTO_INCREMENT UNIQUE NOT NULL,\
                            c_adi	text, c_soyadi text, c_adres text  )")
       # c.execute(
        #    "CREATE TABLE if not exists cari( id integer primary key AUTO_INCREMENT not null , ad  text , soyad text, adres text)  ")

        c.execute(
            "Create table if not exists hareket (h_id integer primary key AUTO_INCREMENT not null,h_aciklama text,"
            "h_alacak integer,h_borc integer,tarih text,zaman real)")
        # Commit our changes
        mydb.commit()

        # Close our connection
        mydb.close()
        print("bağlantı  bitti")

        #return screen_manager
        return Builder.load_file('Cari.kv')

    def hakekle(self):
        print("testi2 geçti")
        self.root.ids.hg_label.text="AkceV1 mail:akatproje@gmail.com"
        self.root.ids.pro_label.text="soru ve öneri için"


    def sil(self):
        self.root.ids.hg_label.text = "silindi"
        self.root.ids.pro_label.text = "TANITIM silindi"

    def veriekle(self):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1234",
            database="akce_db", )
        c = mydb.cursor()
        sql_command = "insert into cari (c_adi,c_soyadi) values (%s,%s)"
        value1 = (self.root.ids.ad_input.text)
        value2 = (self.root.ids.soyad_input.text)

        c.execute(sql_command, (value1,value2))
        self.root.ids.ad_input.text=""
        self.root.ids.soyad_input.text=""
        mydb.commit()
        mydb.close()

    def tablo(self):
        pass

    def ekran(self):
        pass

#uygulama yapımı:
Cari().run()

#-----------------------------  KAYNAKLAR  ----------------------------#
#----------------------------------------------------------------------#

""" NOT:
program hazırlarken veya çalışırken pek çok kaynak bulunabilir,  ancak;
görsel olarak en çok faydalandığım kaynak linklerini  aşağıda belirttim; 
kendilerine yürekten teşekkür ederim
ilgi duyanlara tavsiye ederim
kaynaklar:  

https://kivycoder.com/using-mysql-database-with-kivy-python-kivy-gui-tutorial-56/
https://kivy-tr.readthedocs.io/tr/latest/index.html
"""