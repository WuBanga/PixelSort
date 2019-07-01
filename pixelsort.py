from PIL import Image, ImageDraw

img = Image.open("yourImage.png")
size = width, height = img.size
pixels = img.load()
newcolors = []

newimg = Image.new("RGB", (width,height), (255,255,255))
draw = ImageDraw.Draw(newimg)

for i in range(width):
	for j in range(height):
		color = pixels[i, j]
		newcolors.append(color)
newcolors.sort(key=lambda x: (x[0] + x[1] + x[2]) / 3)
index = 0
for x in range(width):
	for y in range(height):
		draw.point((x,y), fill=newcolors[index])
		index += 1
del draw
newimg.save('sorted.png')