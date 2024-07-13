import customtkinter
from stocklookup import stock_lookup

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("800x600")
root.title('Discounted Cash Flows Generator')



def button_clicked():
    stock_name = stock.get()
    stock_lookup(stock_name)
    #if stock_lookup(stock_name) == 'error':
        #error_label.configure(text='Symbol does not exist or has been delisted')
    #else:
        #error_label.configure(text='')







frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=0, padx=10,  expand=True)

lable = customtkinter.CTkLabel(master=frame, text="Enter Stock Name")
lable.pack(pady=12,padx=10)

stock = customtkinter.CTkEntry(master=frame, placeholder_text="ex. AAPL")
stock.pack(pady=12, padx=10)


button = customtkinter.CTkButton(master=frame, text="Submit", command=button_clicked)
button.pack(pady=12, padx=10)
error_label = customtkinter.CTkLabel(master=frame, text="")
error_label.pack(pady=12,padx=10)

root.mainloop()