class Color:        #Color object in RGB 

    def __init__(self, red: int, green: int, blue: int):
        self.red = red
        self.green = green
        self.blue = blue
    
    # Returns a dictionary of the color attributes
    def to_dict(self):
        return {"red": self.red,"green": self.green,"blue": self.blue}
    
    # Returns a tuple of the color attributes
    def tuple(self):
        return (self.red, self.green,self.blue)
    
    # Returns a list of the color attributes for a row in a CSV file
    def csv_row(self):
        return [self.red, self.green, self.blue]