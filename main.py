"""
Nombre Completo: Williams Tapia Caceres
Carrera: Informatica
Materia: Criptografía
Proyecto: Simulación Interactiva de Criptosistemas de Clave Pública
"""

import tkinter as tk
from tkinter import ttk
from diffie_hellman import DiffieHellmanGUI
from rsa import RSAGUI
from elgamal import ElGamalGUI
from rabin import RabinGUI

class MainApplication:
    def __init__(self, root):
        self.root = root
        self.root.title("Simulador de Criptosistemas")
        self.setup_ui()
        
    def setup_ui(self):
        # Frame principal
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Título
        ttk.Label(main_frame, text="Seleccione un Criptosistema", 
                 font=('Helvetica', 14, 'bold')).pack(pady=10)
        
        # Botones para cada módulo
        buttons = [
            ("Diffie-Hellman", self.open_diffie_hellman),
            ("RSA", self.open_rsa),
            ("ElGamal", self.open_elgamal),
            ("Rabin", self.open_rabin)
        ]
        
        for text, command in buttons:
            btn = ttk.Button(main_frame, text=text, command=command)
            btn.pack(fill=tk.X, pady=5)
    
    def open_diffie_hellman(self):
        dh_window = tk.Toplevel(self.root)
        DiffieHellmanGUI(dh_window, "Usuario A")
        dh_window2 = tk.Toplevel(self.root)
        DiffieHellmanGUI(dh_window2, "Usuario B")
    
    def open_rsa(self):
        rsa_window = tk.Toplevel(self.root)
        RSAGUI(rsa_window, "Usuario A")
        rsa_window2 = tk.Toplevel(self.root)
        RSAGUI(rsa_window2, "Usuario B")
    
    def open_elgamal(self):
        elgamal_window = tk.Toplevel(self.root)
        ElGamalGUI(elgamal_window, "Usuario A")
        elgamal_window2 = tk.Toplevel(self.root)
        ElGamalGUI(elgamal_window2, "Usuario B")
    
    def open_rabin(self):
        rabin_window = tk.Toplevel(self.root)
        RabinGUI(rabin_window, "Usuario A")
        rabin_window2 = tk.Toplevel(self.root)
        RabinGUI(rabin_window2, "Usuario B")

if __name__ == "__main__":
    root = tk.Tk()
    app = MainApplication(root)
    root.mainloop()