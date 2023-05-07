from ClaseViajero import ViajeroFrecuente
from ClaseMenu import Menu
import csv

def BuscarViajero(num_viajero, listaViajeros):
    band= False
    i = 0
    while ((band == False) & (i < len(listaViajeros))):
        if (listaViajeros[i].get_num_viajero() == num_viajero):
            band= True
        else: 
            i = i + 1
    if band == False:
        return -1
    else: 
        return i




if __name__ == '__main__':
    
    with open("Viajeros.csv", "r") as archivo:
            reader=csv.reader(archivo, delimiter=",")
            Lista_viajero=[]
            for fila in reader:
                viajero=ViajeroFrecuente(int(fila[0]),fila[1],fila[2],fila[3],int(fila[4]))
                Lista_viajero.append(viajero)

    num_viajero=int(input("ingrese numero de viajero"))
    
    if(BuscarViajero(num_viajero, Lista_viajero)!=-1):
        i=BuscarViajero(num_viajero, Lista_viajero)
        opciones = ["Consultar cantidad de millas", "Acumular millas ", "Canjear millas"]
        cantidad=3
        menu = Menu(cantidad)
        menu.IngresaOpcion(opciones)
        menu.Muestra()
        op = int(input("Ingrese opcion "))
        while op != (cantidad + 1): 
            if op == 1:
                #consulta cantidad de millas
                millas= Lista_viajero[i].CantidadTotalMillas()
                print("La cantidad de millas son: ", millas)
            elif op== 2:
                #acumula millas
                millas_recorridas= int(input("Ingrese cantidad de millas recorridas "))
                Lista_viajero[i].acumularMillas(millas_recorridas)
            elif op== 3: 
                #canjear Millas
                mllas_a_canjear = int(input("Ingrese millas a canjear "))
                Lista_viajero[i].canjearmillas(mllas_a_canjear)
            else: print("Ingreso opcion incorrecta")
            menu = Menu.Muestra()
            op= int(input("Ingrese opcion: "))
    else:
        print("el numero de viajero que se ingreso no se encontro")

        

        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
   
    