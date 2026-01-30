import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap, BoundaryNorm
import numpy as np
from numpy.ma.extras import average


def plt_data(data1, data2, data3, data4, data5, data6, data7, data9, data10, data11, data12):
    fig, axs = plt.subplots(6,3, figsize = (15,30))

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

    axs[5, 1].plot(angles, data9, linewidth=2, label="Average")
    axs[5, 1].fill(angles, data9, alpha=0.25)
    axs[5, 1].set_xticks(angles[:-1])
    axs[5, 1].set_xticklabels(labels)
    axs[5, 1].set_yticklabels([])
    axs[5, 1].set_ylim(0, 100)
    axs[5, 1].legend(loc='upper right', bbox_to_anchor=(1.2, 1.1))
    axs[5, 1].set_title(f'Average Traits')

    for index, data in enumerate(data10):
        axs[index, 2].imshow(data, cmap='viridis', interpolation='nearest')
        axs[index, 2].title.set_text(f'{data12[index]} Plant Life')
        axs[index, 1] = plt.subplot(6, 3, (index * 3) + 2, polar=True)

    for index, data in enumerate(data11):
        axs[index, 1].plot(angles, data, linewidth=2, label=data12[index])
        axs[index, 1].fill(angles, data, alpha=0.25)
        axs[index, 1].set_xticks(angles[:-1])
        axs[index, 1].set_xticklabels(labels)
        axs[index, 1].set_yticklabels([])
        axs[index, 1].set_ylim(0, 100)
        axs[index, 1].legend(loc='upper right', bbox_to_anchor=(1.2, 1.1))
        axs[index, 1].set_title(f'{data12[index]} Traits')





    plt.tight_layout()
    plt.show()
