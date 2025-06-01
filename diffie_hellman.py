"""
Nombre Completo: Williams Tapia Caceres
Carrera: Informatica
Materia: Criptografía
Proyecto: Simulación Interactiva de Criptosistemas de Clave Pública
"""

# Importa la librería principal de interfaces gráficas de Python
import tkinter as tk
from tkinter import ttk, messagebox
import random

# La clase DiffieHellmanGUI implementa la simulación del protocolo Diffie-Hellman.
# Permite a dos usuarios generar una clave secreta compartida a través de un canal inseguro.
class DiffieHellmanGUI:
    def __init__(self, master, user_name):
        # Guarda la ventana principal de este usuario
        self.master = master
        # Guarda el nombre del usuario (A o B)
        self.user = user_name
        # Inicializa los parámetros por defecto
        self.p = 23  # Primo público
        self.g = 5   # Base pública
        self.a = random.randint(1, 10)  # Secreto privado
        self.A = None  # Clave pública
        self.B = None  # Clave pública del otro usuario
        self.K = None  # Clave secreta compartida
        # Construye la interfaz gráfica
        self.setup_ui()
    
    def setup_ui(self):
        # Paleta de colores personalizada
        bg_color = "#f5f7fa"
        accent = "#5d75cc" if self.user == "Usuario A" else "#77da77"
        button_color = "#f7c873"
        style = ttk.Style()
        style.configure("Main.TFrame", background=bg_color)
        style.configure("Main.TLabel", background=bg_color)
        style.configure("Main.TButton", background=button_color)
        self.master.configure(bg=bg_color)
        # Frame principal
        main_frame = ttk.Frame(self.master, padding="15", style="Main.TFrame")
        main_frame.pack(fill=tk.BOTH, expand=True)
        # Título de la ventana
        title = ttk.Label(main_frame, 
                         text=f"Diffie-Hellman - {self.user}",
                         font=('Helvetica', 12, 'bold'), style="Main.TLabel")
        title.pack(pady=10)
        # Frame para parámetros y generación de claves
        params_frame = ttk.LabelFrame(main_frame, text="Parámetros y Claves", padding="10")
        params_frame.pack(fill=tk.X, pady=5)
        # Entradas para p, g, a
        ttk.Label(params_frame, text="Primo público (p):").grid(row=0, column=0, sticky=tk.W)
        self.p_entry = ttk.Entry(params_frame)
        self.p_entry.insert(0, str(self.p))
        self.p_entry.grid(row=0, column=1, padx=5, pady=2)
        ttk.Label(params_frame, text="Base pública (g):").grid(row=1, column=0, sticky=tk.W)
        self.g_entry = ttk.Entry(params_frame)
        self.g_entry.insert(0, str(self.g))
        self.g_entry.grid(row=1, column=1, padx=5, pady=2)
        ttk.Label(params_frame, text="Secreto privado (a):").grid(row=2, column=0, sticky=tk.W)
        self.a_entry = ttk.Entry(params_frame)
        self.a_entry.insert(0, str(self.a))
        self.a_entry.grid(row=2, column=1, padx=5, pady=2)
        # Botón para generar clave pública
        ttk.Button(params_frame, text="Generar Clave Pública", 
                  command=self.generate_public_key).grid(row=3, column=0, columnspan=2, pady=5)
        # Etiqueta para mostrar la clave pública
        self.A_label = ttk.Label(params_frame, text="Clave pública (A): No calculada")
        self.A_label.grid(row=4, column=0, columnspan=2, sticky=tk.W)
        # Frame para intercambio y cálculo de clave compartida
        exchange_frame = ttk.LabelFrame(main_frame, text="Intercambio y Clave Compartida", padding="10")
        exchange_frame.pack(fill=tk.X, pady=5)
        ttk.Label(exchange_frame, text="Clave pública del otro usuario (B):").grid(row=0, column=0, sticky=tk.W)
        self.B_entry = ttk.Entry(exchange_frame)
        self.B_entry.grid(row=0, column=1, padx=5, pady=2)
        ttk.Button(exchange_frame, text="Calcular Clave Compartida", 
                  command=self.compute_shared_key).grid(row=1, column=0, columnspan=2, pady=5)
        self.K_label = ttk.Label(exchange_frame, text="Clave compartida (K): No calculada")
        self.K_label.grid(row=2, column=0, columnspan=2, sticky=tk.W)
    
    def generate_public_key(self):
        # Obtiene los valores de p, g, a desde la interfaz
        try:
            self.p = int(self.p_entry.get())
            self.g = int(self.g_entry.get())
            self.a = int(self.a_entry.get())
            # Calcula la clave pública A = g^a mod p
            self.A = pow(self.g, self.a, self.p)
            self.A_label.config(text=f"Clave pública (A): {self.A}")
        except ValueError:
            messagebox.showerror("Error", "Ingrese valores numéricos válidos")
    
    def compute_shared_key(self):
        # Calcula la clave compartida usando la clave pública del otro usuario
        try:
            self.B = int(self.B_entry.get())
            # Calcula la clave compartida K = B^a mod p
            self.K = pow(self.B, self.a, self.p)
            self.K_label.config(text=f"Clave compartida (K): {self.K}")
        except ValueError:
            messagebox.showerror("Error", "Ingrese la clave pública del otro usuario")