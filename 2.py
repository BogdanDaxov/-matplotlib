import matplotlib.pyplot as plt
import numpy as np
with open("Данные2/data") as f :
    a=f.read().split("\n")
for i in range(0,6):
    fig, ax = plt.subplots()
    plt.title("Frame " + str(i))
    x=[float(s) for s in a[2*i].split(" ")]
    y=[float(s) for s in a[2*i+1].split(" ")]
    ax.plot(x, y)
    ax.grid(visible=True)
    plt.axis((0,16,-9,12))
    plt.savefig("Граффики 2/"+str(i)+".png")
    plt.close()
