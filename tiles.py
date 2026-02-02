

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
        self.tile_space_avalible = 0
        self.creatures = {}
        self.plants = {}
        #

    def cramp_death(self, un_active_plants):
        #print(f"{self.row}:{self.col} is considering cramp death with {self.tile_space_avalible}")
        if self.tile_space_avalible < 0:



            #print(f"{self.row}:{self.col} activates cramp death")
            sorted_keys = list(self.plants.keys())
            sorted_keys.sort(key=lambda x: self.plants[x].height)

            #print(sorted_keys)
            #print(self.plants)
            max = len(sorted_keys)
            i = 0
            plants = self.plants

            while self.tile_space_avalible < 0:

                plants[sorted_keys[i]].die(un_active_plants)
                i += 1

            self.plants=plants



        #print(f"{self.row}:{self.col} ending with {self.tile_space_avalible} after")
        #print()