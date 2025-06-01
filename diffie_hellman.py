"""
Nombre Completo: Williams Tapia Caceres
Carrera: Informatica
Materia: Criptografía
Proyecto: Simulación Interactiva de Criptosistemas de Clave Pública
"""

# Módulo para la simulación del protocolo Diffie-Hellman
# Importa las librerías necesarias para la interfaz gráfica y la lógica del protocolo
# Define la clase DiffieHellmanGUI para la interacción con el usuario y la simulación
# Incluye métodos para generar claves, calcular valores compartidos y mostrar resultados

import tkinter as tk
from tkinter import ttk
from Crypto.Util import number
import random

class DiffieHellmanGUI:
    def __init__(self, master, user_name):
        self.master = master
        self.user = user_name
        self.private_key = 0
        self.public_key = 0
        self.shared_key = 0
        self.p = 23  # Número primo por defecto (personalizable)
        self.g = 5   # Generador por defecto (personalizable)
        self.setup_ui()
        
    def setup_ui(self):
        # Paleta de colores personalizada
        bg_color = "#f5f7fa"  # Fondo principal (gris claro)
        accent = "#5d75cc" if self.user == "Usuario A" else "#77da77"  # Azul o verde según usuario
        button_color = "#f7c873"  # Amarillo suave para botones
        style = ttk.Style()
        style.configure("Main.TFrame", background=bg_color)
        style.configure("Main.TLabel", background=bg_color)
        style.configure("Main.TButton", background=button_color)
        self.master.configure(bg=bg_color)
        main_frame = ttk.Frame(self.master, padding="15", style="Main.TFrame")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Título
        title = ttk.Label(main_frame, 
                         text=f"Diffie-Hellman - {self.user}",
                         font=('Helvetica', 12, 'bold'))
        title.pack(pady=10)
        
        # Parámetros del grupo
        params_frame = ttk.LabelFrame(main_frame, text="Parámetros del Grupo", padding="10")
        params_frame.pack(fill=tk.X, pady=5)
        
        ttk.Label(params_frame, text="Número primo (p):").grid(row=0, column=0, sticky=tk.W)
        self.p_entry = ttk.Entry(params_frame)
        self.p_entry.insert(0, str(self.p))
        self.p_entry.grid(row=0, column=1, padx=5, pady=2)
        
        ttk.Label(params_frame, text="Generador (g):").grid(row=1, column=0, sticky=tk.W)
        self.g_entry = ttk.Entry(params_frame)
        self.g_entry.insert(0, str(self.g))
        self.g_entry.grid(row=1, column=1, padx=5, pady=2)
        
        # Botón para actualizar parámetros
        ttk.Button(params_frame, text="Actualizar Parámetros", 
                  command=self.update_params).grid(row=2, column=0, columnspan=2, pady=5)
        
        # Generación de claves
        keys_frame = ttk.LabelFrame(main_frame, text="Generación de Claves", padding="10")
        keys_frame.pack(fill=tk.X, pady=5)
        
        ttk.Button(keys_frame, text="Generar Clave Privada", 
                  command=self.generate_private_key).pack(pady=2)
        self.priv_key_label = ttk.Label(keys_frame, text="Clave privada: No generada")
        self.priv_key_label.pack(pady=2)
        
        ttk.Button(keys_frame, text="Calcular Clave Pública", 
                  command=self.generate_public_key).pack(pady=2)
        self.pub_key_label = ttk.Label(keys_frame, text="Clave pública: No calculada")
        self.pub_key_label.pack(pady=2)
        
        # Clave compartida
        shared_frame = ttk.LabelFrame(main_frame, text="Clave Compartida", padding="10")
        shared_frame.pack(fill=tk.X, pady=5)
        
        ttk.Label(shared_frame, text="Clave pública del otro usuario:").pack()
        self.other_pub_key_entry = ttk.Entry(shared_frame)
        self.other_pub_key_entry.pack(pady=2)
        
        ttk.Button(shared_frame, text="Calcular Clave Compartida", 
                  command=self.calculate_shared_key).pack(pady=5)
        self.shared_key_label = ttk.Label(shared_frame, text="Clave compartida: No calculada")
        self.shared_key_label.pack(pady=2)
    
    def update_params(self):
        try:
            self.p = int(self.p_entry.get())
            self.g = int(self.g_entry.get())
            tk.messagebox.showinfo("Éxito", "Parámetros actualizados correctamente")
        except ValueError:
            tk.messagebox.showerror("Error", "Ingrese valores numéricos válidos")
    
    def generate_private_key(self):
        self.private_key = random.randint(2, self.p - 2)
        self.priv_key_label.config(text=f"Clave privada: {self.private_key}")
    
    def generate_public_key(self):
        if not hasattr(self, 'private_key') or self.private_key == 0:
            tk.messagebox.showerror("Error", "Primero genere una clave privada")
            return
        
        self.public_key = pow(self.g, self.private_key, self.p)
        self.pub_key_label.config(text=f"Clave pública: {self.public_key}")
    
    def calculate_shared_key(self):
        if not hasattr(self, 'private_key') or self.private_key == 0:
            tk.messagebox.showerror("Error", "Primero genere una clave privada")
            return
        
        try:
            other_pub_key = int(self.other_pub_key_entry.get())
            self.shared_key = pow(other_pub_key, self.private_key, self.p)
            self.shared_key_label.config(text=f"Clave compartida: {self.shared_key}")
        except ValueError:
            tk.messagebox.showerror("Error", "Ingrese una clave pública válida")