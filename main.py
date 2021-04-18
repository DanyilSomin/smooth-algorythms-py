import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import CheckButtons
from copy import deepcopy

def avgArithmetic(a, b):
    return (a + b) / 2

def avgHarmonious(l):
    denom = 0
    
    for i in range(len(l)):
        denom += 1 / l[i]

    return len(l) / denom 

def avgGeometric(l):
    mul = 1

    for i in range(len(l)):
        mul *= l[i]

    return mul ** (1 / len(l)) 

A = 10
x = 0.024

def getExeact(t):
    s = A * np.sin(t)
    return s

def getWithError(s):
    sNew = deepcopy(s)

    for i in range(len(sNew)):
        sNew[i] *= np.random.uniform(0.95, 1.05)
    return sNew

def getAwgSimple(s):
    sNew = []

    count = 0
    sum = 0

    for i in range(len(s)):
        count += 1
        sum += s[i]

        sNew.append(sum / count)
    return sNew

def getAwgWeighted(s):
    sNew = []

    sNew.append(s[0])
    count = 1

    for i in range(1, len(s)):
        count += (i + 1)
        tmpCount = 1
        sum = 0

        for j in range(i + 1):
            sum += s[j] * tmpCount / count 
            tmpCount += 1

        sNew.append(sum)
    return sNew

def getAwgExp(s):
    sNew = []

    sNew.append(s[0])
    tmp = s[0]

    for i in range(1, len(s)):
        tmp = (s[i] + tmp) / 2
        sNew.append(tmp)

    return sNew

def getAwgModified(s):
    sNew = []

    sNew.append(s[0])
    tmp = s[0]

    n = 1

    for i in range(1, len(s)):
        tmp = (s[i] + tmp * (n - 1)) / n
        n += 1
        sNew.append(tmp)

    return sNew



t = np.arange(0, 1000 * x, x)

sExeact = getExeact(t)
sError = getWithError(sExeact)
sSimple = getAwgSimple(sError)
sWeighted = getAwgWeighted(sError)
sExp = getAwgExp(sError)
sModified = getAwgModified(sError)

fig, ax = plt.subplots()

l0, = ax.plot(t, sExeact)
l1, = ax.plot(t, sError)
l2, = ax.plot(t, sSimple)
l3, = ax.plot(t, sWeighted)
l4, = ax.plot(t, sExp)
l5, = ax.plot(t, sModified)


lines = [l0, l1, l2, l3, l4, l5]

ax.set(xlabel='x', ylabel='y',
       title='Somin Lab 2')
ax.grid()

rax = plt.axes([0.15, 0.14, 0.1, 0.15])
labels = [str(line.get_label()) for line in lines]
visibility = [line.get_visible() for line in lines]
check = CheckButtons(rax, labels, visibility)


def func(label):
    index = labels.index(label)
    lines[index].set_visible(not lines[index].get_visible())
    plt.draw()

check.on_clicked(func)

plt.show()