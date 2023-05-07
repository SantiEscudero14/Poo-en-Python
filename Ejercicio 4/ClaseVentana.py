class Ventana():
    def __init__(self, titulo = " ", valorX_sup = 0 , valorY_sup = 0, valorX_inf  = 500, valorY_inf = 500):
        if (valorX_sup < 0) | (valorY_sup < 0):
            raise ValueError("No se puede ingresar un valor negativo en los ejes superior izquierdo ")
        if (valorX_inf > 500) | (valorY_inf > 500):
            raise ValueError("No se puede ingresar un valor mayor a 500 en los ejes inferior derecha ")
        if (valorX_sup > valorX_inf):
            raise ValueError("Ingreso un valor del eje x superior izquierdo mayor al valor del eje x inferior derecho")
        if (valorY_sup > valorY_inf):
            raise ValueError("Ingreso un valor del eje y superior izquierdo mayor al valor del eje y inferior derecho")
        self.__titulo = titulo
        self.__valorX_sup = valorX_sup
        self.__valorY_sup = valorY_sup
        self.__valorX_inf = valorX_inf
        self.__valorY_inf = valorY_inf
    def getTitulo(self):
        return self.__titulo
    
    def mostrar(self):
        print (self.__titulo)
        print("Valor x del vertice superior izquierdo ", self.__valorX_sup, " valor y del vertice superior izquierdo", self.__valorY_sup)
        print("Valor x del vertice inferior derecho ", self.__valorX_inf, " valor y del vertice inferior derecho", self.__valorY_inf)
    
    def alto(self):
        return (self.__valorY_inf - self.__valorY_sup)
    
    def ancho(self):
        return (self.__valorX_inf - self.__valorX_sup)
    
    def moverDerecha(self, cant = 0):
        self.__valorX_inf += cant
        self.__valorX_sup += cant
    def moverIzquierda(self, cant = 0):
        self.__valorX_inf -= cant
        self.__valorX_sup -= cant
    def subir(self, cant = 0):
        self.__valorY_inf += cant
        self.__valorY_sup += cant
    def bajar(self, cant= 0):
        self.__valorY_inf -= cant
        self.__valorY_sup -= cant
    
            

        
    
    