from tkinter import *

# Dimensions de la fenêtre
root = Tk()
root.title("Calculatrice basique")
root.geometry("1200x780")
root.resizable(0, 0)

# Fonction de clic
def click_btn(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)

# Fonction clear : nettoiera l'input utilisateur
def clear_btn():
    global expression
    expression = ""
    input_text.set("")

# Fonction égal : donnera le résultat de l'opération
def equal_btn():
    global expression
    result = str(eval(expression))
    input_text.set(result)
    expression = ""

expression = ""

# Récupérer l'input utilisateur
input_text = StringVar()

# Input Frame
input_frame = Frame(root, width=700, height=10, bd=0)
input_frame.pack(side=TOP)

# Cadre pour l'input
input_field = Entry(input_frame, font=("Arial", 56, "bold"),
                textvariable=input_text, width=100, bg="#eee", bd=0, justify=RIGHT)
input_field.grid(row=0, column=0)
input_field.pack(ipady=20)

# Frame for Buttons
btns_frame = Frame(root, width=700, height=560)
btns_frame.pack()

# Ligne 1
clear = Button(btns_frame, text = "C", fg = "black", width = 128, height=12, bd=0,
            bg="#fff", cursor="hand2", command=lambda: clear_btn()
            ).grid(row=0, column=0, columnspan=3, padx=1, pady=1)

division = Button(btns_frame, text = "/", fg = "black", width = 40, height=12, bd=0,
            bg="#eee", cursor="hand2", command=lambda: click_btn("/")
            ).grid(row=0, column=3, padx=1, pady=1)

# Ligne 2
sept = Button(btns_frame, text = "7", fg = "black", width = 40, height=12, bd=0,
            bg="#fff", cursor="hand2", command=lambda: click_btn("7")
            ).grid(row=1, column=0, padx=1, pady=1)

huit = Button(btns_frame, text = "8", fg = "black", width = 40, height=12, bd=0,
            bg="#fff", cursor="hand2", command=lambda: click_btn("8")
            ).grid(row=1, column=1, padx=1, pady=1)

neuf = Button(btns_frame, text = "9", fg = "black", width = 40, height=12, bd=0,
            bg="#fff", cursor="hand2", command=lambda: click_btn("9")
            ).grid(row=1, column=2, padx=1, pady=1)

multiplication = Button(btns_frame, text = "*", fg = "black", width = 40, height=12, bd=0,
            bg="#eee", cursor="hand2", command=lambda: click_btn("*")
            ).grid(row=1, column=3, padx=1, pady=1)

# Ligne 3
quatre = Button(btns_frame, text = "4", fg = "black", width = 40, height=12, bd=0,
            bg="#fff", cursor="hand2", command=lambda: click_btn("4")
            ).grid(row=2, column=0, padx=1, pady=1)

cinq = Button(btns_frame, text = "5", fg = "black", width = 40, height=12, bd=0,
            bg="#fff", cursor="hand2", command=lambda: click_btn("5")
            ).grid(row=2, column=1, padx=1, pady=1)

six = Button(btns_frame, text = "6", fg = "black", width = 40, height=12, bd=0,
            bg="#fff", cursor="hand2", command=lambda: click_btn("6")
            ).grid(row=2, column=2, padx=1, pady=1)

soustraction = Button(btns_frame, text = "-", fg = "black", width = 40, height=12, bd=0,
            bg="#eee", cursor="hand2", command=lambda: click_btn("-")
            ).grid(row=2, column=3, padx=1, pady=1)

# Ligne 4
un = Button(btns_frame, text = "1", fg = "black", width = 40, height=12, bd=0,
            bg="#fff", cursor="hand2", command=lambda: click_btn("1")
            ).grid(row=3, column=0, padx=1, pady=1)

deux = Button(btns_frame, text = "2", fg = "black", width = 40, height=12, bd=0,
            bg="#fff", cursor="hand2", command=lambda: click_btn("2")
            ).grid(row=3, column=1, padx=1, pady=1)

trois = Button(btns_frame, text = "3", fg = "black", width = 40, height=12, bd=0,
            bg="#fff", cursor="hand2", command=lambda: click_btn("3")
            ).grid(row=3, column=2, padx=1, pady=1)

addition = Button(btns_frame, text = "+", fg = "black", width = 40, height=12, bd=0,
            bg="#eee", cursor="hand2", command=lambda: click_btn("+")
            ).grid(row=3, column=3, padx=1, pady=1)

# Ligne 5
zero = Button(btns_frame, text = "0", fg = "black", width = 84, height=12, bd=0,
            bg="#fff", cursor="hand2", command=lambda: click_btn("0")
            ).grid(row=4, column=0, columnspan=2, padx=1, pady=1)

point = Button(btns_frame, text = ".", fg = "black", width = 40, height=12, bd=0,
            bg="#fff", cursor="hand2", command=lambda: click_btn(".")
            ).grid(row=4, column=2, padx=1, pady=1)

egal = Button(btns_frame, text = "=", fg = "black", width = 40, height=12, bd=0,
            bg="#eee", cursor="hand2", command=lambda: equal_btn()
            ).grid(row=4, column=3, padx=1, pady=1)


root.mainloop()
