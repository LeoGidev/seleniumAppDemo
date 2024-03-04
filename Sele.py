#Programado por Leo Gimenez, contacto: leogimenez.dev@gmail.com
import pandas as pd
from tkinter import Tk, Label, Text, Button, filedialog, Frame, ttk, Scale, Canvas
import os
from ttkthemes import ThemedTk
import tkinter as tk
from tkinter import ttk
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import openpyxl
from webdriver_manager.chrome import ChromeDriverManager
wb = openpyxl.Workbook()


class ConfiguradorApp:
    def __init__(self, root):
        #configuración de ventana
        self.root = root
        self.root.title('Selenium App')
        self.root.geometry("940x600")
        self.root.configure(bg='#414141')
        
        #estilos de los frames
        style = ttk.Style()        
        self.root.set_theme('equilux')  
        style.configure('barratop.TFrame', background='#414141')
        style.configure('modulo.TFrame', background='white')
        
        
        #configuración de la prioridad para achicar columnas o rows en el resize de la ventana
        self.root.columnconfigure(0, weight=0)
        self.root.columnconfigure(1, weight=0)
        #self.root.rowconfigure(3, weight=1)
        #Configuración del icono
        self.root.iconbitmap(os.path.abspath("selenium.ico"))
        #frame nav        
        self.nav_bar = ttk.Frame(self.root, height=50, style='barratop.TFrame')
        self.nav_bar.grid(row=0, column=0, sticky='ew', pady=0, padx=0, columnspan=4)
        #frame lateral1       
        self.lat1 = ttk.Frame(self.root, width=50, style='barratop.TFrame')
        self.lat1.grid(row=0, column=0, sticky='ns', pady=0, padx=0, rowspan=4)
        #frame lateral2       
        self.lat2 = ttk.Frame(self.root, width=50, style='barratop.TFrame')
        self.lat2.grid(row=0, column=3, sticky='ns', pady=0, padx=0, rowspan=4)
        
        
        #Frame de datos1
        self.datos1 = ttk.Frame(self.root, width=300, style='barratop.TFrame')
        self.datos1 = ttk.LabelFrame(self.root, text='Seleccione el Excel que contiene las IPs', padding=(10,10))
        self.datos1.grid(row=2, column=1, sticky='ew', padx=0, pady=3, columnspan=2)
        #Frame de datosExtras1
        self.datoEx1 = ttk.Frame(self.root, width=300, style='barratop.TFrame')
        self.datoEx1 = ttk.LabelFrame(self.root, text='usuario', padding=(10,10))
        self.datoEx1.grid(row=3, column=1, sticky='ew', padx=0, pady=3)
        #Frame de datosExtras2
        self.datoEx2 = ttk.Frame(self.root, width=300, style='barratop.TFrame')
        self.datoEx2 = ttk.LabelFrame(self.root, text='Pasword', padding=(10,10))
        self.datoEx2.grid(row=3, column=2, sticky='ew', padx=0, pady=3)
        #Frame de boton
        self.listo = ttk.Frame(self.root, width=300, style='barratop.TFrame')
        self.listo = ttk.LabelFrame(self.root, text='Iniciar', padding=(10,10))
        self.listo.grid(row=4, column=1, sticky='ew', padx=0, pady=3, columnspan=2)
        # Barra de progreso
        self.barra_progreso = ttk.Progressbar(self.root, length=300, mode='indeterminate')
        self.barra_progreso.grid(row=5, column=1, columnspan=2, pady=10)
        
        self.create_widgets()

    def create_widgets(self):
        self.create_labels_and_entries()
        self.create_buttons()
        
    def create_labels_and_entries(self):
        style = ttk.Style()        
        style.configure("Dark.TFrame", foreground="white", background="#414141", borderwidth=0) 
        #primer campo
        self.fonint1 = ttk.Frame(self.datos1, width=10, style='Dark.TFrame')
        self.fonint1.grid(row=0, column=0, sticky='ns', padx=0, pady=3, rowspan=2)
        self.arch = Label(self.datos1, text="No hay lista Seleccionada",background="#414141", foreground="white")
        self.arch.grid(row=1,column=1, sticky="ew", pady=10)
       
        #Label de datos usuario
        self.lab2 = Label(self.datoEx1, text="Ingrese el dato a incluir:", background="#414141", foreground="white")
        self.lab2.grid(row=1, column=0, pady=10, padx=10)
        self.texto4 = Text(self.datoEx1, height=1, width=40)
        self.texto4.grid(row=2, column=0, sticky='we', pady=10, padx=10)
        #Label de datos paswordd
        self.lab3 = Label(self.datoEx2, text="Ingrese el dato a incluir:", background="#414141", foreground="white")
        self.lab3.grid(row=1, column=0, pady=10, padx=10)
        self.texto5 = Text(self.datoEx2, height=1, width=40)
        self.texto5.grid(row=2, column=0, sticky='we', pady=10, padx=10)
       
        

    def create_buttons(self):

        style = ttk.Style()        
        style.configure("Fancy.TButton", foreground="white", background="#0099ff", borderwidth=0) 
               
        style.configure("Dark.TFrame", foreground="white", background="#414141", borderwidth=0) 
        
        
        #boton de datoexcel
        self.btn2 = ttk.Button(self.datos1, text="Abrir", command=self.buscador, style='Fancy.TButton')
        self.btn2.grid(row=1, column=4, sticky='w', pady=10, padx=10)
        
        #frame para el boton final
        self.fonint2 = ttk.Frame(self.listo, width=300)
        self.fonint2.grid(row=0, column=0, sticky='ew', padx=0, pady=3, rowspan=2)
        #boton de crear
        
        self.dale = ttk.Button(self.listo, text="Crear etiquetas", command=self.create_buttons, width=30, style='Fancy.TButton')
        self.dale.grid(row=1, column=1, sticky='ew', pady=10, padx=10)
        
        self.fonint3 = ttk.Frame(self.listo, width=300)
        self.fonint3.grid(row=0, column=2, sticky='ew', padx=0, pady=3, rowspan=2)
    
    def buscador(self):
        try:
            archivo2 = filedialog.askopenfilename(initialdir="/",
                                                  title="Elija un archivo",
                                                  filetypes=(("Hoja de Excel", "*.xls*"),
                                                             ("all files", "*.*")))
            
        except Exception as e:
            
            print('error')

    
    def create_web_driver():
        driver = webdriver.Chrome()
        
        driver.set_window_position(0,0)
        driver.maximize_window()
        return driver


if __name__=="__main__":
    root=ThemedTk(theme='equilux')
    app=ConfiguradorApp(root)
    root.mainloop()