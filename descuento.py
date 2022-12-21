monto:float= float(input("ingrese el monto de la compra: "))
if monto >= 800:
    totalcompra= monto -(monto*0.05)
    if monto >=1500:
        totalcompra=monto-(monto*0.10)
    if monto >= 3000:
        totalcompra= monto-(monto*0.15)    
    if monto >=5000:
        totalcompra= monto-(monto*0.20)
    print("El monto a pagar es: ",totalcompra)
else:
    print("El monto a pagar es: ",monto)
                        