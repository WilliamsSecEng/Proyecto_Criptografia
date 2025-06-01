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

# La clase RabinGUI implementa la simulación del algoritmo Rabin.
# Permite al usuario generar claves públicas y privadas, cifrar y descifrar mensajes.
class RabinGUI:
    def __init__(self, master, user_name):
        # Guarda la ventana principal de este usuario
        self.master = master
        # Guarda el nombre del usuario (A o B)
        self.user = user_name
        # Inicializa los parámetros por defecto
        self.p = 7   # Primer primo
        self.q = 11  # Segundo primo
        self.n = 0   # Módulo
        self.m = None  # Mensaje original
        self.c = None  # Mensaje cifrado
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
                         text=f"Rabin - {self.user}",
                         font=('Helvetica', 12, 'bold'), style="Main.TLabel")
        title.pack(pady=10)
        # Frame para generación de claves
        keys_frame = ttk.LabelFrame(main_frame, text="Generación de Claves", padding="10")
        keys_frame.pack(fill=tk.X, pady=5)
        # Entradas para p, q
        ttk.Label(keys_frame, text="Primer primo (p):").grid(row=0, column=0, sticky=tk.W)
        self.p_entry = ttk.Entry(keys_frame)
        self.p_entry.insert(0, str(self.p))
        self.p_entry.grid(row=0, column=1, padx=5, pady=2)
        ttk.Label(keys_frame, text="Segundo primo (q):").grid(row=1, column=0, sticky=tk.W)
        self.q_entry = ttk.Entry(keys_frame)
        self.q_entry.insert(0, str(self.q))
        self.q_entry.grid(row=1, column=1, padx=5, pady=2)
        # Botón para generar clave pública
        ttk.Button(keys_frame, text="Generar Clave Pública", 
                  command=self.generate_public_key).grid(row=2, column=0, columnspan=2, pady=5)
        # Etiqueta para mostrar la clave pública
        self.n_label = ttk.Label(keys_frame, text="Clave pública (n): No calculada")
        self.n_label.grid(row=3, column=0, columnspan=2, sticky=tk.W)
        # Frame para cifrado
        encrypt_frame = ttk.LabelFrame(main_frame, text="Cifrado", padding="10")
        encrypt_frame.pack(fill=tk.X, pady=5)
        ttk.Label(encrypt_frame, text="Mensaje (m):").grid(row=0, column=0, sticky=tk.W)
        self.m_entry = ttk.Entry(encrypt_frame)
        self.m_entry.grid(row=0, column=1, padx=5, pady=2)
        ttk.Button(encrypt_frame, text="Cifrar", 
                  command=self.encrypt).grid(row=1, column=0, columnspan=2, pady=5)
        self.c_label = ttk.Label(encrypt_frame, text="Mensaje cifrado (c): ")
        self.c_label.grid(row=2, column=0, columnspan=2, sticky=tk.W)
        # Frame para descifrado
        decrypt_frame = ttk.LabelFrame(main_frame, text="Descifrado", padding="10")
        decrypt_frame.pack(fill=tk.X, pady=5)
        ttk.Label(decrypt_frame, text="Mensaje cifrado (c):").grid(row=0, column=0, sticky=tk.W)
        self.c_entry = ttk.Entry(decrypt_frame)
        self.c_entry.grid(row=0, column=1, padx=5, pady=2)
        ttk.Button(decrypt_frame, text="Descifrar", 
                  command=self.decrypt).grid(row=1, column=0, columnspan=2, pady=5)
        self.m_label = ttk.Label(decrypt_frame, text="Mensajes posibles: ")
        self.m_label.grid(row=2, column=0, columnspan=2, sticky=tk.W)
    
    def generate_public_key(self):
        # Obtiene los valores de p y q desde la interfaz
        try:
            self.p = int(self.p_entry.get())
            self.q = int(self.q_entry.get())
            # Calcula n = p * q
            self.n = self.p * self.q
            self.n_label.config(text=f"Clave pública (n): {self.n}")
        except ValueError:
            messagebox.showerror("Error", "Ingrese valores numéricos válidos")
    
    def encrypt(self):
        # Cifra el mensaje usando la clave pública
        try:
            self.m = int(self.m_entry.get())
            # Calcula c = m^2 mod n
            self.c = pow(self.m, 2, self.n)
            self.c_label.config(text=f"Mensaje cifrado (c): {self.c}")
        except ValueError:
            messagebox.showerror("Error", "Ingrese un mensaje válido")
    
    def decrypt(self):
        # Descifra el mensaje usando la clave privada
        try:
            c = int(self.c_entry.get())
            # Calcula las cuatro posibles raíces cuadradas de c módulo n
            m1 = self.mod_sqrt(c, self.p)
            m2 = self.p - m1
            m3 = self.mod_sqrt(c, self.q)
            m4 = self.q - m3
            # Muestra los posibles mensajes originales
            self.m_label.config(text=f"Mensajes posibles: {m1}, {m2}, {m3}, {m4}")
        except ValueError:
            messagebox.showerror("Error", "Ingrese un mensaje cifrado válido")
    
    def mod_sqrt(self, a, p):
        # Calcula la raíz cuadrada modular usando el método de Tonelli-Shanks (simplificado para p primo pequeño)
        for x in range(p):
            if (x * x) % p == a % p:
                return x
        return None

# ...existing code...