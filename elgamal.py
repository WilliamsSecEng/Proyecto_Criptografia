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

# La clase ElGamalGUI implementa la simulación del algoritmo ElGamal.
# Permite al usuario generar claves públicas y privadas, cifrar y descifrar mensajes.
class ElGamalGUI:
    def __init__(self, master, user_name):
        # Guarda la ventana principal de este usuario
        self.master = master
        # Guarda el nombre del usuario (A o B)
        self.user = user_name
        # Inicializa los parámetros por defecto
        self.p = 23  # Primo público
        self.g = 5   # Base pública
        self.x = random.randint(1, 10)  # Secreto privado
        self.y = None  # Clave pública
        self.k = None  # Aleatorio para cifrado
        self.c1 = None # Parte 1 del cifrado
        self.c2 = None # Parte 2 del cifrado
        self.m = None  # Mensaje original
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
                         text=f"ElGamal - {self.user}",
                         font=('Helvetica', 12, 'bold'), style="Main.TLabel")
        title.pack(pady=10)
        # Frame para generación de claves
        keys_frame = ttk.LabelFrame(main_frame, text="Generación de Claves", padding="10")
        keys_frame.pack(fill=tk.X, pady=5)
        # Entradas para p, g, x
        ttk.Label(keys_frame, text="Primo público (p):").grid(row=0, column=0, sticky=tk.W)
        self.p_entry = ttk.Entry(keys_frame)
        self.p_entry.insert(0, str(self.p))
        self.p_entry.grid(row=0, column=1, padx=5, pady=2)
        ttk.Label(keys_frame, text="Base pública (g):").grid(row=1, column=0, sticky=tk.W)
        self.g_entry = ttk.Entry(keys_frame)
        self.g_entry.insert(0, str(self.g))
        self.g_entry.grid(row=1, column=1, padx=5, pady=2)
        ttk.Label(keys_frame, text="Secreto privado (x):").grid(row=2, column=0, sticky=tk.W)
        self.x_entry = ttk.Entry(keys_frame)
        self.x_entry.insert(0, str(self.x))
        self.x_entry.grid(row=2, column=1, padx=5, pady=2)
        # Botón para generar clave pública
        ttk.Button(keys_frame, text="Generar Clave Pública", 
                  command=self.generate_public_key).grid(row=3, column=0, columnspan=2, pady=5)
        # Etiqueta para mostrar la clave pública
        self.y_label = ttk.Label(keys_frame, text="Clave pública (y): No calculada")
        self.y_label.grid(row=4, column=0, columnspan=2, sticky=tk.W)
        # Frame para cifrado
        encrypt_frame = ttk.LabelFrame(main_frame, text="Cifrado", padding="10")
        encrypt_frame.pack(fill=tk.X, pady=5)
        ttk.Label(encrypt_frame, text="Mensaje (m):").grid(row=0, column=0, sticky=tk.W)
        self.m_entry = ttk.Entry(encrypt_frame)
        self.m_entry.grid(row=0, column=1, padx=5, pady=2)
        ttk.Button(encrypt_frame, text="Cifrar", 
                  command=self.encrypt).grid(row=1, column=0, columnspan=2, pady=5)
        self.c1_label = ttk.Label(encrypt_frame, text="c1: ")
        self.c1_label.grid(row=2, column=0, columnspan=2, sticky=tk.W)
        self.c2_label = ttk.Label(encrypt_frame, text="c2: ")
        self.c2_label.grid(row=3, column=0, columnspan=2, sticky=tk.W)
        # Frame para descifrado
        decrypt_frame = ttk.LabelFrame(main_frame, text="Descifrado", padding="10")
        decrypt_frame.pack(fill=tk.X, pady=5)
        ttk.Label(decrypt_frame, text="c1:").grid(row=0, column=0, sticky=tk.W)
        self.c1_entry = ttk.Entry(decrypt_frame)
        self.c1_entry.grid(row=0, column=1, padx=5, pady=2)
        ttk.Label(decrypt_frame, text="c2:").grid(row=1, column=0, sticky=tk.W)
        self.c2_entry = ttk.Entry(decrypt_frame)
        self.c2_entry.grid(row=1, column=1, padx=5, pady=2)
        ttk.Button(decrypt_frame, text="Descifrar", 
                  command=self.decrypt).grid(row=2, column=0, columnspan=2, pady=5)
        self.m_label = ttk.Label(decrypt_frame, text="Mensaje original: ")
        self.m_label.grid(row=3, column=0, columnspan=2, sticky=tk.W)
    
    def generate_public_key(self):
        # Obtiene los valores de p, g, x desde la interfaz
        try:
            self.p = int(self.p_entry.get())
            self.g = int(self.g_entry.get())
            self.x = int(self.x_entry.get())
            # Calcula la clave pública y = g^x mod p
            self.y = pow(self.g, self.x, self.p)
            self.y_label.config(text=f"Clave pública (y): {self.y}")
        except ValueError:
            messagebox.showerror("Error", "Ingrese valores numéricos válidos")
    
    def encrypt(self):
        # Cifra el mensaje usando la clave pública
        try:
            self.m = int(self.m_entry.get())
            self.k = random.randint(1, self.p - 2)
            # Calcula c1 = g^k mod p
            self.c1 = pow(self.g, self.k, self.p)
            # Calcula c2 = m * y^k mod p
            self.c2 = (self.m * pow(self.y, self.k, self.p)) % self.p
            self.c1_label.config(text=f"c1: {self.c1}")
            self.c2_label.config(text=f"c2: {self.c2}")
        except ValueError:
            messagebox.showerror("Error", "Ingrese un mensaje válido")
    
    def decrypt(self):
        # Descifra el mensaje usando la clave privada
        try:
            c1 = int(self.c1_entry.get())
            c2 = int(self.c2_entry.get())
            # Calcula el inverso de c1^x mod p
            s = pow(c1, self.x, self.p)
            s_inv = pow(s, -1, self.p)
            # Recupera el mensaje original
            m = (c2 * s_inv) % self.p
            self.m_label.config(text=f"Mensaje original: {m}")
        except ValueError:
            messagebox.showerror("Error", "Ingrese valores válidos para c1 y c2")