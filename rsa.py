"""
Nombre Completo: Williams Tapia Caceres
Carrera: Informatica
Materia: Criptografía
Proyecto: Simulación Interactiva de Criptosistemas de Clave Pública
"""

# Importa la librería principal de interfaces gráficas de Python
import tkinter as tk
# Importa el módulo ttk y messagebox para widgets y mensajes
from tkinter import ttk, messagebox
# Importa utilidades para generación de números primos
from Crypto.Util import number
import math

# La clase RSAGUI implementa la simulación del algoritmo RSA.
# Permite al usuario generar claves públicas y privadas, cifrar y descifrar mensajes.
class RSAGUI:
    def __init__(self, master, user_name):
        # Guarda la ventana principal de este usuario
        self.master = master
        # Guarda el nombre del usuario (A o B)
        self.user = user_name
        # Inicializa los parámetros por defecto
        self.p = 61  # Primer primo
        self.q = 53  # Segundo primo
        self.e = 17  # Exponente público
        self.d = 0   # Exponente privado
        self.n = 0   # Módulo
        self.phi = 0 # Función phi de Euler
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
                         text=f"RSA - {self.user}",
                         font=('Helvetica', 12, 'bold'), style="Main.TLabel")
        title.pack(pady=10)
        # Frame para generación de claves
        keys_frame = ttk.LabelFrame(main_frame, text="Generación de Claves", padding="10")
        keys_frame.pack(fill=tk.X, pady=5)
        # Entradas para p, q, e
        ttk.Label(keys_frame, text="Primer primo (p):").grid(row=0, column=0, sticky=tk.W)
        self.p_entry = ttk.Entry(keys_frame)
        self.p_entry.insert(0, str(self.p))
        self.p_entry.grid(row=0, column=1, padx=5, pady=2)
        ttk.Label(keys_frame, text="Segundo primo (q):").grid(row=1, column=0, sticky=tk.W)
        self.q_entry = ttk.Entry(keys_frame)
        self.q_entry.insert(0, str(self.q))
        self.q_entry.grid(row=1, column=1, padx=5, pady=2)
        ttk.Label(keys_frame, text="Exponente público (e):").grid(row=2, column=0, sticky=tk.W)
        self.e_entry = ttk.Entry(keys_frame)
        self.e_entry.insert(0, str(self.e))
        self.e_entry.grid(row=2, column=1, padx=5, pady=2)
        # Botón para generar claves
        ttk.Button(keys_frame, text="Generar Claves", 
                  command=self.generate_keys).grid(row=3, column=0, columnspan=2, pady=5)
        # Etiquetas para mostrar resultados de generación de claves
        self.n_label = ttk.Label(keys_frame, text="n = p*q: No calculado")
        self.n_label.grid(row=4, column=0, columnspan=2, sticky=tk.W)
        self.phi_label = ttk.Label(keys_frame, text="φ(n) = (p-1)*(q-1): No calculado")
        self.phi_label.grid(row=5, column=0, columnspan=2, sticky=tk.W)
        self.d_label = ttk.Label(keys_frame, text="d = e⁻¹ mod φ(n): No calculado")
        self.d_label.grid(row=6, column=0, columnspan=2, sticky=tk.W)
        # Frame para cifrado y descifrado
        crypto_frame = ttk.LabelFrame(main_frame, text="Cifrado/Descifrado", padding="10")
        crypto_frame.pack(fill=tk.X, pady=5)
        ttk.Label(crypto_frame, text="Mensaje:").grid(row=0, column=0, sticky=tk.W)
        self.message_entry = ttk.Entry(crypto_frame)
        self.message_entry.grid(row=0, column=1, padx=5, pady=2)
        # Botones para cifrar y descifrar
        ttk.Button(crypto_frame, text="Cifrar", 
                  command=self.encrypt).grid(row=1, column=0, pady=5)
        ttk.Button(crypto_frame, text="Descifrar", 
                  command=self.decrypt).grid(row=1, column=1, pady=5)
        # Etiquetas para mostrar resultados
        self.cipher_label = ttk.Label(crypto_frame, text="Mensaje cifrado: ")
        self.cipher_label.grid(row=2, column=0, columnspan=2, sticky=tk.W)
        self.plain_label = ttk.Label(crypto_frame, text="Mensaje descifrado: ")
        self.plain_label.grid(row=3, column=0, columnspan=2, sticky=tk.W)
        # Frame para clave pública del otro usuario
        other_frame = ttk.LabelFrame(main_frame, text="Clave Pública del Otro Usuario", padding="10")
        other_frame.pack(fill=tk.X, pady=5)
        ttk.Label(other_frame, text="n del otro usuario:").grid(row=0, column=0, sticky=tk.W)
        self.other_n_entry = ttk.Entry(other_frame)
        self.other_n_entry.grid(row=0, column=1, padx=5, pady=2)
        ttk.Label(other_frame, text="e del otro usuario:").grid(row=1, column=0, sticky=tk.W)
        self.other_e_entry = ttk.Entry(other_frame)
        self.other_e_entry.grid(row=1, column=1, padx=5, pady=2)
    
    def generate_keys(self):
        # Obtiene los valores de p, q, e desde la interfaz
        try:
            self.p = int(self.p_entry.get())
            self.q = int(self.q_entry.get())
            self.e = int(self.e_entry.get())
            # Verifica que p y q sean primos
            if not (self.is_prime(self.p) and self.is_prime(self.q)):
                messagebox.showerror("Error", "p y q deben ser números primos")
                return
            # Calcula n y phi(n)
            self.n = self.p * self.q
            self.phi = (self.p - 1) * (self.q - 1)
            # Verifica que e sea coprimo con phi(n)
            if math.gcd(self.e, self.phi) != 1:
                messagebox.showerror("Error", "e debe ser coprimo con φ(n)")
                return
            # Calcula el inverso modular de e
            self.d = self.modinv(self.e, self.phi)
            # Actualiza la interfaz con los resultados
            self.n_label.config(text=f"n = p*q: {self.n}")
            self.phi_label.config(text=f"φ(n) = (p-1)*(q-1): {self.phi}")
            self.d_label.config(text=f"d = e⁻¹ mod φ(n): {self.d}")
            messagebox.showinfo("Éxito", "Claves generadas correctamente")
        except ValueError:
            messagebox.showerror("Error", "Ingrese valores numéricos válidos")
    
    def encrypt(self):
        # Cifra el mensaje usando la clave pública del otro usuario
        if not hasattr(self, 'n') or self.n == 0:
            messagebox.showerror("Error", "Primero genere las claves")
            return
        try:
            message = self.message_entry.get()
            if not message.isdigit():
                messagebox.showerror("Error", "El mensaje debe ser un número")
                return
            m = int(message)
            other_n = int(self.other_n_entry.get())
            other_e = int(self.other_e_entry.get())
            # Cifra el mensaje: c = m^e mod n
            cipher = pow(m, other_e, other_n)
            self.cipher_label.config(text=f"Mensaje cifrado: {cipher}")
        except ValueError:
            messagebox.showerror("Error", "Ingrese valores válidos para n y e del otro usuario")
    
    def decrypt(self):
        # Descifra el mensaje usando la clave privada
        if not hasattr(self, 'd') or self.d == 0:
            messagebox.showerror("Error", "Primero genere las claves")
            return
        try:
            cipher = self.message_entry.get()
            if not cipher.isdigit():
                messagebox.showerror("Error", "El mensaje cifrado debe ser un número")
                return
            c = int(cipher)
            # Descifra el mensaje: m = c^d mod n
            plain = pow(c, self.d, self.n)
            self.plain_label.config(text=f"Mensaje descifrado: {plain}")
        except ValueError:
            messagebox.showerror("Error", "Ingrese un mensaje cifrado válido")
    
    @staticmethod
    def is_prime(n):
        # Verifica si n es primo
        if n <= 1:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True
    
    @staticmethod
    def modinv(a, m):
        # Calcula el inverso modular de a módulo m
        g, x, y = RSAGUI.extended_gcd(a, m)
        if g != 1:
            return None  # No existe inverso modular
        else:
            return x % m
    
    @staticmethod
    def extended_gcd(a, b):
        # Algoritmo extendido de Euclides para el inverso modular
        if a == 0:
            return (b, 0, 1)
        else:
            g, y, x = RSAGUI.extended_gcd(b % a, a)
            return (g, x - (b // a) * y, y)