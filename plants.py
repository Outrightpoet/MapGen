from rand_storage import get_random_store_neg_1_1, get_random_store_0_10
from plant_id_getter import get_plant_id

class Plants:
    def __init__(self, id, plant_list, tile, area_map, parent=None):
        self.traits = 'placeholder'
        self.temperature_resistance = [4,6]
        self.nutrition_need = 2
        self.space_requirement = 5
        self.spread_size = 10
        self.spread_distance=1
        self.growth_rate = 1
        self.target_height = 10
        self.height = 0
        #land,semi_aquatic, aquatic
        self.water_affiliation = "land"
        self.status = "seed"
        self.id = id
        self.plant_list = plant_list
        self.tile = tile
        self.area_map = area_map

        #maybe some more unique skills
        self.toxicity = 0

    def die(self):
        self.tile.tile_space_avalible += self.space_requirement
        del self.tile.plants[self.id]
        del self.plant_list[self.id]

    def cycle(self):

        if self.status == "elder" and get_random_store_0_10() == 0:
            self.die()
        elif self.tile.soil_quality < self.nutrition_need:
            self.die()
        elif self.tile.temperature < self.temperature_resistance[0] or self.tile.temperature > self.temperature_resistance[1]:
            self.die()
        elif self.tile.classification == "ocean" and self.water_affiliation != "aquatic":
            self.die()
        elif self.tile.classification == "lake" and self.water_affiliation == "land":
            self.die()
        elif self.tile.water == False and self.water_affiliation != "land":
            self.die()

        if self.height < self.target_height:
            self.height += self.growth_rate
        else:
            self.height += (self.growth_rate/((self.height-self.target_height)+1))

        if self.status == "seed" and self.height > int(self.target_height / 2):
            self.status = "mature"
            self.tile.tile_space_avalible -= self.space_requirement
            self.space_requirement += self.space_requirement
        elif self.status == "mature" and self.height >= self.target_height:
            self.status = "elder"

        if self.status != "seed":
            self.spread()

    def spread(self):
        if get_random_store_0_10() == 0:
            row = self.tile.row
            col = self.tile.col
            if self.spread_distance == 1:
                for _ in range(0,self.spread_size):
                    row = row+get_random_store_neg_1_1()
                    col = col+get_random_store_neg_1_1()
                    try:
                        if self.area_map[row][col].tile_space_avalible > -20:
                            self.offspring(row, col)
                    except IndexError:
                        pass


    def offspring(self, row, col):
        plant_id = get_plant_id()
        offspring = Plants(plant_id, self.plant_list, self.area_map[row][col], self.area_map, self)
        self.plant_list[plant_id] = offspring
        self.area_map[row][col].plants[plant_id] = offspring
        self.area_map[row][col].tile_space_avalible -= offspring.space_requirement


