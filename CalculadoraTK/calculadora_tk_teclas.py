# =====================================================
# CALCULADORA CON TKINTER
# Autor: Grupo 2 - Informatorio 2025
# =====================================================

import tkinter as tk  # Librería para interfaces gráficas

# -----------------------------------------------------
# 1. CONFIGURACIÓN DE LA VENTANA PRINCIPAL
# -----------------------------------------------------
ventana = tk.Tk()
ventana.title("Calculadora")
ventana.resizable(False, False)

# -----------------------------------------------------
# 2. VARIABLE PARA MOSTRAR EL CONTENIDO EN LA PANTALLA
# -----------------------------------------------------
texto_pantalla = tk.StringVar()  # Contenido visible en la pantalla

# -----------------------------------------------------
# 3. VARIABLES PARA CAMBIAR EL SKIN
# -----------------------------------------------------
color_ventana = bg="#3A866E"
color_boton = bg="#479B82", 
color_texto = fg="#FFFFFF"
color_igual = "#6ac762"
color_c = bg="#f28b82"
color_flecha = "#ddb53e"

# Cambiar el color de fondo de la ventana
ventana.configure(bg=color_ventana)

# -----------------------------------------------------
# 4. CAJA DE TEXTO (PANTALLA)
# -----------------------------------------------------
# NOTA IMPORTANTE: usamos state="readonly" (solo lectura) para evitar que la Entry
# inserte caracteres automáticamente cuando el usuario presiona teclas.
# De esta forma controlamos por completo la inserción desde nuestro código,
# evitando duplicados.
pantalla = tk.Entry(
    ventana,
    textvariable=texto_pantalla,
    font=("Arial", 20),
    justify="right",
    bg="#f2f2f2",
    state="readonly" 
)
pantalla.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
pantalla.focus_set()  # El cursor está en la Entry (aunque sea readonly)

# -----------------------------------------------------
# 5. FUNCIONES
# -----------------------------------------------------
def agregar(valor):
    """Agrega un número, operador o paréntesis a la pantalla."""
    texto_pantalla.set(texto_pantalla.get() + valor)

def borrar_todo(event=None):                       # event=None: la función es para ambos casos: con botón o con tecla presionada
    """Borra todo el contenido (también puede ser llamado desde teclado)."""
    texto_pantalla.set("")

def borrar_ultimo(event=None):
    """Borra el último carácter (también puede ser llamado desde teclado)."""
    texto_actual = texto_pantalla.get()
    texto_pantalla.set(texto_actual[:-1])

def calcular(event=None):
    """Evalúa la operación escrita y muestra el resultado (también puede ser llamado desde teclado)."""
    try:                                          # try: se intentá ejecutar este bloque de código…
        resultado = eval(texto_pantalla.get())    # eval: Evalúa la operación escrita
        texto_pantalla.set(str(resultado))        # muestra el resultado
    except:                                       # except: si da error muestra un mensaje
        texto_pantalla.set("Error")

# -----------------------------------------------------
# 6. BOTONES #Listas - tuplas
# -----------------------------------------------------
botones = [
    ("(", 1, 0), (")", 1, 1), ("C", 1, 2), ("/", 1, 3),
    ("7", 2, 0), ("8", 2, 1), ("9", 2, 2), ("*", 2, 3),
    ("4", 3, 0), ("5", 3, 1), ("6", 3, 2), ("-", 3, 3),
    ("1", 4, 0), ("2", 4, 1), ("3", 4, 2), ("+", 4, 3),
    ("0", 5, 0), (".", 5, 1), ("←", 5, 2), ("=", 5, 3),
]

for (texto, fila, columna) in botones:
    if texto == "=":
        tk.Button(
            ventana, text=texto, width=5, height=2, font=("Arial", 16),
            command=calcular, bg=color_igual, fg=color_texto #comman: le dice al botón qué hacer cuando se presiona.
        ).grid(row=fila, column=columna, padx=5, pady=5)
    elif texto == "C":
        tk.Button(
            ventana, text=texto, width=5, height=2, font=("Arial", 16),
            command=borrar_todo, bg=color_c, fg=color_texto
        ).grid(row=fila, column=columna, padx=5, pady=5)
    elif texto == "←":
        tk.Button(
            ventana, text=texto, width=5, height=2, font=("Arial", 16),
            command=borrar_ultimo, bg=color_flecha, fg=color_texto
        ).grid(row=fila, column=columna, padx=5, pady=5)
    else:
        tk.Button(
            ventana, text=texto, width=5, height=2, font=("Arial", 16),
            command=lambda valor=texto: agregar(valor), bg=color_boton, fg=color_texto #lambda: cada botón llama a agregar(valor) con su número u operador correspondiente. 
        ).grid(row=fila, column=columna, padx=5, pady=5)

# -----------------------------------------------------
# 7. METODO TECLADO
# -----------------------------------------------------

# Manejamos las teclas especiales primero (Enter, Backspace, Escape, espacio)
ventana.bind("<Return>", calcular)         # Enter -> calcular
ventana.bind("<KP_Enter>", calcular)       # Enter del teclado numérico -> calcular
ventana.bind("<BackSpace>", borrar_ultimo) # Backspace -> borrar último
ventana.bind("<Escape>", borrar_todo)      # Esc -> borrar todo
ventana.bind("<space>", borrar_todo)       # Espacio -> borrar todo

# Función que procesa teclas imprimibles (números, operadores, paréntesis, punto)
def presionar_tecla(event):
    tecla = event.char                # event.char contiene el carácter que produjo la tecla.
    if tecla in "0123456789+-*/().":  # Solo si tecla está en el conjunto permitido, la agregamos.
        agregar(tecla)

# Vinculamos Key a presionar_tecla y se van insertando los caracteres a pantalla solo desde esta función
ventana.bind("<Key>", presionar_tecla) # Se agregan los caracteres definidos por teclado

# -----------------------------------------------------
# 8. BUCLE PRINCIPAL
# -----------------------------------------------------
ventana.mainloop()
