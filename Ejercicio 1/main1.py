from ClaseEmail import Email
import csv
if __name__ == '__main__':
        instancia=Email("mati", "gmail", ".com", "hermanadelvalenrica")
        nombre=input('ingrese nombre de la persona: ')
        #email=input('ingrese el email de la persona: ')
        instancia.Mostrarmensaje(nombre)
        instancia.modificar_contra()
        instancia2=Email("", "", "", "")
        correo=input("ingrese correo")
        instancia2.crearcuenta(correo)
        with open('direcciones.csv', 'r') as archivo:
            reader=csv.reader(archivo, delimiter=",")
            listaemails=[]
            for fila in reader:
                for i in fila:
                    email=Email("", "", "", "")
                    if email.crearcuenta(fila) == 1:
                        listaemails.append(email)
                    else:
                        print(f'direccion de correo invalida {email}')
        print(listaemails)
        dominio=input("ingrese un tipo de dominio")
        cuentas_dominio=0
        for email in listaemails:
            if email.getdominio()==dominio:
                cuentas_dominio+=1
        
        print(f"la cantidad de cuentas con ese dominio son {cuentas_dominio}") 
               
        
            
         
    
        
                
                
            
        
        
    