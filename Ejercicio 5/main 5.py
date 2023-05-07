from ClasePlanAhorro import PlanAhorro
import csv
from ClaseMenu import Menu

if __name__ == '__main__':
    with open("planes.csv", "r") as archivo:
        reader=csv.reader(archivo, delimiter=";") 
        listaplanes=[] 
        for fila in archivo:
            PlanA=PlanAhorro(int(fila[0]),fila[1],fila[2],fila[3])
            cant=PlanA.getcantidadcuotasparalicitar()
            if (int(fila[4])!=cant):
                PlanA.setcantidadcuotas(int(fila[4]))
                cant =PlanA.getcantidadcuotas()
            if (int(fila[5])!=cant):
                 PlanA.set_cantidadparalicitar(int(fila[5]))
            listaplanes.append(PlanA)
    
    menu=Menu(4)
    opciones = ["Actualizar el valor del vehículo de cada plan. ","Cuotas Menores a valor ingresado."," Mostrar el monto que se debe haber pagado para licitar el vehículo. ","Modificar la cantidad cuotas que debe tener pagas para licitar."]
    menu.ingresaOpcion(opciones)
    menu.muestra()
    op=int(input("ingrese opcion"))
    cantidad = menu.getCantidad() + 1
    while op!=cantidad:
        if opcion == 1:
            for PlanA in listaplanes:
                PlanA.mostrar()
                valor_v=(input("ingrese valor actual del vehiculo"))
                PlanA.setvalor(valor_v)
                print("Se actualizo el valor del vehiculo")
        elif opcion == 2:
            valor_c=(float(input("ingrese valor de cuota ")))
            for PlanA in listaplanes:
                if(valor_c>PlanA.importeCuota()):
                    PlanA.mostrar()
        elif opcion == 3:
            for PlanA in listaplanes:
                PlanA.mostrar()
                print("Monto que se debe pagar para licitar el vehiculo:", PlanA.getcantidadcuotasparalicitar() * PlanA.importeCuota())
        elif opcion == 4:
            codigo = int(input("Ingrese codigo plan "))
            bandera = False
            i = 0
            while (bandera == False) and (i < len(listaplanes)):
             if codigo == listaplanes[i].codigodeplan():
                    bandera = True
            else: i += 1
       
            if i < len(listaplanes):
                cant_cuotas_p_licitar = int(input("Se encontró el plan solicitado, Ingrese nueva cantidad de cuotas para licitar "))
                listaplanes[i].set_cantidadparalicitar(cant_cuotas_p_licitar)
            else:
                print("No se encontró vehículo solicitado ")

        else:
            print("Ingreso opción incorrecta ")
        menu.muestra()
        opcion = int(input("Ingrese opcion "))
    
        
   
    
   

                
        
                

    

    
    