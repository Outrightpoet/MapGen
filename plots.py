import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap, BoundaryNorm
import numpy as np
from numpy.ma.extras import average


def plt_data(area_map, plant_species, data1, data2, data3, data4, data5, data6, data7, data8):
    fig, axs = plt.subplots(6,3, figsize = (30,60))

    axs[0,0].imshow(data1, cmap='Reds', interpolation='nearest')
    axs[0,0].title.set_text('Topographic Level')

    axs[1, 0].imshow(data2, cmap='Blues', interpolation='nearest')
    axs[1, 0].title.set_text('Soil Quality')

    axs[2, 0].imshow(data3, cmap='Blues', interpolation='nearest')
    axs[2, 0].title.set_text('Water Level')

    axs[3, 0].imshow(data4, cmap='Blues', interpolation='nearest')
    axs[3, 0].title.set_text('Moisture Level')

    axs[4, 0].imshow(data5, cmap='RdBu_r', interpolation='nearest')
    axs[4, 0].title.set_text('Tempature')

    BIOME_COLORS = [
        "#003366",  # 0 ocean (deep blue)
        "#3366cc",  # 1 lake (blue)
        "#2e8b57",  # 2 swamp (dark green)
        "#edc9af",  # 3 desert (sand)
        "#7cfc00",  # 4 grassland (bright green)
        "#228b22",  # 5 temperate forest (forest green)
        "#006400",  # 6 rainforest (deep green)
        "#2f4f4f",  # 7 taiga (cold dark green)
        "#e0f8ff",  # 8 tundra (icy blue-white)
        "#8b7765",  # 9 mountain (rock brown)
        "#9acd32",  # 10 alpine (yellow-green)
        "#aaaaaa",  # 11 rocky peak (gray)
        "#b8860b",  # 12 badlands (dry brown)
        "#556b2f",  # 13 farmland (olive)
    ]

    cmap = ListedColormap(BIOME_COLORS)
    norm = BoundaryNorm(np.arange(len(BIOME_COLORS) + 1), cmap.N)

    axs[5, 0].imshow(
        data6,
        cmap=cmap,
        norm=norm,
        interpolation='nearest'
    )

    axs[5, 2].imshow(data7, cmap='viridis', interpolation='nearest')
    axs[5, 2].title.set_text('Plant Life')

    angles = np.linspace(0, 2 * np.pi, 14, endpoint=False).tolist()

    axs[5, 1] = plt.subplot(6, 3, (5 * 3) + 2, polar=True)

    labels = [
        'fruit_growth', 'aquatic_afinity', 'plant_size', 'long_lived',
        'spreading_range', 'spreading_batch', 'low_nutritinal_need',
        'tuff_tissue', 'soft_tissue', 'heat_affinity', 'heat_weakness',
        'cold_affinity', 'cold_weakness'
    ]

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

    axs[5, 1].plot(angles, values, linewidth=2, label="Average")
    axs[5, 1].fill(angles, values, alpha=0.25)
    axs[5, 1].set_xticks(angles[:-1])
    axs[5, 1].set_xticklabels(labels)
    axs[5, 1].set_yticklabels([])
    axs[5, 1].set_ylim(0, 100)
    axs[5, 1].legend(loc='upper right', bbox_to_anchor=(1.2, 1.1))
    axs[5, 1].set_title(f'Average Traits')

    if len(data8) == 5:

        for index, species in enumerate(data8):

            data = np.array([
                [
                    sum(1 for plant in cell.plants.values() if plant.species_name == species)
                    for cell in row
                ]
                for row in area_map
            ])

            axs[index, 2].imshow(data, cmap='viridis', interpolation='nearest')
            axs[index, 2].title.set_text(f'{species} Plant Life')

            axs[index, 1] = plt.subplot(6, 3, (index * 3) + 2, polar=True)

            labels = [
                'fruit_growth', 'aquatic_afinity', 'plant_size', 'long_lived',
                'spreading_range', 'spreading_batch', 'low_nutritinal_need',
                'tuff_tissue', 'soft_tissue', 'heat_affinity', 'heat_weakness',
                'cold_affinity', 'cold_weakness'
            ]

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

            axs[index, 1].plot(angles, values, linewidth=2, label=species)
            axs[index, 1].fill(angles, values, alpha=0.25)
            axs[index, 1].set_xticks(angles[:-1])
            axs[index, 1].set_xticklabels(labels)
            axs[index, 1].set_yticklabels([])
            axs[index, 1].set_ylim(0, 100)
            axs[index, 1].legend(loc='upper right', bbox_to_anchor=(1.2, 1.1))
            axs[index, 1].set_title(f'{species} Traits')





    plt.tight_layout()
    plt.show()

