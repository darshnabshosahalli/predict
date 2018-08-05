from matplotlib import pyplot
import math
import os
import tkinter as tk
class Regression:
    x=[]
    y=list()
    q0=0
    q1=0
    m=0
    a=-3.8732586702082443
    b=1.1907710440912829
    acc=0
    def home_page(self):
        root = tk.Tk()
        root.title("price predictor")
        root.geometry("500x300")
        root.resizable(0,0)
        head = tk.Label(root,text='Profit Predictor')
        head.config(font=('Times New Roman','30'))
        head.place(x='140',y='10')
        target = tk.Label(root,text='Population')
        target.config(font=('Times New Roman', '15'))
        target.place(x='40', y='100')
        predict = tk.Label(root,text='Profit(%)')
        predict.config(font=('Times New Roman', '15'))
        predict.place(x='40', y='150')
        accuracy = tk.Label(root,text='Accuracy(%)')
        accuracy.config(font=('Times New Roman', '15'))
        accuracy.place(x='40', y='200')
        pop = tk.Entry(root,width=30)
        pop.place(x='130',y='100')
        pred = tk.Entry(root,width=30)
        pred.place(x='130', y='150')
        acc = tk.Entry(root,width=25)
        acc.place(x='160', y='200')

        def calc():
            print("calc  in")
            a=0

            xc = float(pop.get())/10000
            yc=(self.a+self.b*xc)
            ac=str(('%.2f'%(yc))+str('%'))
            pred.insert(0,ac)
            self.test_data()
            ac=str(('%.2f'%(self.acc))+str('%'))
            acc.insert(0,ac)

        cal = tk.Button(root,text="calculate",command=calc)
        cal.place(x='255', y='230')
        trn = tk.Button(root, text="Train Data", command=self.gradient)
        trn.place(x='30', y='30')
        grph = tk.Button(root,text="data plot",command=self.plot_data)
        grph.place(x='380',y='100')
        curve = tk.Button(root,text="curve fit",command=self.curve_fit)
        curve.place(x='380',y='200')
        init = tk.Button(root,text="inital fit",command=self.init_fit)
        init.place(x='380',y='150')
        root.mainloop()

    def test_data(self):
        a=0
        r=72
        j=1
        for i in range(72,len(self.x)) :
            h=self.a+self.b*self.x[i]
            a=a+abs(self.y[i]-h)/j
            j+=1
        self.acc=a*10

    def init_fit(self):
        pyplot.title("initial fit")
        pyplot.xlabel("population in 10000's")
        pyplot.ylabel("profit(%)")
        pyplot.xticks(range(0, 30))
        pyplot.yticks(range(-5, 30))
        pyplot.plot(self.x, self.y, 'gx')
        pyplot.grid(True)
        h = list()
        for i in self.x:
            h.append(0)
        pyplot.plot(self.x, h, 'r-')
        pyplot.show()

    def curve_fit(self):
        pyplot.title("curve fit after model training")
        pyplot.xlabel("population in 10000's")
        pyplot.ylabel("profit(%)")
        pyplot.xticks(range(0, 30))
        pyplot.yticks(range(-5, 30))
        pyplot.plot(self.x, self.y, 'gx')
        pyplot.grid(True)
        h=list()
        print("qo = " + str(self.q0) + "q1 = " + str(self.q1))
        for i in self.x:
            h.append(-3.8732586702082443+1.1907710440912829*i)
        pyplot.plot(self.x,h,'r-')
        pyplot.show()

    def read_data(self):
        os.chdir("C:\\Users\\Shiva\\Desktop\\machine-learning-ex1\\ex1")
        f=open("ex1data1.txt")
        for lines in f:
            lines=lines.rstrip()
            a=float(lines[:lines.index(',')])
            b=float(lines[lines.index(',')+1:])
            self.x.append(a)
            self.y.append(b)
        self.m=len(self.x)

    def print_data(self):
        print("x = "+str(self.x)+"\n y = "+str(self.y))

    def plot_data(self):
        print("in")
        pyplot.title("data Plot")
        pyplot.xlabel("population in 10000's")
        pyplot.ylabel("profit(%)")
        pyplot.xticks(range(0, 30))
        pyplot.yticks(range(-5, 30))
        pyplot.plot(self.x,self.y,'gx')
        pyplot.grid(True)
        pyplot.show()

    def hypothesis(self,q0,q1,a):
        return q0+q1*a

    def cost_function(self,q0,q1):
        j=0
        for i in range(self.m):
            h=Regression.hypothesis(self,q0,q1,self.x[i])
            j=j+math.pow((h-self.y[i]),2)
        return j/self.m

    def deriv_j(self,q0,q1):
        a=0
        b=0
        for i in range(self.m):
            h=Regression.hypothesis(self,q0,q1,self.x[i])
            a=a+(h-self.y[i])
            b=b+((h-self.y[i])*self.x[i])
        a=(2/self.m)*a
        b=(2/self.m)*b
        return a,b

    def gradient(self):
        a0=0
        a1=0
        p=0
        for i in range(15000):
            h = list()
            print(i)
            d0,d1=Regression.deriv_j(self,self.q0,self.q1)
            a0=self.q0-0.0015*d0
            a1=self.q1-0.0015*d1
            self.q0=a0
            self.q1=a1
            if  abs(Regression.cost_function(self,self.q0,self.q1)-p)<0.0000001:
                break
            else:
                p=Regression.cost_function(self,self.q0,self.q1)
            for i in range(self.m):
                h.append(Regression.hypothesis(self,self.q0,self.q1,self.x[i]))
        #pyplot.clf()
        #Regression.plot_data(self)
        #pyplot.plot(self.x,h,'r-')


if __name__=="__main__":
    p=Regression()
    p.read_data()
    print(p.m)
    p.print_data()
    p.home_page()
    #p.plot_data()
    #pyplot.show()
    #p.gradient()
    #pyplot.show()
    #print("q0 = "+str(p.q0)+" q1 = "+str(p.q1))
    #x=float(input("enter the popluation"))
    #y=-3.8732586702082443+1.1907710440912829*x
    #print(y)



















