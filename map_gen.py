from time import sleep as s
from rand_storage import get_random_store_1_3, get_random_store_neg_1_1, get_random_store_0_10, get_random_store_0_6, get_random_store_neg_5_5
import random
from tiles import Tile

class Map:
    def __init__(self):
        self.height = 100
        self.width = 100
        self.water_level = 4
        self.temperature_modifier = 0
        self.area_map = []

        self.BIOME_IDS = {
        "ocean": 0,
        "lake": 1,
        "swamp": 2,
        "desert": 3,
        "grassland": 4,
        "temperate_forest": 5,
        "rainforest": 6,
        "taiga": 7,
        "tundra": 8,
        "mountain": 9,
        "alpine": 10,
        "rocky_peak": 11,
        "badlands": 12,
        "farmland": 13,
    }

        #LIST CREATION

        for h in range(0,self.height):
            self.area_map.append([])
            for w in range(0,self.width):
                self.area_map[h].append(Tile(h,w))

        self.topograpical_gen()
        self.soil_quality_gen()
        self.temp_update('b')
        self.update_water_level()

    #TOPOGRAPICAL GEN

    def topograpical_gen(self):

        set=1
        counter1=0
        counter2=0

        self.area_map[0][0].topographic_level = random.randint(0,10)

        while set < self.height*2:
            counter1 = set
            run = counter1
            if run > self.height:
                run = self.height
            for i in range(0,run+1):
                #this if, elif, else statment trys to grab both nehiboring cell toporaphic levels or one based on if it is on one of the walls either counter 1,2 == 0
                if counter2 == 0:
                    try:
                        neighbor1 = self.area_map[counter1-1][0].topographic_level
                    except IndexError:
                        neighbor1 = -1
                    neighbor2 = -1
                elif counter1 == 0:
                    try:
                        neighbor2 = self.area_map[0][counter2-1].topographic_level
                    except IndexError:
                        neighbor2 = -1
                    neighbor1 = -1
                else:
                    try:
                        neighbor1 = self.area_map[counter1-1][counter2].topographic_level
                    except IndexError:
                        neighbor1 = -1
                    try:
                        neighbor2 = self.area_map[counter1][counter2-1].topographic_level
                    except IndexError:
                        neighbor2 = -1

                if counter1 < self.height and counter2 < self.width:
                    #makes sure the cell exists
                    if neighbor1 != -1 and neighbor2 != -1:
                        #assigns the topographic level based on neighbors
                        self.area_map[counter1][counter2].topographic_level = round((neighbor1 + neighbor2)/2) + get_random_store_neg_1_1()
                    else:
                        rand = get_random_store_1_3()
                        if neighbor1 != -1:
                            neighbor_val = neighbor1
                        else:
                            neighbor_val = neighbor2

                        if rand == 1:
                            self.area_map[counter1][counter2].topographic_level = neighbor_val -1
                        elif rand == 2:
                            self.area_map[counter1][counter2].topographic_level = neighbor_val
                        else:
                            self.area_map[counter1][counter2].topographic_level = neighbor_val + 1

                    if get_random_store_0_10() == 0:
                        #pulls the level more central
                        if self.area_map[counter1][counter2].topographic_level > 5:
                            pull = -int((self.area_map[counter1][counter2].topographic_level-5)/2.5)
                            self.area_map[counter1][counter2].topographic_level += pull
                        elif self.area_map[counter1][counter2].topographic_level < 5:
                            pull = int((5-self.area_map[counter1][counter2].topographic_level)/2.5)
                            self.area_map[counter1][counter2].topographic_level += pull

                    if self.area_map[counter1][counter2].topographic_level < 0:
                        self.area_map[counter1][counter2].topographic_level = 0
                    elif self.area_map[counter1][counter2].topographic_level > 10:
                        self.area_map[counter1][counter2].topographic_level = 10

                counter1 -= 1
                counter2 += 1
            set += 1
            counter1 = 0
            counter2 = 0

        #SOIL QUALITY GEN

    def soil_quality_gen(self):
        set=1
        counter1=0
        counter2=0

        self.area_map[0][0].soil_quality = random.randint(0,10)

        while set < self.height*2:
            counter1 = set
            run = counter1
            if run > self.height:
                run = self.height
            for i in range(0,run+1):
                if counter2 == 0:
                    try:
                        neighbor1 = self.area_map[counter1-1][0].soil_quality
                    except IndexError:
                        neighbor1 = -1
                    neighbor2 = -1
                elif counter1 == 0:
                    try:
                        neighbor2 = self.area_map[0][counter2-1].soil_quality
                    except IndexError:
                        neighbor2 = -1
                    neighbor1 = -1
                else:
                    try:
                        neighbor1 = self.area_map[counter1-1][counter2].soil_quality
                    except IndexError:
                        neighbor1 = -1
                    try:
                        neighbor2 = self.area_map[counter1][counter2-1].soil_quality
                    except IndexError:
                        neighbor2 = -1

                if counter1 < self.height and counter2 < self.width:
                    if neighbor1 != -1 and neighbor2 != -1:
                        self.area_map[counter1][counter2].soil_quality = round((neighbor1 + neighbor2)/2) + get_random_store_neg_1_1()
                    else:
                        rand = get_random_store_1_3()
                        if neighbor1 != -1:
                            neighbor_val = neighbor1
                        else:
                            neighbor_val = neighbor2

                        if rand == 1:
                            self.area_map[counter1][counter2].soil_quality = neighbor_val -1
                        elif rand == 2:
                            self.area_map[counter1][counter2].soil_quality = neighbor_val
                        else:
                            self.area_map[counter1][counter2].soil_quality = neighbor_val + 1

                    if get_random_store_0_10() < 2:
                        # pulls the level more central
                        if self.area_map[counter1][counter2].soil_quality > 5:
                            pull = -int((self.area_map[counter1][counter2].soil_quality - 5) / 2.5)
                            self.area_map[counter1][counter2].soil_quality += pull
                        elif self.area_map[counter1][counter2].soil_quality < 5:
                            pull = int((5 - self.area_map[counter1][counter2].soil_quality) / 2.5)
                            self.area_map[counter1][counter2].soil_quality += pull

                    if self.area_map[counter1][counter2].soil_quality < 0:
                        self.area_map[counter1][counter2].soil_quality = 0
                    elif self.area_map[counter1][counter2].soil_quality > 10:
                        self.area_map[counter1][counter2].soil_quality = 10

                    self.area_map[counter1][counter2].tile_space_avalible = (self.area_map[counter1][counter2].soil_quality * 10)+30

                counter1 -= 1
                counter2 += 1
            set += 1
            counter1 = 0
            counter2 = 0

    # TEMP GEN

    def temp_update(self, decider='b'):
        set = 1
        counter1 = 0
        counter2 = 0

        self.area_map[0][0].temperature = random.randint(0, 10)

        if decider == 'r' or decider == 'b':
            while set < self.height * 2:
                counter1 = set
                run = counter1
                if run > self.height:
                    run = self.height
                for i in range(0, run + 1):
                    if counter2 == 0:
                        try:
                            neighbor1 = self.area_map[counter1 - 1][0].temperature
                        except IndexError:
                            neighbor1 = -1
                        neighbor2 = -1
                    elif counter1 == 0:
                        try:
                            neighbor2 = self.area_map[0][counter2 - 1].temperature
                        except IndexError:
                            neighbor2 = -1
                        neighbor1 = -1
                    else:
                        try:
                            neighbor1 = self.area_map[counter1 - 1][counter2].temperature
                        except IndexError:
                            neighbor1 = -1
                        try:
                            neighbor2 = self.area_map[counter1][counter2 - 1].temperature
                        except IndexError:
                            neighbor2 = -1

                    if counter1 < self.height and counter2 < self.width:
                        if neighbor1 != -1 and neighbor2 != -1:
                            self.area_map[counter1][counter2].temperature = round((neighbor1 + neighbor2) / 2) + get_random_store_neg_1_1()
                        else:
                            rand = get_random_store_1_3()
                            if neighbor1 != -1:
                                neighbor_val = neighbor1
                            else:
                                neighbor_val = neighbor2

                            if rand == 1:
                                self.area_map[counter1][counter2].temperature = neighbor_val - 1
                            elif rand == 2:
                                self.area_map[counter1][counter2].temperature = neighbor_val
                            else:
                                self.area_map[counter1][counter2].temperature = neighbor_val + 1

                        if get_random_store_0_10() < 2:
                            # pulls the level more central
                            if self.area_map[counter1][counter2].temperature > 5:
                                pull = -int((self.area_map[counter1][counter2].temperature - 5) / 2.5)
                                self.area_map[counter1][counter2].temperature += pull
                            elif self.area_map[counter1][counter2].temperature < 5:
                                pull = int((5 - self.area_map[counter1][counter2].temperature) / 2.5)
                                self.area_map[counter1][counter2].temperature += pull

                        if self.area_map[counter1][counter2].temperature < 0:
                            self.area_map[counter1][counter2].temperature = 0
                        elif self.area_map[counter1][counter2].temperature > 10:
                            self.area_map[counter1][counter2].temperature = 10

                    counter1 -= 1
                    counter2 += 1
                set += 1
                counter1 = 0
                counter2 = 0

        if decider == 'm' or decider == 'b' or decider == 'r':
            for row in self.area_map:
                for cell in row:
                    cell.temperature_mod = cell.temperature
                    """if cell.topographic_level > 5:
                        cell.temperature_mod -= int(cell.topographic_level / 2)
                    elif cell.topographic_level < 5:
                        cell.temperature_mod += int(cell.topographic_level / 2)
                    if cell.moisture > 5:
                        pass
                        #cell.temperature_mod -= int(cell.moisture / 4)
                    else:
                        pass
                        #cell.temperature_mod += int((10 - cell.moisture) / 4)"""

                    cell.temperature_mod += self.temperature_modifier

                    if cell.temperature_mod < 0:
                        cell.temperature_mod = 0
                    elif cell.temperature_mod > 10:
                        cell.temperature_mod = 10

        self.classify_map()

    # BIOME CLASSIFICATION

    def classify_cell(self, cell):
        topo = cell.topographic_level  # 0–10
        moist = cell.moisture  # 0–10
        soil = cell.soil_quality  # 0–10
        temp = cell.temperature_mod  # 0–10

        # --- WATER ---
        if cell.water:
            if topo != self.water_level:
                return "ocean"
            else:
                return "lake"

        # --- COLD BIOMES ---
        if temp <= 3:
            if topo >= 8:
                return "rocky_peak" if soil <= 3 else "alpine"
            if moist <= 3:
                return "tundra"
            return "taiga"

        # --- HOT BIOMES ---
        if temp >= 7:
            if moist <= 3:
                return "desert"
            if moist >= 7:
                return "rainforest"
            return "grassland"

        # --- TEMPERATE BIOMES ---
        if topo >= 8:
            return "mountain"

        if moist >= 7:
            return "temperate_forest"

        if soil >= 7 and 4 <= moist <= 6:
            return "farmland"

        if moist <= 3:
            return "badlands"

        return "grassland"

    def classify_map(self):
        for row in self.area_map:
            for cell in row:
                biome = self.classify_cell(cell)
                cell.classification = biome
                cell.classification_num = self.BIOME_IDS[biome]

    #MOISTURE AREA

    def check_neighbor_for_land(self, row, col):

        for col1 in range(col - 1, col + 2):
            for row1 in range(row - 1, row + 2):
                try:
                    if self.area_map[row1][col1].water == False:
                        return True
                except IndexError:
                    pass

    def spread_moisture(self, row, col):
        if self.check_neighbor_for_land(row, col):
            for row1 in range(-20,21):
                for col1 in range(-20,21):
                    dis = (abs(row1*row1) + abs(col1*col1))/10
                    ran = get_random_store_neg_5_5()
                    if dis <= 20 + ran:
                        try:
                            moisture_value = round((10-((dis)/2) - (self.area_map[row+row1][col+col1].topographic_level)/3))

                            if self.area_map[row+row1][col+col1].moisture < moisture_value:
                                self.area_map[row+row1][col+col1].moisture = moisture_value
                        except IndexError:
                            pass

    def update_moisture(self):

        for row in self.area_map:
            for cell in row:
                cell.moisture = 0

        for row in self.area_map:
            for cell in row:
                if cell.water == True:
                    cell.moisture = 10
                    self.spread_moisture(cell.row, cell.col)

        for row in self.area_map:
            for cell in row:
                if cell.moisture == -1:
                    cell.moisture = 0

        self.temp_update('m')

    #WATER AREA

    def check_neighbor_for_water(self, row, col):
        if row == 0 or col == 0 or row == self.height - 1 or col == self.width - 1:
            return True

        for col1 in range(col - 1, col + 2):
            for row1 in range(row - 1, row + 2):
                if self.area_map[row1][col1].water == True:
                    return True

    def update_water_level(self):

        for row in self.area_map:
            for cell in row:
                if cell.water == True and cell.topographic_level > self.water_level:
                    cell.water = False

        """counter1 = 0

        for i in range(0,int(self.height/2)):

            for cell in (self.area_map[counter1]):
                if cell.topographic_level <= self.water_level and self.check_neighbor_for_water(cell.row, cell.col):
                    cell.water = True


            for i2 in range(counter1+1, self.height-(counter1+1)):
                if self.area_map[i2][counter1].topographic_level <= self.water_level and self.check_neighbor_for_water(i2, (counter1+1)):
                    cell.water = True

                elif self.area_map[i2][self.width-(counter1+1)].topographic_level <= self.water_level and self.check_neighbor_for_water(i2, (self.width-(counter1+1))):
                    cell.water = True


            for col, cell in enumerate(self.area_map[self.height-(counter1+1)]):
                if cell.topographic_level <= self.water_level and self.check_neighbor_for_water(cell.row, cell.col):
                    cell.water = True

            counter1 += 1

        counter1 = 0

        for i in range(int(self.height/2), 0, -1):

            for cell in (self.area_map[counter1]):
                if cell.topographic_level <= self.water_level and self.check_neighbor_for_water(cell.row, cell.col):
                    cell.water = True

            for col, cell in enumerate(self.area_map[self.height-(counter1+1)]):
                if cell.topographic_level <= self.water_level and self.check_neighbor_for_water(cell.row, cell.col):
                    cell.water = True

            counter1 += 1"""

        """for num1 in range(0,self.height):
            for num2 in range(0,self.height):

                if self.area_map[num1][num2].topographic_level <= self.water_level and self.check_neighbor_for_water(num1, num2):
                    self.area_map[num1][num2].water = True

                if self.area_map[num2][num1].topographic_level <= self.water_level and self.check_neighbor_for_water(num2,num1):
                    self.area_map[num2][num1].water = True

                temp_num2 = num2+1

                if self.area_map[num1][self.height-temp_num2].topographic_level <= self.water_level and self.check_neighbor_for_water(num1, self.height-temp_num2):
                    self.area_map[num1][self.height-temp_num2].water = True

                if self.area_map[self.height-temp_num2][num1].topographic_level <= self.water_level and self.check_neighbor_for_water(self.height-temp_num2,num1):
                    self.area_map[self.height-temp_num2][num1].water = True"""

        water_tiles_to_process = []

        for num1 in range(0,self.height):
            if self.area_map[0][num1].topographic_level <= self.water_level:
                water_tiles_to_process.append(self.area_map[0][num1])
            if self.area_map[99][num1].topographic_level <= self.water_level:
                water_tiles_to_process.append(self.area_map[99][num1])
            if self.area_map[num1][0].topographic_level <= self.water_level:
                water_tiles_to_process.append(self.area_map[num1][0])
            if self.area_map[num1][99].topographic_level <= self.water_level:
                water_tiles_to_process.append(self.area_map[num1][99])

        while water_tiles_to_process != []:
            cell = water_tiles_to_process[0]
            for num1 in range(-1,2):
                for num2 in range(-1,2):
                    try:
                        if self.area_map[cell.row+num1][cell.col+num2].topographic_level <= self.water_level:
                            if self.area_map[cell.row + num1][cell.col + num2].water == False:
                                self.area_map[cell.row + num1][cell.col + num2].water = True
                                water_tiles_to_process.append(self.area_map[cell.row + num1][cell.col + num2])
                    except IndexError:
                        pass
            water_tiles_to_process.pop(0)

        self.update_moisture()

    #ENVIORMENTAL EVENTS

    def simulate_random_events(self):
        for _ in range(0,1):
            print()
            s(1)
            ran = get_random_store_0_6()
            if ran == 0:
                print("RAISED WATER LEVEL")
                self.raise_water()
            elif ran == 1:
                print("LOWER WATER LEVEL")
                self.lower_water()
            elif ran == 2:
                print("RAISED TEMPERATURE LEVEL")
                self.raise_temp()
            elif ran == 3:
                print("LOWER TEMPERATURE LEVEL")
                self.lower_temp()
            elif ran == 4 and 1==2:
                #DISABLED FOR NOW
                print("RANDOMIZED TEMP MAP")
                self.randomize_heat_map()
            elif ran == 5 or ran == 4:
                print("SOIL DEPOSIT")
                self.soil_deposit()
            elif ran == 6:
                print("SOIL EROSION")
                self.soil_erosion()
            else:
                print("PASSED")
            s(1)

    def raise_water(self):
        self.water_level += 1
        print(f"new water level: {self.water_level}\n")
        self.update_water_level()

    def lower_water(self):
        self.water_level -= 1
        print(f"new water level: {self.water_level}\n")
        self.update_water_level()

    def raise_temp(self):
        self.temperature_modifier += 1
        print(f"new temp level: {self.temperature_modifier}\n")
        self.temp_update('m')

    def lower_temp(self):
        self.temperature_modifier -= 1
        print(f"new temp level: {self.temperature_modifier}\n")
        self.temp_update('m')

    def randomize_heat_map(self):
        self.temp_update('r')

    def soil_deposit(self):
        for row in self.area_map:
            for cell in row:
                if cell.water == True:
                    if get_random_store_1_3() == 1:
                        cell.topographic_level += 1
                        if cell.topographic_level > 10:
                            cell.topographic_level = 10

        self.update_water_level()

    def soil_erosion(self):
        for row in self.area_map:
            for cell in row:
                if self.check_neighbor_for_water(cell.row, cell.col):
                    if get_random_store_0_10() == 1:
                        cell.topographic_level -= 1
                        if cell.topographic_level < 0:
                            cell.topographic_level = 0

        self.update_water_level()
