import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

def agregar_tarea(event=None):
    """Agrega una nueva tarea a la lista."""
    tarea = entrada_tarea.get().strip()
    if tarea:
        lista_tareas.insert("", "end", values=(tarea, "Pendiente"), tags=("pendiente",))
        entrada_tarea.delete(0, tk.END)
    else:
        messagebox.showerror("Error", "Por favor, ingrese una tarea.")

def marcar_completada(event=None):
    """Marca la tarea seleccionada como completada."""
    seleccion = lista_tareas.selection()
    if seleccion:
        for item in seleccion:
            valores = lista_tareas.item(item, "values")
            if valores[1] != "Completada":
                lista_tareas.item(item, values=(valores[0], "Completada"), tags=("completada",))
    else:
        messagebox.showerror("Error", "Por favor, seleccione una tarea.")

def eliminar_tarea(event=None):
    """Elimina la tarea seleccionada de la lista."""
    seleccion = lista_tareas.selection()
    if seleccion:
        if messagebox.askyesno("Confirmación", "¿Está seguro de que desea eliminar esta tarea?"):
            for item in seleccion:
                lista_tareas.delete(item)
    else:
        messagebox.showerror("Error", "Por favor, seleccione una tarea.")

def cerrar_aplicacion(event=None):
    """Cierra la aplicación."""
    root.quit()

# Configuración de la ventana principal
root = tk.Tk()
root.title("Gestor de Tareas")
root.geometry("600x400")

# Frame principal
frame_principal = tk.Frame(root)
frame_principal.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Campo de entrada de tareas
tk.Label(frame_principal, text="Nueva Tarea:").grid(row=0, column=0, sticky=tk.W, pady=5)
entrada_tarea = tk.Entry(frame_principal, width=50)
entrada_tarea.grid(row=0, column=1, pady=5)
entrada_tarea.bind("<Return>", agregar_tarea)  # Enter para añadir tarea

# Treeview para mostrar las tareas
lista_tareas = ttk.Treeview(frame_principal, columns=("Tarea", "Estado"), show="headings", height=10)
lista_tareas.heading("Tarea", text="Tarea")
lista_tareas.heading("Estado", text="Estado")
lista_tareas.grid(row=1, column=0, columnspan=2, pady=10, sticky=tk.NSEW)

# Scrollbar para Treeview
scrollbar = ttk.Scrollbar(frame_principal, orient="vertical", command=lista_tareas.yview)
lista_tareas.configure(yscroll=scrollbar.set)
scrollbar.grid(row=1, column=2, sticky="ns")

# Colores para tareas completadas y pendientes
lista_tareas.tag_configure("pendiente", background="white")
lista_tareas.tag_configure("completada", background="#d1ffd1")  # Verde claro

# Frame para los botones
frame_botones = tk.Frame(frame_principal)
frame_botones.grid(row=2, column=0, columnspan=2, pady=10)

# Botones
tk.Button(frame_botones, text="Añadir Tarea", command=agregar_tarea).pack(side=tk.LEFT, padx=5)
tk.Button(frame_botones, text="Marcar como Completada", command=marcar_completada).pack(side=tk.LEFT, padx=5)
tk.Button(frame_botones, text="Eliminar Tarea", command=eliminar_tarea).pack(side=tk.LEFT, padx=5)
tk.Button(frame_botones, text="Salir", command=cerrar_aplicacion).pack(side=tk.LEFT, padx=5)

# Atajos de teclado adicionales
root.bind("<c>", marcar_completada)       # Presionar "c" o "C" para completar
root.bind("<C>", marcar_completada)
root.bind("<d>", eliminar_tarea)          # Presionar "d" o "D" para eliminar
root.bind("<D>", eliminar_tarea)
root.bind("<Delete>", eliminar_tarea)     # También tecla Delete para eliminar
root.bind("<Escape>", cerrar_aplicacion)  # Escape para salir

root.mainloop()