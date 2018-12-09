

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
        if cont == PlotPage:
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
        
        

        label_GH1 = tk.Label(self, text="GH_1", font=LARGE_FONT)
        label_GH1.place(x=50,y=50)
        label_GH1unit = tk.Label(self, text="mol/(L^2)", font=LARGE_FONT)
        label_GH1unit.place(x=300,y=50)
        label_IR1 = tk.Label(self, text="IR_1", font=LARGE_FONT)
        label_IR1.place(x=500,y=50) 
        label_IR1unit = tk.Label(self, text="mol/L", font=LARGE_FONT)
        label_IR1unit.place(x=750,y=50)
        self.GH1 = tk.StringVar()
        self.IR1 = tk.StringVar()
        
        entry_GH1 = tk.Entry(self,textvariable=self.GH1)
        entry_GH1.place(x=90, y=50)
        entry_IR1 = tk.Entry(self, textvariable=self.IR1)
        entry_IR1.place(x=540, y=50)
        #self.GH111 = str(entry_GH1.get())
        label_GH2 = tk.Label(self, text="GH_2", font=LARGE_FONT)
        label_GH2.place(x=50,y=80)
        label_GH2unit = tk.Label(self, text="mol/(L^2)", font=LARGE_FONT)
        label_GH2unit.place(x=300,y=80)
        label_IR2 = tk.Label(self, text="IR_2", font=LARGE_FONT)
        label_IR2.place(x=500,y=80) 
        label_IR2unit = tk.Label(self, text="mol/L", font=LARGE_FONT)
        label_IR2unit.place(x=750,y=80)
        self.GH2 = tk.StringVar()
        self.IR2 = tk.StringVar()
        entry_GH2 = ttk.Entry(self, textvariable=self.GH2)
        entry_GH2.place(x=90, y=80)
        entry_IR2 = ttk.Entry(self, textvariable=self.IR2)
        entry_IR2.place(x=540, y=80)

        label_GH3 = tk.Label(self, text="GH_3", font=LARGE_FONT)
        label_GH3.place(x=50,y=110)
        label_GH3unit = tk.Label(self, text="mol/(L^2)", font=LARGE_FONT)
        label_GH3unit.place(x=300,y=110)
        label_IR3 = tk.Label(self, text="IR_3", font=LARGE_FONT)
        label_IR3.place(x=500,y=110) 
        label_IR3unit = tk.Label(self, text="mol/L", font=LARGE_FONT)
        label_IR3unit.place(x=750,y=110)
        self.GH3 = tk.StringVar()
        self.IR3 = tk.StringVar()
        entry_GH3 = ttk.Entry(self, textvariable=self.GH3)
        entry_GH3.place(x=90, y=110)
        entry_IR3 = ttk.Entry(self, textvariable=self.IR3)
        entry_IR3.place(x=540, y=110)

        label_GH4 = tk.Label(self, text="GH_4", font=LARGE_FONT)
        label_GH4.place(x=50,y=140)
        label_GH4unit = tk.Label(self, text="mol/(L^2)", font=LARGE_FONT)
        label_GH4unit.place(x=300,y=140)
        label_IR4 = tk.Label(self, text="IR_4", font=LARGE_FONT)
        label_IR4.place(x=500,y=140) 
        label_IR4unit = tk.Label(self, text="mol/L", font=LARGE_FONT)
        label_IR4unit.place(x=750,y=140)
        self.GH4 = tk.StringVar()
        self.IR4 = tk.StringVar()
        entry_GH4 = ttk.Entry(self, textvariable=self.GH4)
        entry_GH4.place(x=90, y=140)
        entry_IR4 = ttk.Entry(self, textvariable=self.IR4)
        entry_IR4.place(x=540, y=140)

        self.GH1.set("1.2")
        self.IR1.set("2.0")
        self.GH2.set("1.9")
        self.IR2.set("3.9")
        self.GH3.set("3.0")
        self.IR3.set("6.1")
        self.GH4.set("4.2")
        self.IR4.set("7.9")



        button_confirm = ttk.Button(self, text="Enter", width = 50, command=lambda: controller.show_frame(PlotPage))
        button_confirm.place(x=400, y=200)
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
        self.a.scatter(self.x, self.y)
        self.a.plot(self.x, self.y_pre, '--')
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
        label = tk.Label(self, text="ResultPage", font=LL_FONT)
        label.pack(pady=10, padx=10)
        
        
        button1 = ttk.Button(self, text="Back to Home",command=lambda: controller.show_frame(StartPage))
        button1.pack(side='bottom')
app = LGEmodel()
app.geometry('1280x720')
#
# 主消息循环:
app.mainloop()
