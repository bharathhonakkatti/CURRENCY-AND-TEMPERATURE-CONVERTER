from pickle import APPEND
import tkinter as tk
from forex_python.converter import CurrencyRates


def TEMPERATURE_WINDOW():
    class ConverterApp:
        def __init__(self, root):
            self.root = root
            self.root.title("Temperature Conversion")

        # Temperature conversion widgets
            l1 = tk.Label(root, text="Temperature Conversion",font="20", fg = "red" , bg= "yellow" )
            l1.grid(row=1 , column= 9 , pady = 15)
            l2 = tk.Label(root,text="ENTER TEMPERATURE VALUE : ")
            l2.grid(row= 2 , column= 7 , columnspan=2, padx=15, pady=15, sticky="nsew")
            self.temp_entry = tk.Entry(root)
            self.temp_entry.grid(row= 2 , column= 9, padx=10, pady=15, sticky="nsew")
            self.temp_unit_var = tk.StringVar()
            self.temp_unit_var.set("Select")
            self.temp_unit_menu = tk.OptionMenu(root, self.temp_unit_var, "Celsius ----> Fahrenheit", "Fahrenheit ---> Celsius")
            self.temp_unit_menu.grid( row= 3 , column= 9, pady=15)
            temp_button = tk.Button(root, text="CONVERT", activebackground= "#78d6ff"  , command=self.convert_temperature)
            temp_button.grid( row= 4 , column=9, pady=15)
            self.temp_result_label = tk.Label(root, text="", fg="#F62817" , font=("Times" , 15))
            self.temp_result_label.grid(row= 5 , column= 9 , padx= 10 , pady=15)
            

        

        def convert_temperature(self):
            try:
                temperature = float(self.temp_entry.get())
                unit = self.temp_unit_var.get()

                if unit == "Celsius ----> Fahrenheit":
                    converted_temp = (temperature * 9/5) + 32                     

                    self.temp_result_label.config(text=f"Result: {converted_temp:.2f} Fahrenheit ")
                elif unit == "Fahrenheit ---> Celsius":
                    converted_temp = (temperature - 32) * 5/9
                    self.temp_result_label.config(text=f"Result: {converted_temp:.2f} Celsius")
            except ValueError:
                self.temp_result_label.config(text="ENTER THE VALID TEMPERATURE VALUE !!")

        


    if __name__ == "__main__":
        APPEND().mainloop()
        
    root = tk.Tk()
    root.title("TEMPERATURE CONVERTER")
    root.geometry("900x600")
    app = ConverterApp(root)
    root.mainloop()