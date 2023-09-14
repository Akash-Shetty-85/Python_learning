import colorgram

colors = colorgram.extract('image.jpg', 30)

list_of_colors = []
for i in colors:
    red = i.rgb.r
    green = i.rgb.g
    blue = i.rgb.b
    tuple_color = (red, green, blue)
    list_of_colors.append(tuple_color)

print(list_of_colors)
