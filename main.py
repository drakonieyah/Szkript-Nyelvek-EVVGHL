#Indításhoz szükséges modulok ITT
import tkinter as tk
from random import choice, randint, shuffle
from data_utils_TB import CustomHandler_TB, process_data_TB
from imported_module import factorial

class App:
    #Program indulása ITT
    def __init__(self, root):
        self.root = root
        self.root.title("app")

        #Az ablak középre igazítása
        window_width = 400
        window_height = 200
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        position_top = (screen_height // 2) - (window_height // 2)
        position_right = (screen_width // 2) - (window_width // 2)
        self.root.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")

        #Random nevek generálásához használt adat
        self.names = ["Bálint", "János", "Napsugár", "Fanni", "Adél"]
        self.data_handler = CustomHandler_TB()

        #GUI Elemek
        self.label = tk.Label(root, text="Üdv a random név és adat megjelenítőben!")
        self.label.pack(pady=10)

        self.generate_button = tk.Button(root, text="Véletlenszerű nevek és adatok generálása", command=self.generate_data)
        self.generate_button.pack(pady=5)

        self.factorial_button = tk.Button(root, text="Véletlenszerű faktoriális generálása", command=self.generate_factorial)
        self.factorial_button.pack(pady=5)

        self.exit_button = tk.Button(root, text="Kilépés", command=root.quit)
        self.exit_button.pack(pady=5)

    def generate_data(self):
        """Random név választása és tömbbeli pozíció megadása."""
        shuffle(self.names)  #A nevek listájának megkeverése
        random_name = choice(self.names)  #A lista egy elemének (név) kiválasztása
        self.data_handler.add_data(random_name)
        processed = process_data_TB(self.data_handler.get_data())
        self.label.config(text=f"Név: {random_name} | Nevek hossza: {processed}")

    def generate_factorial(self):
        """Random szám faktoriálisának a megjelenítése"""
        number = randint(1, 10)
        result = factorial(number)
        self.label.config(text=f"{number}! = {result}")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
