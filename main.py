import inquirer
import os
import prettytable
import time

from MENU import menu_crud_admin,menu_multi_login,menu_user,menu_autentikasi_user
from AUTENTIKASI import admin_login,user_login,user_regist


# Program Utama

if __name__ == "__main__":
    while True:
        
        menu_dipilih = menu_multi_login()
        if menu_dipilih == "1":
            admin_login()
            
        elif menu_dipilih == "2":
            menu_autentikasi_dipilih = menu_autentikasi_user()
            
            if menu_autentikasi_dipilih == "1":
                user_login()
            else:
                user_regist()
                
        else: 
            break
        
        
    print("=========PROGRAM BERAKHIR=========")
            
        
    
    
