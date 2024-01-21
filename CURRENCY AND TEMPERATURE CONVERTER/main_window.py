import tkinter as tk
import tkinter.font as font
import file_1
import file_2


root = tk.Tk()
root.title("converter")
root.geometry("600x500")

bottunfont = font.Font(size= 10 , weight= 'bold')

def tem_file():
    root.destroy()
    file_1.TEMPERATURE_WINDOW()



def con_file():
    root.destroy()
    file_2.CURRENCY_WINDOW()


tem_button = tk.Button(root , text='TEMPERATURE CONVERTER' , activebackground= '#78d6ff' , bd= 10 , command= tem_file , width= 25 , height= 2 )
tem_button.pack(pady= 30)

con_button = tk.Button(root , text='CURRENCY CONVERTER' , activebackground= '#78d6ff' , bd= 10 , command= con_file , width= 25 , height= 2 )
con_button.pack()



root.mainloop()