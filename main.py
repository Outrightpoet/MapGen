from map_gen import Map
from plants import Plants
from plant_id_getter import get_plant_id
import random
from plant_species_name_getter import get_plant_species_name

map = Map()
plant_ids = 0
plants = {}
year = 0
spread_requests = []
initian_plant_pop = 10000
first_plant_species_name = "OG_PLANTOIDS"

plant_species = {first_plant_species_name: [initian_plant_pop, {}]}

time_tracking = True

if time_tracking:
    import cProfile, pstats
    import io

    pr = cProfile.Profile()
    pr.enable()


def make_new_plants():
    for _ in range(initian_plant_pop):
        plant_id = get_plant_id()

        row = random.randint(0,map.height-1)
        col = random.randint(0,map.width-1)

        plant = Plants(plant_id, plants, map.area_map[row][col], map.area_map, plant_species, first_plant_species_name)

        plants[plant_id] = plant
        map.area_map[row][col].plants[plant_id] = plant
        map.area_map[row][col].tile_space_avalible -= plant.space_requirement
        plant_species[first_plant_species_name][1][plant_id] = plant
        plant_species[first_plant_species_name][0] += 1

#POST MAP MAKEING STUFFS

#
#CHANGE THIS TO MAP MODE TRUE AND SIMULATE OFF FOR NO PLANTS
#well a few but not important

map_mode = False
simulate_mode = True

#plant_init(area_map)

if map_mode:
    while True:
        map.plot_call()
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
                plants[id].cycle(spread_requests)

            for plant in spread_requests:
                plant.resolve_spread()
            spread_requests = []

            for row in map.area_map:
                for cell in row:
                    cell.cramp_death()

            if year % 100 == 0 and year % 500 != 0:
                map.plot_call()
            if year % 500 == 0:
                map.simulate_random_events()
                map.plot_call()

            big_num = 0
            lowest_num = 100
            for row in map.area_map:
                for cell in row:
                    big_num += cell.tile_space_avalible
                    if lowest_num > cell.tile_space_avalible:
                        lowest_num = cell.tile_space_avalible
            big_num = big_num/10000
            print(big_num, lowest_num)

            big_num = 0
            highest = 0
            for row in map.area_map:
                for cell in row:
                    big_num += len(cell.plants)
                    if highest < len(cell.plants):
                        highest = len(cell.plants)
            big_num = big_num / 10000
            print(big_num, highest)
            print()
            print(len(plant_species))
            print()

            year+=1
            if year == 501:
                break
        except KeyboardInterrupt:
            map.plot_call()
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