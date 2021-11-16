from PIL import Image
import numpy as np


urlimage = input("Укажите имя файла")
urlimage = urlimage+'.jpg'
img = Image.open(urlimage)
arr = np.array(img)
length = len(arr)
size = 10
gray = 6
i = 0


def get_sum_color():
    global n, n1, sum_color
    for n in range(i, i + size):
        sum_color += np.sum(arr[n][j:j+size][:])
    sum_color = sum_color // 100


def get_gray_color():
    global n, n1
    for n in range(i, i + size):
        arr[n][j:j+size][:] = int(sum_color // 50) * 50 // gray


while i < length - 1:
    j = 0
    while j < length - 1:
        sum_color = 0
        get_sum_color()
        get_gray_color()
        j = j + size
    i = i + size

res = Image.fromarray(arr)
res.save('res.jpg')
