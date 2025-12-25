

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
        self.tile_space_avalible = self.soil_quality*10
        self.creatures = {}
        self.plants = {}
        #

    def cramp_death(self):
        if self.tile_space_avalible < 0:

            # 1. Sort plants by height (shortest first)
            plants_by_height = sorted(
                self.plants.values(),
                key=lambda plant: plant.height
            )

            # 2. Index to track which plant to kill next
            i = 0

            # 3. Kill plants until space is available
            while self.tile_space_avalible >= 0:
                plant = plants_by_height[i]

                # Plant handles its own cleanup
                plant.die()

                # Optional: remove from tile dictionary if not handled in die()
                for key, value in list(self.plants.items()):
                    if value is plant:
                        del self.plants[key]
                        break

                i += 1

