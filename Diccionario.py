#!/usr/bin/python3
from colorama import init,Fore,Back,Style

while True:
    init()
    print("Serie de ejercicios Con diccionaios y sus metodos")
    print("ejercicio 1 = '1' :")
    print("ejercicio 2 = '2' :")
    print(Fore.RED+"salir"+" :")
    user_input = input(" :")
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    if user_input == "salir":
        break
    elif user_input == "1":
        print("\nEJERCICIO #1 "+" :")
#1)CREAR UN DICCIONARIO VACIO Y QUE CAPA8 LLENE EL DICCIONARIO y mostrar con for . 
# 2) MOSTRARLA COMO TUPLA. 
# 3)CREAR UN SEGUNDO DICCIONARIO. 
# 4)UTILIZAR METODO UPDATE unificar dirccionario 1 y 2().
# 5) PREGUNTAR SI DECEA ELIMINAR UN ITEM ,USAR METODO POP().
# 6) ORDENAR CON FOR.
# 7) VERIFICAR ITEM CON GET (ENTRADA DE CAPA 8)
        dir1 = dict()#------------------------------------->parte 1)
        print(Fore.LIGHTYELLOW_EX+"\n")
        x = input("ingrese una key "+" :")
        y = input("ingrese un valor"+" :")
        xx = input("ingrese una key"+" :")
        yy = input("ingrese un valor"+" :")
        z = input("ingrese una key"+" :")
        zz = input("ingrese un valor"+" :")

        bull1 = dir1.setdefault(x,y)
        bull2 = dir1.setdefault(xx,yy)
        bull3 = dir1.setdefault(z,zz)
        print("\n\n")
        for k,v in dir1.items():
            print(k,"=",v)
        print("\n\n")
        print(Fore.LIGHTWHITE_EX+"\nTUPLA")
        tp = dir1.items()#---------------------------->parte 2)
        print(tp)
        print("\n\n")
        #---------------------------------------------------->parte 3)
        dir2 = dict(Tortrix="barbacoa",Lenguaje='python',cargo='cargador de bultos')
        dir1.update(dir2)#------------------------------------------>parte 4)
        print(Fore.LIGHTGREEN_EX+"\nDiccionario dir1 y dir 2"+" :")
        print(dir1)
        print("\n\n")
        
        print(Fore.LIGHTYELLOW_EX+"desea eliminar algun item")#----------------------------------->5
        print("si")
        print(Fore.RED+"no")
        in_user = input(" :")
        print(Fore.LIGHTWHITE_EX+"\n")
        if in_user == "si":
            print(dir1)
            po = input("ingrese  una key valido a eliminar"+" :")
            po_ped = dir1.pop(po)
            print(dir1)
            print("\n")
            print("desea eliminar otro"+" :")
            print("si"+": ")
            print(Fore.RED+"no"+": ")
            in_user = input(":")
            print(Fore.WHITE+"\n")
            if in_user == "si":
                print(dir1)
                pi = input("ingrese  una key valido a eliminar"+" :")
                po_ped2 = dir1.pop(pi)
                print(dir1)
                print("\n")
            elif in_user == "no":
                print("deje de chingar")
            else:
                print("")
        elif in_user == "no":
            print("no jodaaa coñoooo")
        else:
            print("") 
        print("ORDENADO CON FOR")#------------------------>parte 6)
        for k,v in dir1.items():
            print(k,":",v)
        print("\n\nMetodo Get")#-------------------------------->parte 7)
        print("desea verificar una key"+" :")
        print("si")
        print("no")
        ul_user = input("\ningrese una opcion valida"+" :")
        if ul_user == "si":
            for k,v in dir1.items():
                print(k,":",v)
            
            print("\n\n")
            a = input("ingrese una key"+":")
            var1 = dir1.get(a)
            print("Esta es la key :",a," "+"Este es el valor :",var1)
            for k,v in dir1.items():
                print(k,":",v)
            print("\n\n")
            print("desea verificar mas key's"+" :")
            print("Si")
            print("no")
            if ul_user == "si":
                print("\n")
                print(dir1)
                print("\n")
                b = input("ingrese una key valida"+" :")
                var2 = dir1.get(b)
                print("Esta es la Key :",b," "+"Este es el valor :",var2)
                for k,v in dir1.items():
                    print(k,":",v)
            elif ul_user == "no":
                print("lol XD")
            else :
                print("")    
            
        elif ul_user == "no":
            print("juasjuasjuas.........")
        else:
            print("")
        print("\n\n")
        


    else :
        print("")



