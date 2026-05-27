import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import os
import sqlite3

class AppFoodTech:
    def __init__(self, root):
        self.root = root
        self.root.title("Food-Tech - Control de Márgenes")
        self.root.geometry("480x620")
        self.root.configure(bg="#111111")
        self.root.resizable(False, False)
        
        # Identidad Visual
        try:
            ruta_logo = os.path.join(os.path.dirname(os.path.abspath(__file__)), "logo.png")
            img = Image.open(ruta_logo).convert("RGB").resize((110, 110), Image.Resampling.LANCZOS)
            self.logo_img = ImageTk.PhotoImage(img)
            tk.Label(self.root, image=self.logo_img, bg="#111111").pack(pady=10)
        except Exception:
            tk.Label(self.root, text="🍔 CLOUD KITCHEN HUB", font=("Arial", 18, "bold"), bg="#111111", fg="#00FF7F").pack(pady=10)
        
        # Módulos CRUD
        frame_crud = tk.Frame(self.root, bg="#111111")
        frame_crud.pack(pady=10)
        
        tk.Button(frame_crud, text="➕ Registrar Venta App", bg="#00FF7F", fg="black", width=28, font=("Arial", 11, "bold"), command=self.crear).pack(pady=5)
        tk.Button(frame_crud, text="📖 Auditar Operaciones", bg="#00BFFF", fg="black", width=28, font=("Arial", 11, "bold"), command=self.leer).pack(pady=5)
        tk.Button(frame_crud, text="✏️ Modificar Precios", bg="#FFD700", fg="black", width=28, font=("Arial", 11, "bold"), command=self.actualizar).pack(pady=5)
        tk.Button(frame_crud, text="🗑️ Eliminar Transacción", bg="#FF3030", fg="white", width=28, font=("Arial", 11, "bold"), command=self.eliminar).pack(pady=5)
        
        tk.Label(self.root, text="Terminal de Inteligencia de Negocios", font=("Arial", 10, "italic"), bg="#111111", fg="#888888").pack(pady=15)
        tk.Button(self.root, text="📊 EJECUTAR POWER BI", bg="#4B0082", fg="white", font=("Arial", 12, "bold"), width=28, command=self.abrir_pbi).pack(pady=5)

    def ruta_db(self):
        return os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "Backend", "foodtech_delivery.db")

    def crear(self):
        ventana = tk.Toplevel(self.root)
        ventana.geometry("320x350")
        ventana.title("Nueva Venta en App")
        ventana.configure(bg="#222222")
        ventana.grab_set()
        
        tk.Label(ventana, text="ID Plato (101-105):", bg="#222222", fg="white").pack(pady=2)
        e_plato = tk.Entry(ventana, justify="center")
        e_plato.pack(pady=2)
        
        tk.Label(ventana, text="ID Cocina Oculta (1-3):", bg="#222222", fg="white").pack(pady=2)
        e_cocina = tk.Entry(ventana, justify="center")
        e_cocina.pack(pady=2)
        
        tk.Label(ventana, text="Costo de Producción ($):", bg="#222222", fg="white").pack(pady=2)
        e_costo = tk.Entry(ventana, justify="center")
        e_costo.pack(pady=2)
        
        tk.Label(ventana, text="Precio de Venta App ($):", bg="#222222", fg="white").pack(pady=2)
        e_precio = tk.Entry(ventana, justify="center")
        e_precio.pack(pady=2)
        
        tk.Label(ventana, text="Fecha (YYYY-MM-DD):", bg="#222222", fg="white").pack(pady=2)
        e_fec = tk.Entry(ventana, justify="center")
        e_fec.pack(pady=2)
        
        def guardar():
            try:
                with sqlite3.connect(self.ruta_db()) as conn:
                    conn.cursor().execute("INSERT INTO fact_operaciones (id_plato, id_cocina, costo_produccion, precio_app, fecha) VALUES (?, ?, ?, ?, ?)",
                                          (int(e_plato.get()), int(e_cocina.get()), float(e_costo.get()), float(e_precio.get()), e_fec.get()))
                    conn.commit()
                messagebox.showinfo("Sistema Operativo", "Transacción registrada en la red Food-Tech.", parent=ventana)
                ventana.destroy()
            except Exception as e:
                messagebox.showerror("Fallo del Sistema", str(e), parent=ventana)
                
        tk.Button(ventana, text="💾 Sincronizar", command=guardar, bg="#00FF7F", fg="black", font=("Arial", 10, "bold")).pack(pady=15)

    def leer(self):
        ventana = tk.Toplevel(self.root)
        ventana.geometry("700x300")
        ventana.title("Auditoría de Pedidos")
        ventana.grab_set()
        
        tabla = ttk.Treeview(ventana, columns=("ID", "Plato", "Zona", "Costo ($)", "Venta App ($)", "Fecha"), show="headings")
        for col in tabla["columns"]: tabla.heading(col, text=col)
        tabla.pack(fill="both", expand=True, padx=10, pady=10)
        
        try:
            with sqlite3.connect(self.ruta_db()) as conn:
                registros = conn.cursor().execute('''SELECT f.id_operacion, p.nombre_plato, c.zona, f.costo_produccion, f.precio_app, f.fecha 
                                                     FROM fact_operaciones f JOIN dim_platos p ON f.id_plato = p.id_plato 
                                                     JOIN dim_cocinas c ON f.id_cocina = c.id_cocina''').fetchall()
                for r in registros: tabla.insert("", tk.END, values=r)
        except Exception as e:
            messagebox.showerror("Error de Red", str(e))

    def actualizar(self):
        v = tk.Toplevel(self.root)
        v.geometry("300x200")
        v.configure(bg="#222222")
        tk.Label(v, text="ID de Operación a modificar:", bg="#222222", fg="white").pack(pady=5)
        e_id = tk.Entry(v, justify="center")
        e_id.pack(pady=5)
        tk.Label(v, text="Nuevo Precio en App ($):", bg="#222222", fg="white").pack(pady=5)
        e_precio = tk.Entry(v, justify="center")
        e_precio.pack(pady=5)
        
        def exec_act():
            try:
                with sqlite3.connect(self.ruta_db()) as conn:
                    cursor = conn.cursor()
                    cursor.execute("UPDATE fact_operaciones SET precio_app=? WHERE id_operacion=?", (float(e_precio.get()), int(e_id.get())))
                    if cursor.rowcount == 0: raise ValueError("ID no localizado en la base de datos.")
                    conn.commit()
                messagebox.showinfo("Éxito", "Márgenes recalculados en el sistema.", parent=v)
                v.destroy()
            except Exception as e: messagebox.showerror("Error", str(e), parent=v)
        tk.Button(v, text="Actualizar Datos", command=exec_act, bg="#FFD700", fg="black", font=("Arial", 10, "bold")).pack(pady=10)

    def eliminar(self):
        v = tk.Toplevel(self.root)
        v.geometry("300x150")
        v.configure(bg="#222222")
        tk.Label(v, text="ID Operación a ELIMINAR:", bg="#222222", fg="#FF3030").pack(pady=10)
        e_id = tk.Entry(v, justify="center")
        e_id.pack(pady=5)
        
        def exec_del():
            try:
                with sqlite3.connect(self.ruta_db()) as conn:
                    cursor = conn.cursor()
                    cursor.execute("DELETE FROM fact_operaciones WHERE id_operacion=?", (int(e_id.get()),))
                    if cursor.rowcount == 0: raise ValueError("ID no localizado.")
                    conn.commit()
                messagebox.showinfo("Purgado", "Transacción eliminada permanentemente.", parent=v)
                v.destroy()
            except Exception as e: messagebox.showerror("Error", str(e), parent=v)
        tk.Button(v, text="🗑️ Eliminar Registro", command=exec_del, bg="#FF3030", fg="white", font=("Arial", 10, "bold")).pack(pady=10)

    def abrir_pbi(self):
        try:
            os.startfile(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "FoodTech_Dashboard.pbix"))
        except Exception as e:
            messagebox.showerror("Error de Archivo", "Asegúrese de guardar Power BI como 'FoodTech_Dashboard.pbix'.")