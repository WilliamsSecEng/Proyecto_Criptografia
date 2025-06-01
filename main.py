"""
Nombre Completo: Williams Tapia Caceres
Carrera: Informatica
Materia: Criptografía
Proyecto: Simulación Interactiva de Criptosistemas de Clave Pública
"""

# Importa la librería principal de interfaces gráficas de Python
import tkinter as tk
# Importa el módulo ttk para widgets mejorados de Tkinter
from tkinter import ttk
# Importa las clases de interfaz gráfica de cada criptosistema
from diffie_hellman import DiffieHellmanGUI
from rsa import RSAGUI
from elgamal import ElGamalGUI
from rabin import RabinGUI

# Define la clase principal de la aplicación
class MainApplication:
    def __init__(self, root):
        # Guarda la ventana principal de Tkinter
        self.root = root
        # Establece el título de la ventana
        self.root.title("Simulador de Criptosistemas")
        # Llama al método para construir la interfaz
        self.setup_ui()
        
    def setup_ui(self):
        # Paleta de colores personalizada para la interfaz
        bg_color = "#f5f7fa"  # Color de fondo principal
        accent_a = "#5d75cc"   # Color para Usuario A
        accent_b = "#77da77"   # Color para Usuario B
        button_color = "#f7c873"  # Color para botones
        # Aplica el color de fondo a la ventana principal
        self.root.configure(bg=bg_color)
        # Crea un estilo personalizado para los widgets
        style = ttk.Style()
        style.configure("Main.TFrame", background=bg_color)
        style.configure("Main.TLabel", background=bg_color)
        style.configure("Main.TButton", background=button_color)
        # Crea el frame principal con el estilo definido
        main_frame = ttk.Frame(self.root, padding="20", style="Main.TFrame")
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Define el texto del encabezado con los datos del proyecto
        encabezado = (
            "Nombre Completo: Williams Tapia Caceres\n"
            "Carrera: Informatica\n"
            "Materia: Criptografía\n"
            "Proyecto: Simulación Interactiva de Criptosistemas de Clave Pública"
        )
        # Muestra el encabezado en la parte superior de la ventana
        ttk.Label(main_frame, text=encabezado, font=('Helvetica', 10), justify=tk.LEFT, style="Main.TLabel").pack(pady=(0, 10), anchor='w')
        
        # Muestra el título principal de la aplicación
        ttk.Label(main_frame, text="Seleccione un Criptosistema", 
                 font=('Comic Sans MS', 14, 'bold'), style="Main.TLabel").pack(pady=10)
        
        # Lista de botones y funciones asociadas para cada criptosistema
        buttons = [
            ("Diffie-Hellman", self.open_diffie_hellman),
            ("RSA", self.open_rsa),
            ("ElGamal", self.open_elgamal),
            ("Rabin", self.open_rabin)
        ]
        
        # Crea y muestra los botones para cada criptosistema
        for text, command in buttons:
            btn = ttk.Button(main_frame, text=text, command=command, style="Main.TButton")
            btn.pack(fill=tk.X, pady=5)
    
    # Abre dos ventanas para simular Diffie-Hellman (Usuario A y B)
    def open_diffie_hellman(self):
        dh_window = tk.Toplevel(self.root)  # Ventana para Usuario A
        DiffieHellmanGUI(dh_window, "Usuario A")
        dh_window2 = tk.Toplevel(self.root)  # Ventana para Usuario B
        DiffieHellmanGUI(dh_window2, "Usuario B")
    
    # Abre dos ventanas para simular RSA (Usuario A y B)
    def open_rsa(self):
        rsa_window = tk.Toplevel(self.root)  # Ventana para Usuario A
        RSAGUI(rsa_window, "Usuario A")
        rsa_window2 = tk.Toplevel(self.root)  # Ventana para Usuario B
        RSAGUI(rsa_window2, "Usuario B")
    
    # Abre dos ventanas para simular ElGamal (Usuario A y B)
    def open_elgamal(self):
        elgamal_window = tk.Toplevel(self.root)  # Ventana para Usuario A
        ElGamalGUI(elgamal_window, "Usuario A")
        elgamal_window2 = tk.Toplevel(self.root)  # Ventana para Usuario B
        ElGamalGUI(elgamal_window2, "Usuario B")
    
    # Abre dos ventanas para simular Rabin (Usuario A y B)
    def open_rabin(self):
        rabin_window = tk.Toplevel(self.root)  # Ventana para Usuario A
        RabinGUI(rabin_window, "Usuario A")
        rabin_window2 = tk.Toplevel(self.root)  # Ventana para Usuario B
        RabinGUI(rabin_window2, "Usuario B")

# Punto de entrada principal de la aplicación
if __name__ == "__main__":
    # Crea la ventana principal de Tkinter
    root = tk.Tk()
    # Instancia la aplicación principal
    app = MainApplication(root)
    # Inicia el bucle principal de la interfaz gráfica
    root.mainloop()