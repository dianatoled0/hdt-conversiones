import tkinter as tk
from tkinter import ttk, messagebox

def longitud(conversion, valor):
    if conversion == "Metros a Kilómetros":
        return valor / 1000, "kilómetros"
    elif conversion == "Pulgadas a Metros":
        return valor * 0.0254, "metros"

def tiempo(conversion, valor):
    if conversion == "Segundos a Minutos":
        return valor / 60, "minutos"
    elif conversion == "Horas a Días":
        return valor / 24, "días"

def masa(conversion, valor):
    if conversion == "Kilogramos a Gramos":
        return valor * 1000, "gramos"
    elif conversion == "Libras a Kilogramos":
        return valor * 0.453592, "kilogramos"

def realizar_conversion(funcion_conversion, caja, entrada, resultado_label):
    try:
        valor = float(entrada.get())
        conversion = caja.get()
        resultado, unidad = funcion_conversion(conversion, valor)
        resultado_label.config(text="Resultado: " + str(round(resultado, 4)) + " " + unidad)
    except ValueError:
        messagebox.showerror("Error", "Ingrese un número válido.")

def mostrar(hacer_conversion):
    ventana = tk.Tk()
    ventana.title("Conversión de " + hacer_conversion)
    ventana.geometry("500x400")
    ventana.configure(bg="#f7dc6f")

    if hacer_conversion == "Longitud":
        conversiones = ["Metros a Kilómetros", "Pulgadas a Metros"]
        funcion = longitud
    elif hacer_conversion == "Masa":
        conversiones = ["Kilogramos a Gramos", "Libras a Kilogramos"]
        funcion = masa
    elif hacer_conversion == "Tiempo":
        conversiones = ["Segundos a Minutos", "Horas a Días"]
        funcion = tiempo

    tk.Label(ventana, text="Conversión de " + hacer_conversion, bg="#f7dc6f", font=("Times", 14)).pack(pady=9)
    tk.Label(ventana, text="Seleccionar tipo de conversión: ", bg="#f7dc6f", font=("Times", 12)).pack()

    caja = ttk.Combobox(ventana, values=conversiones, state="readonly", font=("Times", 12))
    caja.pack(pady=5)
    caja.current(0)

    tk.Label(ventana, text="Valor a convertir: ", bg="#f7dc6f", font=("Times", 12)).pack()
    entrada = tk.Entry(ventana, font=("Times", 12))
    entrada.pack(pady=5)

    resultado_label = tk.Label(ventana, text="Resultado: ", bg="#f7dc6f", font=("Times ", 12))
    resultado_label.pack(pady=10)

    boton_conver = tk.Button(
        ventana,
        text="Convertir",
        command=lambda: realizar_conversion(funcion, caja, entrada, resultado_label),
        bg="#f1c40f", fg="black",
        font=("Times", 12)
    )
    boton_conver.pack(pady=10)

    ventana.mainloop()

def mostrar_menu():
    ventana_menu = tk.Tk()
    ventana_menu.title("Menú de Conversiones")
    ventana_menu.geometry("300x250")
    ventana_menu.configure(bg="#f7dc6f")

    tk.Label(ventana_menu, text="Selecciona una opción:", bg="#f7dc6f", font=("Times", 14)).pack(pady=15)

    tk.Button(ventana_menu, text="Conversión de Longitud", command=lambda: mostrar("Longitud"), font=("Times", 12), bg="#f9e79f").pack(pady=5)
    tk.Button(ventana_menu, text="Conversión de Masa", command=lambda: mostrar("Masa"), font=("Times", 12), bg="#f9e79f").pack(pady=5)
    tk.Button(ventana_menu, text="Conversión de Tiempo", command=lambda: mostrar("Tiempo"), font=("Times", 12), bg="#f9e79f").pack(pady=5)

    ventana_menu.mainloop()

mostrar_menu()

