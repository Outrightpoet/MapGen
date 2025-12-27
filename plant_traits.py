from rand_storage import get_random_store_0_100, get_random_store_neg_10_10


class Plant_Traits():
    def __init__(self, plant, parent_traits=None, dose_speciate=True):

        self.plant = plant

        #self.diet_scale = getattr(parent_traits, "diet_scale", 0)

        if parent_traits != None:
            [self.fruit_growth,
             self.aquatic_afinity,
             self.plant_size,
             self.long_lived,
             self.spreading_range,
             self.spreading_batch,
             self.low_nutritinal_need,
             self.tuff_tissue,
             self.soft_tissue,
             self.heat_affinity,
             self.heat_weakness,
             self.cold_affinity,
             self.cold_weakness] = parent_traits.traits

        else:
            self.fruit_growth = 0
            self.aquatic_afinity = 0
            self.plant_size = 0
            self.long_lived = 0
            self.spreading_range = 0
            self.spreading_batch = 0
            self.low_nutritinal_need = 0
            self.tuff_tissue = 0
            self.soft_tissue = 0
            self.heat_affinity = 0
            self.heat_weakness = 0
            self.cold_affinity = 0
            self.cold_weakness = 0


        #not gonna add yet cuase i dont feel like it
        #self.toxicity = getattr(self, "toxicity", 0)

        self.traits = [self.fruit_growth,
                       self.aquatic_afinity,
                       self.plant_size,
                       self.long_lived,
                       self.spreading_range,
                       self.spreading_batch,
                       self.low_nutritinal_need,
                       self.tuff_tissue,
                       self.soft_tissue,
                       self.heat_affinity,
                       self.heat_weakness,
                       self.cold_affinity,
                       self.cold_weakness]

        if dose_speciate == True:
            self.speciate()

    def speciate(self):
        for trait in range(0,len(self.traits)):
            if get_random_store_0_100() == 0:
                if trait == 7 or trait == 9 or trait == 11 and self.traits[trait+1] == 0:
                    if trait == 8 or trait == 10 or trait == 12 and self.traits[trait-1] == 0:
                        self.plant.ready_to_split += 1
                        self.traits[trait] += get_random_store_neg_10_10()

                        if self.traits[trait] > 100:
                            self.traits[trait] = 99
                        elif self.traits[trait] < 0:
                            self.traits[trait] = 1
                elif trait < 7:
                    self.plant.ready_to_split += 1
                    self.traits[trait] += get_random_store_neg_10_10()

                    if self.traits[trait] > 100:
                        self.traits[trait] = 99
                    elif self.traits[trait] < 0:
                        self.traits[trait] = 1

        [self.fruit_growth,
        self.aquatic_afinity,
        self.plant_size,
        self.long_lived,
        self.spreading_range,
        self.spreading_batch,
        self.low_nutritinal_need,
        self.tuff_tissue,
        self.soft_tissue,
        self.heat_affinity,
        self.heat_weakness,
        self.cold_affinity,
        self.cold_weakness] = self.traits

    def get_stats(self):

        if self.aquatic_afinity <= 33:
            self.plant.water_affiliation = "land"
        elif self.aquatic_afinity <= 66:
            self.plant.water_affiliation = "semi-aquatic"
        else:
            self.plant.water_affiliation = "aquatic"

        self.plant.temperature_resistance[0] = 4 - (self.cold_affinity/25) - (self.tuff_tissue/50) + (self.cold_weakness/20) + (self.soft_tissue/40)
        self.plant.temperature_resistance[1] = 6 + (self.heat_affinity/25) - (self.tuff_tissue/50) + (self.heat_weakness/20) - (self.soft_tissue/40)
        self.plant.nutrition_need = 4
        self.plant.space_requirement = 10
        self.plant.spread_size = 10
        self.plant.spread_distance = 1
        self.plant.growth_rate = 1 + self.aquatic_afinity*100
        self.plant.target_height = 10 + self.aquatic_afinity*1000