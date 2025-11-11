import os
import json
from pathlib import Path


def beli_game():
    pass

def top_up(id_akun_saat_ini):
    
    
    lokasiFile = Path(__file__).resolve()
    folderSekarang = lokasiFile.parent
    path_json = folderSekarang / "DATA" / "DATA_USER.json"
    
    with open(path_json, "r") as file:
        data_user = json.load(file)
    
    print("=================== MENU TOP UP ===================\n")
    
    nominal = int(input("Masukan Nominal Top Up: "))
    
    
    
    akun_saat_ini = data_user[id_akun_saat_ini]
    saldo_akun = akun_saat_ini["saldo"]
     
    percobaan = 0
    while True:
        pin = int(input("Masukan PIN anda: "))
        if pin == akun_saat_ini["PIN"]:
            saldo_akun += nominal
            
            with open(path_json, "w") as newValue: 
                json.dump(data_user, newValue, indent=4)

            print("==================================================\n")    

            print("Top Up Berhasil!")
            print(f"saldo anda saat ini: {saldo_akun}")
            break
        else:
            print("Pin Anda Salah, silahkan coba lagi")
            percobaan+=1
            if percobaan == 5:
                print("Terlalu Banyak Mencoba, Anda akan dibawa kemabli ke Menu Utama")
                


    
    
    
    
    
    