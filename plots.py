import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import numpy as np

def plt_data(data1, data2, data3, data4, data5, data6):
    fig, axs = plt.subplots(3,2, figsize = (20,30))

    axs[0,0].imshow(data1, cmap='Reds', interpolation='nearest')
    axs[0,0].title.set_text('Topographic Level')

    axs[0, 1].imshow(data2, cmap='Blues', interpolation='nearest')
    axs[0, 1].title.set_text('Soil Quality')

    axs[1, 0].imshow(data3, cmap='Blues', interpolation='nearest')
    axs[1, 0].title.set_text('Water Level')

    axs[1, 1].imshow(data4, cmap='Blues', interpolation='nearest')
    axs[1, 1].title.set_text('Moisture Level')

    axs[2, 0].imshow(data5, cmap='RdBu_r', interpolation='nearest')
    axs[2, 0].title.set_text('Tempature')

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
    axs[2, 1].imshow(data5, cmap=cmap, interpolation='nearest')

    axs[2, 1].imshow(data6, cmap=cmap, interpolation='nearest')
    axs[2, 1].title.set_text('Biomes')

    plt.tight_layout()
    plt.show()

