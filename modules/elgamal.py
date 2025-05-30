"""
Nombre Completo: Williams Tapia Caceres
Carrera: Informatica
Materia: Criptografía
Proyecto: Simulación Interactiva de Criptosistemas de Clave Pública
"""

import math
import tkinter as tk
from tkinter import ttk, messagebox
#from Crypto.Util import number  # Removed unused import
import random
import sys

class ElGamalGUI:
    def __init__(self, master, user_name):
        self.master = master
        self.user = user_name
        self.private_key = 0
        self.public_key = (0, 0, 0)  # (p, g, h)
        self.setup_ui()
        
    def setup_ui(self):
        # Configuración de colores personalizados
        bg_color = "#f0f0f0" if self.user == "Usuario A" else "#ffe0e0"
        self.master.configure(bg=bg_color)
        
        # Frame principal
        main_frame = ttk.Frame(self.master, padding="15")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Título
        title = ttk.Label(main_frame, 
                         text=f"ElGamal - {self.user}",
                         font=('Helvetica', 12, 'bold'))
        title.pack(pady=10)
        
        # Generación de claves
        keys_frame = ttk.LabelFrame(main_frame, text="Generación de Claves", padding="10")
        keys_frame.pack(fill=tk.X, pady=5)
        
        # Parámetros
        ttk.Label(keys_frame, text="Número primo (p):").grid(row=0, column=0, sticky=tk.W)
        self.p_entry = ttk.Entry(keys_frame)
        self.p_entry.insert(0, "23")  # Valor por defecto
        self.p_entry.grid(row=0, column=1, padx=5, pady=2)
        
        ttk.Label(keys_frame, text="Generador (g):").grid(row=1, column=0, sticky=tk.W)
        self.g_entry = ttk.Entry(keys_frame)
        self.g_entry.insert(0, "5")  # Valor por defecto
        self.g_entry.grid(row=1, column=1, padx=5, pady=2)
        
        ttk.Button(keys_frame, text="Generar Clave Privada", 
                  command=self.generate_private_key).grid(row=2, column=0, pady=5)
        ttk.Button(keys_frame, text="Calcular Clave Pública", 
                  command=self.generate_public_key).grid(row=2, column=1, pady=5)
        
        self.priv_key_label = ttk.Label(keys_frame, text="Clave privada (x): No generada")
        self.priv_key_label.grid(row=3, column=0, columnspan=2, sticky=tk.W)
        
        self.pub_key_label = ttk.Label(keys_frame, text="Clave pública (p, g, h): No calculada")
        self.pub_key_label.grid(row=4, column=0, columnspan=2, sticky=tk.W)
        
        # Cifrado
        encrypt_frame = ttk.LabelFrame(main_frame, text="Cifrado", padding="10")
        encrypt_frame.pack(fill=tk.X, pady=5)
        
        ttk.Label(encrypt_frame, text="Mensaje (número):").grid(row=0, column=0, sticky=tk.W)
        self.message_entry = ttk.Entry(encrypt_frame)
        self.message_entry.grid(row=0, column=1, padx=5, pady=2)
        
        ttk.Label(encrypt_frame, text="Clave pública del receptor (p, g, h):").grid(row=1, column=0, sticky=tk.W)
        self.other_pub_key_entry = ttk.Entry(encrypt_frame)
        self.other_pub_key_entry.grid(row=1, column=1, padx=5, pady=2)
        
        ttk.Button(encrypt_frame, text="Cifrar Mensaje", 
                  command=self.encrypt).grid(row=2, column=0, columnspan=2, pady=5)
        
        self.cipher_label = ttk.Label(encrypt_frame, text="Mensaje cifrado (c1, c2): ")
        self.cipher_label.grid(row=3, column=0, columnspan=2, sticky=tk.W)
        
        # Descifrado
        decrypt_frame = ttk.LabelFrame(main_frame, text="Descifrado", padding="10")
        decrypt_frame.pack(fill=tk.X, pady=5)
        
        ttk.Label(decrypt_frame, text="Mensaje cifrado (c1, c2):").grid(row=0, column=0, sticky=tk.W)
        self.cipher_entry = ttk.Entry(decrypt_frame)
        self.cipher_entry.grid(row=0, column=1, padx=5, pady=2)
        
        ttk.Button(decrypt_frame, text="Descifrar Mensaje", 
                  command=self.decrypt).grid(row=1, column=0, columnspan=2, pady=5)
        
        self.plain_label = ttk.Label(decrypt_frame, text="Mensaje descifrado: ")
        self.plain_label.grid(row=2, column=0, columnspan=2, sticky=tk.W)
    
    def generate_private_key(self):
        try:
            p = int(self.p_entry.get())
            self.private_key = random.randint(1, p-2)
            self.priv_key_label.config(text=f"Clave privada (x): {self.private_key}")
        except ValueError:
            messagebox.showerror("Error", "Ingrese un número primo válido")
    
    def generate_public_key(self):
        if not hasattr(self, 'private_key') or self.private_key == 0:
            messagebox.showerror("Error", "Primero genere una clave privada")
            return
            
        try:
            p = int(self.p_entry.get())
            g = int(self.g_entry.get())
            
            h = pow(g, self.private_key, p)
            self.public_key = (p, g, h)
            self.pub_key_label.config(text=f"Clave pública (p, g, h): {self.public_key}")
        except ValueError:
            messagebox.showerror("Error", "Ingrese valores numéricos válidos")
    
    def encrypt(self):
        try:
            message = int(self.message_entry.get())
            pub_key_str = self.other_pub_key_entry.get()
            p, g, h = map(int, pub_key_str.strip("()").split(","))
            
            # Generar un número aleatorio k coprimo con p-1
            k = random.randint(1, p-2)
            while math.gcd(k, p-1) != 1:
                k = random.randint(1, p-2)
            
            c1 = pow(g, k, p)
            c2 = (message * pow(h, k, p)) % p
            
            self.cipher_label.config(text=f"Mensaje cifrado (c1, c2): ({c1}, {c2})")
        except (ValueError, AttributeError):
            messagebox.showerror("Error", "Ingrese valores válidos")
    
    def decrypt(self):
        if not hasattr(self, 'private_key') or self.private_key == 0:
            messagebox.showerror("Error", "Primero genere una clave privada")
            return
            
        try:
            cipher_str = self.cipher_entry.get()
            c1, c2 = map(int, cipher_str.strip("()").split(","))
            
            p = self.public_key[0]
            s = pow(c1, self.private_key, p)
            s_inv = self.modinv(s, p)
            plain = (c2 * s_inv) % p
            
            self.plain_label.config(text=f"Mensaje descifrado: {plain}")
        except (ValueError, AttributeError):
            messagebox.showerror("Error", "Ingrese un mensaje cifrado válido")
    
    @staticmethod
    def modinv(a, m):
        g, x, y = ElGamalGUI.extended_gcd(a, m)
        if g != 1:
            return None  # No existe inverso modular
        else:
            return x % m
    
    @staticmethod
    def extended_gcd(a, b):
        if a == 0:
            return (b, 0, 1)
        else:
            g, y, x = ElGamalGUI.extended_gcd(b % a, a)
            return (g, x - (b // a) * y, y)