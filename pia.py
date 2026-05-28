import sqlite3
import bcrypt

x=True
intentos=0

while x:
    try: 
        op=int(input("""
        -----------------------------------------------------
            MENÚ
            1. Iniciar sesión 
            2. Registrar personal  
            3. Salir 
        -----------------------------------------------------
        """))

        match op:
            case 1:
                usuario=input("Ingrese el nombre de usuario:")
                contraseña=input("Ingrese contraseña del usuario:")
                
                #Compara la contraseña ingresada con el hash
                conn=sqlite3.connect("login.db")
                cursor=conn.cursor()    
                cursor.execute("""
                               SELECT password_hash FROM login WHERE usuario=?
                               """, (usuario,)) 
                resultado=cursor.fetchone()
                if resultado:
                    hash_almacenado=resultado[0]

                    #CONTRASEÑA CORRECTA
                    if bcrypt.checkpw(contraseña.encode(), hash_almacenado):
                        cursor.execute("""
                                       SELECT activo FROM login WHERE usuario=?
                                        """, (usuario,))
                        validar_activo=cursor.fetchone()[0]
                        if validar_activo:
                            print("Inicio de sesión exitoso")   
                        else:
                            print("La cuenta está bloqueada. Pida a un administrador que la desbloquee.")

                    #CONTRASEÑA INCORRECTA
                    else:
                        if intentos>=5:
                            print("Demasiados intentos fallidos. La cuenta ha sido bloqueada. Pida a un administrador que la desbloquee.")
                            cursor.execute("""
                                           UPDATE login SET activo=? WHERE usuario=?
                                           """, (False, usuario))
                            conn.commit()
                        else:
                            print("Contraseña incorrecta. Intente nuevamente.")
                            intentos=intentos+1

                else:
                    print("Usuario no encontrado")
                conn.close()    

        #valirdar que coincida con BDu

            case 2:
                usuario=input("Ingrese el nombre de usuario:")
                contraseña=input("Ingrese la contraseña del usuario:")
                contraseña=bcrypt.hashpw(contraseña.encode(), bcrypt.gensalt())
                #Crear la base de datos, tabla y guardar el usuario con contraseña hasheada
                conn=sqlite3.connect("login.db")
                cursor=conn.cursor()
                cursor.execute("""
                               CREATE TABLE IF NOT EXISTS login (
                                id INTEGER PRIMARY KEY AUTOINCREMENT, 
                               usuario TEXT,
                               password_hash BLOB, 
                               activo BOOLEAN
                               )
                               """)
                
                cursor.execute("""
                               INSERT INTO login (usuario, password_hash, activo)
                               VALUES (?,?,?)
                               """, (usuario, contraseña, True))
                conn.commit()
                conn.close()

        #hashear la contraseña, guardar en BD
            case 3:
                exit()
            case _:
                print("Ingrese una opción válida") 

    except ValueError:
        print("Ingrese una opción válida") 
