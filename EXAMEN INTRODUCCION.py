# BY KEVIN BORGE
#SE IMPORTAN FUNCIONALIDADES
from tkinter import *
import math
import datetime
#SE ESTABLECE LA CLASE VENTANA CON SUS ATRIBUTOS

class Desk:
    def __init__(self, ventana):
        X = 600
        Y = 600

     #SE ESTABLECE TITULO DE LA VENTANA
        self.wind = ventana
        self.wind.geometry(str(X)+'x'+str(Y))
        self.wind.title('Examen Final Kevin Neftali Borge Tobar')

#SE ESTABLECE EL TITULO DE BIENVENIDA
        frame = LabelFrame(self.wind, text = 'BIENVENIDO')
        frame.grid(columnspan = 5, pady = 25,)

        #SE ESTABLECEN LOS DIFERENTES ENTRYS CON SUS DESCRIPCIONES
        Label(frame, text = 'Nombre: ').grid(row = 1, column = 0)
        self.x1 = Entry(frame)
        self.x1.focus()
        self.x1.grid(row = 1, columnspan=5)


        Label(frame, text = 'Apellido: ').grid(row = 2, column = 0)
        self.x2 = Entry(frame)
        self.x2.grid(row = 2, columnspan = 6)


        Label(frame, text = 'Dia: ').grid(row = 3, column = 0)
        self.x3 = Entry(frame)
        self.x3.grid(row = 3, columnspan=5)


        Label(frame, text = 'Mes: ').grid(row = 4, column = 0)
        self.x4 = Entry(frame)
        self.x4.grid(row = 4, columnspan = 5)


        Label(frame, text = 'Año: ').grid(row = 5, column = 0)
        self.x5 = Entry(frame)
        self.x5.grid(row = 5, columnspan = 5)


        #SE ESTABLECIERON LOS BOTONES PARA LAS FUNCIONES
        Button(frame, text = 'funcion1', command = self.funcion1).grid(row = 6, column = 0 )
        Button(frame, text = 'funcion2', command = self.funcion2).grid(row = 6, column = 1 )
        Button(frame, text = 'funcion3', command = self.funcion3).grid(row = 6, column = 2 )
        Button(frame, text = 'funcion4', command = self.funcion4).grid(row = 6, column = 3 )
        Button(frame, text = 'funcion5', command = self.funcion5).grid(row = 6, column = 4 )


        #AREA DE RESULTADOS
        self.message = Label(text = '', fg = 'red')
        self.message.grid(row = 3, column = 0,)


    #SE ESTABLECE CADA UNO DE SUS PARAMETROS PARA MOSTRAR SUS RESULTADOS


    def funcion1(self):
        Dia=int(self.x3.get())
        Mes=int(self.x4.get())
        Año=int(self.x5.get())

        Rdia=format(Dia, '0b' )
        Rmes=format(Mes, '0b')
        Raño=format(Año, '0b')

        self.message['text'] = 'La fecha ingresada es : {}/{}/{} y  binario es:{}/{}/{}'.format(Dia, Mes, Año, Rdia, Rmes,Raño)




    def funcion2(self):
        DiaA=int(self.x3.get())
        MesA=int(self.x4.get())
        AñoA=int(self.x5.get())
        fecha_de_nacimiento = datetime.datetime(AñoA, MesA, DiaA)
        fecha_de_hoy = datetime.datetime.now()
        diferencia = fecha_de_hoy - fecha_de_nacimiento
        dias_vividos = diferencia.days
        self.message['text'] = 'Usted nacion {}/{}/{}: y a la cantidad  de dias vividos es{} dias'.format(DiaA,MesA,AñoA,dias_vividos)



    def funcion3(self):
        nom=str(self.x1.get())
        ap=str(self.x2.get())
        name=int(len(nom))
        apellido=int(len(ap))
        if name%2==0 and apellido %2==0 :
            self.message['text'] = '{} {}  tu  nombre  es par y  tu apellido es par'.format(nom,ap)

        elif name%2==0 and apellido %2==1:
            self.message['text'] = ' {} {} tu nombre es par y  tu apellido es impar'.format(nom,ap)
        elif name%2==1 and apellido %2==0:
            self.message['text'] = '{} {} tu nombre es impar y  tu apellido es par'.format(nom,ap)
        else:
            self.message['text'] = '{} {} tu  nombre es impar y tu apellido es impar'.format(nom,ap)


    def funcion4(self):
        letrasN=str(self.x1.get())
        letrasA=str(self.x2.get())
        contador = 0
        for carac in letrasN:
            if carac == 'a' or carac =='A' or carac =='e' or carac =='E' or carac =='i' or carac =='I' or carac=='o' or carac =="O" or carac =="u" or carac=="U" or carac == 'á' or carac =='Á' or carac =='é' or carac =='É' or carac =='í' or carac =='Í' or carac=='ó' or carac =="Ó" or carac =="ú" or carac=="Ú":
                contador += 1
        for carac in letrasA:
            if carac == 'a' or carac =='A' or carac =='e' or carac =='E' or carac =='i' or carac =='I' or carac=='o' or carac =="O" or carac =="u" or carac=="U" or  carac == 'á' or carac =='Á' or carac =='é' or carac =='É' or carac =='í' or carac =='Í' or carac=='ó' or carac =="Ó" or carac =="ú" or carac=="Ú":
                contador += 1
        Noletras=len(letrasN)
        Apletras=len(letrasA)
        cons=Noletras+Apletras-contador

        self.message['text'] = 'Su nombre y apellido tienen {} vocales y {} consonantes'.format(contador,cons)



    def funcion5(self):
        nombre=str(self.x1.get())
        apellido=str(self.x2.get())
        invert = ""
        invert2= ""
        for caracter in nombre:
            invert= caracter + invert
        for caracter2 in apellido:
            invert2 = caracter2 +  invert2
        self.message['text'] = '{} {} o al revez {} {}'.format(nombre,apellido,invert,invert2)


    
#validamos si estamos en la aplicación inicial
if __name__ == '__main__':
    pantalla = Tk()
    
    #SE ESTABLECE EL PARAMETRO VENTANA
    app = Desk(pantalla)

    #EJECUTAMOS LA VENTANA EN UN BUCLE INFINITO PARA QUE NO SE CIERRE
    pantalla.mainloop()

