#1
def nombre_empresa ():
    global nombre_empresa
    return f"Bienvenido a la empresa {nombre_empresa}"



#2
def calcular_total():
    total = 10 + 5
    print("total =", total)

calcular_total()

#3
contador = 0

def incrementar_contador():
    global contador
    contador += 1
    print("Contador = ", contador)


incrementar_contador() #1
incrementar_contador() #2
incrementar_contador() #3