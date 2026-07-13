juegos = {
'G001': ['Eclipse Runner', 'PC', 'accion', 'T', True,
'NovaStudio'],
'G002': ['Puzzle Atlas', 'Switch', 'puzzle', 'E', False,
'BrightWorks'],
'G003': ['Sky Legends', 'PS5', 'aventura', 'T', True,
'OrionGames'],
'G004': ['Racing Pulse', 'PC', 'carreras', 'E', True,
'VelocityLab'],
'G005': ['Mystic Farm', 'Switch', 'simulacion', 'E', False,
'GreenSeed'],
'G006': ['Shadow Tactics', 'Xbox', 'estrategia', 'M', False,
'IronGate']
}
inventario = {
'G001': [9990, 7],
'G002': [19990, 0],
'G003': [42990, 3],
'G004': [14990, 5],
'G005': [17990, 9],
'G006': [39990, 2],
}
def mostrar_menu():
    print("""
        1. stock por plataforma
        2. busqueda de juegos por rango de precio
        3. actualizar precio de juego
        4. agregar juego
        5. eliminar juego
        6. salir""")


def validar_opcion():
    while True:
        try:
            opc=int(input("Ingrese una opcion del 1 al 6: "))
            if opc <1 or opc >6:
                print("Error no existe esa opcion")
            else:
                break
            print("error debe ser un numero dentro del indicado")
        except ValueError:
            print("")
    return opc

def validar_titulo(titulo):
    if titulo.strip()=="":
        return False
    else:
        return True

def validar_plataforma(plataforma):
    if plataforma.strip()=="":
        return False
    else:
        return True

def validar_genero(genero):
    if genero.strip()=="":
        return False
    else:
        return True

def validar_calificacion(calificacion):
    if calificacion.strip()=="" and calificacion=="E" and calificacion=="T" and calificacion=="M":
        return False
    else:
        return True

def validar_codigo(codigo):
    if codigo.strip()=="":
        return False
    else:
        return True

def validar_multiplayer(multiplayer):
    if multiplayer.lower()==""  != "s" and multiplayer != "n":
        return False
    else:
        return True



def validar_editor(editor):
    if editor.strip()=="":
        return False
    else:
        return True


def validar_precio(precio):
    if precio<=0:
        return False
    else:
        return True

def validar_stock(stock):
    if stock<0:
        return False
    else:
        return True



def leer_opcion():
        print("""
        1. stock por plataforma
        2. busqueda de juegos por rango de precio
        3. actualizar precio de juego
        4. agregar juego
        5. eliminar juego
        6. salir""")

        opc=int(input("Ingrese una opcion"))
        while opc<1 or opc >6:
            print("Opcion valida")
            opc=int(input("Ingrese una opcion"))
        return opc


def buscar_codigo(codigo):
    for clave in inventario:
        if clave.upper()==codigo.upper():
            return True
    return False

def actualizar_precio(codigo, nuevo_precio):
    if buscar_codigo(codigo):
        for clave in inventario:
            if clave.upper()== codigo.upper():
                inventario[clave][0] =nuevo_precio
                return True
    return False

def stock_plataforma(plataforma, juegos, inventario):
    t_stock=0
    for codigo in juegos:
        if juegos[codigo][1]==plataforma:
            t_stock=t_stock+inventario[codigo][1]
            print(f"El stock disponible es:{t_stock}")

def busqueda_precio(p_min, p_max):
    lista_resultados=[]
    for codigo, datos_inv in inventario.items():
        precio=datos_inv["precio"]
        stock= datos_inv["stock"]
    if p_min<=precio<=p_max and stock>0:
        titulo=juegos[codigo]["titulo"]
    lista_resultados.append(f"{titulo}-{codigo}")
    if lista_resultados:
        lista_resultados.sort()
        for juegos in lista_resultados:
            print("juego")
    
def agregar_juego(codigo, titulo, plataforma, genero, calificacion, multiplayer, editor, precio, stock, juegos, inventario):
    if buscar_codigo(codigo, inventario)==False:
        juegos[codigo]=(titulo, plataforma, genero, calificacion, multiplayer,editor)
        inventario[codigo]=[precio, stock]
        return True
    else:
        return False




def eliminar_juego(codigo):
    if buscar_codigo(codigo):
        juegos.pop(codigo)
        inventario.pop(codigo)
        return True
    else:
        return False


while True:
    mostrar_menu()
    opc=leer_opcion()
    if opc==1:
        plataforma=input("Ingrese una plataforma: ")
        stock_plataforma(plataforma, juegos, inventario)
    elif opc==2:
        while True:
            try:
                p_min=int(input("Ingrese el precio minimo: "))
                p_max=int(input("Ingrese el precio maximo: "))
                if p_min>=0 and p_max>=0 and p_min <=p_max:
                    break
                else:
                    print("Debe ingresar numeros enteros(mayores o igual a cero y minimo menor o igual al maximo)")
            except ValueError:
                print("Debe ingresar valores entero")
    
    elif opc==3:
        pass
    elif opc==4:
        codigo=input("Ingrese el codigo de su juego: ").upper
        if validar_codigo(codigo)==False:
            print("El codigo esta vacio, vuelva a escribir")
            continue
        titulo =input("Ingrese el nombre: ").upper
        if validar_titulo(titulo)==False:
            print("No puede estar vacios ni tener espacio")
            continue
        plataforma=input("Ingrese la plataforma del juego: ").upper
        if validar_plataforma(plataforma):
            print("No puede estar vacio ni con espacio")
            continue
        genero=input("Ingrese genero del juego: ").upper
        print("No puede estar vacio ni con espacios")
        calificacion=input("Ingrese su calificacion debe ser E,T,M: ").upper
        if validar_calificacion(calificacion)==False:
            print("No esta dentro de la opciones validas")
        multiplayer=input("Juego es multiplaye, ingrese S o N: ").upper
        if validar_multiplayer(multiplayer)==(False):
            print("Debe ser S o N")
            continue
        editor=input("Ingrese su editor: ").upper
        if validar_editor(editor)==False:
            print("No debe estar vacio ni llevar espacio")
            continue
        precio=int("Ingrese precio del juego: ")
        if validar_precio(precio)==False:
            print("El precio debe ser un numero entero mayor a 0")
            continue
        stock=int("Ingrese stock del juego: ")
        if validar_stock(stock)==False:
            print("Debe ser mayor o igual a 0")
            pass
    elif opc==5:
        codigo=input("Ingrese el codigo del juego")
        if eliminar_juego(codigo):
            print("Se elimino el juego")
        else:
            print("No existe ese codigo de juego")
    elif opc==6:
        print("Programa finalizado")
        break