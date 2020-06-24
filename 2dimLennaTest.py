import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from dydwt import DyDWT

def normalize(target):
    max = 255*((target - np.min(target)) / (np.max(target) - np.min(target)))
    return max

#2次スプライン係数
h = [0, 0.125, 0.375, 0.375, 0.125, 0] 
g = [0, 0, -0.5, 0.5, 0, 0]

h = [i * np.sqrt(2) for i in h]
g = [i * np.sqrt(2) for i in g]
model = DyDWT(h, g, cenH=2, cenG=2)

im = np.array(Image.open('resource/LENNA.bmp')) #入力画像

result = np.zeros((4, im.shape[0], im.shape[1]))

tmpA = np.zeros((im.shape[0], im.shape[1]))
tmpD = np.zeros((im.shape[0], im.shape[1]))
 
#最初に垂直方向(画像の上から下に向かって横一列をDyDWT)
for i in range(im.shape[0]):
    tmpA[i, :], tmpD[i, :] = model.translate(im[i, :], 1)

#途中の変換を保存 tmpA:低周波 tmpD:高周波
tmpA = 255*((tmpA - np.min(tmpA)) / (np.max(tmpA) - np.min(tmpA)))
tmpD = 255*((tmpD - np.min(tmpD)) / (np.max(tmpD) - np.min(tmpD)))

resultImg = Image.fromarray(tmpA).convert('L')
resultImg.save('result/tmpA.bmp')
resultImg = Image.fromarray(tmpD).convert('L')
resultImg.save('result/tmpD.bmp')

#それぞれ転置(水平方向の変換を簡単にするため)
tmpA = tmpA.T
tmpD = tmpD.T

for i in range(im.shape[0]):
    result[0, i, :], result[1, i, :] = model.translate(tmpA[i, :], 1)

for i in range(im.shape[0]):
    result[2, i, :], result[3, i, :] = model.translate(tmpD[i, :], 1)

result = result.transpose(0, 2, 1)

for i in range(result.shape[0]):
    result[i] = normalize(result[i])


resultImg = Image.fromarray(result[0]).convert('L')
resultImg.save('result/C.bmp')

resultImg = Image.fromarray(result[1]).convert('L')
resultImg.save('result/D2.bmp')

resultImg = Image.fromarray(result[2]).convert('L')
resultImg.save('result/D1.bmp')

resultImg = Image.fromarray(result[3]).convert('L')
resultImg.save('result/D3.bmp')
