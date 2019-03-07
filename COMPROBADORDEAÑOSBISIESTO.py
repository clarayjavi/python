#!/usr/bin/env   pyhton
# __*__   coding:utf-8  __*__
def main():
    print("COMPROBADOR DE AÑOS BISIESTOS")
    fecha = int(input("Escriba un año y le diré si es bisiesto; "))
    if fecha % 400 == 0:
        print("El año {} es un año bisiesto porque es múltiplo de 400.".format(fecha))
    elif fecha % 100== 0:
        print("El año {} NO es un año bisiesto porque es múltiplo de 100 sin ser múltiplo de 400.".format(fecha))
    elif fecha % 4==0:
        print("El año {} es un año bisiesto porque es múltiplo de 4.".format(fecha))
    else:
        print("El año {} NO es un año bisiesto.".format(fecha))
if __name__=="__main__":
    main()
