def change():
    expense = 23.75
    money = 100
    vuelto = money - expense
    pesos = int(vuelto)
    cents = vuelto - pesos
    cents = int(cents*100)

    print (f"Ingresar gasto:\n{expense}\nDinero recibido\n{money}\n\nVuelto\n\nPesos:\n{pesos}\nCentavos:\n{cents}")
    
