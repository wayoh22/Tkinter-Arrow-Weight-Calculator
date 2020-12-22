import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkmacosx import Button

mainwindow = Tk()
mainwindow.title("Nock On Arrow Spine Selector")
mainwindow.geometry('1000x680')

mainframe = Frame(mainwindow, background = "lawn green")
mainframe.pack(fill = "both" , expand = True)

#---Functions
def phrase_display():
    prompt = (axis_or_fmj() * arrow_measurement()) + tip_weight_function() + insert_choice_function() + arrow_wrap_function() +(vane_choice_function() * number_of_vanes_function()) + nock_choice_function()
    prompt_display = Text(vertical_frame, height = 5, width = 10)
    prompt_display.pack(fill = "x")
    prompt_display.insert(tk.END, prompt)

axis_400 = 9.0
axis_340 = 9.5
axis_300 = 10.7
axis_260 = 11.5
fmj_400 = 10.2
fmj_340 = 11.3
fmj_300 = 12.0

def axis_or_fmj():
    axis_or_fmj = str(arrow_name.get())
    global spine
    if axis_or_fmj == "Axis":
        spine = axis_or_fmj
        def axis_choice():
            arrow_spine_dd = int(arrow_spine.get())
            global arrow_weight_final
            if arrow_spine_dd == 400:
                arrow_weight_final = axis_400
            elif arrow_spine_dd == 340:
                arrow_weight_final = axis_340
            elif arrow_spine_dd == 300:
                arrow_weight_final = axis_300
            elif arrow_spine_dd == 260:
                arrow_weight_final = axis_300
        axis_choice()
        return arrow_weight_final

    elif axis_or_fmj == "FMJ":
        spine = axis_or_fmj
        def fmj_choice():
            arrow_spine_dd = int(arrow_spine.get())
            global arrow_weight_final
            if arrow_spine_dd == 400:
                arrow_weight_final = fmj_400
            elif arrow_spine_dd == 340:
                arrow_weight_final = fmj_340
            elif arrow_spine_dd == 300:
                arrow_weight_final = fmj_300
            elif arrow_spine_dd == 260:
                arrow_weight_final = 0
        fmj_choice()
        return arrow_weight_final

def arrow_measurement():
    global arrow_measurement
    arrow_measurement = int(arrow_length.get())
    return arrow_measurement

def tip_weight_function():
    global tip_weight_final
    tip_weight_final = tip_weight.get()
    return tip_weight_final

HIT_insert = 16
brass_insert_50 = 50
brass_insert_75 = 75

def insert_choice_function():
    global insert_choice_function
    insert_choice_function = str(insert_choice.get())
    if insert_choice_function == "HIT":
        insert_choice_weight = HIT_insert
    elif insert_choice_function == "50g Brass":
        insert_choice_weight = brass_insert_50
    elif insert_choice_function == "75g Brass":
        insert_choice_weight == brass_insert_75
    return insert_choice_weight

def arrow_wrap_function():
    global arrow_wrap_weight
    arrow_wrapp_choice = str(arrow_wrap.get())
    if arrow_wrapp_choice == "Yes":
        arrow_wrap_weight = 4
    elif arrow_wrapp_choice == "No":
        arrow_wrap_weight = 0
    return arrow_wrap_weight

max_stealth_vane = 9.2
max_hunter_vane = 7.5
max_23_vane = 5
max_pro_vane = 4.9
pm20_target_vane = 4.9

def vane_choice_function():
    global vane_choice_final
    vane_choice_weight = str(vane_choice.get())
    if vane_choice_weight == "Max Stealth Vane":
        vane_choice_final = max_stealth_vane
    elif vane_choice_weight == "Max Hunter Vane":
        vane_choice_final = max_hunter_vane
    elif vane_choice_weight == "Max 23 Vane":
        vane_choice_final = max_23_vane
    elif vane_choice_weight == "Pro Max Vane":
        vane_choice_final = max_pro_vane
    elif vane_choice_weight == "PM 2.0 Target Vane":
        vane_choice_final = pm20_target_vane
    return vane_choice_final

def number_of_vanes_function():
    global number_of_vanes_weight
    number_of_vanes_weight = int(number_of_vanes.get())
    return number_of_vanes_weight

easton_x_nock_weight = 9
nockturnal_nock_weight = 25

def nock_choice_function():
    global nock_weight_final
    nock = str(nock_choice.get())
    if nock == "X Nock":
        nock_weight_final = easton_x_nock_weight
    elif nock == "Nockturnals":
        nock_weight_final = nockturnal_nock_weight
    return nock_weight_final












#---Vertical Layout with Data
vertical_frame = Frame(mainframe, bg = "black")

title = Label(vertical_frame, text = "Nock On Arrow Spine Selector", font = ("Arial", 32), background = "lawn green", foreground = "black", padx = 10, pady = 10)
title.pack(fill = "x")#, padx = 10, pady = 10)

item1 = Label(vertical_frame, text = "Choose things and I'll do the math.", font = ("Arial", 25), background = "black", foreground = "lawn green", padx = 10, pady = 10)
item1.pack(fill = "x")#, padx = 10, pady = 10)
vertical_frame.pack(fill = "x")

#---Horizontal Layout with Data
horizontal_frame = Frame(mainframe, background = "gray30")

#---Button
button_image = ImageTk.PhotoImage(file = "/Users/rtamburro//Desktop/Tkinter_Projects/NockOnLogo.jpg")
img_label = Label(image = button_image)

my_button = Button(horizontal_frame, image = button_image, background = "black", command = phrase_display)
my_button.grid(column = 2, rowspan = 10, sticky = "nsew")

#---Labels and Entries
label1 = Label(horizontal_frame, text = "Axis or FMJ:", font = ("Arial", 16), background = "gray30", foreground = "lawn green", padx = 10, pady = 10, relief = "sunken")
label1.grid(row = 0, column = 0, sticky = "nsew")

arrow_name = StringVar()
arrow_name.set("--- Select ---")
label_1_dropdown = OptionMenu(horizontal_frame, arrow_name, "Axis", "FMJ")
label_1_dropdown.grid(row = 0,column = 1, sticky = "nsew")
label_1_dropdown.config(background = "gray30", foreground = "black")
#----------------------------------------------------------------------------------------------
label2=Label(horizontal_frame, text = "Arrow Spine:", font = ("Arial", 16), background = "gray30",foreground = "lawn green", padx = 10, pady = 10, relief = "sunken")
label2.grid(row = 1,column = 0,sticky = "nsew")
arrow_spine = IntVar()
arrow_spine.set("--- Select ---")
label_2_dropdown = OptionMenu(horizontal_frame, arrow_spine, 400, 340, 300, 260)
label_2_dropdown.grid(row = 1,column = 1, sticky = "nsew")
label_2_dropdown.config(background = "gray30", foreground = "black")
#----------------------------------------------------------------------------------------------
label3=Label(horizontal_frame, text = "Arrow Length:", font = ("Arial", 16), background = "gray30",foreground = "lawn green", padx = 10, pady = 10, relief = "sunken")
label3.grid(row = 2,column = 0,sticky = "nsew")
arrow_length = IntVar()
arrow_length.set("--- Select ---")
label_3_dropdown = OptionMenu(horizontal_frame, arrow_length, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32)
label_3_dropdown.grid(row = 2,column = 1, sticky = "nsew")
label_3_dropdown.config(background = "gray30", foreground = "black")
#----------------------------------------------------------------------------------------------
label4=Label(horizontal_frame, text = "Tip Weight:", font = ("Arial", 16), background = "gray30",foreground = "lawn green", padx = 10, pady = 10, relief = "sunken")
label4.grid(row = 3,column = 0,sticky = "nsew")
tip_weight = IntVar()
tip_weight.set("--- Select ---")
label_4_dropdown = OptionMenu(horizontal_frame, tip_weight, 75, 100, 125, 150, 175, 200)
label_4_dropdown.grid(row = 3,column = 1, sticky = "nsew")
label_4_dropdown.config(background = "gray30", foreground = "black")
#----------------------------------------------------------------------------------------------
label5=Label(horizontal_frame, text = "Type of Insert", font = ("Arial", 16), background = "gray30",foreground = "lawn green", padx = 10, pady = 10, relief = "sunken")
label5.grid(row = 4,column = 0,sticky = "nsew")
insert_choice = StringVar()
insert_choice.set("--- Select ---")
label_5_dropdown = OptionMenu(horizontal_frame, insert_choice, "HIT", "50g Brass", "75g Brass")
label_5_dropdown.grid(row = 4,column = 1, sticky = "nsew")
label_5_dropdown.config(background = "gray30", foreground = "black")
#----------------------------------------------------------------------------------------------
label6=Label(horizontal_frame, text = "Arrow Wrap:", font = ("Arial", 16), background = "gray30",foreground = "lawn green", padx = 10, pady = 10, relief = "sunken")
label6.grid(row = 5,column = 0,sticky = "nsew")
arrow_wrap = StringVar()
arrow_wrap.set("--- Select ---")
label_6_dropdown = OptionMenu(horizontal_frame, arrow_wrap, "Yes", "No")
label_6_dropdown.grid(row = 5,column = 1, sticky = "nsew")
label_6_dropdown.config(background = "gray30", foreground = "black")
#----------------------------------------------------------------------------------------------
label7=Label(horizontal_frame, text = "Vane Choice:", font = ("Arial", 16), background = "gray30",foreground = "lawn green", padx = 10, pady = 10, relief = "sunken")
label7.grid(row = 6,column = 0,sticky = "nsew")
vane_choice = StringVar()
vane_choice.set("--- Select ---")
label_7_dropdown = OptionMenu(horizontal_frame, vane_choice, "Max Stealth Vane", "Max Hunter Vane", "Max 23 Vane", "Max Pro Vane", "PM 2.0 Target Vane")
label_7_dropdown.grid(row = 6,column = 1, sticky = "nsew")
label_7_dropdown.config(background = "gray30", foreground = "black")
#----------------------------------------------------------------------------------------------
label8=Label(horizontal_frame, text = "Number of Vanes:", font = ("Arial", 16), background = "gray30",foreground = "lawn green", padx = 10, pady = 10, relief = "sunken")
label8.grid(row = 7,column = 0,sticky = "nsew")
number_of_vanes = IntVar()
number_of_vanes.set("--- Select ---")
label_8_dropdown = OptionMenu(horizontal_frame, number_of_vanes, 3, 4, 6)
label_8_dropdown.grid(row = 7,column = 1, sticky = "nsew")
label_8_dropdown.config(background = "gray30", foreground = "black")
#----------------------------------------------------------------------------------------------
label9=Label(horizontal_frame, text = "Type of Nock:", font = ("Arial", 16), background = "gray30",foreground = "lawn green", padx = 10, pady = 10, relief = "sunken")
label9.grid(row = 8,column = 0,sticky = "nsew")
nock_choice = StringVar()
nock_choice.set("--- Select ---")
label_9_dropdown = OptionMenu(horizontal_frame, nock_choice, "X Nock", "Nockturnals")
label_9_dropdown.grid(row = 8,column = 1, sticky = "nsew")
label_9_dropdown.config(background = "gray30", foreground = "black")
#----------------------------------------------------------------------------------------------
horizontal_frame.grid_columnconfigure(0, weight = 1)
horizontal_frame.grid_columnconfigure(1, weight = 1)
horizontal_frame.grid_columnconfigure(2, weight = 1)

horizontal_frame.pack(fill = "x")

mainwindow.mainloop()
