import numpy as np
import matplotlib.pyplot as plt

class DyDWT:
    
    def __init__(self, h, g, cenH = 0, cenG = 0):
        self.h = h
        self.g = g

        self.cenH = cenH
        self.cenG = cenG
    

    def printCoef(self):
        print('h:', self.h)
        print('g:', self.g)

        print('center h:', self.h[self.cenH])
        print('center g:', self.g[self.cenG])

    def translate(self, target, j): #target:変換対象 j:レベル
        a = [0] * len(target) #低周波成分
        d = [0] * len(target) #ウェーブレット成分

        for i in range(len(target)):

            for l in range(len(self.h)):
                if len(target) <= i + 2**j * (l - self.cenH) or 0 > i + 2**j * (l - self.cenH):
                    continue
                else :
                    a[i] += self.h[l] * target[i + 2**j * (l - self.cenH)]
            
            for l in range(len(self.g)):
                if len(target) <= i + 2**j * (l - self.cenG) or 0 > i + 2**j * (l - self.cenG):
                    continue
                else:
                    d[i] += self.g[l] * target[i + 2**j * (l - self.cenG)]
            
        return a, d

 
