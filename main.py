from map_gen import Map
from plants_def import Plants
from plant_id_getter import get_plant_id
import random
import numpy as np
from plots import plt_data
from rand_storage import get_random_store_neg_1_1
from multiprocessing import Process

def make_new_plants():
    for _ in range(initian_plant_pop):
        plant_id = get_plant_id()

        row = random.randint(0,map.height-1)
        col = random.randint(0,map.width-1)

        plant = Plants(plant_id, plants, map.area_map[row][col], map.area_map, plant_species, first_plant_species_name, map.height, map.width)
        if map.area_map[row][col].water == True:
            plant.traits.traits[1] = 100
            plant.water_affiliation = "aquatic"
            plant.species_name = "OG_PLANTOIDS_AQUATIC"
            plant_species[first_plant_species_name_aquatic][1][plant_id] = plant
            plant_species[first_plant_species_name_aquatic][0] += 1
        else:
            plant_species[first_plant_species_name][1][plant_id] = plant
            plant_species[first_plant_species_name][0] += 1

        plants[plant_id] = plant
        map.area_map[row][col].plants[plant_id] = plant
        map.area_map[row][col].tile_space_avalible -= plant.space_requirement

#POST MAP MAKEING STUFFS

def plot_call(area_map):
    try:
        p.join()
    except:
        pass

    data1 = np.array([[tile.topographic_level for tile in row] for row in area_map])
    data2 = np.array([[tile.soil_quality for tile in row] for row in area_map])
    data3 = np.array([[tile.water for tile in row] for row in area_map])
    data4 = np.array([[tile.moisture for tile in row] for row in area_map])
    data5 = np.array([[tile.temperature_mod for tile in row] for row in area_map])
    data6 = np.array([[tile.classification_num for tile in row] for row in area_map])
    data7 = np.array([[len(tile.plants) for tile in row] for row in area_map])
    data8 = sorted(plant_species, key=lambda x: plant_species[x][0], reverse=True)[:5]

    #this looks awful so i added the if to collapse it
    if 1==1:
        average1 = 0
        average2 = 0
        average3 = 0
        average4 = 0
        average5 = 0
        average6 = 0
        average7 = 0
        average8 = 0
        average9 = 0
        average10 = 0
        average11 = 0
        average12 = 0
        average13 = 0

        for species in plant_species.keys():
            average1 = plant_species[species][2][0] + average1
            average2 = plant_species[species][2][1] + average2
            average3 = plant_species[species][2][2] + average3
            average4 = plant_species[species][2][3] + average4
            average5 = plant_species[species][2][4] + average5
            average6 = plant_species[species][2][5] + average6
            average7 = plant_species[species][2][6] + average7
            average8 = plant_species[species][2][7] + average8
            average9 = plant_species[species][2][8] + average9
            average10 = plant_species[species][2][9] + average10
            average11 = plant_species[species][2][10] + average11
            average12 = plant_species[species][2][11] + average12
            average13 = plant_species[species][2][12] + average13

        average1 = average1 / len(plant_species)
        average2 = average2 / len(plant_species)
        average3 = average3 / len(plant_species)
        average4 = average4 / len(plant_species)
        average5 = average5 / len(plant_species)
        average6 = average6 / len(plant_species)
        average7 = average7 / len(plant_species)
        average8 = average8 / len(plant_species)
        average9 = average9 / len(plant_species)
        average10 = average10 / len(plant_species)
        average11 = average11 / len(plant_species)
        average12 = average12 / len(plant_species)
        average13 = average13 / len(plant_species)

        values = [average1,
                  average2,
                  average3,
                  average4,
                  average5,
                  average6,
                  average7,
                  average8,
                  average9,
                  average10,
                  average11,
                  average12,
                  average13]

        values += values[:1]
        data9 = values

        data10 = []
        data11 = []
        data12 = []

        for index, species in enumerate(data8):
            data = np.array([
                [
                    sum(1 for plant in cell.plants.values() if plant.species_name == species)
                    for cell in row
                ]
                for row in area_map
            ])

            data10.append(data)

            values = [plant_species[species][2][0],
                      plant_species[species][2][1],
                      plant_species[species][2][2],
                      plant_species[species][2][3],
                      plant_species[species][2][4],
                      plant_species[species][2][5],
                      plant_species[species][2][6],
                      plant_species[species][2][7],
                      plant_species[species][2][8],
                      plant_species[species][2][9],
                      plant_species[species][2][10],
                      plant_species[species][2][11],
                      plant_species[species][2][12]]

            values += values[:1]
            data11.append(values)
            data12.append(species)

    p = Process(target=plt_data, args=(data1, data2, data3, data4, data5, data6, data7, data9, data10, data11, data12))
    p.start()

if __name__ == '__main__':
    map = Map()
    plant_ids = 0
    plants = {}
    un_active_plants = []
    year = 0
    spread_requests = []
    initian_plant_pop = 10000
    run_time = 100001
    first_plant_species_name = "OG_PLANTOIDS"
    first_plant_species_name_aquatic = "OG_PLANTOIDS_AQUATIC"

    plant_species = {first_plant_species_name: [0, {}, [0,0,0,0,0,0,0,0,0,0,0,0,0]],
                     first_plant_species_name_aquatic: [0, {}, [0,100,0,0,0,0,0,0,0,0,0,0,0]]}

    time_tracking = True

    if time_tracking:
        import cProfile, pstats
        import io

        pr = cProfile.Profile()
        pr.enable()


    #
    #CHANGE THIS TO MAP MODE TRUE AND SIMULATE OFF FOR NO PLANTS
    #well a few but not important
    #

    map_mode = False
    simulate_mode = True

    #plant_init(area_map)

    if map_mode:
        while True:
            plot_call(map.area_map)
            print(f"Pass: p\nRaise water level: rw\nLower water level: lw\nRaise temp: rt\nLower temp: lt\nRandomize temp map: rnt\nSoil Deposit: sd\nSoil Erosion: se\nSimulate Random events: re\nQuit: q\n")
            response = input('enviormental change: ').lower()
            print()
            if response == 'p':
                pass
            elif response == 'rw':
                map.raise_water()
            elif response == 'lw':
                map.lower_water()
            elif response == 'rt':
                map.raise_temp()
            elif response == 'lt':
                map.lower_temp()
            elif response == 'rnt':
                map.randomize_heat_map()
            elif response == 'sd':
                map.soil_deposit()
            elif response == 'se':
                map.soil_erosion()
            elif response == 're':
                map.simulate_random_events()
            elif response == 'q':
                break
    elif simulate_mode:
        while True:
            try:
                print(year, len(plants))
                if plants == {}:
                    make_new_plants()

                keys = list(plants.keys())
                cycle = Plants.cycle

                for id in keys:
                    plants[id].cycle(spread_requests, un_active_plants)


                for plant in spread_requests:
                    row = plant.tile.row
                    col = plant.tile.col
                    if plant.spread_distance == 1:
                        for _ in range(0, plant.spread_size):
                            row = row + get_random_store_neg_1_1()
                            col = col + get_random_store_neg_1_1()
                            if row >= 0 and row < plant.map_height and col >= 0 and col < plant.map_width:
                                if plant.area_map[row][col].tile_space_avalible > -20:
                                    if plant.species_name not in plant.plant_species:
                                        traits = plant.traits
                                        plant.plant_species[plant.species_name] = [0, {}, [traits.fruit_growth,
                                                                                         traits.aquatic_afinity,
                                                                                         traits.plant_size,
                                                                                         traits.long_lived,
                                                                                         traits.spreading_range,
                                                                                         traits.spreading_batch,
                                                                                         traits.low_nutritinal_need,
                                                                                         traits.tuff_tissue,
                                                                                         traits.soft_tissue,
                                                                                         traits.heat_affinity,
                                                                                         traits.heat_weakness,
                                                                                         traits.cold_affinity,
                                                                                         traits.cold_weakness]]

                                    if un_active_plants == []:
                                        plant_id = get_plant_id()
                                        offspring = Plants(plant_id, plant.plant_list, plant.area_map[row][col], plant.area_map,plant.plant_species, plant.species_name, plant.map_height, plant.map_width,plant.ready_to_split, plant)
                                    else:
                                        offspring = un_active_plants[0]
                                        un_active_plants.pop(0)
                                        plant_id = offspring.id
                                        offspring.height = 0
                                        offspring.status = "seed"
                                        offspring.tile = offspring.area_map[row][col]
                                        offspring.plant_species = plant_species
                                        offspring.species_name = plant.species_name
                                        offspring.ready_to_split = plant.ready_to_split
                                        offspring.parent = plant
                                        offspring.traits.traits = plant.traits.traits
                                        offspring.traits.speciate()
                                        offspring.traits.get_stats()

                                    plant.plant_list[plant_id] = offspring
                                    plant.area_map[row][col].plants[plant_id] = offspring
                                    plant.area_map[row][col].tile_space_avalible -= offspring.space_requirement
                                    plant.plant_species[plant.species_name][1][plant_id] = offspring
                                    plant.plant_species[plant.species_name][0] += 1
                                    offspring.check_and_split()

                spread_requests = []

                for row in map.area_map:
                    for cell in row:
                        cell.cramp_death(un_active_plants)

                if year % 100 == 0 and year % 500 != 0:
                    plot_call(map.area_map)
                if year % 4000 == 0:
                    map.simulate_random_events()
                    plot_call(map.area_map)

                big_num = 0
                lowest_num = 100
                for row in map.area_map:
                    for cell in row:
                        big_num += cell.tile_space_avalible
                        if lowest_num > cell.tile_space_avalible:
                            lowest_num = cell.tile_space_avalible
                big_num = big_num/10000
                #(big_num, lowest_num)

                big_num = 0
                highest = 0
                for row in map.area_map:
                    for cell in row:
                        big_num += len(cell.plants)
                        if highest < len(cell.plants):
                            highest = len(cell.plants)
                big_num = big_num / 10000
                #print(big_num, highest)
                #print()
                #print(len(plant_species))
                #print()

                year+=1
                if year == run_time:
                    break
            except KeyboardInterrupt:
                plot_call(map.area_map)
                break

    """for row in area_map:
        for tile in row:
            print(tile.water,end=" ")
        print()"""

    if time_tracking:
        pr.disable()
        s = io.StringIO()
        ps = pstats.Stats(pr, stream=s).sort_stats("cumtime")
        ps.print_stats(15)  # top 15 slowest functions
        print(s.getvalue())