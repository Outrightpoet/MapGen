from rand_storage import get_random_store_0_100, get_random_store_neg_10_10


class Plant_Traits():
    def __init__(self, plant, parent_traits=None, dose_speciate=True):

        self.plant = plant

        #self.diet_scale = getattr(parent_traits, "diet_scale", 0)

        self.fruit_growth = getattr(self, "fruit_growth", 0)
        self.aquatic_afinity = getattr(self, "aquatic_afinity", 0)
        self.plant_size = getattr(self, "plant_size", 0)
        self.long_lived = getattr(self, "long_lived", 0)
        self.spreading_range = getattr(self, "spreading_range", 0)
        self.spreading_batch = getattr(self, "spreading_batch", 10)
        self.low_nutritinal_need = getattr(self, "low_nutritinal_need", 0)

        self.tuff_tissue = getattr(self, "tuff_tissue", 0)
        self.soft_tissue = getattr(self, "soft_tissue", 0)

        self.heat_affinity = getattr(self, "heat_affinity", 0)
        self.heat_weakness = getattr(self, "heat_weakness", 0)

        self.cold_affinity = getattr(self, "cold_affinity", 0)
        self.cold_weakness = getattr(self, "cold_weakness", 0)

        #not gonna add yet cuase i dont feel like it
        self.toxicity = getattr(self, "toxicity", 0)

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

        self.plant.temperature_resistance = [4, 6]
        self.plant.nutrition_need = 2
        self.plant.space_requirement = 10
        self.plant.spread_size = 10
        self.plant.spread_distance = 1
        self.plant.growth_rate = 1
        self.plant.target_height = 10
        self.plant.height = 0