import pyPasswordGen as pg
import tkinter as tk
perfectVar = False
creationCounter = 0
def PerfectMode():
    global perfectVar
    if perfectVar == False:
        Perf.config(relief='sunken')
        A.configure(to=102)
        N.configure(to=102)
        S.configure(to=102)
        perfectVar = True
    else:
        Perf.config(relief='raised')
        A.configure(to=100)
        N.configure(to=100)
        S.configure(to=100)
        perfectVar = False
def setSlides(SetA,SetN,SetS):
    A.set(SetA)
    N.set(SetN)
    S.set(SetS)
def runPassGen():
    global creationCounter
    creationCounter +=1
    Amount = M.get()
    for i in range(0,Amount):
        alp = A.get()
        num = N.get()
        spe = S.get()
        leng = L.get()
        restricted = Rest.get("1.0",tk.END)
        output = str(pg.PassGeneratorSampl(alp,num,spe,leng,restricted))
        #print(output)
        Outp.insert(1.0,output+'\n')
        #Outp.insert(tk.END,'\n')
    Outp.insert(1.0,'--G#'+str(creationCounter)+'('+str(alp)+','+str(num)+','+str(spe)+')--\n')
root = tk.Tk()
root.title("Password Generator by Ralsdoge")

# Create three labels
label1 = tk.Label(root, text="Randomized Password Generator V1.0")
label2 = tk.Label(root, text="These sliders adjust the \nweight given to the \nspecific type of character\nto be randomly chosen.\n\nSeperate illegal characters\nwith ,'s.")
label3 = tk.Label(root, text="Illegal Characters:")
A = tk.Scale(root, from_=0, to=100,orient = "horizontal")
N = tk.Scale(root, from_=0, to=100,orient = "horizontal")
S = tk.Scale(root, from_=0, to=100,orient = "horizontal")
L = tk.Scale(root, from_=1, to=30,orient = "vertical")
M = tk.Scale(root, from_=1, to=10,orient = "vertical")

Atxt = tk.Label(root, text="Alphabetic")#al")
Ntxt = tk.Label(root, text="Numerical")
Stxt = tk.Label(root, text="Special")
Ltxt = tk.Label(root, text="Length")
Mtxt = tk.Label(root, text="# of Gens")
Pre1 = tk.Button(root,text="Preset #1",command=lambda: setSlides(19,14,20))
Pre2 = tk.Button(root,text="Preset #2",command=lambda: setSlides(1,2,2))
Pre3 = tk.Button(root,text="Preset #3",command=lambda: setSlides(3,1,4))
Pre4 = tk.Button(root,text="Preset #4",command=lambda: setSlides(70,40,40))
Perf = tk.Button(root,text="PerfMode",command=lambda: PerfectMode())
Gogo = tk.Button(root,text='Generate',command=lambda: runPassGen())
Outp = tk.Text(root,height = 10,width = 25,bg = "light yellow")
Rest = tk.Text(root,height = 1,width = 25,bg = "pink")
Cler = tk.Button(root,text=' Clear ',width=7,command=lambda: Outp.delete('1.0', tk.END))

label1.grid(row=0, column=0,columnspan=4)
label2.grid(row=1, column=0,rowspan=3,columnspan=2,sticky='n')
label3.grid(row=3, column=0,rowspan=1,columnspan=2,sticky='sw')
Atxt.grid(row=1, column=2)
Ntxt.grid(row=2, column=2)
Stxt.grid(row=3, column=2)
Ltxt.grid(row=6, column=4)
Mtxt.grid(row=6, column=3)
A.grid(row=1, column=3,columnspan=2)
N.grid(row=2, column=3,columnspan=2)
S.grid(row=3, column=3,columnspan=2)
L.grid(row=7, column=4,rowspan=2)#columnspan=2)
M.grid(row=7, column=3,rowspan=2)#columnspan=2)
A.set(100)
N.set(100)
S.set(100)
L.set(20)
M.set(1)
Pre1.grid(row=4,column=3)
Pre2.grid(row=4,column=4)
Pre3.grid(row=5,column=3)
Pre4.grid(row=5,column=4)
Perf.grid(row=0,column=4)
Gogo.grid(row=9,column=0)
Cler.grid(row=9,column=2)
Rest.grid(row=4,column=0,columnspan=3,rowspan=1)
Outp.grid(row=5,column=0,columnspan=3,rowspan=3)
root.mainloop()