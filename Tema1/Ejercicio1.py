class Ejercicio3:
    @staticmethod
    def anadirTexto(texto):
        f = open("C:\\Users\\Javi\\Desktop\\Ejercicios.txt", "a")
        f.write(texto + "\n")
        f.close()

instancia = Ejercicio3()
instancia.anadirTexto("Hasta luego")