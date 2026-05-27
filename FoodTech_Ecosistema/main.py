import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import tkinter as tk
from Backend.database import FoodTechDB
from Frontend.app_foodtech import AppFoodTech

if __name__ == '__main__':
    FoodTechDB.inicializar()
    root = tk.Tk()
    app = AppFoodTech(root)
    root.mainloop() 