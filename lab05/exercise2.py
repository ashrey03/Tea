try:
    namearchive = input("Por favor ingrese el nombre del archivo\->")
    opener = open(namearchive, "r", encoding="UTF-8")

    for linea in opener:
        print(linea.upper())
except:
    print("Intente nuevamente")