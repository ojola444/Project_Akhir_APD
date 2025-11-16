def input_string_handling(input_user):
    if input_user == "" or input_user.isspace() :
       raise ValueError("input tidak boleh kosong atau spasi saja")
    
    elif input_user.isdigit() :
       raise ValueError("input tidak boleh nomor saja")

      
def input_number_handling(input_user):
    try :
        input_user
        
    except ValueError :
        raise ValueError("input bukan angka")
    
    if input_user < 0 :
        raise ValueError("angka tidak boleh kurang dari 1")
    

