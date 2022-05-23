import tkinter as tk                
from tkinter import Label, font  as tkfont 

import random
from random import choice

class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, PageOne, PageTwo):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="I Need a Pump", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="Phase One",
                            command=lambda: controller.show_frame("PageOne"))
        button2 = tk.Button(self, text="Phase Two",
                            command=lambda: controller.show_frame("PageTwo"))
        button1.pack()
        button2.pack()


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='green')
        self.controller = controller
        label = tk.Label(self, text="Phase One", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack(pady=10)


        mid_press_list = ['dumbell flat bench', 'barbell flat bench', 'hammer strength flat']
        mid_fly_list = ['standing cable mid', 'pec dec']
        lower_chest_list = ['dips', 'standing cable low fly']
        

        def chest_one():
            mid_press = random.choice(mid_press_list)
            mid_fly = random.choice(mid_fly_list)
            lower_chest = random.choice(lower_chest_list)
            print((mid_fly_list),(mid_press_list))
            mid_press_label = Label(self, text = mid_press).pack()
            mid_fly_label = Label(self, text = mid_fly).pack()
            lower_chest_label = Label(self, text = lower_chest).pack()


        phaseone_chest_button=tk.Button(self, text='Chest', command=chest_one,).pack()


        upper_back_list = ['high tbar', 'high machine row', 'straight bar lat pull', 'high seated cable', 'pull ups']
        mid_back_list = ['mid tbar', 'mid machine row', 'mid db row', 'hammer strength row', 'bb row', 'close grip cable']

        def back_one():
            upper_back = random.choice(upper_back_list)
            mid_back = random.choice(mid_back_list)
            print((upper_back_list),( mid_back_list))
            upper_back_label = Label(self, text = upper_back).pack()
            mid_back_label = Label(self, text = mid_back).pack()
            


        phaseone_back_button=tk.Button(self, text='Back', command=back_one,).pack()


        shoulder_press_list = ['smith machine press', 'dumbell shoulder press']
        front_delt_list = ['seated db front raise', 'standing chest assisted front raise', 'cable front delt raise']
        side_delt_list = ['machine lateral raise', 'seated db lateral raise', 'cable lateral raise']
        rear_delt_list = ['cable rear delt pull', 'chest support rear delt swing', 'chest supported rear delt row']

        def shoulder_one():
            shoulder_press = random.choice(shoulder_press_list)
            front_delt = random.choice(front_delt_list)
            side_delt = random.choice(side_delt_list)
            rear_delt = random.choice(rear_delt_list)
            print((shoulder_press_list),(front_delt_list), (side_delt_list), (rear_delt_list))
            shoulder_press_label = Label(self, text = shoulder_press).pack()
            front_delt_label = Label(self, text = front_delt).pack()
            side_delt_label = Label(self, text = side_delt).pack()
            rear_delt_label = Label(self, text = rear_delt).pack()

        phaseone_shoulder_button=tk.Button(self, text='Shoulders', command=shoulder_one,).pack()



        bicep_list = ['db hammer curl', 'rope cable hammer curl', 'EZ bar curl', 'straight bar cable', 'seated db curl', 'face away curls', 'preacher curl']
        tricep_list = ['tricep pull down', 'tricep push down', 'skull crusher', 'overhead pulls', 'cross cable tri extension', 'single arm cable extensions']

        def bicep_tricep():
            bicep = random.choice(bicep_list)
            tricep = random.choice(tricep_list)
            print((bicep),(tricep))
            bicep_label = Label(self, text = bicep).pack()
            tricep_label = Label(self, text = tricep).pack()

        arms_button=tk.Button(self, text='Arms', command=bicep_tricep,).pack()







class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='purple')
        self.controller = controller
        label = tk.Label(self, text="Phase Two", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()

        upper_press_list = ['dumbell incline bench', 'barbell incline bench', 'hammer strength incline']
        upper_fly_list = ['standing cable high', 'pec dec']
        lower_chest_list = ['dips', 'standing cable low fly']
        

        def chest_two():
            upper_press = random.choice(upper_press_list)
            upper_fly = random.choice(upper_fly_list)
            lower_chest = random.choice(lower_chest_list)
            print((upper_fly_list),(upper_press_list), (lower_chest_list))
            upper_press_label = Label(self, text = upper_press).pack()
            upper_fly_label = Label(self, text = upper_fly).pack()
            lower_chest_label = Label(self, text = lower_chest).pack()


        phasetwo_chest_button=tk.Button(self, text='Chest', command=chest_two,).pack()


        upper_lat_list = ['hammer strength lat pull', 'single arm high cable']
        mid_lat_list = ['standing hammer strength lat pull', 'd handle cable lat pull', 'neutral grip bar cable lat pull', 'dumbell chest supported lat row']

        def back_two():
            upper_lat = random.choice(upper_lat_list)
            mid_lat = random.choice(mid_lat_list)
            print((upper_lat_list),( mid_lat_list))
            upper_lat_label = Label(self, text = upper_lat).pack()
            mid_lat_label = Label(self, text = mid_lat).pack()
            


        phasetwo_lat_button=tk.Button(self, text='Back', command=back_two,).pack()


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()