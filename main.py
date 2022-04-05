import os
import sys
import tkinter as tk
from tkinter import E, EW, NSEW, W, Menu, ttk
from tkinter import messagebox


absolute_folder_path = os.path.dirname(os.path.realpath(__file__))
absolute_image_path = os.path.join(absolute_folder_path, 'icon.ico')
class LoginVentana(tk.Tk):
    def __init__(self):
        super().__init__()
        #
        self.geometry('300x120')
        self.title('Login')
        self.iconbitmap(absolute_image_path)
        self.resizable(0,0)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=3)
        # Creamos los componentes
        self._crear_componentes()
        
    # Definir el metodo crear componentes
    def _crear_componentes(self):
        # usuario
        
        usuario_etiqueta = tk.Label(self, text='Usuario:')
        usuario_etiqueta.grid(row=0, column=0, ipadx=10, sticky=tk.E, padx=5, pady=5)
        self.usuario_entrada = tk.Entry(self, width=30)
        self.usuario_entrada.grid(row=0, column=1, sticky=tk.W, padx=5, pady=5)
        
        # Password
        password_etiqueta = tk.Label(self, text='Password:')
        password_etiqueta.grid(row=1, column=0, sticky=tk.E, padx=5, pady=5)
        self.password_entrada = tk.Entry(self, show='*')
        self.password_entrada.grid(row=1, column=1,  sticky=tk.W, padx=5, pady=5)
        
        # boton login
        login_boton = ttk.Button(self, text='Login', command=self._login)
        login_boton.grid(row=3, column=0, columnspan=2)
        
    def _login(self):
        messagebox.showinfo('Datos Login',
            f'usuario: {self.usuario_entrada.get()}, Password: {self.password_entrada.get()}')
        
# Ejecutar la ventana
if __name__ == '__main__':
    login_ventana = LoginVentana()
    login_ventana.mainloop()