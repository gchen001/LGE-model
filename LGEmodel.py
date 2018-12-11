

import tkinter as tk
from tkinter import  ttk
from tkinter import messagebox
import numpy as np
import matplotlib.backends.tkagg as tkagg
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
LARGE_FONT = ("Verdana", 12)
LL_FONT = ("Verdana", 18)
#global testGH1
#testGH1="nan"
class LGEmodel(tk.Tk):
    
    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.wm_title(self, "LGE_model")
        
        container = tk.Frame(self)
        container.pack(side = "top", fill = "both", expand = True)
        container.grid_rowconfigure(0, weight =1)
        container.grid_columnconfigure(0, weight=1)
        
        self.frames = {}
        
        for F in (StartPage, InputPage, PlotPage, ResultPage):
            #print(F)
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        
        self.show_frame(StartPage)
    
    def show_frame(self, cont):
        #for frame in self.frames.values():
        #    frame.grid_forget()
        frame = self.frames[cont]
        if cont == PlotPage or cont == ResultPage:
            frame.update()
        frame.tkraise()
    def get_page(self, page_class):
        return self.frames[page_class]


# In[16]:


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text=("""This app is to help to determine the salt concentration 
        	in one-step elution based on the linear gradient elution results and LGE model developed in early 1980s by Yamamoto et al."""), font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        button1 = ttk.Button(self, text="Start",
                            command=lambda: controller.show_frame(InputPage))
        button1.pack()
        
        button2 = ttk.Button(self, text="Quit", 
                            command=quit)
        button2.pack()


# In[17]:


class InputPage(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="InputPage", font=LL_FONT)
        label.pack(pady=10, padx=10)
        
        

        label_GH1 = ttk.Label(self, text="GH_1", font=LARGE_FONT)
        label_GH1.place(x=50,y=50)
        label_GH1unit = ttk.Label(self, text="mol/(L^2)", font=LARGE_FONT)
        label_GH1unit.place(x=300,y=50)
        label_IR1 = ttk.Label(self, text="IR_1", font=LARGE_FONT)
        label_IR1.place(x=500,y=50) 
        label_IR1unit = ttk.Label(self, text="mol/L", font=LARGE_FONT)
        label_IR1unit.place(x=750,y=50)
        self.GH1 = tk.StringVar()
        self.IR1 = tk.StringVar()
        
        entry_GH1 = ttk.Entry(self,textvariable=self.GH1)
        entry_GH1.place(x=100, y=50)
        entry_IR1 = ttk.Entry(self, textvariable=self.IR1)
        entry_IR1.place(x=550, y=50)
        #self.GH111 = str(entry_GH1.get())
        label_GH2 = ttk.Label(self, text="GH_2", font=LARGE_FONT)
        label_GH2.place(x=50,y=100)
        label_GH2unit = ttk.Label(self, text="mol/(L^2)", font=LARGE_FONT)
        label_GH2unit.place(x=300,y=100)
        label_IR2 = ttk.Label(self, text="IR_2", font=LARGE_FONT)
        label_IR2.place(x=500,y=100) 
        label_IR2unit = ttk.Label(self, text="mol/L", font=LARGE_FONT)
        label_IR2unit.place(x=750,y=100)
        self.GH2 = tk.StringVar()
        self.IR2 = tk.StringVar()
        entry_GH2 = ttk.Entry(self, textvariable=self.GH2)
        entry_GH2.place(x=100, y=100)
        entry_IR2 = ttk.Entry(self, textvariable=self.IR2)
        entry_IR2.place(x=550, y=100)

        label_GH3 = ttk.Label(self, text="GH_3", font=LARGE_FONT)
        label_GH3.place(x=50,y=150)
        label_GH3unit = ttk.Label(self, text="mol/(L^2)", font=LARGE_FONT)
        label_GH3unit.place(x=300,y=150)
        label_IR3 = ttk.Label(self, text="IR_3", font=LARGE_FONT)
        label_IR3.place(x=500,y=150) 
        label_IR3unit = ttk.Label(self, text="mol/L", font=LARGE_FONT)
        label_IR3unit.place(x=750,y=150)
        self.GH3 = tk.StringVar()
        self.IR3 = tk.StringVar()
        entry_GH3 = ttk.Entry(self, textvariable=self.GH3)
        entry_GH3.place(x=100, y=150)
        entry_IR3 = ttk.Entry(self, textvariable=self.IR3)
        entry_IR3.place(x=550, y=150)

        label_GH4 = ttk.Label(self, text="GH_4", font=LARGE_FONT)
        label_GH4.place(x=50,y=200)
        label_GH4unit = ttk.Label(self, text="mol/(L^2)", font=LARGE_FONT)
        label_GH4unit.place(x=300,y=200)
        label_IR4 = ttk.Label(self, text="IR_4", font=LARGE_FONT)
        label_IR4.place(x=500,y=200) 
        label_IR4unit = ttk.Label(self, text="mol/L", font=LARGE_FONT)
        label_IR4unit.place(x=750,y=200)
        self.GH4 = tk.StringVar()
        self.IR4 = tk.StringVar()
        entry_GH4 = ttk.Entry(self, textvariable=self.GH4)
        entry_GH4.place(x=100, y=200)
        entry_IR4 = ttk.Entry(self, textvariable=self.IR4)
        entry_IR4.place(x=550, y=200)

        label_IC = ttk.Label(self, text = "Ionic Capacity", font=LARGE_FONT)
        label_IC.place(x=50,y=250)
        label_ICunit = ttk.Label(self, text="mM", font=LARGE_FONT)
        label_ICunit.place(x=350, y=250)
        self.IC = tk.StringVar()
        entry_IC = ttk.Entry(self,textvariable=self.IC)
        entry_IC.place(x=150, y=250)

        self.GH1.set("34.41")
        self.IR1.set("0.2393")
        self.GH2.set("17.21")
        self.IR2.set("0.2295")
        self.GH3.set("11.47")
        self.IR3.set("0.2200")
        self.GH4.set("8.60")
        self.IR4.set("0.2151")
        self.IC.set("105.58")



        button_confirm = ttk.Button(self, text="Enter", width = 50, command=lambda: controller.show_frame(PlotPage))
        button_confirm.place(x=400, y=350)
        button1 = ttk.Button(self, text="Back to Home",command=lambda: controller.show_frame(StartPage))
        button1.pack(side='bottom')



class PlotPage(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="PlotPage", font=LL_FONT)
        label.pack(pady=10, padx=10)
    
        inputpage = self.controller.get_page(InputPage)
        self.GH1 = inputpage.GH1.get()
        self.IR1 = inputpage.IR1.get()
        self.GH2 = inputpage.GH2.get()
        self.IR2 = inputpage.IR2.get()
        self.GH3 = inputpage.GH3.get()
        self.IR3 = inputpage.IR3.get()
        self.GH4 = inputpage.GH4.get()
        self.IR4 = inputpage.IR4.get()
        self.y = [float(self.GH1),float(self.GH2),float(self.GH3),float(self.GH4)]
        self.x = [float(self.IR1),float(self.IR2),float(self.IR3),float(self.IR4)]

        self.fig = Figure(figsize=(5,5), dpi=100)
        #self.a = self.fig.add_subplot(111, xlabel='IR', ylabel='GH')
        self.a = self.fig.add_subplot(111)
        self.a.plot(self.y,self.x)
        self.a.set_ylabel('log(GH)')
        self.a.set_xlabel('log(IR)')
        #self.fig.legend("GH = %10.5f * IR + %10.5f"%(self.m, self.n), loc=0)



        
        canvas = FigureCanvasTkAgg(self.fig, self)
        self.canvas = canvas
        self.canvas.draw()
        canvas_widget = canvas.get_tk_widget()
        self.canvas_widget = canvas_widget
        canvas_widget.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        
        button1 = ttk.Button(self, text="Back to Home",command=lambda: controller.show_frame(StartPage))
        button1.pack(side='bottom')
        button2 = ttk.Button(self, text="<-Back",command=lambda: controller.show_frame(InputPage))
        button2.pack(side='bottom')
        button2 = ttk.Button(self, text="Next->",command=lambda: controller.show_frame(ResultPage))
        button2.pack(side='bottom')

    def update(self):

        inputpage = self.controller.get_page(InputPage)
        self.GH1 = float(inputpage.GH1.get())
        self.IR1 = inputpage.IR1.get()
        self.GH2 = inputpage.GH2.get()
        self.IR2 = inputpage.IR2.get()
        self.GH3 = inputpage.GH3.get()
        self.IR3 = inputpage.IR3.get()
        self.GH4 = inputpage.GH4.get()
        self.IR4 = inputpage.IR4.get()
        try:
            self.GH1 = float(self.GH1)
        except:
            pass
        
        try:
            self.IR1 = float(self.IR1)
        except:
            pass            
        
        try:
            self.GH2 = float(self.GH2)
        except:
            pass
        
        try:
            self.IR2 = float(self.IR2)
        except:
            pass
        
        try:
            self.GH3 = float(self.GH3)
        except:
            pass
        
        try:
            self.IR3 = float(self.IR3)
        except:
            pass
        
        try:
            self.GH4 = float(self.GH4)
        except:
            pass

        try:
            self.IR4 = float(self.IR4)
        except:
            pass

        zero_flag = 0
        for i in [self.GH1, self.GH2, self.GH3, self.GH4, self.IR1, self.IR2, self.IR3, self.IR4 ]:
            if i == 0:
                zero_flag = 1
        if zero_flag == 1:
            messagebox.showinfo(title='Notation', message='GH and IR could not be assigned as 0')


        #self.y = [float(self.GH1),float(self.GH2),float(self.GH3),float(self.GH4)]
        #self.x = [float(self.IR1),float(self.IR2),float(self.IR3),float(self.IR4)]
        #print(self.x, self.y)

        self.x = []
        self.y = []
        if type(self.GH1) == float and self.GH1 > 0 and type(self.IR1) == float and self.IR1 > 0:
            self.x.append(np.log10(self.IR1))
            self.y.append(np.log10(self.GH1))
        if type(self.GH2) == float and self.GH2 > 0 and type(self.IR2) == float and self.IR2 > 0:
            self.x.append(np.log10(self.IR2))
            self.y.append(np.log10(self.GH2))
        if type(self.GH3) == float and self.GH3 > 0 and type(self.IR3) == float and self.IR3 > 0:
            self.x.append(np.log10(self.IR3))
            self.y.append(np.log10(self.GH3))
        if type(self.GH4) == float and self.GH4 > 0 and type(self.IR4) == float and self.IR4 > 0:
            self.x.append(np.log10(self.IR4))
            self.y.append(np.log10(self.GH4))

        #print(self.x, self.y)
        self.x = np.array(self.x)
        self.y = np.array(self.y)
        self.m, self.n = np.polyfit(self.x, self.y, 1)
        #print(type(self.x), type(self.y), type(self.m), type(self.n))
        self.y_pre = self.m * self.x + self.n

        self.a.clear()
        self.a.scatter(self.x, self.y, color='orange')
        self.a.plot(self.x, self.y_pre, 'b--')
        self.a.set_ylabel('log(GH)')
        self.a.set_xlabel('log(IR)')
        self.canvas.draw()
        
        '''
        self.fig_x, self.fig_y = 100, 100
        self.fig_photo = self.draw_figure(self.canvas, self.fig, self.fig_x, self.fig_y)
        self.fig_w, self.fig_h = self.fig_photo.width(), self.fig_photo.height()
        '''
        #self.label_1['text'] = str(self.v)




class ResultPage(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="ResultPage", font=LL_FONT)
        label.pack(pady=10, padx=10)
        plotpage = self.controller.get_page(PlotPage)
        try:
            self.m = plotpage.m.get()
            label1 = tk.Label(self, text="m should be"+str(self.m), font=LARGE_FONT)
        except:
            pass
            label1 = tk.Label(self, text="m didnt pass to this page", font=LARGE_FONT)
        #label1 = tk.Label(self, text="m should be"+str(m), font=LARGE_FONT)
        self.label1 = label1
        label1.pack()


        self.fig = Figure(figsize=(5,5), dpi=100)
        #self.a = self.fig.add_subplot(111, xlabel='IR', ylabel='GH')
        self.a = self.fig.add_subplot(111)
        #self.a.plot(self.y,self.x)
        self.a.set_ylabel('K')
        self.a.set_xlabel('Ionic Concentration(mM)')
        #self.fig.legend("GH = %10.5f * IR + %10.5f"%(self.m, self.n), loc=0)
        canvas = FigureCanvasTkAgg(self.fig, self)
        self.canvas = canvas
        self.canvas.draw()
        canvas_widget = canvas.get_tk_widget()
        self.canvas_widget = canvas_widget
        canvas_widget.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


        
        button1 = ttk.Button(self, text="Back to Home",command=lambda: controller.show_frame(StartPage))
        button1.pack(side='bottom')

    def update(self):
        plotpage = self.controller.get_page(PlotPage)
        inputpage = self.controller.get_page(InputPage)
        self.IC = float(inputpage.IC.get())*0.001
        self.m = float(plotpage.m)
        self.n = float(plotpage.n)
        self.B = self.m - 1
        #self.IC = 105.58 * 0.001 # This value needs further modification.
        self.Keq = np.power(10,-self.n)/(self.m*np.power(self.IC,self.B))

        self.I = np.arange(20,500,5)
        self.len_I = len(self.I)
        self.k = -1*np.ones(self.len_I)
        self.flag = 0
        self.best_k = -111
        self.best_I = -111
        for i,j in zip(self.I, np.arange(self.len_I)):
            self.k[j] = self.Keq*np.power(self.IC,self.B)*np.power(i*0.001,-self.B)+0.8
            #self.k[j] = self.Keq*np.power(0.10558,11.68473)*np.power(i*0.001,-11.68473)+0.8
            if self.k[j] < 0.81 and self.flag == 0:
                self.best_k = self.k[j]
                self.best_I = i
                self.flag = 1
                #print(self.IC,self.B)
        self.a.clear()
        #fig = plt.figure(figsize=(20,8),dpi=80)
        #ax = fig.add_subplot(111)
        self.a.plot(self.I,self.k,'b-')
        self.a.scatter(self.best_I, self.best_k,color='r')
        self.a.annotate('best choice I =%6.2f mM, K =%6.2f mM'%(self.best_I, self.best_k), xy=(self.best_I, self.best_k), 
            xytext = (+50,+50), textcoords='offset points',xycoords='data',  
            fontsize=16, arrowprops=dict(arrowstyle='->', connectionstyle="arc3,rad=.2"))
        self.a.set_ylabel('K')
        self.a.set_xlabel('Ionic Concentration(mM)')
        self.canvas.draw()
        self.label1['text']="slope:%5.2f,  interception:%5.2f,  B:%5.2f,  Keq:%5.2f"%(self.m, self.n, self.B, self.Keq)




app = LGEmodel()
app.geometry('1280x720')
#
# 主消息循环:
app.mainloop()
