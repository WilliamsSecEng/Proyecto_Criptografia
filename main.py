"""
Nombre Completo: Williams Tapia Caceres
Carrera: Informatica
Materia: Criptografía
Proyecto: Simulación Interactiva de Criptosistemas de Clave Pública
"""

# Importación de librerías necesarias para la interfaz gráfica y los módulos de criptosistemas
import tkinter as tk
from tkinter import ttk
from diffie_hellman import DiffieHellmanGUI
from rsa import RSAGUI
from elgamal import ElGamalGUI
from rabin import RabinGUI

# Clase principal de la aplicación
class MainApplication:
    def __init__(self, root):
        self.root = root
        self.root.title("Simulador de Criptosistemas")  # Título de la ventana principal
        self.setup_ui()  # Inicializa la interfaz de usuario
        
    def setup_ui(self):
        # Paleta de colores personalizada
        bg_color = "#f5f7fa"  # Fondo principal (gris claro)
        accent_a = "#5d75cc"   # Azul para Usuario A
        accent_b = "#77da77"   # Verde para Usuario B
        button_color = "#f7c873"  # Amarillo suave para botones
        self.root.configure(bg=bg_color)
        # Frame principal que contiene todos los widgets
        style = ttk.Style()
        style.configure("Main.TFrame", background=bg_color)
        style.configure("Main.TLabel", background=bg_color)
        style.configure("Main.TButton", background=button_color)
        main_frame = ttk.Frame(self.root, padding="20", style="Main.TFrame")
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Encabezado con los datos del proyecto
        encabezado = (
            "Nombre Completo: Williams Tapia Caceres\n"
            "Carrera: Informatica\n"
            "Materia: Criptografía\n"
            "Proyecto: Simulación Interactiva de Criptosistemas de Clave Pública"
        )
        ttk.Label(main_frame, text=encabezado, font=('Helvetica', 10), justify=tk.LEFT, style="Main.TLabel").pack(pady=(0, 10), anchor='w')
        
        # Título de la aplicación
        ttk.Label(main_frame, text="Seleccione un Criptosistema", 
                 font=('Comic Sans MS', 14, 'bold'), style="Main.TLabel").pack(pady=10)
        
        # Definición de los botones para cada criptosistema
        buttons = [
            ("Diffie-Hellman", self.open_diffie_hellman),
            ("RSA", self.open_rsa),
            ("ElGamal", self.open_elgamal),
            ("Rabin", self.open_rabin)
        ]
        
        # Creación y disposición de los botones en la interfaz
        for text, command in buttons:
            btn = ttk.Button(main_frame, text=text, command=command, style="Main.TButton")
            btn.pack(fill=tk.X, pady=5)
    
    # Métodos para abrir las ventanas de cada criptosistema
    def open_diffie_hellman(self):
        dh_window = tk.Toplevel(self.root)  # Ventana para Usuario A
        DiffieHellmanGUI(dh_window, "Usuario A")
        dh_window2 = tk.Toplevel(self.root)  # Ventana para Usuario B
        DiffieHellmanGUI(dh_window2, "Usuario B")
    
    def open_rsa(self):
        rsa_window = tk.Toplevel(self.root)  # Ventana para Usuario A
        RSAGUI(rsa_window, "Usuario A")
        rsa_window2 = tk.Toplevel(self.root)  # Ventana para Usuario B
        RSAGUI(rsa_window2, "Usuario B")
    
    def open_elgamal(self):
        elgamal_window = tk.Toplevel(self.root)  # Ventana para Usuario A
        ElGamalGUI(elgamal_window, "Usuario A")
        elgamal_window2 = tk.Toplevel(self.root)  # Ventana para Usuario B
        ElGamalGUI(elgamal_window2, "Usuario B")
    
    def open_rabin(self):
        rabin_window = tk.Toplevel(self.root)  # Ventana para Usuario A
        RabinGUI(rabin_window, "Usuario A")
        rabin_window2 = tk.Toplevel(self.root)  # Ventana para Usuario B
        RabinGUI(rabin_window2, "Usuario B")

# Punto de entrada principal de la aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = MainApplication(root)
    root.mainloop()