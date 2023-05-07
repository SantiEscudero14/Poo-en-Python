class ViajeroFrecuente():

    def __init__(self, num_viajero, dni, nombre, apellido, millas_acum):
        self.__num_viajero=num_viajero 
        self.__dni=dni
        self.__nombre=nombre
        self.__apellido=apellido
        self.__millas_acum=millas_acum
        
    def get_num_viajero(self):
        return self.__num_viajero

    def cantidadTotalMillas(self):
        return self.__millas_acum
    
    def acumularMillas(self, millas_recorridas):
        self.__millas_acum+=millas_recorridas
        return self.__millas_acum
    
    def canjearmillas(self, cant_millas_a_canjear):
        if cant_millas_a_canjear<=self.__millas_acum:
            self.__millas_acum-=cant_millas_a_canjear
        else:
            print("error en la operacion")
        return self.__millas_acum

    def mostrar_datos(self):
        def MostrarDatos(self):
            print(f"Numero de viajero:{self.__num_viajero}\n{self.__apellido} {self.__nombre}\n Tiene {self.__millas_acum} millas acumuladas .\n Su dni es: {self.__dni}")
        
        
    
            
            
            




        
    
    





        

    

        
