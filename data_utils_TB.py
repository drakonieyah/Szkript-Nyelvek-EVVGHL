class CustomHandler_TB:
    """Egy osztály, amely az adatokat dolgozza fel."""
    
    def __init__(self):
        self.data = []
    
    def add_data(self, item):
        """Hozzáad egy adott elemet a listához."""
        self.data.append(item)
    
    def get_data(self):
        """Minden elemet vissza ad a listából."""
        return self.data

def process_data_TB(data):
    """Saját függvény amely feldolgozza az adatokat és visszaadja minden elem hosszát."""
    return [len(str(item)) for item in data]
