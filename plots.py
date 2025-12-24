import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap, BoundaryNorm
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

    BIOME_COLORS = {
        0: "#003366",  # ocean (deep blue)
        1: "#3366cc",  # lake (blue)
        2: "#2e8b57",  # swamp (dark green)
        3: "#edc9af",  # desert (sand)
        4: "#7cfc00",  # grassland (bright green)
        5: "#228b22",  # temperate forest (forest green)
        6: "#006400",  # rainforest (deep green)
        7: "#2f4f4f",  # taiga (cold dark green)
        8: "#e0f8ff",  # tundra (icy blue-white)
        9: "#8b7765",  # mountain (rock brown)
        10: "#9acd32",  # alpine (yellow-green)
        11: "#aaaaaa",  # rocky peak (gray)
        12: "#b8860b",  # badlands (dry brown)
        13: "#556b2f",  # farmland (olive)
    }

    axs[2, 1].imshow(data6, cmap=BIOME_COLORS, interpolation='nearest')
    axs[2, 2].title.set_text('Biomes')

    plt.tight_layout()
    plt.show()

