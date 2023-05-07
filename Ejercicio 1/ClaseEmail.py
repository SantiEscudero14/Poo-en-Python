class Email():

    def __init__(self, idCuenta, dominio, tipodominio, contrasena):
        self.__idCuenta=idCuenta 
        self.__dominio=dominio 
        self.__tipdominio=tipodominio
        self.__contrasena=contrasena
    def retornaEMAIL(self):
        return self.__idCuenta + "@" + self.__dominio + "," + self.__tipdominio

    def getdominio(self):
        return self.__dominio

    def crearcuenta(self, email):
        if email.split("@"):
            partes=email.split("@")
            self.__idCuenta=partes[0]
            if partes[1].split("."):
                partes=partes[1].split(".")
                self.__dominio=partes[0]
                self.__tipdominio=partes[1]
                self.__contrasena=(input('ingrese contraseña'))
                return 1
        else:
            print("direccion de correo invalido")
            
    def modificar_contra(self):
        vieja=(input('ingrese contraseña anterior:'))
        if vieja==self.__contrasena:
            nueva=(input('ingrese nueva contraseña:'))
            self.__contraseña=nueva
            print('contraseña cambiada')
        else:
            print('contraseña incorrecta')
            
    def crearemails(self, fila):
        print('ingrese los datos:')
        idCuenta=input('Idcuenta: ') 
        dominio=input('Dominio: ')
        tipdominio=input('Tipo de dominio: ')
        contraseña=input('COntraseña:')
        email=Email(idCuenta, dominio, tipdominio, contrasena)
        return email

    def Mostrarmensaje(self, nombre):
        print(f'estimado {nombre} te enviaremos tus mensajes a la direccion {self.retornaEMAIL()}')