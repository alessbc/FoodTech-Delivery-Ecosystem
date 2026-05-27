import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_NAME = os.path.join(BASE_DIR, "foodtech_delivery.db")

class FoodTechDB:
    @staticmethod
    def inicializar():
        with sqlite3.connect(DB_NAME) as conn:
            cursor = conn.cursor()
            
            # Esquema Estrella (Dimensiones y Hechos)
            cursor.execute('''CREATE TABLE IF NOT EXISTS dim_platos (
                                id_plato INTEGER PRIMARY KEY, nombre_plato TEXT, categoria TEXT)''')
                                
            cursor.execute('''CREATE TABLE IF NOT EXISTS dim_cocinas (
                                id_cocina INTEGER PRIMARY KEY, zona TEXT, tipo_tecnologia TEXT)''')
                                
            cursor.execute('''CREATE TABLE IF NOT EXISTS fact_operaciones (
                                id_operacion INTEGER PRIMARY KEY AUTOINCREMENT,
                                id_plato INTEGER, id_cocina INTEGER,
                                costo_produccion REAL, precio_app REAL, fecha TEXT,
                                FOREIGN KEY(id_plato) REFERENCES dim_platos(id_plato),
                                FOREIGN KEY(id_cocina) REFERENCES dim_cocinas(id_cocina))''')
            
            # Data Seeding (Autogeneración de 5 registros mínimos)
            cursor.execute("SELECT COUNT(*) FROM dim_platos")
            if cursor.fetchone()[0] == 0:
                print("Iniciando despliegue de Base de Datos Food-Tech...")
                
                cursor.executemany("INSERT INTO dim_platos VALUES (?, ?, ?)", 
                                   [(101, "Burger Tech Pro", "Comida Rápida"), (102, "Sushi Cloud", "Asiática"), 
                                    (103, "Pizza Data", "Italiana"), (104, "Salad Bot", "Saludable"), 
                                    (105, "Tacos Delivery", "Mexicana")])
                                    
                cursor.executemany("INSERT INTO dim_cocinas VALUES (?, ?, ?)", 
                                   [(1, "Hub Chapinero", "Dark Kitchen 2.0"), (2, "Centro Norte", "Cocina Híbrida"), 
                                    (3, "Logística Sur", "Automatizada")])
                
                # Operaciones base
                operaciones = [
                    (101, 1, 8000, 25000, "2026-05-01"),
                    (102, 2, 12000, 35000, "2026-05-05"),
                    (103, 1, 10000, 28000, "2026-05-10"),
                    (104, 3, 5000, 18000, "2026-05-15"),
                    (105, 2, 6000, 20000, "2026-05-20")
                ]
                cursor.executemany("INSERT INTO fact_operaciones (id_plato, id_cocina, costo_produccion, precio_app, fecha) VALUES (?, ?, ?, ?, ?)", operaciones)
                
            conn.commit()