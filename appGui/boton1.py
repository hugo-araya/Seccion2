from tkinter import *
def funcion(n):
    print(n)

def funcion1():
    print('consola')

if __name__== '__main__' :
    ventana = Tk()
    n = 5
    boton = Button(ventana, text='Boton 1', command = funcion1(n))
    boton.grid(column=0, row=0)
    ventana.mainloop()

