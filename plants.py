from rand_storage import get_random_store_neg_1_1, get_random_store_0_10
from plant_id_getter import get_plant_id
from plant_species_name_getter import get_plant_species_name
from plant_traits import Plant_Traits

class Plants:
    def __init__(self, id, plant_list, tile, area_map, plant_species, species_name, map_height, map_width, ready_to_split=0, parent=None):

        self.temperature_resistance = [4,6]
        self.nutrition_need = 2
        self.space_requirement = 10
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
        self.map_height = map_height
        self.map_width = map_width
        self.plant_species = plant_species
        self.species_name = species_name

        self.ready_to_split = ready_to_split

        #maybe some more unique skills
        self.toxicity = 0


        if parent == None:
            self.traits = Plant_Traits(self)
        else:
            self.traits = Plant_Traits(self, parent.traits)

        self.traits.get_stats()

        self.parent = "done"


    def check_and_split(self):
        if self.ready_to_split == 2:
            self.ready_to_split = 0
            new_name = get_plant_species_name()
            self.plant_species[new_name] = [1, {self.id: self}, [self.traits.fruit_growth,
                                                                self.traits.aquatic_afinity,
                                                                self.traits.plant_size,
                                                                self.traits.long_lived,
                                                                self.traits.spreading_range,
                                                                self.traits.spreading_batch,
                                                                self.traits.low_nutritinal_need,
                                                                self.traits.tuff_tissue,
                                                                self.traits.soft_tissue,
                                                                self.traits.heat_affinity,
                                                                self.traits.heat_weakness,
                                                                self.traits.cold_affinity,
                                                                self.traits.cold_weakness]]

            if len(self.plant_species[self.species_name][1]) == 1:
                del self.plant_species[self.species_name]
            else:
                self.plant_species[self.species_name][0] -= 1
                del self.plant_species[self.species_name][1][self.id]
            self.species_name = new_name
            #print(f"species ({new_name}) has been split")

    def die(self):
        self.tile.tile_space_avalible += self.space_requirement
        if self.plant_species[self.species_name][0] == 1:
            #print(f"{self.species_name} has gone extinct")
            del self.plant_species[self.species_name]
        else:
            self.plant_species[self.species_name][0] -= 1
            del self.plant_species[self.species_name][1][self.id]
        del self.tile.plants[self.id]
        del self.plant_list[self.id]

    def cycle(self, spread_requests):

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
        elif self.tile.water == False and self.water_affiliation == "ocean":
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
            self.tile.tile_space_avalible -= self.space_requirement
            self.space_requirement += self.space_requirement

        if self.status != "seed" and get_random_store_0_10() == 0:
            spread_requests.append(self)

    def resolve_spread(self):
        row = self.tile.row
        col = self.tile.col
        if self.spread_distance == 1:
            for _ in range(0, self.spread_size):
                row = row + get_random_store_neg_1_1()
                col = col + get_random_store_neg_1_1()
                if row >= 0 and row < self.map_height and col >= 0 and col < self.map_width:
                    if self.area_map[row][col].tile_space_avalible > -20:
                        self.offspring(row, col)


    def offspring(self, row, col):

        if self.species_name not in self.plant_species:
            self.plant_species[self.species_name] = [0, {}, [self.traits.fruit_growth,
                                                                self.traits.aquatic_afinity,
                                                                self.traits.plant_size,
                                                                self.traits.long_lived,
                                                                self.traits.spreading_range,
                                                                self.traits.spreading_batch,
                                                                self.traits.low_nutritinal_need,
                                                                self.traits.tuff_tissue,
                                                                self.traits.soft_tissue,
                                                                self.traits.heat_affinity,
                                                                self.traits.heat_weakness,
                                                                self.traits.cold_affinity,
                                                                self.traits.cold_weakness]]

        plant_id = get_plant_id()
        offspring = Plants(plant_id, self.plant_list, self.area_map[row][col], self.area_map, self.plant_species, self.species_name, self.map_height, self.map_width, self.ready_to_split, self)
        self.plant_list[plant_id] = offspring
        self.area_map[row][col].plants[plant_id] = offspring
        self.area_map[row][col].tile_space_avalible -= offspring.space_requirement
        self.plant_species[self.species_name][1][plant_id] = offspring
        self.plant_species[self.species_name][0] += 1
        offspring.check_and_split()


