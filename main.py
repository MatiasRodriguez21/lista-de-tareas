import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from tkcalendar import DateEntry
import json
from ttkthemes import ThemedTk
from PIL import Image, ImageTk
from datetime import datetime
import threading
import time

# Crear ventana principal con tema
root = ThemedTk(theme="arc")
root.title("Lista de Tareas")
root.geometry("1080x600")
root.configure(bg="#2c308e")  # Color de fondo de la ventana

# Definir colores y fuentes globales
BACKGROUND_COLOR = "#2c308e"
ENTRY_BACKGROUND = "#edebeb"
BUTTON_BACKGROUND = "black"
BUTTON_FOREGROUND = "black"
FONT = ("Arial", 12)
HEADER_FONT = ("Arial", 14, "bold")

# Aplicar estilos globales
style = ttk.Style()

# Estilo para los botones
style.configure("TButton", font=FONT, padding=10, background=BUTTON_BACKGROUND, foreground=BUTTON_FOREGROUND)
style.map("TButton",
          background=[("active", "#45a049")],
          foreground=[("active", BUTTON_FOREGROUND)])

# Estilo para las entradas de texto
style.configure("TEntry", font=FONT, fieldbackground=ENTRY_BACKGROUND)

# Estilo para los comboboxes
style.configure("TCombobox", font=FONT, fieldbackground=ENTRY_BACKGROUND)

# Estilo para las listas
style.configure("TListbox", font=FONT, background=ENTRY_BACKGROUND, foreground="black")

# Crear barra de menú
menubar = tk.Menu(root)
root.config(menu=menubar)

# Menú de archivo
file_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Archivo", menu=file_menu)
file_menu.add_command(label="Abrir", command=lambda: load_tasks())
file_menu.add_command(label="Guardar", command=lambda: save_tasks())
file_menu.add_separator()
file_menu.add_command(label="Salir", command=root.quit)

# Encabezado de la aplicación
header_label = tk.Label(root, text="Lista de Tareas", font=HEADER_FONT, bg=BACKGROUND_COLOR)
header_label.pack(pady=10)

# Crear marco para las tareas
frame = tk.Frame(root, bg=BACKGROUND_COLOR)
frame.pack(pady=10)

# Etiqueta para la entrada de tareas
task_label = tk.Label(frame, text="Nueva Tarea:", font=FONT, bg=BACKGROUND_COLOR)
task_label.pack(side=tk.LEFT, padx=10)

# Crear una caja de texto multilínea para ingresar tareas
task_entry = tk.Text(frame, width=20, height=0.3, font=FONT, bg=ENTRY_BACKGROUND, fg="grey")
task_entry.pack(side=tk.LEFT, padx=10)

# Funciones para manejar el texto de sugerencia
def add_placeholder(event):
    if task_entry.get("1.0", "end-1c") == "":
        task_entry.insert("1.0", "Escriba la tarea")
        task_entry.config(fg="grey")

def remove_placeholder(event):
    if task_entry.get("1.0", "end-1c") == "Escriba la tarea":
        task_entry.delete("1.0", "end")
        task_entry.config(fg="black")

# Añadir el texto de sugerencia inicialmente
task_entry.insert("1.0", "Escriba la tarea")

# Vincular eventos para manejar el texto de sugerencia
task_entry.bind("<FocusIn>", remove_placeholder)
task_entry.bind("<FocusOut>", add_placeholder)

# Función para redimensionar iconos
def resize_icon(file, size):
    image = Image.open(file)
    image = image.resize(size, Image.LANCZOS)
    return ImageTk.PhotoImage(image)

# Redimensionar iconos
icon_size = (24, 24)  # Aumentar el tamaño de los iconos
add_task_icon = resize_icon("logos/add_icon.png", icon_size)
complete_task_icon = resize_icon("logos/complete_icon.png", icon_size)
delete_task_icon = resize_icon("logos/delete_icon.png", icon_size)
save_tasks_icon = resize_icon("logos/save_icon.png", icon_size)
uncomplete_task_icon = resize_icon("logos/uncomplete_icon.png", icon_size)  # Icono para desmarcar tarea

# Etiqueta para la categoría
category_label = tk.Label(frame, text="Categoría:", font=FONT, bg=BACKGROUND_COLOR)
category_label.pack(side=tk.LEFT, padx=10)

# Añadir un combobox moderno para seleccionar categorías
categories = ["Trabajo", "Personal", "Urgente", "Otro"]
category_var = tk.StringVar(value="Seleccionar Categoría")
category_combobox = ttk.Combobox(frame, textvariable=category_var, values=categories, state="readonly", width=15)
category_combobox.pack(side=tk.LEFT, padx=10)

# Personalizar el combobox
style.configure("TCombobox", font=FONT, fieldbackground=ENTRY_BACKGROUND, background=ENTRY_BACKGROUND)
style.map("TCombobox", fieldbackground=[("readonly", ENTRY_BACKGROUND)])

# Etiqueta para la fecha límite
duedate_label = tk.Label(frame, text="Fecha Límite:", font=FONT, bg=BACKGROUND_COLOR)
duedate_label.pack(side=tk.LEFT, padx=10)

# Añadir un DateEntry moderno para seleccionar fecha límite
duedate_entry = DateEntry(
    frame,
    width=15,
    background="darkblue",
    foreground="white",
    borderwidth=2,
    date_pattern="yyyy-mm-dd",  # Formato de fecha: AAAA-MM-DD
    font=FONT,
)
duedate_entry.pack(side=tk.LEFT, padx=10)

# Personalizar el DateEntry
style.configure("DateEntry", font=FONT, background=ENTRY_BACKGROUND)

# Botón para agregar tarea
add_task_btn = ttk.Button(frame, text="Agregar Tarea", image=add_task_icon, compound=tk.LEFT, command=lambda: add_task(task_entry.get("1.0", tk.END).strip(), category_var.get(), duedate_entry.get()), style="TButton")
add_task_btn.pack(side=tk.LEFT)

# Lista para mostrar tareas
task_listbox = tk.Listbox(root, width=45, height=15, font=FONT, foreground="black", background=ENTRY_BACKGROUND, selectbackground=BUTTON_BACKGROUND)
task_listbox.pack(pady=20)

# Crear un marco para los botones de acciones
action_frame = tk.Frame(root, bg=BACKGROUND_COLOR)
action_frame.pack(pady=10)

# Función para agregar tarea
def add_task(task, category, duedate):
    if task != "" and category != "Seleccionar Categoría":
        task_with_details = f"[{category}] {task} (Fecha Límite: {duedate})"
        task_listbox.insert(tk.END, task_with_details)
        task_entry.delete("1.0", tk.END)
        category_var.set("Seleccionar Categoría")
        add_placeholder(None)  # Volver a mostrar el texto de sugerencia si la entrada está vacía

# Función para marcar tarea como completada
def complete_task():
    try:
        task_index = task_listbox.curselection()[0]
        task = task_listbox.get(task_index)
        if "✓" not in task:
            task_listbox.delete(task_index)
            task_listbox.insert(tk.END, f"{task} ✓")
    except IndexError:
        pass

# Función para desmarcar tarea
def uncomplete_task():
    try:
        task_index = task_listbox.curselection()[0]
        task = task_listbox.get(task_index)
        if "✓" in task:
            task = task.replace(" ✓", "")
            task_listbox.delete(task_index)
            task_listbox.insert(tk.END, task)
    except IndexError:
        pass

complete_task_btn = ttk.Button(action_frame, text="Tarea Completada", image=complete_task_icon, compound=tk.LEFT, command=complete_task, style="TButton")
complete_task_btn.pack(side=tk.LEFT, padx=5)

uncomplete_task_btn = ttk.Button(action_frame, text="Desmarcar Tarea", image=uncomplete_task_icon, compound=tk.LEFT, command=uncomplete_task, style="TButton")
uncomplete_task_btn.pack(side=tk.LEFT, padx=5)

# Función para eliminar tarea
def delete_task():
    try:
        task_index = task_listbox.curselection()[0]
        task_listbox.delete(task_index)
    except IndexError:
        pass

delete_task_btn = ttk.Button(action_frame, text="Eliminar Tarea", image=delete_task_icon, compound=tk.LEFT, command=delete_task, style="TButton")
delete_task_btn.pack(side=tk.LEFT, padx=5)

# Función para guardar tareas en un archivo
def save_tasks():
    tasks = task_listbox.get(0, tk.END)
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path:
        with open(file_path, "w") as file:
            for task in tasks:
                file.write(task + "\n")
        messagebox.showinfo("Guardar Tareas", "Tareas guardadas exitosamente")

save_tasks_btn = ttk.Button(action_frame, text="Guardar Tareas", image=save_tasks_icon, compound=tk.LEFT, command=save_tasks, style="TButton")
save_tasks_btn.pack(side=tk.LEFT, padx=5)

# Función para cargar tareas desde un archivo
def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
            for task in tasks:
                task_listbox.insert(tk.END, task)
    except FileNotFoundError:
        pass
    except json.JSONDecodeError:
        pass  # Si el archivo está vacío o no es un JSON válido, simplemente no cargar nada

load_tasks()

root.mainloop()