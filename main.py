#data1 = np.array([[cell.terrain_value for cell in row] for row in area_map])
from matplotlib import pyplot as plt
from numpy.ma.extras import average

from rand_storage import get_random_store_1_3, get_random_store_neg_1_1, get_random_store_0_10
import random
from tiles import Tile
import numpy as np
from plots import plt_data


height = 100
width = 100
water_level = 3
temperature_modifier = 0
area_map = []

#LIST CREATION

for h in range(0,height):
    area_map.append([])
    for w in range(0,width):
        area_map[h].append(Tile(h,w))

#TOPOGRAPICAL GEN

set=1
counter1=0
counter2=0

area_map[0][0].topographic_level = random.randint(0,10)

while set < height*2:
    counter1 = set
    run = counter1
    if run > height:
        run = height
    for i in range(0,run+1):
        if counter2 == 0:
            try:
                neighbor1 = area_map[counter1-1][0].topographic_level
            except IndexError:
                neighbor1 = -1
            neighbor2 = -1
        elif counter1 == 0:
            try:
                neighbor2 = area_map[0][counter2-1].topographic_level
            except IndexError:
                neighbor2 = -1
            neighbor1 = -1
        else:
            try:
                neighbor1 = area_map[counter1-1][counter2].topographic_level
            except IndexError:
                neighbor1 = -1
            try:
                neighbor2 = area_map[counter1][counter2-1].topographic_level
            except IndexError:
                neighbor2 = -1

        if counter1 < height and counter2 < width:
            if neighbor1 != -1 and neighbor2 != -1:
                area_map[counter1][counter2].topographic_level = round((neighbor1 + neighbor2)/2) + get_random_store_neg_1_1()
            else:
                rand = get_random_store_1_3()
                if neighbor1 != -1:
                    neighbor_val = neighbor1
                else:
                    neighbor_val = neighbor2

                if rand == 1:
                    area_map[counter1][counter2].topographic_level = neighbor_val -1
                elif rand == 2:
                    area_map[counter1][counter2].topographic_level = neighbor_val
                else:
                    area_map[counter1][counter2].topographic_level = neighbor_val + 1

            if get_random_store_0_10() == 0 and get_random_store_0_10() == 0:
                if area_map[counter1][counter2].topographic_level > 5:
                    area_map[counter1][counter2].topographic_level -= 1
                elif area_map[counter1][counter2].topographic_level < 5:
                    area_map[counter1][counter2].topographic_level += 1

            if area_map[counter1][counter2].topographic_level < 0:
                area_map[counter1][counter2].topographic_level = 0
            elif area_map[counter1][counter2].topographic_level > 10:
                area_map[counter1][counter2].topographic_level = 10

        counter1 -= 1
        counter2 += 1
    set += 1
    counter1 = 0
    counter2 = 0

#SOIL QUALITY GEN

set=1
counter1=0
counter2=0

area_map[0][0].soil_quality = random.randint(0,10)

while set < height*2:
    counter1 = set
    run = counter1
    if run > height:
        run = height
    for i in range(0,run+1):
        if counter2 == 0:
            try:
                neighbor1 = area_map[counter1-1][0].soil_quality
            except IndexError:
                neighbor1 = -1
            neighbor2 = -1
        elif counter1 == 0:
            try:
                neighbor2 = area_map[0][counter2-1].soil_quality
            except IndexError:
                neighbor2 = -1
            neighbor1 = -1
        else:
            try:
                neighbor1 = area_map[counter1-1][counter2].soil_quality
            except IndexError:
                neighbor1 = -1
            try:
                neighbor2 = area_map[counter1][counter2-1].soil_quality
            except IndexError:
                neighbor2 = -1

        if counter1 < height and counter2 < width:
            if neighbor1 != -1 and neighbor2 != -1:
                area_map[counter1][counter2].soil_quality = round((neighbor1 + neighbor2)/2) + get_random_store_neg_1_1()
            else:
                rand = get_random_store_1_3()
                if neighbor1 != -1:
                    neighbor_val = neighbor1
                else:
                    neighbor_val = neighbor2

                if rand == 1:
                    area_map[counter1][counter2].soil_quality = neighbor_val -1
                elif rand == 2:
                    area_map[counter1][counter2].soil_quality = neighbor_val
                else:
                    area_map[counter1][counter2].soil_quality = neighbor_val + 1

            if get_random_store_0_10() == 0 and get_random_store_0_10() == 0:
                if area_map[counter1][counter2].soil_quality > 5:
                    area_map[counter1][counter2].soil_quality -= 1
                elif area_map[counter1][counter2].soil_quality < 5:
                    area_map[counter1][counter2].soil_quality += 1

            if area_map[counter1][counter2].soil_quality < 0:
                area_map[counter1][counter2].soil_quality = 0
            elif area_map[counter1][counter2].soil_quality > 10:
                area_map[counter1][counter2].soil_quality = 10

        counter1 -= 1
        counter2 += 1
    set += 1
    counter1 = 0
    counter2 = 0


# TEMP GEN

def temp_update(area_map, decider='b'):
    set = 1
    counter1 = 0
    counter2 = 0

    area_map[0][0].temperature = random.randint(0, 10)

    if decider == 'r' or decider == 'b':
        while set < height * 2:
            counter1 = set
            run = counter1
            if run > height:
                run = height
            for i in range(0, run + 1):
                if counter2 == 0:
                    try:
                        neighbor1 = area_map[counter1 - 1][0].temperature
                    except IndexError:
                        neighbor1 = -1
                    neighbor2 = -1
                elif counter1 == 0:
                    try:
                        neighbor2 = area_map[0][counter2 - 1].temperature
                    except IndexError:
                        neighbor2 = -1
                    neighbor1 = -1
                else:
                    try:
                        neighbor1 = area_map[counter1 - 1][counter2].temperature
                    except IndexError:
                        neighbor1 = -1
                    try:
                        neighbor2 = area_map[counter1][counter2 - 1].temperature
                    except IndexError:
                        neighbor2 = -1

                if counter1 < height and counter2 < width:
                    if neighbor1 != -1 and neighbor2 != -1:
                        area_map[counter1][counter2].temperature = round(
                            (neighbor1 + neighbor2) / 2) + get_random_store_neg_1_1()
                    else:
                        rand = get_random_store_1_3()
                        if neighbor1 != -1:
                            neighbor_val = neighbor1
                        else:
                            neighbor_val = neighbor2

                        if rand == 1:
                            area_map[counter1][counter2].temperature = neighbor_val - 1
                        elif rand == 2:
                            area_map[counter1][counter2].temperature = neighbor_val
                        else:
                            area_map[counter1][counter2].temperature = neighbor_val + 1

                    if get_random_store_0_10() == 0 and get_random_store_0_10() == 0:
                        if area_map[counter1][counter2].temperature > 5:
                            area_map[counter1][counter2].temperature -= 1
                        elif area_map[counter1][counter2].temperature < 5:
                            area_map[counter1][counter2].temperature += 1

                    if area_map[counter1][counter2].temperature < 0:
                        area_map[counter1][counter2].temperature = 0
                    elif area_map[counter1][counter2].temperature > 10:
                        area_map[counter1][counter2].temperature = 10

                counter1 -= 1
                counter2 += 1
            set += 1
            counter1 = 0
            counter2 = 0

    if decider == 'm' or decider == 'b' or decider == 'r':
        for row in area_map:
            for cell in row:
                cell.temperature_mod = cell.temperature
                if cell.topographic_level > 5:
                    cell.temperature_mod -= int(cell.topographic_level / 2)
                elif cell.topographic_level < 5:
                    cell.temperature_mod += int(cell.topographic_level / 2)
                if cell.moisture > 5:
                    cell.temperature_mod -= int(cell.moisture / 4)
                else:
                    cell.temperature_mod += int((10 - cell.moisture) / 4)

                cell.temperature_mod += temperature_modifier

                if cell.temperature_mod < 0:
                    cell.temperature_mod = 0
                elif cell.temperature_mod > 10:
                    cell.temperature_mod = 10

    classify_map(area_map)


# BIOME CLASSIFICATION

BIOME_IDS = {
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

def classify_cell(cell):
    topo = cell.topographic_level  # 0–10
    moist = cell.moisture  # 0–10
    soil = cell.soil_quality  # 0–10
    temp = cell.temperature_mod  # 0–10

    # --- WATER ---
    if cell.water:
        if topo <= 3:
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

def classify_map(area_map):
    for row in area_map:
        for cell in row:
            biome = classify_cell(cell)
            cell.classification = biome
            cell.classification_num = BIOME_IDS[biome]


#MOISTURE AREA

def spread_moisture(area_map, row, col):
    for dis in range(1,20):
        for row1 in range(row-dis,row+dis+1):
            for col1 in range(col-dis,col+dis+1):
                try:
                    if area_map[row1][col1].moisture < int((20-dis)/2):
                        area_map[row1][col1].moisture = int((20-dis)/2)
                except IndexError:
                    pass

def update_moisture(area_map):

    for row in area_map:
        for cell in row:
            cell.moisture = 0

    for row in area_map:
        for cell in row:
            if cell.water == True:
                cell.moisture = 10
                spread_moisture(area_map, cell.row, cell.col)

    for row in area_map:
        for cell in row:
            if cell.moisture == -1:
                cell.moisture = 0

    temp_update(area_map, 'm')

temp_update(area_map, 'b')

#WATER AREA

def update_water_level(area_map, water_level):

    for row in area_map:
        for cell in row:
            if cell.water == True and cell.topographic_level > water_level:
                cell.water = False

    counter1 = 0

    def check_neighbor_for_water(area_map, row, col):
        if row == 0 or col == 0 or row == height - 1 or col == width - 1:
            return True

        for col1 in range(col-1,col+2):
            for row1 in range(row-1,row+2):
                if area_map[row1][col1].water == True:
                    return True

    for i in range(0,int(height/2)):

        for i in range(0,3):
            for cell in (area_map[counter1]):
                if cell.topographic_level <= water_level and check_neighbor_for_water(area_map, cell.row, cell.col):
                    cell.water = True


            for i2 in range(counter1+1, height-(counter1+1)):
                if area_map[i2][counter1].topographic_level <= water_level and check_neighbor_for_water(area_map, i2, (counter1+1)):
                    cell.water = True

                elif area_map[i2][width-(counter1+1)].topographic_level <= water_level and check_neighbor_for_water(area_map, i2, (width-(counter1+1))):
                    cell.water = True


            for col, cell in enumerate(area_map[height-(counter1+1)]):
                if cell.topographic_level <= water_level and check_neighbor_for_water(area_map, cell.row, cell.col):
                    cell.water = True


        counter1 += 1

    update_moisture(area_map)

update_water_level(area_map, water_level)

#PLOTING AREA

def plot_call(area_map):

    data1 = np.array([[tile.topographic_level for tile in row] for row in area_map])
    data2 = np.array([[tile.soil_quality for tile in row] for row in area_map])
    data3 = np.array([[tile.water for tile in row] for row in area_map])
    data4 = np.array([[tile.moisture for tile in row] for row in area_map])
    data5 = np.array([[tile.temperature_mod for tile in row] for row in area_map])
    data6 = np.array([[tile.classification_num for tile in row] for row in area_map])

    plt_data(data1, data2, data3, data4, data5, data6)


#ENVIORMENTAL CHANGES

while True:
    plot_call(area_map)
    print(f"Pass: p\nRaise water level: rw\nLower water level: lw\nRaise temp: rt\nLower temp: lt\nRandomize temp map: rnt\nQuit: q\n")
    response = input('enviormental change: ').lower()
    print()
    if response == 'p':
        pass
    elif response == 'rw':
        water_level += 1
        print(f"new water level: {water_level}\n")
        update_water_level(area_map, water_level)
    elif response == 'lw':
        water_level -= 1
        print(f"new water level: {water_level}\n")
        update_water_level(area_map, water_level)
    elif response == 'rt':
        temperature_modifier += 1
        print(f"new temp level: {temperature_modifier}\n")
        temp_update(area_map, 'm')
    elif response == 'lt':
        temperature_modifier -= 1
        print(f"new temp level: {temperature_modifier}\n")
        temp_update(area_map, 'm')
    elif response == 'rnt':
        temp_update(area_map, 'r')
    elif response == 'q':
        break

"""for row in area_map:
    for tile in row:
        print(tile.water,end=" ")
    print()"""