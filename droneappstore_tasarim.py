# -*- coding: utf-8 -*-
"""
Created on Tue May 17 16:11:33 2022

@author: okmen
"""
import sys
import time
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow,QMessageBox,QMessageBox,QFileDialog,QTableWidgetItem
from PyQt5 import QtWidgets
from PyQt5.QtCore import QThread, pyqtSignal,Qt
from DroneAppStore_python import Ui_MainWindow2
from giris_python import Ui_MainWindow
import requests
from requests.auth import HTTPBasicAuth
import json
import zipfile, io,glob
import os
global girisyaponay
import runpy
girisyaponay=False
from datetime import datetime
import shutil

class MainWindow(QMainWindow):
        def __init__(self):
            super(MainWindow, self).__init__()
            self.ui = Ui_MainWindow()
            self.ui.setupUi(self)
            self.ui.girisbuton.clicked.connect(self.girisbuton)
            
            
            try:                      
                    with open("files/hatirla.txt","r") as dosya:
                        hatirlama=dosya.readline()
                    dosya.close()
                    hatirlama=hatirlama.split(";")
                    self.ui.email.setText(hatirlama[0])
                    self.ui.sifre.setText(hatirlama[1])
                    self.ui.checkBox.setChecked(True)
            except:
                    pass
            
            
        def girisbuton(self):
            kullaniciusername=str(self.ui.email.toPlainText())
            kullanicisifre=str(self.ui.sifre.toPlainText())
            
            global girisyaponay   
            base= "https://www.droneappstore.com/api";
            
            response = requests.get(
                base+"/index",
                auth=HTTPBasicAuth(kullaniciusername,kullanicisifre),                   
            )
            
            #print(response.text)
            sonuc = json.loads(response.text)
            if sonuc["message"]=="Connection Successful":
                girisyaponay=True
                
                if self.ui.checkBox.isChecked():
                    try:
                            
                        with open("files/hatirla.txt","w") as dosya:
                            dosya.write(kullaniciusername+";"+kullanicisifre)
                        dosya.close()
                    except:
                        pass
                else:
                    try:
                            
                        with open("files/hatirla.txt","w") as dosya:
                            dosya.write("")
                        dosya.close()
                    except:
                        pass
                self.cams = MainWindow2() 
                self.cams.show()
                self.close()
global gorevbitmedenbakma               
gorevbitmedenbakma=True                
   
class AThread(QThread):
    finished = pyqtSignal()
    progress = pyqtSignal(dict)
    def __init__(self):
        super().__init__()

    def run(self):
        while 1:
            
            global queid,app,appID,updates,link,droneid,gorevbitmedenbakma
            #print(gorevbitmedenbakma)
            try:
                     
                def dronegoreval(droneid):
                    try:
                            
                        global queid,app,appID,updates,link
                        base= "https://www.droneappstore.com/api";
                        post = {"droneID": droneid}
                        response = requests.post(
                            base+"/ques",
                            data=post,
                            auth=HTTPBasicAuth("test","test"),                   
                        )
                        
                        #print(response.text)
                        sonuc = json.loads(response.text)
                        sonuc=sonuc[0]
                        self.progress.emit((sonuc))
                    except Exception as e:
                        pass
                        #print(sonuc)
                    #print(sonuc)
                
                
                
                    
                if gorevbitmedenbakma==True:   
                    gorevbitmedenbakma=False                     
                    dronegoreval(droneid)
                    time.sleep(5)
            except Exception as e:
                #print(e)
                pass

# 2. bir thread durdur
global fname
class uygulama(QThread):
    hata = pyqtSignal(str)
    bitti = pyqtSignal(str)
    def __init__(self):
        super().__init__()

    def run(self):
        hatavar1=False
        global gorevbitmedenbakma
        gorevbitmedenbakma=False       
        try:               
                file_globals = runpy.run_path(fname[0])      
        except:                 
                self.hata.emit("aa")
                hatavar1=True
                                    
        finally:
            if hatavar1==True:
                hatavar1=False         
            else:
               self.bitti.emit("aa")
            

class MainWindow2(QMainWindow):
        def __init__(self):
            global gorevbitmedenbakma
            super(MainWindow2, self).__init__()
            self.ui = Ui_MainWindow2()
            self.ui.setupUi(self)
            self.setWindowTitle("Drone App Store")
            
            self.ui.urunsec.clicked.connect(self.manuelpysec)
            self.ui.dronesec.currentTextChanged.connect(self.droneal)
            self.ui.chance_drone.clicked.connect(self.chance_drone)
            self.ui.startmission.clicked.connect(self.startmission)
            self.ui.stopmission.clicked.connect(self.stop)
            
            self.ui.dronesec.clear()
        
            base= "https://www.droneappstore.com/api";
        
            response = requests.get(
                base+"/drones",
                auth=HTTPBasicAuth("test","test"),                   
            )
            
            
            self.ui.chance_drone.setVisible(False)
            sonuc = json.loads(response.text)
            durum=sonuc["status"]
            if durum==True:            
                kacdronevar=len(sonuc["drones"])
                self.ui.dronesec.addItem("Select Drone")
                for droneindex in range(0,kacdronevar):     
                    droneid=sonuc["drones"][droneindex]["droneID"]
                    dronename=sonuc["drones"][droneindex]["name"]
                    self.ui.dronesec.addItem("Drone:"+str(dronename)+" | id:"+str(droneid))
                    print(str(droneid)+" ; "+str(dronename))
            
            
            #hazırlık bitti
            global myworker
            self.myworker = AThread()
            self.myworker.finished.connect(self.finishedAThread)
            self.myworker.progress.connect(self.reportProgress)
            self.myworker.start()
          
        def stop(self):
            try:                  
                self.myworker.terminate()         
                self.myworker = None
            except:
                pass
            try:                  
                self.myworker_uygulama.terminate()
                self.myworker_uygulama = None
            except:pass
            
            erorrr = QTableWidgetItem(str("Waiting"))  
            self.ui.log.setItem(0, 3, erorrr)
            #self.myworker.quit()                    
            
            
        def startmission(self):
            global fname,dronename,gorevbitmedenbakma,droneida
            gorevbitmedenbakma=True
            try:
                droneida=self.ui.dronesec.currentText()   
                dronename=droneida.split("Drone:")[1].split(" |")[0]
                dronename=str(dronename)
                try:
                    erorrr = QTableWidgetItem(str("Working"))  
                    self.ui.log.setItem(0, 3, erorrr)
                    print(fname[0])
                    
                    global myworker_uygulama
                    self.myworker_uygulama = uygulama()
                    #self.myworker_uygulama.finished.connect(self.finishedAThread)
    
                    self.myworker_uygulama.hata.connect(self.hata_progress)
                    self.myworker_uygulama.bitti.connect(self.bitti_progress)
                    self.myworker_uygulama.start()
                        
                    dronenamea = QTableWidgetItem(str(dronename))   
                    newitem_app = QTableWidgetItem(str((fname[0]).split("/")[-1])) 
                    newitem_updates = QTableWidgetItem(str(datetime.now()))  
                    self.ui.log.setItem(0, 0, dronenamea)
                    self.ui.log.setItem(0, 1, newitem_app)
                    self.ui.log.setItem(0, 2, newitem_updates)             
                
                except:
                    pass
            except:
                pass
        
        global gorevbitmedenbakma
        
        def hata_progress(self,n):
            global gorevbitmedenbakma
            erorrr = QTableWidgetItem(str("Error"))  
            self.ui.log.setItem(0, 3, erorrr)
            gorevbitmedenbakma=True
            
        def bitti_progress(self,n):
            print("gorev bitti")
            global gorevbitmedenbakma
            erorrr = QTableWidgetItem(str("Completed"))  
            self.ui.log.setItem(0, 3, erorrr)
            gorevbitmedenbakma=True

        
        
        
        def chance_drone(self):
            self.ui.chance_drone.setVisible(False)
            self.ui.dronesec.setEnabled(True)
        def droneal(self):
          

            try:
                        
                    global droneid,dronename,onlinemi,gorevbitmedenbakma
                    droneida=self.ui.dronesec.currentText()
                    droneid=droneida.split("id:")[1]
                    droneid=int(droneid)
                    dronename=droneida.split("Drone:")[1].split(" |")[0]
                    dronename=str(dronename)
                    print("dronename")
                    print(dronename)
                    self.ui.chance_drone.setVisible(True)
                    self.ui.dronesec.setEnabled(False)
                    gorevbitmedenbakma=True
                    
            except:
                pass
        global indirme_basarilimi
        indirme_basarilimi=False   
        #report porgresler        
        def reportProgress(self, sonuc):
            def indirmebaslat(link):
                shutil.rmtree('files/apps')
                time.sleep(2)
                os.mkdir('files/apps')
                time.sleep(0.1)
                # indirmeye başlat
                global indirme_basarilimi
                r = requests.get(link)
                z = zipfile.ZipFile(io.BytesIO(r.content))
                z.extractall("files/apps/")
                indirme_basarilimi=True 
            
            global dronename,indirme_basarilimi,queid,onlinemi
            #print(sonuc)
            queid=sonuc["queID"]
            app=sonuc["app"]
            appID=sonuc["appID"]
            updates=sonuc["updates"][0]["date"]
            link=sonuc["updates"][0]["link"]
            newitem_queid = QTableWidgetItem(str(queid))
            newitem_app = QTableWidgetItem(str(app))   
            newitem_appID = QTableWidgetItem(str(appID))   
            newitem_updates = QTableWidgetItem(str(updates))   
            newitem_link = QTableWidgetItem(str(link))   
            dronenamea = QTableWidgetItem(str(dronename))   
            
            self.ui.log.setItem(0, 0, dronenamea)
            self.ui.log.setItem(0, 1, newitem_app)
            self.ui.log.setItem(0, 2, newitem_updates)
            #print(indirme_basarilimi)
         
            
            
            
            def statusdegistir(queid,status):
                            # 0 => Waiting,
                            # 1 => Completed,
                            # 2 => Working
                            # 3 => Error
                            ###############################################3   
                            base= "https://www.droneappstore.com/api";   
                            post = {"queID":queid, "status": status}
                            response = requests.post(
                                base+"/status",
                                data=post,
                                auth=HTTPBasicAuth("test","test"),                   
                            )
                            
                            #sonuc = json.loads(response.text)
            
            global gorevbitmedenbakma
            if indirme_basarilimi==False:                
                indirmebaslat(link)
                hatavar=False
                if indirme_basarilimi==True:
                    gorevbitmedenbakma=False
                    print("İndirme Tamamlandı")
                    time.sleep(2)
                    
                    
                    listelemeicin = glob.glob('files/apps/*.py')
                    kutuphane = listelemeicin[0].split("\\")[1]
                    try:
                        
                        file_globals = runpy.run_path(listelemeicin[0])
                        statusdegistir(queid,2)
                        time.sleep(0.01)
                    except Exception as e:
                        print(e)
                        erorrr = QTableWidgetItem(str("Error"))  
                        self.ui.log.setItem(0, 3, erorrr)
                        gorevbitmedenbakma=True
                        
                        #statusdegistir(queid,3)
                        hatavar=True
                    finally:
                        
                        print("bitti")
                        if hatavar==True:                           
                            statusdegistir(queid,3)
                        else:
                            statusdegistir(queid,1)
                        gorevbitmedenbakma=True
                    print("çalışması lazım ")
            
            
            
                        
            
            
            
            
            
            
        def finishedAThread(self):
            self.myworker = None 
        #bitti o kısım progress kısımları
        
        global fname
        def manuelpysec(self):
            global fname
            fname=QFileDialog.getOpenFileName(self, 'Open file', 'D:\codefirst.io\PyQt5 tutorials\Browse Files', 'Images (*.py)')
            print(fname[0])
            self.ui.secilenurunlabel.setText((fname[0]).split("/")[-1])
        
        def closeEvent(self, event): 
            reply = QMessageBox.question(self, 'Dikkat !!',
                "Çıkış Yapmak Üzeresiniz, kapatmak istediğinize emin misiniz?",
                 QMessageBox.Yes,
                 QMessageBox.No)
            if reply == QMessageBox.Yes:         
                if self.myworker:
                    #self.myworker = None 
                    self.myworker.quit() 
                    self.myworker.terminate()         
                    self.myworker = None
                del self.myworker
                super(MainWindow2, self).closeEvent(event)
            else:
                event.ignore()
            
            
       
            



 

if __name__ == "__main__":
        app = QApplication(sys.argv)

        window = MainWindow()
        window.setWindowTitle("Giriş")
        window.show()

        sys.exit(app.exec_())
        