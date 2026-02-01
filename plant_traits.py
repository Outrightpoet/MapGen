from rand_storage import get_random_store_0_100, get_random_store_neg_10_10, get_random_store_0_12
import numpy as np
import math

class Plant_Traits():
    def __init__(self, plant, parent_traits=None, dose_speciate=True):

        self.plant = plant

        # Number of traits
        N = 13

        if parent_traits is not None:

            # Fast NumPy copy
            self.traits = parent_traits.traits.copy()

        else:
            # Initialize all traits to 0
            self.traits = np.zeros(N, dtype=np.float32)

        # Optional: unpack if you still need named access
        (
            self.fruit_growth,
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
            self.cold_weakness
        ) = self.traits

        if dose_speciate:
            if get_random_store_0_100() < 10:
                self.speciate()

    def speciate(self):

        self.plant.ready_to_split += 1

        ran_trait = get_random_store_0_12()

        if ran_trait > 6:
            if ran_trait % 2 == 0:
                if self.traits[ran_trait-1] != 0:
                    ran_trait -= 1
            else:
                if self.traits[ran_trait+1] != 0:
                    ran_trait += 1

        self.traits[ran_trait] += get_random_store_neg_10_10()

        if self.traits[ran_trait] > 100:
            self.traits[ran_trait] = 99
        elif self.traits[ran_trait] < 0:
            self.traits[ran_trait] = 1


    def get_stats(self):

        plant = self.plant



        if plant.parent != None and plant.ready_to_split == plant.parent.ready_to_split:
            parent = plant.parent
            plant.water_affiliation = parent.water_affiliation
            plant.temperature_resistance[0] = parent.temperature_resistance[0]
            plant.temperature_resistance[1] = parent.temperature_resistance[1]
            plant.nutrition_need = parent.nutrition_need
            plant.init_space_requirement = parent.init_space_requirement
            plant.space_requirement = parent.init_space_requirement
            plant.spread_size = parent.spread_size
            plant.spread_distance = parent.spread_distance
            plant.growth_rate = parent.growth_rate
            plant.target_height = parent.target_height

        else:
            if self.aquatic_afinity <= 33:
                plant.water_affiliation = "land"
            elif self.aquatic_afinity <= 66:
                plant.water_affiliation = "semi-aquatic"
            else:
                plant.water_affiliation = "aquatic"

            plant.temperature_resistance[0] = math.floor(4 - (self.cold_affinity/25) - (self.tuff_tissue/50) + (self.cold_weakness/20) + (self.soft_tissue/40))
            plant.temperature_resistance[1] = math.ceil(6 + (self.heat_affinity/25) + (self.tuff_tissue/50) - (self.heat_weakness/20) - (self.soft_tissue/40))
            plant.nutrition_need = 4 - (self.low_nutritinal_need/50) + (self.tuff_tissue/50) - (self.soft_tissue/50) + (self.fruit_growth/25)
            plant.init_space_requirement = 10 + (self.plant_size/10) + (self.tuff_tissue/10) - (self.soft_tissue/10)
            plant.space_requirement = plant.init_space_requirement
            plant.spread_size = int(10 + (self.spreading_batch/5))
            plant.spread_distance = int(1 + (self.spreading_range/33))
            plant.growth_rate = ((1 + (self.soft_tissue/33) + (self.cold_weakness/33) + (self.heat_weakness/33) - (self.cold_affinity/20) - (self.heat_affinity/20)) / (1 + self.tuff_tissue/50)) / (1 + self.long_lived/50)
            plant.target_height = 10 + (self.plant_size/10) + (self.tuff_tissue/10) - (self.heat_affinity/10)