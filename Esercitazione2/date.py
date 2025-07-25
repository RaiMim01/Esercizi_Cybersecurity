class Date: #Definizione di una classe
    """ Rappresenta una data del tipo gg/mm/aaaa """

    def __init__(self, day, month, year): # Costruttore della classe
        self.day = day
        self.month = month
        self.year = year  
    
    def __str__(self): # Metodo che restituisce una rappresentazione in stringa dell'oggetto
        # Restituisce la data nel formato gg/mm/aaaa
        return f"{self.day:02d}/{self.month:02d}/{self.year}" 
        # 02d indica che il numero deve essere stampato con almeno due cifre, 
        # aggiungendo uno zero a sinistra se necessario  
    
    def __eq__(self, other): # Metodo che restituisce True se due oggetti sono uguali
        # Restituisce True se la data è uguale a other
        return (
        self.day == other.day 
        and self.month == other.month 
        and self.year == other.year  
        )
    
    def to_tuple(self): # Metodo che restituisce una tupla con i valori della data
        return (self.year, self.month, self.day)

    def __lt__(self, value): # Metodo che restituisce True se la data è minore di value
        return self.to_tuple() < value.to_tuple()

    def __le__(self, value): # Metodo che restituisce True se la data è minore o uguale a value
        return self.to_tuple() <= value.to_tuple()
    



