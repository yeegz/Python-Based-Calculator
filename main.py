import tkinter as tk

calculation = ""

def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)

def evaluate_calculation():
    global calculation
    try:
        result = str(eval(calculation))
        calculation = ""
        text_result.delete(1.0, "end")
        text_result.insert(1.0, result)
    except:
        clear_field()
        text_result.insert(1.0, "Error")

def clear_field():
    global calculation
    calculation= ""
    text_result.delete(1.0, "end")


root = tk.Tk()
root.geometry("600x350")

text_result = tk.Text(root, height=4, width=28, font=("Arial", 24))
text_result.grid(columnspan=25)

btn_1 = tk.Button(root, text="1", command=lambda: add_to_calculation(1), width=6, font=("Arial", 28))
btn_1.grid(row=2, column=1)
btn_2 = tk.Button(root, text="2", command=lambda: add_to_calculation(2), width=6, font=("Arial", 28))
btn_2.grid(row=2, column=3)
btn_3 = tk.Button(root, text="3", command=lambda: add_to_calculation(3), width=6, font=("Arial", 28))
btn_3.grid(row=2, column=5)
btn_4 = tk.Button(root, text="4", command=lambda: add_to_calculation(4), width=6, font=("Arial", 28))
btn_4.grid(row=3, column=1)
btn_5 = tk.Button(root, text="5", command=lambda: add_to_calculation(5), width=6, font=("Arial", 28))
btn_5.grid(row=3, column=3)
btn_6 = tk.Button(root, text="6", command=lambda: add_to_calculation(6), width=6, font=("Arial", 28))
btn_6.grid(row=3, column=5)
btn_7 = tk.Button(root, text="7", command=lambda: add_to_calculation(7), width=6, font=("Arial", 28))
btn_7.grid(row=4, column=1)
btn_8 = tk.Button(root, text="8", command=lambda: add_to_calculation(8), width=6, font=("Arial", 28))
btn_8.grid(row=4, column=3)
btn_9 = tk.Button(root, text="9", command=lambda: add_to_calculation(9), width=6, font=("Arial", 28))
btn_9.grid(row=4, column=5)
btn_0 = tk.Button(root, text="0", command=lambda: add_to_calculation(0), width=6, font=("Arial", 28))
btn_0.grid(row=5, column=3)
btn_plus = tk.Button(root, text="+", command=lambda: add_to_calculation("+"), width=10, font=("Arial", 28))
btn_plus.grid(row=2, column=25)
btn_minus = tk.Button(root, text="-", command=lambda: add_to_calculation("-"), width=10, font=("Arial", 28))
btn_minus.grid(row=3, column=25)
btn_div = tk.Button(root, text="/", command=lambda: add_to_calculation("/"), width=10, font=("Arial", 28))
btn_div.grid(row=5, column=25)
btn_mult = tk.Button(root, text="*", command=lambda: add_to_calculation("*"), width=10, font=("Arial", 28))
btn_mult.grid(row=4, column=25)
btn_open = tk.Button(root, text="(", command=lambda: add_to_calculation("("), width=6, font=("Arial", 28))
btn_open.grid(row=5, column=1)
btn_close = tk.Button(root, text=")", command=lambda: add_to_calculation(")"), width=6, font=("Arial", 28))
btn_close.grid(row=5, column=5)
btn_equals = tk.Button(root, text="=", command=evaluate_calculation, width=10, font=("Arial", 28))
btn_equals.grid(row=6, column=25)
btn_clear = tk.Button(root, text="C", command=clear_field, width=10, font=("Arial", 28))
btn_clear.grid(row=0, column=25)
root.mainloop()