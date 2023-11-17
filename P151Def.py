

# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 20:06:17 2023




@author: Aidan
"""




from tkinter import *




root = Tk()
root.title("P151")
root.geometry("850x1450")
root.configure(background="violet")




mes = Label(root)
costo = Label(root)
costoMax = Label(root)
costoMin = Label(root)


meses = ("enero","febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre")
ganancia = (250,755,320,2500,1070,325,896,453,125,565,235,450)




mes["text"] = "Meses del año:" + " " + str(meses)


costo["text"] = "Ganancias Por Mes:" + " " + str(ganancia)




def maximo():    
    gananciaMax = max(ganancia)
    indiceMax = ganancia.index(gananciaMax)   
    GanMaxMes = meses[indiceMax] 
    costoMax["text"] = "la ganancia maxima fue de:" + " " + str(gananciaMax) + " " + "Y fue en el mes de:" + " " + str(GanMaxMes)
    
def minimo():
    
    gananciaMin= min(ganancia)  
    indiceMin = ganancia.index(gananciaMin)  
    GanMinMes = meses[indiceMin]   
    costoMin["text"] = "la ganancia minima fue de:" + " " + str(gananciaMin) + " " + "Y fue en el mes de:" + " " + str(GanMinMes)
   
mes.place(relx=0.5, rely=0.2, anchor=CENTER)
costo.place(relx=0.5, rely=0.3, anchor=CENTER)
costoMax.place(relx=0.5, rely=0.6, anchor=CENTER)
costoMin.place(relx=0.5, rely=0.7, anchor=CENTER)
                                                                                                                    
btnMax = Button(root, text="ganancia maxima", command=maximo, bg="pink", fg="black")  
btn = Button(root, text="Ganancia mínima", command=minimo, bg="pink", fg="black")
                                                                             




btnMax.place(relx=0.5, rely=0.4, anchor=CENTER)
btn.place(relx=0.5, rely=0.5, anchor=CENTER)




root.mainloop()
