from ClaseViajero import ViajeroFrecuente
import csv


if __name__ == '__main__':
    
    with open("Viajeros.csv", "r") as archivo:
            reader=csv.reader(archivo, delimiter=",")
            Lista_viajero=[]
            for fila in reader:
                viajero=ViajeroFrecuente(int(fila[0]),fila[1],fila[2],fila[3],int(fila[4]))
                Lista_viajero.append(viajero)

    viajeroMaximo = []
    
    #Busqueda numero máximo de millas
    numeroMillasMax = 0
    
    for i in Lista_viajero:
        if i.cantidadTotalMillas() > numeroMillasMax:
            numeroMillasMax = i.cantidadTotalMillas()
    
    print ("Viajeros que poseen la mayor cantidad de millas: \n")
    
    #compara si es el mismo número
    for i in Lista_viajero:
        if numeroMillasMax == i.cantidadTotalMillas():
            i.mostrar_datos()
            viajeroMaximo.append(i)
    
    #sobrecarga de operador utiizando suma(+)
    Lista_viajero[1] = Lista_viajero[1] + 100
    Lista_viajero[1].mostrar_datos()
    
    #sobrecarga de operador utiizando resta(-)
    Lista_viajero[1] = Lista_viajero[1] - 150
    Lista_viajero[1].mostra_Datos() 

        

        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
   
    