

class Tile:
    def __init__(self,row,col):
        self.row = row
        self.col = col
        self.topographic_level = -1
        self.water = False
        self.moisture = -1
        self.soil_quality = -1
        self.temperature = -1
        self.temperature_mod = -1
        self.classification = "none"
        self.classification_num = -1
        #
