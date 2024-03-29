#Programado por Leo Gimenez, contacto: leogimenez.dev@gmail.com
import pandas as pd
from tkinter import Tk, Label, Text, Button, filedialog, Frame, ttk, Scale, Canvas
import os
from ttkthemes import ThemedTk
import tkinter as tk
from tkinter import ttk
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class ConfiguradorApp:
    def __init__(self, root):
        #configuración de ventana
        self.root = root
        self.root.title('Selenium App')
        self.root.geometry("1100x400")
        self.root.configure(bg='#414141')
        
        #estilos de los frames
        style = ttk.Style()        
        self.root.set_theme('equilux')  
        style.configure('barratop.TFrame', background='#414141')
        style.configure('modulo.TFrame', background='white')
        
        
        #configuración de la prioridad para achicar columnas o rows en el resize de la ventana
        self.root.columnconfigure(0, weight=0)
        self.root.columnconfigure(1, weight=0)
      
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
        self.datoEx1 = ttk.LabelFrame(self.root, text='Usuario', padding=(10,10))
        self.datoEx1.grid(row=3, column=1, sticky='ew', padx=0, pady=3)
        #Frame de datosExtras2
        self.datoEx2 = ttk.Frame(self.root, width=300, style='barratop.TFrame')
        self.datoEx2 = ttk.LabelFrame(self.root, text='Pasword', padding=(10,10))
        self.datoEx2.grid(row=3, column=2, sticky='ew', padx=0, pady=3)
        #Frame de boton
        self.listo = ttk.Frame(self.root, width=300, style='barratop.TFrame')
        self.listo = ttk.LabelFrame(self.root, text='Iniciar', padding=(10,10))
        self.listo.grid(row=4, column=1, sticky='ew', padx=0, pady=3, columnspan=2)
        
        
        self.create_widgets()

    def create_widgets(self):
        self.create_labels_and_entries()
        self.create_buttons()
        
    def create_labels_and_entries(self):
        #estilos
        style = ttk.Style()        
        style.configure("Dark.TFrame", foreground="white", background="#414141", borderwidth=0) 
        
        #primer campo
        self.fonint1 = ttk.Frame(self.datos1, width=100, style='Dark.TFrame')
        self.fonint1.grid(row=0, column=0, sticky='ns', padx=0, pady=3, rowspan=2)
        self.arch = Label(self.datos1, text="No hay lista Seleccionada",background="#414141", foreground="white")
        self.arch.grid(row=1,column=1, sticky="ew", pady=10)
       
        #Label de datos usuario
        self.fraUss1 = ttk.Frame(self.datoEx1, width=50)
        self.fraUss1.grid(row=0, column=0, sticky='e', padx=0, pady=3, rowspan=3)

        self.lab2 = Label(self.datoEx1, text="Usuario:", background="#414141", foreground="white", width=50)
        self.lab2.grid(row=1, column=1, pady=10, padx=10)
        
        self.texto4 = Text(self.datoEx1, height=1, width=1)
        self.texto4.grid(row=2, column=1, sticky='ew', pady=10, padx=10)
        
        self.fraUss2 = ttk.Frame(self.datoEx1, width=50)
        self.fraUss2.grid(row=0, column=3, sticky='w', padx=0, pady=3, rowspan=3)
        
        #Label de datos paswordd
        self.fraPsw1 = ttk.Frame(self.datoEx2, width=50)
        self.fraPsw1.grid(row=0, column=0, sticky='e', padx=0, pady=3, rowspan=3)

        self.lab3 = Label(self.datoEx2, text="Ingrese el password", background="#414141", foreground="white", width=50)
        self.lab3.grid(row=1, column=1, pady=10, padx=10)       
        
        # Simular campo de contraseña con Entry

        self.entry_contraseña = tk.Entry(self.datoEx2, show="*", width=50)
        self.entry_contraseña.grid(row=2, column=1, sticky='we', pady=10, padx=10)

        self.fraPsw2 = ttk.Frame(self.datoEx2, width=50)
        self.fraPsw2.grid(row=0, column=2, sticky='e', padx=0, pady=3, rowspan=3)
        
        # Configurar asteriscos
        self.entry_contraseña.config(show="*")
       
        

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
        
        self.dale = ttk.Button(self.listo, text="Iniciar", command=self.scrapear, width=30, style='Fancy.TButton')
        self.dale.grid(row=1, column=1, sticky='ew', pady=10, padx=10)
        
        self.fonint3 = ttk.Frame(self.listo, width=300)
        self.fonint3.grid(row=0, column=2, sticky='ew', padx=0, pady=3, rowspan=2)
    
    def buscador(self):
        try:
            archivo2 = filedialog.askopenfilename(initialdir="/",
                                                  title="Elija un archivo",
                                                  filetypes=(("Hoja de Excel", "*.xls*"),
                                                             ("all files", "*.*")))
            arch = pd.read_excel(archivo2)

            df_sel = arch['IP']

            self.ip=[] 
            for dato in df_sel:
                try:
           
                   self.ip.append(dato)
                   self.arch.config(text='Archivo seleccionado')
                except:
                    print("error")
                    self.arch.config(text='Error')

        except Exception as e:
            
            print('error')

    
    def create_web_driver(self):
        self.driver = webdriver.Chrome()
        
        self.driver.set_window_position(0,0)
        self.driver.maximize_window()
        return self.driver
    
    
    def envia_uss(self):
        
        self.obu = self.texto4.get("1.0", "end-1c")
        self.uss = self.driver.find_element(By.XPATH,"//*[@id='userName']")
        print(self.obu)
        print("ahora aqui")
        self.uss.send_keys(self.obu)
        time.sleep(4)
        print("salimos de uss")
    
    def enviar_pass(self):
        #Envía el password
        print("ingresamos a pass")
        self.obp = self.entry_contraseña.get()
        print("pass:", self.obp)
        self.password = self.driver.find_element(By.XPATH,"//*[@id='pcPassword']")
        self.password.send_keys(self.obp)
        self.password.send_keys(Keys.RETURN)
        time.sleep(4)

   
    
    def tools(self):
        try:
            # seleccion de fram
            self.driver.switch_to.frame(1)  # Esto sucede porque tplink usaframes

            # Espera hasta 10 segundos para que el elemento esté presente en el frame
            wait = WebDriverWait(self.driver, 10)
            self.cerrar = wait.until(
                EC.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/ul/li[17]/a"))
            )

            print("Botón encontrado")
            self.cerrar.click()
            print("Clic hecho")
            time.sleep(5)

        except Exception as e:
            print(f"No se pudo cerrar la sesión: {e}")
    
    def diagnostic(self):
        
        wait = WebDriverWait(self.driver, 10)
        self.diag = wait.until(
                EC.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/ul/li[17]/ul/li[2]/a"))
            )
        self.diag.click()
        print("diagnostico seleccionado")
        # Vuelve al contexto principal después de trabajar con el frame
        self.driver.switch_to.default_content()
        print(self.driver.page_source)

        time.sleep(4)
    
    def dom(self):
        try:
            # Cambia al frame "mainFrame"
            self.driver.switch_to.frame("mainFrame")
            print("Frame seleccionado")

            # Espera hasta 10 segundos para que el elemento esté presente en el frame
            waits = WebDriverWait(self.driver, 10)
            self.dom_input = waits.until(
                EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div[1]/p[3]/input"))
            )

            print("Campo encontrado")
            self.dom_input.send_keys('8.8.8.8')
            print("DNS colocado en 8.8.8.8")           
            time.sleep(4)

        except Exception as e:
            print(f"No se pudo poner DNS en la sesión: {e}")
    
    def inicio(self):
        try:
           
            print("se busca inicio")

            # Espera hasta 10 segundos para que el elemento esté presente en el frame
            waits = WebDriverWait(self.driver, 10)
            self.ini_btn = waits.until(
                EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div[1]/p[1]/input[3]"))
            )

            print("Botón encontrado")
            self.ini_btn.click()
            print("Ping iniciado")

            # Vuelve al contexto principal después de trabajar con el frame
            self.driver.switch_to.default_content()            
            time.sleep(20)

        except Exception as e:
            print(f"No se pudo iniciar ping {e}")

    
    def scrapear(self):
        for dat in self.ip:
            driver = self.create_web_driver()
            direccion = 'http://' + dat 
            print(direccion)
            #Abre la página
            driver.get(direccion)
            time.sleep(5)
            try:
                self.envia_uss()
                self.enviar_pass()
                
                self.tools()
                self.diagnostic()
                self.dom()
                self.inicio()
                driver.close()
            except Exception as e:
                print('Error', e)
                driver.close()
    



if __name__=="__main__":
    root=ThemedTk(theme='equilux')
    app=ConfiguradorApp(root)
    root.mainloop()