class PlanAhorro():
    __cant_cuotasplan=int=24
    __cant_cuotas_p_licitar=int=10
   
    def __init__(self, codigo_plan, modelo, version_vehiculo, valor_vehiculo):
        self.__codigo_plan=codigo_plan
        self.__modelo=modelo
        self.__version_vehiculo= version_vehiculo
        self.__valor_vehiculo=valor_vehiculo
        
    def importeCuota(self):
        return((self.__valor_vehiculo/self.getcantidadcuotasparalicitar()) + self.__valor_vehiculo * 0.10)
   
   
    def mostrar(self):
        print(self.__codigo_plan, " ", self.__modelo, " ", self.__version_vehiculo)
    
    def getcodigodeplan(self):
        return self.__codigo_plan
    
    def getmodelo(self):
        return self.__modelo
    
    def getversion(self):
        return self.__version_vehiculo
    
    def getvalor(self):
        return self.__valor_vehiculo
    
    def setvalor(self, valor):
        self.__valor_vehiculo=valor
    
    def actualizar_valorde_vehiculo(self, valorh):
        valor_v= input("ingrese valor de vehiculo para actualizar")
        self.__valor_vehiculo=valor_v
    
    @classmethod
    def getcantidadcuotas(cls):
        return cls.__cant_cuotasplan
    
    def setcantidadcuotas(cls, cantidad):
        cls.__cant_cuotasplan=cantidad
    
    @classmethod
    def getcantidadcuotasparalicitar(cls):
        return cls.__cant_cuotas_p_licitar
    
    @classmethod
    def set_cantidadparalicitar(cls, cantidad):
         cls.__cant_cuotas_p_licitar = cantidad
    