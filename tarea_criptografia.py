from math import gcd

x=True
while x:
    try: 
        op=int(input("""MENU
        1. Generar claves usando Diffie-Hellman
        2. Generar claves usando RSA
        3. Salir\n"""))
        match op:
            case 1:
                #PROGRAMA PARA GENERAR CLAVES DIFFIE-HELLMAN
                def validar_num(x):
                    y=True
                    while y:
                        try:
                            x=int(input(f"Eliga un valor público ({x}):"))
                        except ValueError:
                            print("Favor de verificar que haya ingresado un número entero")
                        else:
                            y=False
                            return x
                        
                print("""
                --------------------------------------------------------
                      Creación de claves públicas con Diffie-Hellman
                --------------------------------------------------------""")
                p=validar_num('p')
                g=validar_num('g')
                a=validar_num('a')
                b=validar_num('b')

                print("\nGenerando las claves públicas...")
                A=(g**a)%p
                B=(g**b)%p

                print("Llave pública de Alice (A): ", A)
                print("Llave pública de Bob (B): ", B)

                alice_key=(B**a)%p
                bob_key=(A**b)%p

                print("Llave de Alice: ", alice_key)
                print("Llave de Bob: ", bob_key,"\n")

            case 2:
                print("""
                --------------------------------------------------------
                                  Creación de claves RSA
                --------------------------------------------------------""")
                def validar_numprimos(x):
                        y=True
                        while y:
                            try:
                                x=int(input(f"Eliga un número primo ({x}):"))
                                if x%2==0 or x%3==0 or x%5==0 or x%7==0:
                                    print("Favor de verificar que haya ingresado un número primo")
                                    x=""
                                else:
                                    y=False
                                    return x
                            except ValueError:
                                print("Favor de verificar que haya ingresado un número primo")
                
                p=validar_numprimos('p')
                q=validar_numprimos('q')

                n=p*q
                pn=(p-1)*(q-1)
                for i in range(4, pn):
                    if gcd(i, pn)==1:
                        e=i
                        break
                
                d=pow(e,-1, pn)
                print(f"\nClave pública:, ({e},{n})")
                print(f"Clave privada:, ({d},{n})\n")

            case 3:
                x=False
                print("Saliendo...")
            case _:
                print("Ingrese una opción válida")
    
    except ValueError:
        print("Ingrese una opción válida")
    



