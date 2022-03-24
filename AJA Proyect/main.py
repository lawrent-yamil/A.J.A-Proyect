from func.func import mostrar_informacion

while True:
    print("""
                A.J.A
        Codigos de ingreso:
        C     3000-3999
        RRHH  1000-1999
        P     5000-5999
        G     9000-9999
        M     4000-4999

    """)
    try:
        codigo_ingreso = int(input("Digite su Codigo de Ingreso: "))

        if codigo_ingreso >= 3000  and codigo_ingreso <= 3999:
            mostrar_informacion("C",3500)
        elif codigo_ingreso >= 1000 and codigo_ingreso <= 1999:
            mostrar_informacion("RRHH",2250)
        elif codigo_ingreso >= 5000 and codigo_ingreso <= 5999:
            mostrar_informacion("P",5700)
        elif codigo_ingreso >= 9000 and codigo_ingreso <= 9999:
            mostrar_informacion("G",4200)
        elif codigo_ingreso >= 4000 and codigo_ingreso <= 4999:
            mostrar_informacion("M",3200)
        else:
            print("Ingrese un numero Correcto")
    except:
        print("Solo Números")

    s_n = input("¿Desea salir? S/N ")
    if s_n == "S" or s_n == "Si" or s_n == "s" or s_n == "si":
        break
    else:
        continue