class calculadora:






    def suma():
        numero1 = int(input("Ingrese un numero"))
        numero2 = int(input("Ingrese un numero"))
        print ("El resultado de su suma es:", numero1 + numero2)

    def resta():
        numero1 = int(input("Ingrese un numero"))
        numero2 = int(input("Ingrese un numero"))
        print("El resultado de su suma es:",numero1 - numero2)

    def multiplicacion():
        numero1 = int(input("Ingrese un numero"))
        numero2 = int(input("Ingrese un numero"))
        print("El resultado de su suma es:",numero1 * numero2)

    def division():
        numero1 = int(input("Ingrese un numero"))
        numero2 = int(input("Ingrese un numero"))
        print("El resultado de su suma es:",numero1 / numero2)

    print("Bienvenido a su calculadora Python")

    print(""""""""""""
          """"""""""""""""""
          )
    Operacion_a_realizar = input("¿Que clase de operacion desea hacer?")
    Lista_De_Operaciones = ["suma", "resta", "multiplicacion", "division"]

    while (Operacion_a_realizar != Lista_De_Operaciones):
        if (Operacion_a_realizar == Operacion_a_realizar):

            while (Operacion_a_realizar == "suma"):
                suma()
                Operacion_a_realizar = +1

            while (Operacion_a_realizar == "resta"):
                resta()

                Operacion_a_realizar = +1

            while (Operacion_a_realizar == "multiplicacion"):
                multiplicacion()

                Operacion_a_realizar = +1

            while (Operacion_a_realizar == "division"):
                division()

                print("Gracias por usar la calculadora")




































                        









































