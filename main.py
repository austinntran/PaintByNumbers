import math
from color import color
import numpy as np
from PIL import Image
import cv2
from sklearn.cluster import KMeans


clust = 20
INFILE = "austinwacko.jpeg"
INPATH = r"img/" + INFILE
OUTPATH = "out/" + INFILE.split('.')[0] + str(clust) + '.' +INFILE.split('.')[1]


image = cv2.imread('img/' + INFILE)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
reshape = image.reshape((image.shape[0] * image.shape[1], 3))
cluster = KMeans(n_clusters=clust).fit(reshape)
color_list = []

for c in cluster.cluster_centers_:
    color_list.append(color(int(c[0]), int(c[1]), int(c[2])))

im = Image.open(INPATH)
rgb_im = im.convert('RGB')
print(rgb_im)
h, w = im.size
# color_list = [color(64, 55, 49), color(236, 233, 234), color(114, 120, 119), color(162, 166, 168), color(138, 143, 145)]
# color_list = [color(255, 0, 0), color(0, 255, 0), color(0, 0, 255), color(0, 0, 0), color(255, 255, 255), color(255, 255, 0), color(0, 255, 255), color(255, 0, 255)]


def main():
    img = Image.new('RGB', (h, w))
    c5 = math.floor(w / 20)
    global color_list
    for col in range(w):
        for row in range(h):
            r, g, b = rgb_im.getpixel((row, col))
            src = color(r, g, b)
            for i in range(len(color_list)):
                color_list[i].calculate_distance(src)

            # hq.heapify(color_list)
            # c = color_list[0]
            c = min(color_list)
            img.putpixel((row, col), (c.r, c.g, c.b))
        if col % c5 == 0:
            print(str(col / w * 100) + "%")

    img.save(OUTPATH)




if __name__ == "__main__":
    main()
