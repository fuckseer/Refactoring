from PIL import Image
import numpy as np
img = Image.open("img2.jpg")
arr = np.array(img)
length = len(arr)
length1 = len(arr[1])
size = 10
gray = 6
i = 0

def get_sum_color():
    global n, n1, sum_color
    for n in range(i, i + size):
        for n1 in range(j, j + size):
            red = int(arr[n][n1][0])
            green = int(arr[n][n1][1])
            blue = int(arr[n][n1][2])
            sum_color += red + green + blue
    sum_color = int(sum_color // 100)


def get_gray_color():
    global n, n1
    for n in range(i, i + size):
        for n1 in range(j, j + size):
            arr[n][n1][0] = int(sum_color // 50) * 50 // gray
            arr[n][n1][1] = int(sum_color // 50) * 50 // gray
            arr[n][n1][2] = int(sum_color // 50) * 50 // gray


while i < length - 1:
    j = 0
    while j < length1 - 1:
        sum_color = 0
        get_sum_color()
        get_gray_color()
        j = j + size
    i = i + size
res = Image.fromarray(arr)
res.show()
res.save('res.jpg')
