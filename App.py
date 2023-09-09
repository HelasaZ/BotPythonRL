from tkinter import *
from main import Read
import matplotlib.pyplot as plt
import numpy as np
from pandas import *


class App(Read):

    def __init__(self):
        # Fenêtre
        super().__init__()
        window = Tk()
        window.title("Bot Trading RL")
        window.geometry("1280x720")
        window.resizable(False, False)
        window.iconbitmap("LOGORL.ico")
        window.config(background="blue")

        # Frame
        frame = Frame(window, bg='blue')

        # Image
        bg = PhotoImage(file="background.png")
        label1 = Label(window, image=bg)
        label1.place(x=0, y=0)

        readfennec = Read().get_Fennec()
        readzomba = Read().get_Zomba()
        readoctane = Read().get_Octane()
        readmainframe = Read().get_Mainframe()
        readinterstellar = Read().get_Interstellar()

        mtext = Read().get_mtext()
        itext = Read().get_itext()
        otext = Read().get_otext()
        ztext = Read().get_ztext()
        ftext = Read().get_ftext()

        def WindowF():
            newWindow = Toplevel(window)
            newWindow.geometry("400x600")
            newWindow.resizable(False, False)
            newWindow.iconbitmap("LOGORL.ico")
            newWindow.config(background="red")

            bk = PhotoImage(file="aze.png")
            canvas = Canvas(newWindow, width=400, height=600)
            canvas.pack(expand=YES, fill=BOTH)

            canvas.create_image(50, 10, image=bk, anchor=NW)
            canvas.bk = bk
            canvas.place(x=0, y=0)

            label_text = Label(newWindow, text="{0} \n Son pourcentage est d'actuellement de : {1} %".format(ftext, readfennec), font=("Heroes Legend", 8))
            label_text.place(x=0, y=310)
            label_text.pack

        def WindowM():
            newWindow = Toplevel(window)
            newWindow.geometry("400x600")
            newWindow.resizable(False, False)
            newWindow.iconbitmap("LOGORL.ico")
            newWindow.config(background="red")

            bk = PhotoImage(file="aze.png")
            canvas = Canvas(newWindow, width=400, height=600)
            canvas.pack(expand=YES, fill=BOTH)

            canvas.create_image(50, 10, image=bk, anchor=NW)
            canvas.bk = bk
            canvas.place(x=0, y=0)

            label_text = Label(newWindow, text="{0} \n Son pourcentage est d'actuellement de : {1} %".format(mtext, readmainframe), font=("Heroes Legend", 8))
            label_text.place(x=0, y=310)
            label_text.pack

        def WindowO():
            newWindow = Toplevel(window)
            newWindow.geometry("400x600")
            newWindow.resizable(False, False)
            newWindow.iconbitmap("LOGORL.ico")
            newWindow.config(background="red")

            bk = PhotoImage(file="aze.png")
            canvas = Canvas(newWindow, width=400, height=600)
            canvas.pack(expand=YES, fill=BOTH)

            canvas.create_image(50, 10, image=bk, anchor=NW)
            canvas.bk = bk
            canvas.place(x=0, y=0)

            label_text = Label(newWindow, text="{0} \n Son pourcentage est d'actuellement de : {1} %".format(otext, readoctane), font=("Heroes Legend", 8))
            label_text.place(x=0, y=310)
            label_text.pack

        def WindowZ():
            newWindow = Toplevel(window)
            newWindow.geometry("400x600")
            newWindow.resizable(False, False)
            newWindow.iconbitmap("LOGORL.ico")
            newWindow.config(background="red")

            bk = PhotoImage(file="aze.png")
            canvas = Canvas(newWindow, width=400, height=600)
            canvas.pack(expand=YES, fill=BOTH)

            canvas.create_image(50, 10, image=bk, anchor=NW)
            canvas.bk = bk
            canvas.place(x=0, y=0)

            label_text = Label(newWindow, text="{0} \n Son pourcentage est d'actuellement de : {1} %".format(ztext, readzomba), font=("Heroes Legend", 8))
            label_text.place(x=0, y=310)
            label_text.pack

        def WindowI():
            newWindow = Toplevel(window)
            newWindow.geometry("400x600")
            newWindow.resizable(False, False)
            newWindow.iconbitmap("LOGORL.ico")
            newWindow.config(background="red")

            bk = PhotoImage(file="aze.png")
            canvas = Canvas(newWindow, width=400, height=600)
            canvas.pack(expand=YES, fill=BOTH)

            canvas.create_image(50, 10, image=bk, anchor=NW)
            canvas.bk = bk
            canvas.place(x=0, y=0)

            label_text = Label(newWindow, text="{0} \n Son pourcentage est d'actuellement de : {1} %".format(itext, readinterstellar), font=("Heroes Legend", 8))
            label_text.place(x=0, y=310)
            label_text.pack

        def Graph():
            plt.close("all")



        # Bouton
        Fennec = Button(window, text="Fennec", font=("Heroes Legend", 5), bg='White', borderwidth=0, command=WindowF)
        Fennec.config(height=1, width=39)
        Fennec.pack()
        Fennec.place(x=490, y=265)

        Octane = Button(window, text="Crimson Octane", font=("Heroes Legend", 5), bg='White', borderwidth=0, command=WindowO)
        Octane.config(height=1, width=39)
        Octane.pack()
        Octane.place(x=490, y=315)

        Interstellar = Button(window, text="Interstellar", font=("Heroes Legend", 5), bg='White', borderwidth=0, command=WindowI)
        Interstellar.config(height=1, width=42)
        Interstellar.pack()
        Interstellar.place(x=486, y=365)

        Zomba = Button(window, text="Zomba Titanium White", font=("Heroes Legend", 5), bg='White', borderwidth=0, command=WindowZ)
        Zomba.config(height=1, width=39)
        Zomba.pack()
        Zomba.place(x=490, y=415)

        Mainframe = Button(window, text="Mainframe", font=("Heroes Legend", 5), bg='White', borderwidth=0, command=WindowM)
        Mainframe.config(height=1, width=39)
        Mainframe.pack()
        Mainframe.place(x=490, y=465)

        Graph = Button(window, text="Graphique", font=("Heroes Legend", 7), bg='White', borderwidth=0, command=Graph)
        Graph.config(height=4, width=32)
        Graph.pack()
        Graph.place(x=475, y=530)

        # Ajouter frame
        frame.pack(expand=YES)

        # Affichage app
        window.mainloop()


App()
