from pickle import APPEND
import tkinter  as tk
from forex_python.converter import CurrencyRates


def CURRENCY_WINDOW():
    class ConverterApp:
        def __init__(self, root):
            self.root = root
            self.root.title("Currency Conversion")


            # Currency conversion widgets
            l1 = tk.Label(root, text="Currency Conversion",font="20", fg = "red",  bg= "yellow")
            l1.grid(row=1 , column= 9 , pady = 15)
            l2 = tk.Label(root,text="ENTER THE AMOUNT : ")
            l2.grid(row= 2 , column= 7 , columnspan=2, padx=15, pady=15, sticky="nsew")
            self.amount_entry = tk.Entry(root)
            self.amount_entry.grid(row= 2 , column= 9, padx=10, pady=15, sticky="nsew")
            self.currency_var = tk.StringVar()
            self.currency_var.set("Select")
            self.currency_menu = tk.OptionMenu(root, self.currency_var, "INR ---> EUR","EUR ---> INR" ,"INR ---> USD" , "USD ---> INR" )
            self.currency_menu.grid(row= 3 , column= 9, pady=15)
            currency_button = tk.Button(root, text="CONVERT", activebackground= "#78d6ff" ,  command=self.convert_currency)
            currency_button.grid(row= 4 , column=9, pady=15)
            self.currency_result_label = tk.Label(root, text="" , fg="#F62817" , font=("Times" , 15))
            self.currency_result_label.grid(row= 5 , column= 9 , padx= 10 , pady=15)



        def convert_currency(self):
            try:
                amount = float(self.amount_entry.get())
                target_currency = self.currency_var.get()

                if target_currency == "INR ---> EUR":
                    converted_amount = amount * 0.011
                    self.currency_result_label.config(text=f"Result: {converted_amount:.2f} Euro")
                    
                elif target_currency == "EUR ---> INR":
                    converted_amount = amount * 92.03
                    self.currency_result_label.config(text=f"Result: {converted_amount:.2f} Rupees")

                elif target_currency == "INR ---> USD":
                    converted_amount = amount * 0.012
                    self.currency_result_label.config(text=f"Result: {converted_amount:.2f} USD")

                elif target_currency == "USD ---> INR":
                    converted_amount = amount * 83.25
                    self.currency_result_label.config(text=f"Result: {converted_amount:.2f} INR")
            except ValueError:
                self.currency_result_label.config(text="ENTER THE VALID INPUT VALUE !!")

    if __name__ == "__main__":
        APPEND().mainloop()

        
    root = tk.Tk()
    root.title("CURRENCY CONVERTER")
    root.geometry("900x600")
    app = ConverterApp(root)
    root.mainloop()