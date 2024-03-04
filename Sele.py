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





