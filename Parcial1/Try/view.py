import tkinter as tk
from tkinter import messagebox
from login import *

def auto():
    user = entry_user.get()
    password = entry_password.get()
    
    user_obj = Verification(user,password)
    verifi = user_obj.veri()

ventana = tk.Tk()

tk.Label(ventana , text= "Usuario: ").grid(row=0, column=0)
entry_user = tk.Entry(ventana)
entry_user.grid(row=0, column=1)

tk.Label(ventana, text="Contraseña: ").grid(row=1, column=0)
entry_password = tk.Entry(ventana)
entry_password.grid(row=1, column=1)

button_verification = tk.Button(ventana, text="Iniciar sesion", command=auto)
button_verification.grid(row=3, columnspan=2)

ventana.mainloop()