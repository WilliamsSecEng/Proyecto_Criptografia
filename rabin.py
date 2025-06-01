"""
Nombre Completo: Williams Tapia Caceres
Carrera: Informatica
Materia: Criptografía
Proyecto: Simulación Interactiva de Criptosistemas de Clave Pública
"""

# Módulo para la simulación del algoritmo Rabin
# Importa las librerías necesarias para la interfaz gráfica y la lógica de Rabin
# Define la clase RabinGUI para la interacción con el usuario y la simulación
# Incluye métodos para generar claves, cifrar, descifrar y mostrar resultados

import tkinter as tk
from tkinter import ttk, messagebox
from Crypto.Util import number
import math
import random

class RabinGUI:
    def __init__(self, master, user_name):
        self.master = master
        self.user = user_name
        self.p = 7  # Primer primo por defecto (personalizable)
        self.q = 11 # Segundo primo por defecto (personalizable)
        self.n = 0  # Módulo
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
                         text=f"Rabin - {self.user}",
                         font=('Helvetica', 12, 'bold'))
        title.pack(pady=10)
        
        # Generación de claves
        keys_frame = ttk.LabelFrame(main_frame, text="Generación de Claves", padding="10")
        keys_frame.pack(fill=tk.X, pady=5)
        
        # Entradas para parámetros
        ttk.Label(keys_frame, text="Primer primo (p):").grid(row=0, column=0, sticky=tk.W)
        self.p_entry = ttk.Entry(keys_frame)
        self.p_entry.insert(0, str(self.p))
        self.p_entry.grid(row=0, column=1, padx=5, pady=2)
        
        ttk.Label(keys_frame, text="Segundo primo (q):").grid(row=1, column=0, sticky=tk.W)
        self.q_entry = ttk.Entry(keys_frame)
        self.q_entry.insert(0, str(self.q))
        self.q_entry.grid(row=1, column=1, padx=5, pady=2)
        
        ttk.Button(keys_frame, text="Generar Claves", 
                  command=self.generate_keys).grid(row=2, column=0, columnspan=2, pady=5)
        
        # Resultados de generación de claves
        self.n_label = ttk.Label(keys_frame, text="n = p*q: No calculado")
        self.n_label.grid(row=3, column=0, columnspan=2, sticky=tk.W)
        
        # Cifrado
        encrypt_frame = ttk.LabelFrame(main_frame, text="Cifrado", padding="10")
        encrypt_frame.pack(fill=tk.X, pady=5)
        
        ttk.Label(encrypt_frame, text="Mensaje (número < n):").grid(row=0, column=0, sticky=tk.W)
        self.message_entry = ttk.Entry(encrypt_frame)
        self.message_entry.grid(row=0, column=1, padx=5, pady=2)
        
        ttk.Label(encrypt_frame, text="n del receptor:").grid(row=1, column=0, sticky=tk.W)
        self.other_n_entry = ttk.Entry(encrypt_frame)
        self.other_n_entry.grid(row=1, column=1, padx=5, pady=2)
        
        ttk.Button(encrypt_frame, text="Cifrar Mensaje", 
                  command=self.encrypt).grid(row=2, column=0, columnspan=2, pady=5)
        
        self.cipher_label = ttk.Label(encrypt_frame, text="Mensaje cifrado: ")
        self.cipher_label.grid(row=3, column=0, columnspan=2, sticky=tk.W)
        
        # Descifrado
        decrypt_frame = ttk.LabelFrame(main_frame, text="Descifrado", padding="10")
        decrypt_frame.pack(fill=tk.X, pady=5)
        
        ttk.Label(decrypt_frame, text="Mensaje cifrado:").grid(row=0, column=0, sticky=tk.W)
        self.cipher_entry = ttk.Entry(decrypt_frame)
        self.cipher_entry.grid(row=0, column=1, padx=5, pady=2)
        
        ttk.Button(decrypt_frame, text="Descifrar Mensaje", 
                  command=self.decrypt).grid(row=1, column=0, columnspan=2, pady=5)
        
        self.solutions_label = ttk.Label(decrypt_frame, text="Posibles mensajes originales: ")
        self.solutions_label.grid(row=2, column=0, columnspan=2, sticky=tk.W)
        
        self.correct_label = ttk.Label(decrypt_frame, text="Mensaje correcto: ")
        self.correct_label.grid(row=3, column=0, columnspan=2, sticky=tk.W)
    
    def generate_keys(self):
        try:
            self.p = int(self.p_entry.get())
            self.q = int(self.q_entry.get())
            
            if not (self.is_prime(self.p) and self.is_prime(self.q)):
                messagebox.showerror("Error", "p y q deben ser números primos")
                return
                
            if self.p % 4 != 3 or self.q % 4 != 3:
                messagebox.showerror("Error", "p y q deben ser primos congruentes con 3 módulo 4")
                return
                
            self.n = self.p * self.q
            self.n_label.config(text=f"n = p*q: {self.n}")
            
            messagebox.showinfo("Éxito", "Claves generadas correctamente")
        except ValueError:
            messagebox.showerror("Error", "Ingrese valores numéricos válidos")
    
    def encrypt(self):
        try:
            message = int(self.message_entry.get())
            n = int(self.other_n_entry.get())
            
            if message >= n:
                messagebox.showerror("Error", "El mensaje debe ser menor que n")
                return
                
            cipher = pow(message, 2, n)
            self.cipher_label.config(text=f"Mensaje cifrado: {cipher}")
        except ValueError:
            messagebox.showerror("Error", "Ingrese valores numéricos válidos")
    
    def decrypt(self):
        if not hasattr(self, 'n') or self.n == 0:
            messagebox.showerror("Error", "Primero genere las claves")
            return
            
        try:
            cipher = int(self.cipher_entry.get())
            
            # Calcular raíces cuadradas módulo p y q
            mp = pow(cipher, (self.p + 1) // 4, self.p)
            mq = pow(cipher, (self.q + 1) // 4, self.q)
            
            # Aplicar el teorema chino del resto
            yp, yq = self.extended_gcd(self.p, self.q)[1:]
            x1 = (yp * self.p * mq + yq * self.q * mp) % self.n
            x2 = self.n - x1
            x3 = (yp * self.p * mq - yq * self.q * mp) % self.n
            x4 = self.n - x3
            
            solutions = sorted([x1, x2, x3, x4])
            self.solutions_label.config(text=f"Posibles mensajes originales: {solutions}")
            
            # Identificar el mensaje correcto (en un caso real se usaría información auxiliar)
            correct = min(solutions)  # Simplemente elegimos el más pequeño como ejemplo
            self.correct_label.config(text=f"Mensaje correcto (ejemplo): {correct}")
        except ValueError:
            messagebox.showerror("Error", "Ingrese un mensaje cifrado válido")
    
    @staticmethod
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True
    
    @staticmethod
    def extended_gcd(a, b):
        if a == 0:
            return (b, 0, 1)
        else:
            g, y, x = RabinGUI.extended_gcd(b % a, a)
            return (g, x - (b // a) * y, y)