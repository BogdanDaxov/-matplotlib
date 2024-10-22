import matplotlib.pyplot as plt


with open("00"+"1"+".dat") as f :
    a=f.read().split("\n")
n=int(a[0])
plt.title("Number of points: "+str(n))
x=[]
y=[]
for g in range(1,n+1):
    x.append(float(a[g].split(" ")[0]))
    y.append(float(a[g].split(" ")[1]))
plt.scatter(x,y)
plt.savefig("1_1.png")
plt.close()


with open("00"+"2"+".dat") as f :
    a=f.read().split("\n")
n=int(a[0])
plt.title("Number of points: "+str(n))
x=[]
y=[]
for g in range(1,n+1):
    x.append(float(a[g].split(" ")[0]))
    y.append(float(a[g].split(" ")[1]))
plt.scatter(x,y)
plt.savefig("1_2.png")
plt.close()

with open("00"+"3"+".dat") as f :
    a=f.read().split("\n")
n=int(a[0])
plt.title("Number of points: "+str(n))
x=[]
y=[]
for g in range(1,n+1):
    x.append(float(a[g].split(" ")[0]))
    y.append(float(a[g].split(" ")[1]))
plt.scatter(x,y)
plt.savefig("1_3.png")
plt.close()

with open("00"+"4"+".dat") as f :
    a=f.read().split("\n")
n=int(a[0])
plt.title("Number of points: "+str(n))
x=[]
y=[]
for g in range(1,n+1):
    x.append(float(a[g].split(" ")[0]))
    y.append(float(a[g].split(" ")[1]))
plt.scatter(x,y,s=1)
plt.savefig("1_4.png")
plt.close()

with open("00"+"5"+".dat") as f :
    a=f.read().split("\n")
n=int(a[0])
plt.title("Number of points: "+str(n))
x=[]
y=[]
for g in range(1,n+1):
    x.append(float(a[g].split(" ")[0]))
    y.append(float(a[g].split(" ")[1]))
plt.scatter(x,y,s=0.1)
plt.savefig("1_5.png")
plt.close()
