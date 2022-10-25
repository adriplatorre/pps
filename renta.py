

renta = int(input("Introduzca su renta anual: "))

if renta < 10000:
    print ("Su tipo impositivo es de un 5%")
    impositivo5= renta *(5 / 100)
    print (impositivo5)
    
elif renta >= 10000 and renta <= 20000 :
    print ("Su tipo impositivo es de un 15%")
    impositivo15= renta *(15 / 100)
    print (impositivo15)

elif renta >= 20001 and renta <= 35000 :
    print ("Su tipo impositivo es de un 20%")
    impositivo20= renta *(20 / 100)
    print (impositivo20)

elif renta >= 35001 and renta <= 60000 :
    print ("Su tipo impositivo es de un 30%")
    impositivo30= renta *(30 / 100)
    print (impositivo30)    

elif renta > 60001 :
    print ("Su tipo impositivo es de un 45%")
    impositivo45= renta *(45 / 100)
    print (impositivo45)  