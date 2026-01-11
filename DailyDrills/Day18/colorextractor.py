import colorgram

colors = colorgram.extract("img.png", 30)
colors_rgb = []

def rgb_extractor():
    for i in range (len(colors)):
        r = colors[i].rgb.r
        g = colors[i].rgb.g
        b = colors[i].rgb.b
        rgb = (r,g,b)
        colors_rgb.append(rgb)
    return colors_rgb


print(rgb_extractor())