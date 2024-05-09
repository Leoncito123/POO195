from tkinter import messagebox

class Verification :
        
    def veri(self, user, password):
        try: 
            self.__user == 'root'
            self.__password == 'root'
            return True
        except:
            print(messagebox.showerror('showeeror', 'Error en las credenciales, verifique'))
            
            