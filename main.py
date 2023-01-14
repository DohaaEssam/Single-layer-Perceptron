import tkinter
from tkinter import *
import Algorithm

def interface():

    top = Tk()
    top.geometry("1000x600")
    top.config(bg="black")
    blank=Label(top, text="blank", bg="black",fg="black", width=20, height=2, anchor=W)
    features = Label(top, text="Select two features", bg="black", fg="white",
                     font=("Helvetica", 14,'bold'), width=20, height=3, anchor=W)

    bill_length = StringVar()
    bill_depth = StringVar()
    flipper_length = StringVar()
    gender = StringVar()
    body_mass = StringVar()
    bias=IntVar()

    bill_length_buttton = Radiobutton(top, text="Bill length", variable=bill_length, value="bill_length_mm", bg="black", fg="cyan",
                               font=("Helvetica", 12,'bold'), width=10
                            )
    bill_depth_button = Radiobutton(top, text="Bill Depth", variable=bill_depth, value="bill_depth_mm", bg="black", fg="cyan",
                               font=("Helvetica", 12,'bold'), width=10
                               )
    flipper_length_button = Radiobutton(top, text="Flipper Length", variable=flipper_length, value="flipper_length_mm", bg="black", fg="cyan",
                               font=("Helvetica", 12,'bold'), width=10
                               )
    gender_button = Radiobutton(top, text="Gender", variable=gender, value="gender", bg="black", fg="cyan",
                               font=("Helvetica", 12,'bold'), width=10
                               )
    body_mass_button = Radiobutton(top, text="Body Mass", variable=body_mass, value="body_mass_g", bg="black", fg="cyan",
                                   font=("Helvetica", 12,'bold'), width=10
                              )

    c = Label(top, text="Select two classes", bg="black", fg="white",
                    font=("Helvetica", 14,'bold'), width=20, height=3, anchor=W)

    class1 = StringVar()
    class2 = StringVar()
    class3 = StringVar()

    class1button = Radiobutton(top, text="Adelie", variable=class1, value="Adelie", bg="black", fg="cyan",
                               font=("Helvetica", 12,'bold'), width=10
                    )
    class2button = Radiobutton(top, text="Gentoo", variable=class2, value="Gentoo", bg="black", fg="cyan",
                               font=("Helvetica", 12,'bold'), width=10
                              )
    class3button = Radiobutton(top, text="Chinstrap", variable=class3, value="Chinstrap", bg="black", fg="cyan",
                               font=("Helvetica", 12,'bold'), width=10
                               )

    learning_rate_label = Label(top, text="Learning Rate", bg="black", fg="white", font=("Helvetica", 14,'bold'), width=20,
                                height=3, anchor=W)
    learning_rate = Entry(top)
    epochs_num_label = Label(top, text="Number of epochs ", bg="black", fg="white", font=("Helvetica", 14,'bold'), width=20,
                             height=3, anchor=W)
    epochs_num = Entry(top)
    add_bias_label = Label(top, text="Bias", bg="black", fg="white", font=("Helvetica", 14,'bold'), width=20, height=3,
                           anchor=W)
    add_bias = Checkbutton(top, text="Add", variable=bias, bg="black", fg="cyan", width=10,
                           font=("Helvetica", 12,'bold'))
    threshold_label = Label(top, text="threshold", bg="black", fg="white", font=("Helvetica", 14, 'bold'),
                                width=20,
                                height=3, anchor=W)
    threshold_in= Entry(top)
    enter = Button(top,text = "Enter" , bg="black", fg="cyan", width=15 , font=("Helvetica", 12,'bold'), command=lambda: mix() )
    blank.grid(row=0)
    features.grid(row=1)
    bill_length_buttton.grid(row=1,column=1)
    bill_depth_button.grid(row=1, column=2)
    flipper_length_button.grid(row=1, column=3)
    gender_button.grid(row=1, column=4)
    body_mass_button.grid(row=1, column=5)
    c.grid(row=2)
    class1button.grid(row=2, column=1)
    class2button.grid(row=2, column=2)
    class3button.grid(row=2, column=3)
    learning_rate_label.grid(row=3)
    learning_rate.grid(row=3, column=1)
    epochs_num_label.grid(row=4)
    epochs_num.grid(row=4, column=1)
    add_bias_label.grid(row=5)
    add_bias.grid(row=5, column=1)
    threshold_label.grid(row=6)
    threshold_in.grid(row=6,column=1)
    enter.grid(row =7)

    def classes_selection(val1, val2, val3):
        c1=[]
        c2=[]
        if val1 == "Adelie" and val2 == "Gentoo":
            class3button['state'] = 'disabled'
            c1, c2 = Algorithm.classes(val1,val2)

        if val1 == "Adelie" and val3 == "Chinstrap":
            class2button['state'] = 'disabled'
            c1, c2 = Algorithm.classes(val1,val3)
        if val2 == "Gentoo" and val3 == "Chinstrap":
            class1button['state'] = 'disabled'
            c1, c2 = Algorithm.classes(val2,val3)
        return c1, c2



    def features_selection(val1,val2,val3,val4,val5):

        f1 =StringVar()
        f2 = StringVar()
        if val1 == "bill_length_mm" and val2 == "bill_depth_mm":
            flipper_length_button['state'] = 'disabled'
            gender_button['state'] = 'disabled'
            body_mass_button['state'] = 'disabled'
            f1 = "bill_length_mm"
            f2 = "bill_depth_mm"
        if val1 == "bill_length_mm" and val3 == "flipper_length_mm":
            bill_depth_button['state'] = 'disabled'
            gender_button['state'] = 'disabled'
            body_mass_button['state'] = 'disabled'
            f1 = "bill_length_mm"
            f2 = "flipper_length_mm"
        if val1 == "bill_length_mm" and val4 == "gender":
            flipper_length_button['state'] = 'disabled'
            bill_depth_button['state'] = 'disabled'
            body_mass_button['state'] = 'disabled'
            f1 = "bill_length_mm"
            f2 = "gender"
        if val1 == "bill_length_mm" and val5 == "body_mass_g":
            flipper_length_button['state'] = 'disabled'
            gender_button['state'] = 'disabled'
            bill_depth_button['state'] = 'disabled'
            f1 = "bill_length_mm"
            f2 = "body_mass_g"
        if val2 == "bill_depth_mm" and val3 == "flipper_length_mm":
            bill_length_buttton['state'] = 'disabled'
            gender_button['state'] = 'disabled'
            body_mass_button['state'] = 'disabled'
            f1 ="bill_depth_mm"
            f2 = "flipper_length_mm"
        if val2 == "bill_depth_mm" and val4 == "gender":
            flipper_length_button['state'] = 'disabled'
            bill_length_buttton['state'] = 'disabled'
            body_mass_button['state'] = 'disabled'
            f1 = "bill_depth_mm"
            f2 = "gender"
        if val2 == "bill_depth_mm" and val5 == "body_mass_g":
            flipper_length_button['state'] = 'disabled'
            gender_button['state'] = 'disabled'
            bill_length_buttton['state'] = 'disabled'
            f1 = "bill_depth_mm"
            f2 = "body_mass_g"
        if val3 == "flipper_length_mm"and val4 == "gender":
            bill_length_buttton['state'] = 'disabled'
            bill_depth_button['state'] = 'disabled'
            body_mass_button['state'] = 'disabled'
            f1 = "flipper_length_mm"
            f2 = "gender"
        if val3 == "flipper_length_mm"and val5 == "body_mass_g":
            bill_length_buttton['state'] = 'disabled'
            gender_button['state'] = 'disabled'
            bill_depth_button['state'] = 'disabled'
            f1 = "flipper_length_mm"
            f2 = "body_mass_g"
        if val4 == "gender" and val5 == "body_mass_g":
            flipper_length_button['state'] = 'disabled'
            bill_depth_button['state'] = 'disabled'
            bill_length_buttton['state'] = 'disabled'
            f1 = "gender"
            f2 = "body_mass_g"
        return f1,f2

    def mix():
        c1,c2=classes_selection(class1.get(), class2.get(), class3.get())
        f1, f2 = features_selection(bill_length.get(), bill_depth.get(), flipper_length.get(), gender.get(),
                                    body_mass.get())
        print(f1,f2)
        if len(c1)!=0 and len(c2)!=0 :
            Algorithm.training(c1, c2, epochs_num.get(), f1, f2, learning_rate.get(),bias.get(),threshold_in.get())



    top.mainloop()


interface()