import tkinter as tk
import math

# Variable global para la memoria
memoria = 0

def evaluar():
    try:
        expresion = entrada.get()
        resultado = eval(expresion, {"__builtins__": None}, vars(math))
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, str(resultado))
    except:
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, "Error")

def presionar(valor):
    entrada.insert(tk.END, valor)

def limpiar():
    entrada.delete(0, tk.END)

def memoria_guardar():
    global memoria
    try:
        memoria = float(entrada.get())
    except:
        memoria = 0

def memoria_recuperar():
    entrada.insert(tk.END, str(memoria))

def memoria_sumar():
    global memoria
    try:
        memoria += float(entrada.get())
    except:
        pass

def memoria_restar():
    global memoria
    try:
        memoria -= float(entrada.get())
    except:
        pass

def factorial():
    try:
        valor = int(entrada.get())
        resultado = math.factorial(valor)
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, str(resultado))
    except:
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, "Error")

# Ventana principal
ventana = tk.Tk()
ventana.title("🧮 Calculadora Científica")
ventana.configure(bg="#1e1e1e")
ventana.resizable(False, False)

entrada = tk.Entry(
    ventana, width=30, font=("Consolas", 20),
    fg="#00ffcc", bg="#2d2d2d", insertbackground="white",
    borderwidth=0, relief="flat", justify="right"
)
entrada.grid(row=0, column=0, columnspan=5, pady=20, padx=10)

# Lista de botones: texto mostrado y función asociada
botones = [
    ("MC", memoria_guardar), ("MR", memoria_recuperar), ("M+", memoria_sumar), ("M-", memoria_restar), ("C", limpiar),
    ("(", lambda: presionar("(")), (")", lambda: presionar(")")), ("%", lambda: presionar("/100")), ("√", lambda: presionar("sqrt(")), ("x²", lambda: presionar("**2")),
    ("7", lambda: presionar("7")), ("8", lambda: presionar("8")), ("9", lambda: presionar("9")), ("/", lambda: presionar("/")), ("x", lambda: presionar("*")),
    ("4", lambda: presionar("4")), ("5", lambda: presionar("5")), ("6", lambda: presionar("6")), ("-", lambda: presionar("-")), ("+/-", lambda: presionar("-")),
    ("1", lambda: presionar("1")), ("2", lambda: presionar("2")), ("3", lambda: presionar("3")), ("+", lambda: presionar("+")), ("." , lambda: presionar(".")),
    ("0", lambda: presionar("0")), ("π", lambda: presionar("pi")), ("e", lambda: presionar("e")), ("exp", lambda: presionar("exp(")), ("!", factorial),
    ("sin", lambda: presionar("sin(")), ("cos", lambda: presionar("cos(")), ("tan", lambda: presionar("tan(")), ("log", lambda: presionar("log10(")), ("ln", lambda: presionar("log(")),
    ("=", evaluar)
]

# Crear los botones en la interfaz
fila = 1
col = 0
for texto, comando in botones:
    ancho = 6 if texto != "=" else 30
    colspan = 1 if texto != "=" else 5
    tk.Button(
        ventana, text=texto, width=ancho, height=2, font=("Arial", 12, "bold"),
        bg="#444" if texto != "=" else "#2ecc71", fg="white", activebackground="#666",
        command=comando, relief="flat"
    ).grid(row=fila, column=col, columnspan=colspan, padx=2, pady=2)
    col += 1
    if col >= 5:
        col = 0
        fila += 1

ventana.mainloop()