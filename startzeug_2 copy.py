import tkinter as tk
from tkinter import ttk
from random import randint

class Datenbank(object):
    def __init__(self):
        pass
    def Eintragen(self, Highscore, Nickname, Datum):
        Datenbank1 = open('Datenbank-Highscore.txt', 'a')
        Datenbank1.write(Highscore)
        Datenbank1.write('; ')
        Datenbank1.write(Nickname)
        Datenbank1.write('; ')
        Datenbank1.write(Datum)
        Datenbank1.write('\n')
        Datenbank1.close()
    def Ausgeben(self):
        x = open('Datenbank-Highscore.txt').read()
        print(x)
    def Sortieren(self):
        Liste = []
        b = -1
        x = open('Datenbank-highscore.txt').readlines()
        Laenge = len(x) -1
        while True:
            x = open('Datenbank-highscore.txt').readlines()
            b = b + 1
            Liste.append(x[b])
            if b == Laenge:
                break
        if Laenge >= 2:
            Liste.sort()
            Liste.reverse()
            x = open('Datenbank-Highscore.txt', 'w')
            x.write(Liste[0])
            x.close
            x = open('Datenbank-Highscore.txt', 'a')
            b = 0
            while True:
                b = b + 1
                x.write(Liste[b])
                if b == Laenge:
                    break
            x.close()

def wuerfeln(self):
    r1=randint(1,6)
    return r1

class Kniffel(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)

        tk.Tk.wm_title(self, "Kniffel")
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}



        for F in (spieleranzahl,start,nameneingeben1,nameneingeben2,nameneingeben3,nameneingeben4,hauptseitefuer4):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(start)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

class spieleranzahl (tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.numplayer=0
        self.logo = tk.PhotoImage(file='kniffel_logo.gif')

        label =tk.Label(self, image=self.logo)
        label.grid(row=0,column=0,pady=10)

        labelSpieler = tk.Label(self,text='Spieler',
         fg="black", bg="gray", font=("Arial", 25))
#        labelSpieler.grid(padx=200 ,pady=150)
        labelSpieler.grid(row=2, column = 0)



        labelTitel = tk.Label(self,text='Spielerauswahl',
         fg="black", bg="gray", font=("Arial", 30))
#        labelTitel.grid(padx=285 ,pady=0)
        labelTitel.grid(row = 1, column = 0)
        labelTitel.grid(columnspan = 2)


        #Spieler Button
        self.buttonSpieler1 = tk.Button(self,text="1 Spieler", fg="black", bg="blue",
         font=('Arial', 10), command= lambda:controller.show_frame(nameneingeben1))
#        ButtonSpieler1.grid(padx=240 ,pady=250)
        self.buttonSpieler1.grid(row = 3, column = 0)

        self.buttonSpieler2 = tk.Button(self,text="2 Spieler", fg="black", bg="red",
         font=('Arial', 10), command= lambda:controller.show_frame(nameneingeben2))
#        ButtonSpieler2.grid(padx=240 ,pady=350)
        self.buttonSpieler2.grid(row = 4, column = 0)

        self.buttonSpieler3 = tk.Button(self,text="3 Spieler", fg="black", bg="green",
         font=('Arial', 10),command= lambda:controller.show_frame(nameneingeben3))
#        ButtonSpieler3.grid(padx=240 ,pady=450)
        self.buttonSpieler3.grid(row = 5, column = 0)

        self.buttonSpieler4 = tk.Button(self,text="4 Spieler", fg="black", bg="yellow",
         font=('Arial', 10), command= lambda:controller.show_frame(nameneingeben4))
#        ButtonSpieler4.grid(padx=240 ,pady=550)
        self.buttonSpieler4.grid(row = 6, column = 0)


        #KI Button


class start (ttk.Frame):
    def __init__(self,parent,controller):
        ttk.Frame.__init__(self,parent)
        self.logo = tk.PhotoImage(file='kniffel_logo.gif')


        buttonSpielen = tk.Button(self, text="Spielen", fg="black",
         bg="gray", font=('Arial', 25),
                    command=lambda: controller.show_frame(spieleranzahl))
        buttonSpielen.grid(row = 1, column = 0, padx=100,pady=70,sticky="S")

        buttonBeenden = tk.Button(self, text="Beenden", fg="black",
         bg="gray", font=('Arial', 25), command=lambda: controller.destroy())
        buttonBeenden.grid(row = 2, column = 0, pady=10)

        label =tk.Label(self, image=self.logo)
        label.grid(row=0,column=0)

class nameneingeben4 (tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.logo = tk.PhotoImage(file='kniffel_logo.gif')

        label =tk.Label(self, image=self.logo)
        label.grid(row=0,column=0, rowspan=2)

        entrySpielername1 = tk.Entry(self,bg='white')
        entrySpielername1.grid(row=3,column=0)

        labelSpieler1 = tk.Label(self,fg='black', text='Spieler 1' , font=('Arial',30))
        labelSpieler1.grid(row = 2, column = 0)


        entrySpielername2 = tk.Entry(self, bg='white')
        entrySpielername2.grid(row=5,column=0)

        labelSpieler2 = tk.Label(self, fg='black', text='Spieler 2' , font=('Arial',30))
        labelSpieler2.grid(row = 4, column = 0)


        entrySpielername3 =tk. Entry( self,bg='white')
        entrySpielername3.grid(row=7,column=0)

        labelSpieler3 = tk.Label(self,fg='black', text='Spieler 3' , font=('Arial',30))
        labelSpieler3.grid(row = 6, column = 0)


        entrySpielername4 = tk.Entry(self,bg='white')
        entrySpielername4.grid(row = 9, column = 0)

        labelSpieler4 = tk.Label(self,fg='black', text='Spieler 4' , font=('Arial',30))
        labelSpieler4.grid(row = 8, column = 0)


        buttonWeiter = tk.Button(self,bg='gray', fg='black',text='Weiter', command=lambda:controller.show_frame(hauptseitefuer4))
        buttonWeiter.grid(row = 9,rowspan=2, column = 1, padx=40)

class nameneingeben3 (tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.logo = tk.PhotoImage(file='kniffel_logo.gif')

        label =tk.Label(self, image=self.logo)
        label.grid(row=0,column=0, rowspan=2)

        entrySpielername1 = tk.Entry(self,bg='white')
        entrySpielername1.grid(row=3,column=0)

        labelSpieler1 = tk.Label(self,fg='black', text='Spieler 1' , font=('Arial',30))
        labelSpieler1.grid(row = 2, column = 0)


        entrySpielername2 = tk.Entry(self,bg='white')
        entrySpielername2.grid(row=5,column=0)

        labelSpieler2 = tk.Label(self,fg='black', text='Spieler 2' , font=('Arial',30))
        labelSpieler2.grid(row = 4, column = 0)

        entrySpielername3 = tk.Entry(self, bg='white')
        entrySpielername3.grid(row=7,column=0)

        labelSpieler3 = tk.Label(self,fg='black', text='Spieler 3' , font=('Arial',30))
        labelSpieler3.grid(row = 6, column = 0)

        buttonWeiter = tk.Button(self,bg='gray', fg='black',text='Weiter', command=lambda:controller.show_frame(hauptseitefuer4))
        buttonWeiter.grid(row = 7,rowspan=2, column = 1, padx=40)

class nameneingeben2 (tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.logo = tk.PhotoImage(file='kniffel_logo.gif')

        label =tk.Label(self, image=self.logo)
        label.grid(row=0,column=0, rowspan=2)

        entrySpielername1 = tk.Entry(self,bg='white')
        entrySpielername1.grid(row=3,column=0)


        labelSpieler1 = tk.Label(self, fg='black', text='Spieler 1' , font=('Arial',30))
        labelSpieler1.grid(row = 2, column = 0)


        entrySpielername2 = tk.Entry(self, bg='white')
        entrySpielername2.grid(row=5,column=0)

        labelSpieler2 = tk.Label(self, fg='black', text='Spieler 2' , font=('Arial',30))
        labelSpieler2.grid(row = 4, column = 0)
        buttonWeiter = tk.Button(self,bg='gray', fg='black',text='Weiter', command=lambda:controller.show_frame(hauptseitefuer4))
        buttonWeiter.grid(row = 5,rowspan=2, column = 1, padx=40)

class nameneingeben1 (tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.logo = tk.PhotoImage(file='kniffel_logo.gif')

        label =tk.Label(self, image=self.logo)
        label.grid(row=0,column=0, columnspan=2)


        self.entrySpielername1 = tk.Entry(self, bg='white')
        self.entrySpielername1.grid(row=2,column=0)

        self.labelSpieler1 = tk.Label(self, fg='black', text='Spieler 1' , font=('Arial',30))
        self.labelSpieler1.grid(row = 1, column = 0)

        buttonWeiter = tk.Button(self,bg='gray', fg='black',text='Weiter', command=lambda:controller.show_frame(hauptseitefuer4))
        buttonWeiter.grid(row = 2,rowspan=2, column = 1, padx=40)

class hauptseitefuer4 (tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)

        self.round=1 #die wievielte runde grad am Laufen ist

        self.turn = 0

        self.P1Eins = True  # benÃ¶tigt fÃ¼r die Buttons
        self.P1Zwei = True
        self.P1Drei = True
        self.P1Vier = True
        self.P1Fuenf = True
        self.P1Sechs = True
        self.P13Pasch = True
        self.P14Pasch = True
        self.P1Haus = True
        self.P1Kstrasse = True
        self.P1GStrasse = True
        self.P1Kniffel = True
        self.P1Chance = True

        self.P2Eins = True
        self.P2Zwei = True
        self.P2Drei = True
        self.P2Vier = True
        self.P2Fuenf = True
        self.P2Sechs = True
        self.P23Pasch = True
        self.P24Pasch = True
        self.P2Haus = True
        self.P2Kstrasse = True
        self.P2GStrasse = True
        self.P2Kniffel = True
        self.P2Chance = True

        self.P3Eins = True
        self.P3Zwei = True
        self.P3Drei = True
        self.P3Vier = True
        self.P3Fuenf = True
        self.P3Sechs = True
        self.P33Pasch = True
        self.P34Pasch = True
        self.P3Haus = True
        self.P3Kstrasse = True
        self.P3GStrasse = True
        self.P3Kniffel = True
        self.P3Chance = True

        self.P4Eins = True
        self.P4Zwei = True
        self.P4Drei = True
        self.P4Vier = True
        self.P4Fuenf = True
        self.P4Sechs = True
        self.P43Pasch = True
        self.P44Pasch = True
        self.P4Haus = True
        self.P4Kstrasse = True
        self.P4GStrasse = True
        self.P4Kniffel = True
        self.P4Chance = True


        self.Einser = 0   #Anzahl der einser zweier usw, wird unten noch wichtig
        self.Zweier = 0
        self.Dreier = 0
        self.Vierer = 0
        self.Fuenfer = 0
        self.Sechser = 0

        self.Punkte1 = 0    #Punkte fuer SP1
        self.Punkte2 = 0    # SP2
        self.Punkte3 = 0    # SP3
        self.Punkte4 = 0    # und SP4
        self.SP = 1         # Spieler der grad dran ist (wird weiter unten durch naechster Spieler Button gewechselt)
        self.augen1 = 0
        self.augen2 = 0
        self.augen3 = 0
        self.augen4 = 0
        self.augen5 = 0
        labelDran=tk.Label(self, text="An der Reihe ist Spieler "+str(self.SP))
        labelDran.grid(row=10,column=2)
        labelround=tk.Label(self, text="Runde: "+str(self.round))
        labelround.grid(row=12,column=2)

        self.red1 = 'Nein'
        self.red2 = 'Nein'
        self.red3 = 'Nein'
        self.red4 = 'Nein'
        self.red5 = 'Nein'

        # Bilder
        self.imageWuerfel1 = tk.PhotoImage(file='w1.gif')
        self.imageWuerfel2 = tk.PhotoImage(file='w2.gif')
        self.imageWuerfel3 = tk.PhotoImage(file='w3.gif')
        self.imageWuerfel4 = tk.PhotoImage(file='w4.gif')
        self.imageWuerfel5 = tk.PhotoImage(file='w5.gif')
        self.imageWuerfel6 = tk.PhotoImage(file='w6.gif')
        self.imageWuerfel11 = tk.PhotoImage(file='w7.gif')
        self.imageWuerfel22 = tk.PhotoImage(file='w8.gif')
        self.imageWuerfel33 = tk.PhotoImage(file='w9.gif')
        self.imageWuerfel44 = tk.PhotoImage(file='w10.gif')
        self.imageWuerfel55 = tk.PhotoImage(file='w11.gif')
        self.imageWuerfel66 = tk.PhotoImage(file='w12.gif')
        self.Karte=tk.PhotoImage(file="karte.gif")

        # Button zum Wuerfeln
        buttonWuerfel = tk.Button(self,text='Wuerfeln', command=self.buttonWuerfelnClick)
        buttonWuerfel.grid(row=6,column=2)

        # Button zum Auswalen
        buttonAuswaehlen1 = tk.Button(self,image = self.imageWuerfel1 ,command = self.buttonAuswahl1Click, state='disabled')
        buttonAuswaehlen1.grid(row=2,column=0,padx=20,pady=40, rowspan=5)
        buttonAuswaehlen2 = tk.Button(self,image = self.imageWuerfel1 ,state='disabled',command = self.buttonAuswahl2Click)
        buttonAuswaehlen2.grid(row=2,column=1,padx=20,pady=40, rowspan=5)
        buttonAuswaehlen3 = tk.Button(self,image = self.imageWuerfel1, state='disabled',command = self.buttonAuswahl3Click)
        buttonAuswaehlen3.grid(row=2,column=2,padx=20,pady=40, rowspan=5)
        buttonAuswaehlen4 = tk.Button(self,image = self.imageWuerfel1 , state='disabled',command = self.buttonAuswahl4Click)
        buttonAuswaehlen4.grid(row=2,column=3,padx=20,pady=40, rowspan=5)
        buttonAuswaehlen5 = tk.Button(self,image = self.imageWuerfel1 , state='disabled', command = self.buttonAuswahl5Click)
        buttonAuswaehlen5.grid(row=2,column=4,padx=20,pady=40, rowspan=5)

        #Kniffelkarte        ----NEW----
        labelKarte = tk.Label(self, image=self.Karte)
        labelKarte.grid(row=2, column=5, rowspan=21)

        # Button bei den Wuerfelergebnissen von 1-6
        buttonEins = tk.Button(self, bg='white',width=15, text= "Einser Zaehlen", height=1, command=self.buttonEinsClick, state='disabled')
        buttonEins.grid(row=2, column=6)
        buttonZwei = tk.Button(self, bg='white',width=15, text= "Zweier Zaehlen", command=self.buttonZweiClick, state='disabled')
        buttonZwei.grid(row=3, column=6)
        buttonDrei = tk.Button(self, bg='white',width=15, text= "Dreier Zaehlen", command=self.buttonDreiClick, state='disabled')
        buttonDrei.grid(row=4, column=6)
        buttonVier = tk.Button(self, bg='white',width=15, text= "Vierer Zaehlen", command=self.buttonVierClick, state='disabled')
        buttonVier.grid(row=5, column=6)
        buttonFuenf = tk.Button(self, bg='white',width=15, text= "Fuenfer Zaehlen", command=self.buttonFuenfClick, state='disabled')
        buttonFuenf.grid(row=6, column=6)
        buttonSechs = tk.Button(self, bg='white',width=15, text= "Sechser Zaehlen", command=self.buttonSechsClick, state='disabled')
        buttonSechs.grid(row=7, column=6)

        #Button fuer Zwischensumme und Bonus
        buttonZwischensumme = tk.Button(self, bg='white',width=15,state='disabled')
        buttonZwischensumme.grid(row=8, column=6)
        buttonEmpty=tk.Label(self)
        buttonEmpty.grid(row=11,column=6)
        buttonzero1=tk.Label(self)
        buttonzero1.grid(row=9,column=6)
        buttonzero3=tk.Label(self)
        buttonzero3.grid(row=10,column=6)
        #Button untere Haelfte
        buttonDreierpasch = tk.Button(self, bg='white',width=15, text= "Alle Augen Zaehlen", state='disabled', command=self.button3PaschClick)#
        buttonDreierpasch.grid(row=12, column=6)
        buttonViererpasch = tk.Button(self, bg='white',width=15, text= "Alle Augen Zaehlen", state='disabled', command=self.button4PaschClick)
        buttonViererpasch.grid(row=13, column=6)
        buttonHaus = tk.Button(self, bg='white',width=15, text= "25 Punkte", state='disabled',command=self.HouseClick)
        buttonHaus.grid(row=14, column=6)
        buttonKStrasse = tk.Button(self, bg='white',width=15, text= "30 Punkte", state='disabled')
        buttonKStrasse.grid(row=15,column=6)
        buttonGStrasse = tk.Button(self, bg='white',width=15, text= "40 Punkte", state='disabled')
        buttonGStrasse.grid(row=16, column=6 )
        buttonKniffel = tk.Button(self, bg='white',width=15, text= "50 Punkte", state='disabled',command=self.KniffelClick)
        buttonKniffel.grid(row=17, column=6)
        buttonChance = tk.Button(self, bg='white',width=15, text= "Alle Augen Zaehlen", state='disabled')
        buttonChance.grid(row=18, column=6)

        #Button Summe + Ergebnis
        buttonSumme2 = tk.Button(self, bg='white',width=15,state='disabled')
        buttonSumme2.grid(row=19, column=6)
        buttonzero2=tk.Label(self)
        buttonzero2.grid(row=20,column=6)
        buttonGesamt = tk.Button(self, bg='white',width=15,state='disabled')
        buttonGesamt.grid(row=21, column=6)


        #                            ----------Label----------
        nameeins=tk.Label(self, text='Spieler 1')
        nameeins.grid(row=1,column=7)
        namezwei=tk.Label(self, text="Spieler 2")
        namezwei.grid(row=1,column=8)
        namedrei=tk.Label(self, text="Spieler 3")
        namedrei.grid(row=1,column=9)
        namevier=tk.Label(self, text="Spieler 4")
        namevier.grid(row=1,column=10)

        buttonNaechster= tk.Button(self, width=20, text='naechster', command = self.buttonNaechsterClick, state="disabled")
        buttonNaechster.grid(row=19,column=2)





    def buttonNaechsterClick(self):
        if self.round==14:
            gesamtup1=self.wert1+self.wert21+self.wert31+self.wert41+self.wert51+self.wert61
            gesamtOber1=tk.Label(self, text=str(gesamtup1))
            gesamtOber1.grid(row=8,column=7)
            if gesamtup1+35 >=63:
                bonus=tk.Label(self, text="Ja!")
                bonus.grid(row=9,column=7)
                gesammtOber1=tk.Label(self,text=str(gesamtup1+35))
                gesammtOber1.grid(row=10,column=7)
                gesammmtOber1=tk.Label(self,text=str(gesamtup1+35))
                gesammmtOber1.grid(row=19,column=7)
                gesamtUnter1=tk.Label(self,text=Punkte1)
                gesamtUnter1.grid(row=20,column=7)
            else:
                bonus=tk.Label(self, text="X")
                bonus.grid(row=9,column=7)
                gesammtOber1=tk.Label(self,text=str(gesamtup1))
                gesammtOber1.grid(row=10,column=7)
                gesammmtOber1=tk.Label(self,text=str(gesamtup1))
                gesammmtOber1.grid(row=19,column=7)
                gesamtUnter1=tk.Label(self,text=Punkte1)
                gesamtUnter1.grid(row=20,column=7)
            gesamtup2=self.wert2+self.wert22+self.wert32+self.wert42+self.wert52+self.wert62
            gesamtOber2=tk.Label(self, text=str(gesamtup2))
            gesamtOber2.grid(row=8,column=7)
            if gesamtup2+35 >=63:
                bonus=tk.Label(self, text="Ja!")
                bonus.grid(row=9,column=8)
                gesammtOber2=tk.Label(self,text=str(gesamtup2+35))
                gesammtOber2.grid(row=10,column=8)
                gesammmtOber2=tk.Label(self,text=str(gesamtup2+35))
                gesammmtOber2.grid(row=19,column=8)
                gesamtUnter2=tk.Label(self,text=Punkte2)
                gesamtUnter2.grid(row=20,column=8)
            else:
                bonus=tk.Label(self, text="X")
                bonus.grid(row=9,column=8)
                gesammtOber2=tk.Label(self,text=str(gesamtup2))
                gesammtOber2.grid(row=10,column=8)
                gesammmtOber2=tk.Label(self,text=str(gesamtup2))
                gesammmtOber2.grid(row=19,column=8)
                gesamtUnter2=tk.Label(self,text=Punkte1)
                gesamtUnter2.grid(row=20,column=8)
            gesamtup3=self.wert3+self.wert23+self.wert33+self.wert43+self.wert53+self.wert63
            gesamtOber3=tk.Label(self, text=str(gesamtup3))
            gesamtOber3.grid(row=8,column=9)
            if gesamtup1+35 >=63:
                bonus=tk.Label(self, text="Ja!")
                bonus.grid(row=9,column=9)
                gesammtOber3=tk.Label(self,text=str(gesamtup3+35))
                gesammtOber3.grid(row=10,column=9)
                gesammmtOber3=tk.Label(self,text=str(gesamtup3+35))
                gesammmtOber3.grid(row=19,column=9)
                gesamtUnter3=tk.Label(self,text=Punkte3)
                gesamtUnter3.grid(row=20,column=9)
            else:
                bonus=tk.Label(self, text="X")
                bonus.grid(row=9,column=9)
                gesammtOber3=tk.Label(self,text=str(gesamtup3))
                gesammtOber3.grid(row=10,column=9)
                gesammmtOber3=tk.Label(self,text=str(gesamtup3))
                gesammmtOber3.grid(row=19,column=9)
                gesamtUnter3=tk.Label(self,text=Punkte3)
                gesamtUnter3.grid(row=20,column=9)
            gesamtup4=self.wert4+self.wert24+self.wert34+self.wert44+self.wert54+self.wert64
            gesamtOber4=tk.Label(self, text=str(gesamtup4))
            gesamtOber4.grid(row=8,column=10)
            if gesamtup1+35 >=63:
                bonus=tk.Label(self, text="Ja!")
                bonus.grid(row=9,column=10)
                gesammtOber4=tk.Label(self,text=str(gesamtup4+35))
                gesammtOber4.grid(row=10,column=10)
                gesammmtOber4=tk.Label(self,text=str(gesamtup4+35))
                gesammmtOber4.grid(row=19,column=10)
                gesamtUnter4=tk.Label(self,text=Punkte4)
                gesamtUnter4.grid(row=20,column=7)

            else:
                bonus=tk.Label(self, text="X")
                bonus.grid(row=9,column=10)
                gesammtOber4=tk.Label(self,text=str(gesamtup4))
                gesammtOber4.grid(row=10,column=10)
                gesammmtOber4=tk.Label(self,text=str(gesamtup4))
                gesammmtOber4.grid(row=19,column=10)

            X = Datenbank()
            X.Eintragen(self.Punkte1, 'Spieler1', input('Datum'))
            X.Eintragen(self.Punkte2, 'Spieler2', input('Datum'))
            X.Eintragen(self.Punkte3, 'Spieler3', input('Datum'))
            X.Eintragen(self.Punkte4, 'Spieler4', input('Datum'))
            X.Sortieren()


        self.red1="Nein"
        self.red2="Nein"
        self.red3="Nein"
        self.red4="Nein"
        self.red5="Nein"
        buttonAuswaehlen1 = tk.Button(self,image = self.imageWuerfel1 ,command = self.buttonAuswahl1Click, state='disabled')
        buttonAuswaehlen1.grid(row=2,column=0,padx=20,pady=40, rowspan=5)
        buttonAuswaehlen2 = tk.Button(self,image = self.imageWuerfel1 ,state='disabled',command = self.buttonAuswahl2Click)
        buttonAuswaehlen2.grid(row=2,column=1,padx=20,pady=40, rowspan=5)
        buttonAuswaehlen3 = tk.Button(self,image = self.imageWuerfel1, state='disabled',command = self.buttonAuswahl3Click)
        buttonAuswaehlen3.grid(row=2,column=2,padx=20,pady=40, rowspan=5)
        buttonAuswaehlen4 = tk.Button(self,image = self.imageWuerfel1 , state='disabled',command = self.buttonAuswahl4Click)
        buttonAuswaehlen4.grid(row=2,column=3,padx=20,pady=40, rowspan=5)
        buttonAuswaehlen5 = tk.Button(self,image = self.imageWuerfel1 , state='disabled', command = self.buttonAuswahl5Click)
        buttonAuswaehlen5.grid(row=2,column=4,padx=20,pady=40, rowspan=5)
        buttonNaechster= tk.Button(self, width=20, text='naechster', command = self.buttonNaechsterClick, state="disabled")
        buttonNaechster.grid(row=19,column=2)
        buttonWuerfel=tk.Button(self,text='Wuerfeln', command=self.buttonWuerfelnClick)
        buttonWuerfel.grid(row=6,column=2)
        if self.SP == 1:
            self.SP = self.SP+1
            if self.P2Eins == True:

                buttonEins = tk.Button(self, bg='white',width=15, text= "Einser Zaehlen", height=1, command=self.buttonEinsClick)
                buttonEins.grid(row=2, column=6)
            else:
                buttonEins = tk.Button(self, bg='white',width=15, text= "Einser Zaehlen", height=1, command=self.buttonEinsClick,state="disabled")
                buttonEins.grid(row=2, column=6)
            if self.P2Zwei == True:

                buttonZwei = tk.Button(self, bg='white',width=15, text= "Zweier Zaehlen", command=self.buttonZweiClick)
                buttonZwei.grid(row=3, column=6)
            else:
                buttonZwei = tk.Button(self, bg='white',width=15, text= "Zweier Zaehlen", command=self.buttonZweiClick,state="disabled")
                buttonZwei.grid(row=3, column=6)
            if self.P2Drei == True:
                buttonDrei = tk.Button(self, bg='white',width=15, text= "Dreier Zaehlen", command=self.buttonDreiClick)
                buttonDrei.grid(row=4, column=6)
            else:
                buttonDrei = tk.Button(self, bg='white',width=15, text= "Dreier Zaehlen", command=self.buttonDreiClick, state="disabled")
                buttonDrei.grid(row=4, column=6)
            if self.P2Vier == True:
                buttonVier = tk.Button(self, bg='white',width=15, text= "Vierer Zaehlen", command=self.buttonVierClick)
                buttonVier.grid(row=5, column=6)
            else:
                buttonVier = tk.Button(self, bg='white',width=15, text= "Vierer Zaehlen", command=self.buttonVierClick,state="disabled")
                buttonVier.grid(row=5, column=6)
            if self.P2Fuenf == True:

                buttonFuenf = tk.Button(self, bg='white',width=15, text= "Fuenfer Zaehlen", command=self.buttonFuenfClick)
                buttonFuenf.grid(row=6, column=6)
            else:
                buttonFuenf = tk.Button(self, bg='white',width=15, text= "Fuenfer Zaehlen", command=self.buttonFuenfClick, state="disabled")
                buttonFuenf.grid(row=6, column=6)
            if self.P2Sechs == True:
                buttonSechs = tk.Button(self, bg='white',width=15, text= "Sechser Zaehlen", command=self.buttonSechsClick)
                buttonSechs.grid(row=7, column=6)
            else:
                buttonSechs = tk.Button(self, bg='white',width=15, text= "Sechser Zaehlen", command=self.buttonSechsClick, state="disabled")
                buttonSechs.grid(row=7, column=6)

                #Button untere Haelfte
            if self.P23Pasch == True:
                buttonDreierpasch = tk.Button(self, bg='white',width=15, text= "Alle Augen Zaehlen", command=self.button3PaschClick)#
                buttonDreierpasch.grid(row=12, column=6)
            else:
                buttonDreierpasch = tk.Button(self, bg='white',width=15, text= "Alle Augen Zaehlen", state="disabled")#
                buttonDreierpasch.grid(row=12, column=6)
            if self.P24Pasch == True:
                buttonViererpasch = tk.Button(self, bg='white',width=15, text= "Alle Augen Zaehlen", command=self.button4PaschClick)
                buttonViererpasch.grid(row=13, column=6)
            else:
                buttonViererpasch = tk.Button(self, bg='white',width=15, text= "Alle Augen Zaehlen", state="disabled")
                buttonViererpasch.grid(row=13, column=6)
            if self.P2Haus == True:
                buttonHaus = tk.Button(self, bg='white',width=15, text= "25 Punkte",command=self.HouseClick)
                buttonHaus.grid(row=14, column=6)
            else:
                buttonHaus = tk.Button(self, bg='white',width=15, text= "25 Punkte", state="disabled")
                buttonHaus.grid(row=14, column=6)
            if self.P2Kstrasse == True:
                buttonKStrasse = tk.Button(self, bg='white',width=15, text= "30 Punkte", command=self.KStrasseClick)
                buttonKStrasse.grid(row=15,column=6)
            else:
                buttonKStrasse = tk.Button(self, bg='white',width=15, text= "30 Punkte", state="disabled")
                buttonKStrasse.grid(row=15,column=6)
            if self.P2GStrasse == True:
                buttonGStrasse = tk.Button(self, bg='white',width=15, text= "40 Punkte",command=self.GStrasseClick)
                buttonGStrasse.grid(row=16, column=6 )
            else:
                buttonGStrasse = tk.Button(self, bg='white',width=15, text= "40 Punkte", state="disabled")
                buttonGStrasse.grid(row=16, column=6 )
            if self.P2Kniffel == True:
                buttonKniffel = tk.Button(self, bg='white',width=15, text= "50 Punkte",command=self.KniffelClick)
                buttonKniffel.grid(row=17, column=6)
            else:
                buttonKniffel = tk.Button(self, bg='white',width=15, text= "50 Punkte", state="disabled")
                buttonKniffel.grid(row=17, column=6)
            if self.P2Chance == True:
                buttonChance = tk.Button(self, bg='white',width=15, text= "Alle Augen Zaehlen",command=self.ChanceClick)
                buttonChance.grid(row=18, column=6)
            else:
                buttonChance = tk.Button(self, bg='white',width=15, text= "Alle Augen Zaehlen", state="disabled")
                buttonChance.grid(row=18, column=6)

        elif self.SP == 2:
            self.SP = self.SP+1  #FÃƒÂ¼r die verschiedenen Spieler, es wird immer +1 gerechnet, und dann wieder zum Anfang (Ist fÃƒÂ¼r 4 Spieler, nicht weniger :/
            if self.P3Eins == True:

                buttonEins = tk.Button(self, bg='white',width=15, text= "Einser Zaehlen", height=1, command=self.buttonEinsClick)
                buttonEins.grid(row=2, column=6)
            else:
                buttonEins = tk.Button(self, bg='white',width=15, text= "Einser Zaehlen", height=1, command=self.buttonEinsClick,state="disabled")
                buttonEins.grid(row=2, column=6)
            if self.P3Zwei == True:

                buttonZwei = tk.Button(self, bg='white',width=15, text= "Zweier Zaehlen", command=self.buttonZweiClick)
                buttonZwei.grid(row=3, column=6)
            else:
                buttonZwei = tk.Button(self, bg='white',width=15, text= "Zweier Zaehlen", command=self.buttonZweiClick,state="disabled")
                buttonZwei.grid(row=3, column=6)
            if self.P3Drei == True:
                buttonDrei = tk.Button(self, bg='white',width=15, text= "Dreier Zaehlen", command=self.buttonDreiClick)
                buttonDrei.grid(row=4, column=6)
            else:
                buttonDrei = tk.Button(self, bg='white',width=15, text= "Dreier Zaehlen", state="disabled")
                buttonDrei.grid(row=4, column=6)
            if self.P3Vier == True:
                buttonVier = tk.Button(self, bg='white',width=15, text= "Vierer Zaehlen", command=self.buttonVierClick)
                buttonVier.grid(row=5, column=6)
            else:
                buttonVier = tk.Button(self, bg='white',width=15, text= "Vierer Zaehlen", command=self.buttonVierClick,state="disabled")
                buttonVier.grid(row=5, column=6)
            if self.P3Fuenf == True:

                buttonFuenf = tk.Button(self, bg='white',width=15, text= "Fuenfer Zaehlen", command=self.buttonFuenfClick)
                buttonFuenf.grid(row=6, column=6)
            else:
                buttonFuenf = tk.Button(self, bg='white',width=15, text= "Fuenfer Zaehlen", command=self.buttonFuenfClick, state="disabled")
                buttonFuenf.grid(row=6, column=6)
            if self.P3Sechs == True:
                buttonSechs = tk.Button(self, bg='white',width=15, text= "Sechser Zaehlen", command=self.buttonSechsClick)
                buttonSechs.grid(row=7, column=6)
            else:
                buttonSechs = tk.Button(self, bg='white',width=15, text= "Sechser Zaehlen", command=self.buttonSechsClick, state="disabled")
                buttonSechs.grid(row=7, column=6)

                #Button untere Haelfte
            if self.P33Pasch == True:
                buttonDreierpasch = tk.Button(self, bg='white',width=15, text= "Alle Augen Zaehlen", command=self.button3PaschClick)#
                buttonDreierpasch.grid(row=12, column=6)
            else:
                buttonDreierpasch = tk.Button(self, bg='white',width=15, text= "Alle Augen Zaehlen", state="disabled")#
                buttonDreierpasch.grid(row=12, column=6)
            if self.P34Pasch == True:
                buttonViererpasch = tk.Button(self, bg='white',width=15, text= "Alle Augen Zaehlen", command=self.button4PaschClick)
                buttonViererpasch.grid(row=13, column=6)
            else:
                buttonViererpasch = tk.Button(self, bg='white',width=15, text= "Alle Augen Zaehlen", state="disabled")
                buttonViererpasch.grid(row=13, column=6)
            if self.P3Haus == True:
                buttonHaus = tk.Button(self, bg='white',width=15, text= "25 Punkte", command=self.HouseClick)
                buttonHaus.grid(row=14, column=6)
            else:
                buttonHaus = tk.Button(self, bg='white',width=15, text= "25 Punkte", state="disabled")
                buttonHaus.grid(row=14, column=6)
            if self.P3Kstrasse == True:
                buttonKStrasse = tk.Button(self, bg='white',width=15, text= "30 Punkte", command=self.KStrasseClick)
                buttonKStrasse.grid(row=15,column=6)
            else:
                buttonKStrasse = tk.Button(self, bg='white',width=15, text= "30 Punkte", state="disabled")
                buttonKStrasse.grid(row=15,column=6)
            if self.P3GStrasse == True:
                buttonGStrasse = tk.Button(self, bg='white',width=15, text= "40 Punkte", command=self.GStrasseClick)
                buttonGStrasse.grid(row=16, column=6 )
            else:
                buttonGStrasse = tk.Button(self, bg='white',width=15, text= "40 Punkte", state="disabled")
                buttonGStrasse.grid(row=16, column=6 )
            if self.P3Kniffel == True:
                buttonKniffel = tk.Button(self, bg='white',width=15, text= "50 Punkte",command=self.KniffelClick)
                buttonKniffel.grid(row=17, column=6)
            else:
                buttonKniffel = tk.Button(self, bg='white',width=15, text= "50 Punkte", state="disabled")
                buttonKniffel.grid(row=17, column=6)
            if self.P3Chance == True:
                buttonChance = tk.Button(self, bg='white',width=15, text= "Alle Augen Zaehlen", command=self.ChanceClick)
                buttonChance.grid(row=18, column=6)
            else:
                buttonChance = tk.Button(self, bg='white',width=15, text= "Alle Augen Zaehlen", state="disabled")
                buttonChance.grid(row=18, column=6)

        elif self.SP == 3:
            self.SP = self.SP+1
            if self.P4Eins == True:

                buttonEins = tk.Button(self, bg='white',width=15, text= "Einser Zaehlen", height=1, command=self.buttonEinsClick)
                buttonEins.grid(row=2, column=6)
            else:
                buttonEins = tk.Button(self, bg='white',width=15, text= "Einser Zaehlen", height=1, command=self.buttonEinsClick,state="disabled")
                buttonEins.grid(row=2, column=6)
            if self.P4Zwei == True:

                buttonZwei = tk.Button(self, bg='white',width=15, text= "Zweier Zaehlen", command=self.buttonZweiClick)
                buttonZwei.grid(row=3, column=6)
            else:
                buttonZwei = tk.Button(self, bg='white',width=15, text= "Zweier Zaehlen", command=self.buttonZweiClick,state="disabled")
                buttonZwei.grid(row=3, column=6)
            if self.P4Drei == True:
                buttonDrei = tk.Button(self, bg='white',width=15, text= "Dreier Zaehlen", command=self.buttonDreiClick)
                buttonDrei.grid(row=4, column=6)
            else:
                buttonDrei = tk.Button(self, bg='white',width=15, text= "Dreier Zaehlen", command=self.buttonDreiClick, state="disabled")
                buttonDrei.grid(row=4, column=6)
            if self.P4Vier == True:
                buttonVier = tk.Button(self, bg='white',width=15, text= "Vierer Zaehlen", command=self.buttonVierClick)
                buttonVier.grid(row=5, column=6)
            else:
                buttonVier = tk.Button(self, bg='white',width=15, text= "Vierer Zaehlen", command=self.buttonVierClick,state="disabled")
                buttonVier.grid(row=5, column=6)
            if self.P4Fuenf == True:

                buttonFuenf = tk.Button(self, bg='white',width=15, text= "Fuenfer Zaehlen", command=self.buttonFuenfClick)
                buttonFuenf.grid(row=6, column=6)
            else:
                buttonFuenf = tk.Button(self, bg='white',width=15, text= "Fuenfer Zaehlen", command=self.buttonFuenfClick, state="disabled")
                buttonFuenf.grid(row=6, column=6)
            if self.P4Sechs == True:
                buttonSechs = tk.Button(self, bg='white',width=15, text= "Sechser Zaehlen", command=self.buttonSechsClick)
                buttonSechs.grid(row=7, column=6)
            else:
                buttonSechs = tk.Button(self, bg='white',width=15, text= "Sechser Zaehlen", command=self.buttonSechsClick, state="disabled")
                buttonSechs.grid(row=7, column=6)

                #Button untere Haelfte
            if self.P43Pasch == True:
                buttonDreierpasch = tk.Button(self, bg='white',width=15, text= "Alle Augen Zaehlen", command=self.button3PaschClick)#
                buttonDreierpasch.grid(row=12, column=6)
            else:
                buttonDreierpasch = tk.Button(self, bg='white',width=15, text= "Alle Augen Zaehlen", state="disabled")#
                buttonDreierpasch.grid(row=12, column=6)
            if self.P44Pasch == True:
                buttonViererpasch = tk.Button(self, bg='white',width=15, text= "Alle Augen Zaehlen",  command=self.button4PaschClick)
                buttonViererpasch.grid(row=13, column=6)
            else:
                buttonViererpasch = tk.Button(self, bg='white',width=15, text= "Alle Augen Zaehlen", state="disabled")
                buttonViererpasch.grid(row=13, column=6)
            if self.P4Haus == True:
                buttonHaus = tk.Button(self, bg='white',width=15, text= "25 Punkte", command=self.HouseClick)
                buttonHaus.grid(row=14, column=6)
            else:
                buttonHaus = tk.Button(self, bg='white',width=15, text= "25 Punkte", state="disabled")
                buttonHaus.grid(row=14, column=6)
            if self.P4Kstrasse == True:
                buttonKStrasse = tk.Button(self, bg='white',width=15, text= "30 Punkte", command=self.KStrasseClick)
                buttonKStrasse.grid(row=15,column=6)
            else:
                buttonKStrasse = tk.Button(self, bg='white',width=15, text= "30 Punkte", state="disabled")
                buttonKStrasse.grid(row=15,column=6)
            if self.P4GStrasse == True:
                buttonGStrasse = tk.Button(self, bg='white',width=15, text= "40 Punkte", command=self.GStrasseClick)
                buttonGStrasse.grid(row=16, column=6 )
            else:
                buttonGStrasse = tk.Button(self, bg='white',width=15, text= "40 Punkte", state="disabled")
                buttonGStrasse.grid(row=16, column=6 )
            if self.P4Kniffel == True:
                buttonKniffel = tk.Button(self, bg='white',width=15, text= "50 Punkte",command=self.KniffelClick)
                buttonKniffel.grid(row=17, column=6)
            else:
                buttonKniffel = tk.Button(self, bg='white',width=15, text= "50 Punkte", state="disabled")
                buttonKniffel.grid(row=17, column=6)
            if self.P4Chance == True:
                buttonChance = tk.Button(self, bg='white',width=15, text= "Alle Augen Zaehlen", command=self.ChanceClick)
                buttonChance.grid(row=18, column=6)
            else:
                buttonChance = tk.Button(self, bg='white',width=15, text= "Alle Augen Zaehlen", state="disabled")
                buttonChance.grid(row=18, column=6)


        elif self.SP == 4:
            self.SP = self.SP-3
            self.round=self.round+1
            if self.P1Eins == True:

                buttonEins = tk.Button(self, bg='white',width=15, text= "Einser Zaehlen", height=1, command=self.buttonEinsClick)
                buttonEins.grid(row=2, column=6)
            else:
                buttonEins = tk.Button(self, bg='white',width=15, text= "Einser Zaehlen", height=1, command=self.buttonEinsClick,state="disabled")
                buttonEins.grid(row=2, column=6)
            if self.P1Zwei == True:

                buttonZwei = tk.Button(self, bg='white',width=15, text= "Zweier Zaehlen", command=self.buttonZweiClick)
                buttonZwei.grid(row=3, column=6)
            else:
                buttonZwei = tk.Button(self, bg='white',width=15, text= "Zweier Zaehlen", command=self.buttonZweiClick,state="disabled")
                buttonZwei.grid(row=3, column=6)
            if self.P1Drei == True:
                buttonDrei = tk.Button(self, bg='white',width=15, text= "Dreier Zaehlen", command=self.buttonDreiClick)
                buttonDrei.grid(row=4, column=6)
            else:
                buttonDrei = tk.Button(self, bg='white',width=15, text= "Dreier Zaehlen", command=self.buttonDreiClick, state="disabled")
                buttonDrei.grid(row=4, column=6)
            if self.P1Vier == True:
                buttonVier = tk.Button(self, bg='white',width=15, text= "Vierer Zaehlen", command=self.buttonVierClick)
                buttonVier.grid(row=5, column=6)
            else:
                buttonVier = tk.Button(self, bg='white',width=15, text= "Vierer Zaehlen", command=self.buttonVierClick,state="disabled")
                buttonVier.grid(row=5, column=6)
            if self.P1Fuenf == True:

                buttonFuenf = tk.Button(self, bg='white',width=15, text= "Fuenfer Zaehlen", command=self.buttonFuenfClick)
                buttonFuenf.grid(row=6, column=6)
            else:
                buttonFuenf = tk.Button(self, bg='white',width=15, text= "Fuenfer Zaehlen", command=self.buttonFuenfClick, state="disabled")
                buttonFuenf.grid(row=6, column=6)
            if self.P1Sechs == True:
                buttonSechs = tk.Button(self, bg='white',width=15, text= "Sechser Zaehlen", command=self.buttonSechsClick)
                buttonSechs.grid(row=7, column=6)
            else:
                buttonSechs = tk.Button(self, bg='white',width=15, text= "Sechser Zaehlen", command=self.buttonSechsClick, state="disabled")
                buttonSechs.grid(row=7, column=6)

                #Button untere Haelfte
            if self.P13Pasch == True:
                buttonDreierpasch = tk.Button(self, bg='white',width=15, text= "Alle Augen Zaehlen", command=self.button3PaschClick)#
                buttonDreierpasch.grid(row=12, column=6)
            else:
                buttonDreierpasch = tk.Button(self, bg='white',width=15, text= "Alle Augen Zaehlen", state="disabled")#
                buttonDreierpasch.grid(row=12, column=6)
            if self.P14Pasch == True:
                buttonViererpasch = tk.Button(self, bg='white',width=15, text= "Alle Augen Zaehlen",  command=self.button4PaschClick)
                buttonViererpasch.grid(row=13, column=6)
            else:
                buttonViererpasch = tk.Button(self, bg='white',width=15, text= "Alle Augen Zaehlen", state="disabled")
                buttonViererpasch.grid(row=13, column=6)
            if self.P1Haus == True:
                buttonHaus = tk.Button(self, bg='white',width=15, text= "25 Punkte", command=self.HouseClick)
                buttonHaus.grid(row=14, column=6)
            else:
                buttonHaus = tk.Button(self, bg='white',width=15, text= "25 Punkte", state="disabled")
                buttonHaus.grid(row=14, column=6)
            if self.P1Kstrasse == True:
                buttonKStrasse = tk.Button(self, bg='white',width=15, text= "30 Punkte", command=self.KStrasseClick)
                buttonKStrasse.grid(row=15,column=6)
            else:
                buttonKStrasse = tk.Button(self, bg='white',width=15, text= "30 Punkte", state="disabled")
                buttonKStrasse.grid(row=15,column=6)
            if self.P1GStrasse == True:
                buttonGStrasse = tk.Button(self, bg='white',width=15, text= "40 Punkte", command=self.GStrasseClick)
                buttonGStrasse.grid(row=16, column=6 )
            else:
                buttonGStrasse = tk.Button(self, bg='white',width=15, text= "40 Punkte", state="disabled")
                buttonGStrasse.grid(row=16, column=6 )
            if self.P1Kniffel == True:
                buttonKniffel = tk.Button(self, bg='white',width=15, text= "50 Punkte",command=self.KniffelClick)
                buttonKniffel.grid(row=17, column=6)
            else:
                buttonKniffel = tk.Button(self, bg='white',width=15, text= "50 Punkte", state="disabled")
                buttonKniffel.grid(row=17, column=6)
            if self.P1Chance == True:
                buttonChance = tk.Button(self, bg='white',width=15, text= "Alle Augen Zaehlen", command=self.ChanceClick)
                buttonChance.grid(row=18, column=6)
            else:
                buttonChance = tk.Button(self, bg='white',width=15, text= "Alle Augen Zaehlen", state="disabled")
                buttonChance.grid(row=18, column=6)
        labelDran=tk.Label(self, text="An der Reihe ist Spieler "+str(self.SP))
        labelDran.grid(row=10,column=2)
        labelround=tk.Label(self, text="Runde: "+str(self.round))
        labelround.grid(row=12,column=2)


       #Berechnet alle einsen fÃƒÂ¼r den Spieler der grad dran ist (nur markierte zaehlen!) und Punkte werden addiert ur momentanen punktzahl
    def buttonEinsClick(self):
        self.turn=1
        self.red1 == 'Nein'
        self.red2 == 'Nein'
        self.red3 == 'Nein'
        self.red4 == 'Nein'
        self.red5 == 'Nein'
        buttonWuerfel = tk.Button(self,text='Wuerfeln', command=self.buttonWuerfelnClick,state="disabled")
        buttonWuerfel.grid(row=6,column=2)
        buttonNaechster=tk.Button(self, width=20, text='naechster', command = self.buttonNaechsterClick)
        buttonNaechster.grid(row=19,column=2)

        if self.SP == 1:
            if self.P1Eins == True:
               buttonEins = tk.Button(self, bg='white',width=15, text= "Einser Zaehlen", height=1, command=self.buttonEinsClick, state="disabled")
               buttonEins.grid(row=2, column=6)
               self.wert1=self.Einser
               self.P1Eins = False
               labelEins1 = tk.Label(self, width=5, text=self.Einser)
               labelEins1.grid(row=2, column=7)
               self.Punkte1=self.Punkte1+self.wert1


        if self.SP == 2 and self.P2Eins == True:
             buttonEins = tk.Button(self, bg='white',width=15, text= "Einser Zaehlen", height=1, command=self.buttonEinsClick, state="disabled")
             buttonEins.grid(row=2, column=6)
             self.wert2=self.Einser
             self.P2Eins = False
             labelEins2 = tk.Label(self, width=5, text=self.Einser)
             labelEins2.grid(row=2, column=8)
             self.Punkte2=self.Punkte2+self.wert2

        if self.SP == 3 and self.P3Eins == True:
             buttonEins = tk.Button(self, bg='white',width=15, text= "Einser Zaehlen", height=1, command=self.buttonEinsClick, state="disabled")
             buttonEins.grid(row=2, column=6)
             self.wert3=self.Einser
             self.P3Eins = False
             labelEins3 = tk.Label(self, width=5, text=self.Einser)
             labelEins3.grid(row=2, column=9)
             self.Punkte3=self.Punkte3+self.wert3

        if self.SP == 4 and self.P4Eins == True:
             buttonEins = tk.Button(self, bg='white',width=15, text= "Einser Zaehlen", height=1, command=self.buttonEinsClick, state="disabled")
             buttonEins.grid(row=2, column=6)
             self.wert4=self.Einser
             self.P4Eins = False
             labelEins4 = tk.Label(self, width=5, text=self.Einser)
             labelEins4.grid(row=2, column=10)
             self.Punkte4=self.Punkte4+self.wert4
        self.Sechser=0
        self.Fuenfer=0
        self.Vierer=0
        self.Dreier=0
        self.Zweier=0
        self.Einser=0

#Berechnet alle zweien fÃƒÂ¼r den Spieler der grad dran ist (nur markierte zaehlen!) und Punkte werden addiert ur momentanen punktzahl

    def buttonZweiClick(self):
        self.turn=1
        self.red1 == 'Nein'
        self.red2 == 'Nein'
        self.red3 == 'Nein'
        self.red4 == 'Nein'
        self.red5 == 'Nein'
        buttonWuerfel = tk.Button(self,text='Wuerfeln', command=self.buttonWuerfelnClick,state="disabled")
        buttonWuerfel.grid(row=6,column=2)
        buttonNaechster=tk.Button(self, width=20, text='naechster', command = self.buttonNaechsterClick)
        buttonNaechster.grid(row=19,column=2)
        if self.SP == 1 and self.P1Zwei== True:
               self.P1Zwei=False
               buttonZwei = tk.Button(self, bg='white',width=15, text= "Zweier Zaehlen", command=self.buttonZweiClick, state="disabled")
               buttonZwei.grid(row=3, column=6)
               self.P1Zwei = False
               labelZwei1 = tk.Label(self, width=5, text=(self.Zweier)*2)
               labelZwei1.grid(row=3, column=7)
               self.wert21=(self.Zweier)*2
               self.Punkte1=self.Punkte1+(self.Zweier)*2
        if self.SP == 2 and self.P2Zwei== True:
           self.P2Zwei== False
           buttonZwei = tk.Button(self, bg='white',width=15, text= "Zweier Zaehlen", command=self.buttonZweiClick, state="disabled")
           buttonZwei.grid(row=3, column=6)
           labelZwei2 = tk.Label(self, width=5, text=(self.Zweier)*2)
           labelZwei2.grid(row=3, column=8)
           self.Punkte2=self.Punkte2+(self.Zweier)*2
           self.wert22=(self.Zweier)*2
        if self.SP == 3 and self.P3Zwei== True:
           self.P3Zwei== False
           buttonZwei = tk.Button(self, bg='white',width=15, text= "Zweier Zaehlen", command=self.buttonZweiClick, state="disabled")
           buttonZwei.grid(row=3, column=6)
           labelZwei3 = tk.Label(self, width=5, text=(self.Zweier)*2)
           labelZwei3.grid(row=3, column=9)
           self.Punkte3=self.Punkte3+(self.Zweier)*2
           self.wert23=(self.Zweier)*2
        if self.SP == 4 and self.P4Zwei== True:
           self.P4Zwei== False
           buttonZwei = tk.Button(self, bg='white',width=15, text= "Zweier Zaehlen", command=self.buttonZweiClick, state="disabled")
           buttonZwei.grid(row=3, column=6)
           labelZwei4 = tk.Label(self, width=5, text=(self.Zweier)*2)
           labelZwei4.grid(row=3, column=10)
           self.Punkte4=self.Punkte4+(self.Zweier)*2
           self.wert24=(self.Zweier)*2
        self.Sechser=0
        self.Fuenfer=0
        self.Vierer=0
        self.Dreier=0
        self.Zweier=0
        self.Einser=0

#Berechnet alle dreien fÃƒÂ¼r den Spieler der grad dran ist (nur markierte zaehlen!) und Punkte werden addiert ur momentanen punktzahl
    def buttonDreiClick(self):
        self.turn=1
        self.red1 == 'Nein'
        self.red2 == 'Nein'
        self.red3 == 'Nein'
        self.red4 == 'Nein'
        self.red5 == 'Nein'
        buttonWuerfel = tk.Button(self,text='Wuerfeln', command=self.buttonWuerfelnClick,state="disabled")
        buttonWuerfel.grid(row=6,column=2)
        buttonNaechster=tk.Button(self, width=20, text='naechster', command = self.buttonNaechsterClick)
        buttonNaechster.grid(row=19,column=2)
        if self.SP == 1 and self.P1Drei== True:
           buttonDrei = tk.Button(self, bg='white',width=15, text= "Dreier Zaehlen", command=self.buttonDreiClick, state="disabled")
           buttonDrei.grid(row=4, column=6)
           self.P1Drei = False
           labelDrei1 = tk.Label(self, width=5, text=(self.Dreier)*3)
           labelDrei1.grid(row=4, column=7)
           self.wert31=(self.Dreier)*3
           self.Punkte1=self.Punkte1+self.wert31
        if self.SP == 2 and self.P2Drei== True:
           buttonDrei = tk.Button(self, bg='white',width=15, text= "Dreier Zaehlen", command=self.buttonDreiClick, state="disabled")
           buttonDrei.grid(row=4, column=6)
           self.P2Drei = False
           labelDrei2 = tk.Label(self, width=5, text=(self.Dreier)*3)
           labelDrei2.grid(row=4, column=8)
           self.wert32=(self.Dreier)*3
           self.Punkte2=self.Punkte2+self.wert32
        if self.SP == 3 and self.P3Drei== True:
           buttonDrei = tk.Button(self, bg='white',width=15, text= "Dreier Zaehlen", command=self.buttonDreiClick, state="disabled")
           buttonDrei.grid(row=4, column=6)
           self.P3Drei = False
           self.wert33=(self.Dreier)*3
           labelDrei3 = tk.Label(self, width=5, text=self.wert33)
           labelDrei3.grid(row=4, column=9)
           self.Punkte3=self.Punkte3+self.wert33
        if self.SP == 4 and self.P4Drei== True:
           buttonDrei = tk.Button(self, bg='white',width=15, text= "Dreier Zaehlen", command=self.buttonDreiClick, state="disabled")
           buttonDrei.grid(row=4, column=6)
           self.P4Drei = False

           self.wert34=(self.Dreier)*3
           labelDrei4 = tk.Label(self, width=5, text=self.wert34)
           labelDrei4.grid(row=4, column=10)
           self.Punkte4=self.Punkte4+self.wert34
        self.Sechser=0
        self.Fuenfer=0
        self.Vierer=0
        self.Dreier=0
        self.Zweier=0
        self.Einser=0

#Berechnet alle vieren fÃƒÂ¼r den Spieler der grad dran ist (nur markierte zaehlen!) und Punkte werden addiert ur momentanen punktzahl
    def buttonVierClick(self):

        self.turn=1
        self.red1 == 'Nein'
        self.red2 == 'Nein'
        self.red3 == 'Nein'
        self.red4 == 'Nein'
        self.red5 == 'Nein'
        buttonWuerfel = tk.Button(self,text='Wuerfeln', command=self.buttonWuerfelnClick,state="disabled")
        buttonWuerfel.grid(row=6,column=2)
        buttonNaechster=tk.Button(self, width=20, text='naechster', command = self.buttonNaechsterClick)
        buttonNaechster.grid(row=19,column=2)
        if self.SP == 1 and self.P1Vier== True:
           buttonVier = tk.Button(self, bg='white',width=15, text= "Vierer Zaehlen", command=self.buttonVierClick, state="disabled")
           buttonVier.grid(row=5, column=6)
           self.P1Vier = False
           labelVier1 = tk.Label(self, width=5, text=(self.Vierer)*4)
           labelVier1.grid(row=5, column=7)
           self.wert41=(self.Vierer)*4
           self.Punkte1=self.Punkte1+(self.Vierer)*4
        if self.SP == 2 and self.P2Vier== True:
           buttonVier = tk.Button(self, bg='white',width=15, text= "Vierer Zaehlen", command=self.buttonVierClick, state="disabled")
           buttonVier.grid(row=5, column=6)
           self.P2Vier = False
           labelVier2 = tk.Label(self, width=5, text=(self.Vierer)*4)
           labelVier2.grid(row=5, column=8)
           self.wert42=(self.Vierer)*4
           self.Punkte2=self.Punkte2+(self.Vierer)*4
        if self.SP == 3 and self.P3Vier== True:
           buttonVier = tk.Button(self, bg='white',width=15, text= "Vierer Zaehlen", command=self.buttonVierClick, state="disabled")
           buttonVier.grid(row=5, column=6)
           self.P3Vier = False
           labelVier3 = tk.Label(self, width=5, text=(self.Vierer)*4)
           labelVier3.grid(row=5, column=9)
           self.wert43=(self.Vierer)*4
           self.Punkte3=self.Punkte3+(self.Vierer)*4
        if self.SP == 4 and self.P4Vier== True:
           buttonVier = tk.Button(self, bg='white',width=15, text= "Vierer Zaehlen", command=self.buttonVierClick, state="disabled")
           buttonVier.grid(row=5, column=6)
           self.P4Vier = False
           labelVier4 = tk.Label(self, width=5, text=(self.Vierer)*4)
           labelVier4.grid(row=5, column=10)
           self.wert44=(self.Vierer)*4
           self.Punkte4=self.Punkte4+(self.Vierer)*4
        self.Sechser=0
        self.Fuenfer=0
        self.Vierer=0
        self.Dreier=0
        self.Zweier=0
        self.Einser=0

#Berechnet alle fuenfen fÃƒÂ¼r den Spieler der grad dran ist (nur markierte zaehlen!) und Punkte werden addiert ur momentanen punktzahl
    def buttonFuenfClick(self):
        self.turn=1
        self.red1 == 'Nein'
        self.red2 == 'Nein'
        self.red3 == 'Nein'
        self.red4 == 'Nein'
        self.red5 == 'Nein'
        buttonWuerfel = tk.Button(self,text='Wuerfeln', command=self.buttonWuerfelnClick,state="disabled")
        buttonWuerfel.grid(row=6,column=2)
        buttonNaechster=tk.Button(self, width=20, text='naechster', command = self.buttonNaechsterClick)
        buttonNaechster.grid(row=19,column=2)
        if self.SP == 1 and self.P1Fuenf== True:
           buttonFuenf = tk.Button(self, bg='white',width=15, text= "Fuenfer Zaehlen", command=self.buttonFuenfClick, state="disabled")
           buttonFuenf.grid(row=6, column=6)
           self.P1Fuenf = False
           labelFuenf1 = tk.Label(self, width=5, text=(self.Fuenfer)*5)
           labelFuenf1.grid(row=6, column=7)
           self.wert51=(self.Fuenfer)*5
           self.Punkte1=self.Punkte1+(self.Fuenfer)*5
        if self.SP == 2 and self.P2Fuenf== True:
           buttonFuenf = tk.Button(self, bg='white',width=15, text= "Fuenfer Zaehlen", command=self.buttonFuenfClick, state="disabled")
           buttonFuenf.grid(row=6, column=6)
           self.P2Fuenf = False
           labelFuenf2 = tk.Label(self, width=5, text=(self.Fuenfer)*5)
           labelFuenf2.grid(row=6, column=8)
           self.wert52=(self.Fuenfer)*5
           self.Punkte2=self.Punkte2+(self.Fuenfer)*5
        if self.SP == 3  and self.P3Fuenf== True:
           buttonFuenf = tk.Button(self, bg='white',width=15, text= "Fuenfer Zaehlen", command=self.buttonFuenfClick, state="disabled")
           buttonFuenf.grid(row=6, column=6)
           self.P3Fuenf = False
           labelFuenf3 = tk.Label(self, width=5, text=(self.Fuenfer)*5)
           labelFuenf3.grid(row=6, column=9)
           self.wert53=(self.Fuenfer)*5
           self.Punkte3=self.Punkte3+(self.Fuenfer)*5
        if self.SP == 4 and self.P4Fuenf== True:
           buttonFuenf = tk.Button(self, bg='white',width=15, text= "Fuenfer Zaehlen", command=self.buttonFuenfClick, state="disabled")
           buttonFuenf.grid(row=6, column=6)
           self.P4Fuenf = False
           labelFuenf4 = tk.Label(self, width=5, text=(self.Fuenfer)*5)
           labelFuenf4.grid(row=6, column=10)
           self.wert54=(self.Fuenfer)*5
           self.Punkte4=self.Punkte4+(self.Fuenfer)*5
        self.Sechser=0
        self.Fuenfer=0
        self.Vierer=0
        self.Dreier=0
        self.Zweier=0
        self.Einser=0

        #Berechnet alle sechsen fÃƒÂ¼r den Spieler der grad dran ist (nur markierte zaehlen!) und Punkte werden addiert ur momentanen punktzahl
    def buttonSechsClick(self):
        self.turn=1
        self.red1 == 'Nein'
        self.red2 == 'Nein'
        self.red3 == 'Nein'
        self.red4 == 'Nein'
        self.red5 == 'Nein'
        buttonWuerfel = tk.Button(self,text='Wuerfeln', command=self.buttonWuerfelnClick,state="disabled")
        buttonWuerfel.grid(row=6,column=2)
        buttonNaechster=tk.Button(self, width=20, text='naechster', command = self.buttonNaechsterClick)
        buttonNaechster.grid(row=19,column=2)

        if self.SP == 1 and self.P1Sechs== True:
           buttonSechs = tk.Button(self, bg='white',width=15, text= "Sechser Zaehlen", command=self.buttonSechsClick, state="disabled")
           buttonSechs.grid(row=7, column=6)
           self.P1Sechs = False
           labelSechs1 = tk.Label(self, width=5, text=(self.Sechser)*6)
           labelSechs1.grid(row=7, column=7)
           self.wert61=(self.Sechser)*6
           self.Punkte1=self.Punkte1+(self.Sechser)*6

        if self.SP == 2 and self.P2Sechs== True:
           buttonSechs = tk.Button(self, bg='white',width=15, text= "Sechser Zaehlen", command=self.buttonSechsClick, state="disabled")
           buttonSechs.grid(row=7, column=6)
           self.P2Sechs = False
           labelSechs2 = tk.Label(self, width=5, text=(self.Sechser)*6)
           labelSechs2.grid(row=7, column=8)
           self.wert62=(self.Sechser)*6
           self.Punkte2=self.Punkte2+(self.Sechser)*6

        if self.SP == 3 and self.P3Sechs== True:
           buttonSechs = tk.Button(self, bg='white',width=15, text= "Sechser Zaehlen", command=self.buttonSechsClick, state="disabled")
           buttonSechs.grid(row=7, column=6)
           self.P3Sechs = False
           labelSechs3 = tk.Label(self, width=5, text=(self.Sechser)*6)
           labelSechs3.grid(row=7, column=9)
           self.wert63=(self.Sechser)*6
           self.Punkte3=self.Punkte3+(self.Sechser)*6

        if self.SP == 4 and self.P4Sechs== True:
           buttonSechs = tk.Button(self, bg='white',width=15, text= "Sechser Zaehlen", command=self.buttonSechsClick, state="disabled")
           buttonSechs.grid(row=7, column=6)
           self.P4Sechs = False
           labelSechs4 = tk.Label(self, width=5, text=(self.Sechser)*6)
           labelSechs4.grid(row=7, column=10)
           self.wert64=(self.Sechser)*6
           self.Punkte1=self.Punkte1+(self.Sechser)*6
        self.Sechser=0
        self.Fuenfer=0
        self.Vierer=0
        self.Dreier=0
        self.Zweier=0
        self.Einser=0


    def button3PaschClick(self):
        self.turn=1
        self.red1 == 'Nein'
        self.red2 == 'Nein'
        self.red3 == 'Nein'
        self.red4 == 'Nein'
        self.red5 == 'Nein'
        buttonWuerfel = tk.Button(self,text='Wuerfeln', command=self.buttonWuerfelnClick,state="disabled")
        buttonWuerfel.grid(row=6,column=2)
        buttonNaechster=tk.Button(self, width=20, text='naechster', command = self.buttonNaechsterClick)
        buttonNaechster.grid(row=19,column=2)

        if self.SP==1:
            if self.Einser>=3 or self.Zweier>=3 or self.Dreier>=3 or self.Vierer>=3 or self.Fuenfer>=3 or self.Sechser>=3:
                self.P13Pasch = False
                self.wertePasch31=((self.Einser)*1+(self.Zweier)*2+(self.Dreier)*3+(self.Vierer)*4+(self.Fuenfer)*5+(self.Sechser)*6)
                labelDreierPasch1=tk.Label(self, width=5, text=self.wertePasch31)
                labelDreierPasch1.grid(row=12, column=7)
                buttonDreierpasch = tk.Button(self, bg='white',width=15, text= "Alle Augen Zaehlen", state='disabled', command=self.button3PaschClick)
                buttonDreierpasch.grid(row=12, column=6)
            else:
                buttonDreierpasch = tk.Button(self, bg='white',width=15, text= "Alle Augen Zaehlen", state='disabled', command=self.button3PaschClick)
                buttonDreierpasch.grid(row=12, column=6)
                labelDreierPasch1=tk.Label(self, width=5, text="X")
                labelDreierPasch1.grid(row=12, column=7)

        elif self.SP==2:
            if self.Einser>=3 or self.Zweier>=3 or self.Dreier>=3 or self.Vierer>=3 or self.Fuenfer>=3 or self.Sechser>=3:
                self.P23Pasch = False
                self.wertePasch32=((self.Einser)*1+(self.Zweier)*2+(self.Dreier)*3+(self.Vierer)*4+(self.Fuenfer)*5+(self.Sechser)*6)
                labelDreierPasch2=tk.Label(self, width=5, text=self.wertePasch32)
                labelDreierPasch2.grid(row=12, column=8)
                buttonDreierpasch = tk.Button(self, bg='white',width=15, text= "Alle Augen Zaehlen", state='disabled', command=self.button3PaschClick)
                buttonDreierpasch.grid(row=12, column=6)
            else:
                buttonDreierpasch = tk.Button(self, bg='white',width=15, text= "Alle Augen Zaehlen", state='disabled', command=self.button3PaschClick)
                buttonDreierpasch.grid(row=12, column=6)
                labelDreierPasch1=tk.Label(self, width=5, text="X")
                labelDreierPasch1.grid(row=12, column=8)
        elif self.SP==3:
            if self.Einser>=3 or self.Zweier>=3 or self.Dreier>=3 or self.Vierer>=3 or self.Fuenfer>=3 or self.Sechser>=3:
                self.P33Pasch = False
                self.wertePasch33=((self.Einser)*1+(self.Zweier)*2+(self.Dreier)*3+(self.Vierer)*4+(self.Fuenfer)*5+(self.Sechser)*6)
                labelDreierPasch3=tk.Label(self, width=5, text=self.wertePasch33)
                labelDreierPasch3.grid(row=12, column=9)
                buttonDreierpasch = tk.Button(self, bg='white',width=15, text= "Alle Augen Zaehlen", state='disabled', command=self.button3PaschClick)
                buttonDreierpasch.grid(row=12, column=6)
            else:
                buttonDreierpasch = tk.Button(self, bg='white',width=15, text= "Alle Augen Zaehlen", state='disabled', command=self.button3PaschClick)
                buttonDreierpasch.grid(row=12, column=6)
                labelDreierPasch1=tk.Label(self, width=5, text="X")
                labelDreierPasch1.grid(row=12, column=9)
        elif self.SP==4:
            if self.Einser>=3 or self.Zweier>=3 or self.Dreier>=3 or self.Vierer>=3 or self.Fuenfer>=3 or self.Sechser>=3:
                self.P43Pasch = False
                self.wertePasch34=((self.Einser)*1+(self.Zweier)*2+(self.Dreier)*3+(self.Vierer)*4+(self.Fuenfer)*5+(self.Sechser)*6)
                labelDreierPasch4=tk.Label(self, width=5, text=self.wertePasch34)
                labelDreierPasch4.grid(row=12, column=10)
                buttonDreierpasch = tk.Button(self, bg='white',width=15, text= "Alle Augen Zaehlen", state='disabled', command=self.button3PaschClick)
                buttonDreierpasch.grid(row=12, column=6)
            else:
                buttonDreierpasch = tk.Button(self, bg='white',width=15, text= "Alle Augen Zaehlen", state='disabled', command=self.button3PaschClick)
                buttonDreierpasch.grid(row=12, column=6)
                labelDreierPasch1=tk.Label(self, width=5, text="X")
                labelDreierPasch1.grid(row=12, column=10)
        self.Sechser=0
        self.Fuenfer=0
        self.Vierer=0
        self.Dreier=0
        self.Zweier=0
        self.Einser=0

    def button4PaschClick(self):
        self.turn=1
        self.red1 == 'Nein'
        self.red2 == 'Nein'
        self.red3 == 'Nein'
        self.red4 == 'Nein'
        self.red5 == 'Nein'
        buttonWuerfel = tk.Button(self,text='Wuerfeln', command=self.buttonWuerfelnClick,state="disabled")
        buttonWuerfel.grid(row=6,column=2)
        buttonNaechster=tk.Button(self, width=20, text='naechster', command = self.buttonNaechsterClick)
        buttonNaechster.grid(row=19,column=2)

        if self.SP==1:
            if self.Einser>=4 or self.Zweier>=4 or self.Dreier>=4 or self.Vierer>=4 or self.Fuenfer>=4 or self.Sechser>=4:
                self.P14Pasch = False
                self.wertePasch41=((self.Einser)*1+(self.Zweier)*2+(self.Dreier)*3+(self.Vierer)*4+(self.Fuenfer)*5+(self.Sechser)*6)
                labelViererPasch1=tk.Label(self, width=5, text=self.wertePasch41)
                labelViererPasch1.grid(row=13, column=7)
                self.wertePasch41=0
                buttonViererpasch = tk.Button(self, bg='white',width=15, text= "Alle Augen Zaehlen", state='disabled', command=self.button4PaschClick)
                buttonViererpasch.grid(row=13, column=6)
            else:
                labelViererPasch1=tk.Label(self, width=5, text="X")
                labelViererPasch1.grid(row=13, column=7)
                buttonViererpasch = tk.Button(self, bg='white',width=15, text= "Alle Augen Zaehlen", state='disabled', command=self.button4PaschClick)
                buttonViererpasch.grid(row=13, column=6)
        elif self.SP==2:
            if self.Einser>=4 or self.Zweier>=4 or self.Dreier>=4 or self.Vierer>=4 or self.Fuenfer>=4 or self.Sechser>=4:
                self.P24Pasch = False
                self.wertePasch42=((self.Einser)*1+(self.Zweier)*2+(self.Dreier)*3+(self.Vierer)*4+(self.Fuenfer)*5+(self.Sechser)*6)
                labelViererPasch2=tk.Label(self, width=5, text=self.wertePasch42)
                labelViererPasch2.grid(row=13, column=8)
                self.wertePasch42=0
                buttonViererpasch = tk.Button(self, bg='white',width=15, text= "Alle Augen Zaehlen", state='disabled', command=self.button4PaschClick)
                buttonViererpasch.grid(row=13, column=6)
            else:
                labelViererPasch1=tk.Label(self, width=5, text="X")
                labelViererPasch1.grid(row=13, column=8)
                buttonViererpasch = tk.Button(self, bg='white',width=15, text= "Alle Augen Zaehlen", state='disabled', command=self.button4PaschClick)
                buttonViererpasch.grid(row=13, column=6)
        elif self.SP==3:
            if self.Einser>=4 or self.Zweier>=4 or self.Dreier>=4 or self.Vierer>=4 or self.Fuenfer>=4 or self.Sechser>=4:
                self.P34Pasch = False
                self.wertePasch43=((self.Einser)*1+(self.Zweier)*2+(self.Dreier)*3+(self.Vierer)*4+(self.Fuenfer)*5+(self.Sechser)*6)
                labelViererPasch3=tk.Label(self, width=5, text=self.wertePasch43)
                labelViererPasch3.grid(row=13, column=9)
                buttonViererpasch = tk.Button(self, bg='white',width=15, text= "Alle Augen Zaehlen", state='disabled', command=self.button4PaschClick)
                buttonViererpasch.grid(row=13, column=6)
            else:
                labelViererPasch1=tk.Label(self, width=5, text="X")
                labelViererPasch1.grid(row=13, column=9)
                buttonViererpasch = tk.Button(self, bg='white',width=15, text= "Alle Augen Zaehlen", state='disabled', command=self.button4PaschClick)
                buttonViererpasch.grid(row=13, column=6)
        elif self.SP==4:
            if self.Einser>=4 or self.Zweier>=4 or self.Dreier>=4 or self.Vierer>=4 or self.Fuenfer>=4 or self.Sechser>=4:
                self.P44Pasch = False
                self.wertePasch44=((self.Einser)*1+(self.Zweier)*2+(self.Dreier)*3+(self.Vierer)*4+(self.Fuenfer)*5+(self.Sechser)*6)
                labelViererPasch4=tk.Label(self, width=5, text=self.wertePasch44)
                labelViererPasch4.grid(row=13, column=10)
                self.wertePasch44=0
                buttonViererpasch = tk.Button(self, bg='white',width=15, text= "Alle Augen Zaehlen", state='disabled', command=self.button4PaschClick)
                buttonViererpasch.grid(row=13, column=6)
            else:
                labelViererPasch1=tk.Label(self, width=5, text="X")
                labelViererPasch1.grid(row=13, column=10)
                buttonViererpasch = tk.Button(self, bg='white',width=15, text= "Alle Augen Zaehlen", state='disabled', command=self.button4PaschClick)
                buttonViererpasch.grid(row=13, column=6)
        self.Sechser=0
        self.Fuenfer=0
        self.Vierer=0
        self.Dreier=0
        self.Zweier=0
        self.Einser=0

    def HouseClick(self):
        self.turn=1
        self.red1 == 'Nein'
        self.red2 == 'Nein'
        self.red3 == 'Nein'
        self.red4 == 'Nein'
        self.red5 == 'Nein'
        buttonWuerfel = tk.Button(self,text='Wuerfeln', command=self.buttonWuerfelnClick,state="disabled")
        buttonWuerfel.grid(row=6,column=2)
        buttonNaechster=tk.Button(self, width=20, text='naechster', command = self.buttonNaechsterClick)
        buttonNaechster.grid(row=19,column=2)
        if self.SP==1:
            if self.Einser==3 and (self.Zweier==2 or self.Dreier==2 or self.Vierer==2 or self.Fuenfer==2 or self.Sechser==2):
                self.P1Haus=False
                labelHaus1=tk.Label(self,width=5,text="25")
                labelHaus1.grid(row=14,column=7)
                buttonHaus=tk.Button(self, bg='white',width=15, text= "25 Punkte", state='disabled')
                buttonHaus.grid(row=14, column=6)
            elif self.Zweier==3 and (self.Einser==2 or self.Dreier==2 or self.Vierer==2 or self.Fuenfer==2 or self.Sechser==2):
                self.P1Haus=False
                labelHaus1=tk.Label(self,width=5,text="25")
                labelHaus1.grid(row=14,column=7)
                buttonHaus=tk.Button(self, bg='white',width=15, text= "25 Punkte", state='disabled')
                buttonHaus.grid(row=14, column=6)
            elif self.Dreier==3 and (self.Einser==2 or self.Zweier==2 or self.Vierer==2 or self.Fuenfer==2 or self.Sechser==2):
                self.P1Haus=False
                labelHaus1=tk.Label(self,width=5,text="25")
                labelHaus1.grid(row=14,column=7)
                buttonHaus=tk.Button(self, bg='white',width=15, text= "25 Punkte", state='disabled')
                buttonHaus.grid(row=14, column=6)
            elif self.Vierer==3 and (self.Einser==2 or self.Zweier==2 or self.Dreier==2 or self.Fuenfer==2 or self.Sechser==2):
                self.P1Haus=False
                labelHaus1=tk.Label(self,width=5,text="25")
                labelHaus1.grid(row=14,column=7)
                buttonHaus=tk.Button(self, bg='white',width=15, text= "25 Punkte", state='disabled')
                buttonHaus.grid(row=14, column=6)
            elif self.Fuenfer==3 and (self.Einser==2 or self.Zweier==2 or self.Dreier==2 or self.Vierer==2 or self.Sechser==2):
                self.P1Haus=False
                labelHaus1=tk.Label(self,width=5,text="25")
                labelHaus1.grid(row=14,column=7)
                buttonHaus=tk.Button(self, bg='white',width=15, text= "25 Punkte", state='disabled')
                buttonHaus.grid(row=14, column=6)
            elif self.Sechser==3 and (self.Einser==2 or self.Zweier==2 or self.Dreier==2 or self.Vierer==2 or self.Fuenfer==2):
                self.P1Haus=False
                labelHaus1=tk.Label(self,width=5,text="25")
                labelHaus1.grid(row=14,column=7)
                buttonHaus=tk.Button(self, bg='white',width=15, text= "25 Punkte", state='disabled')
                buttonHaus.grid(row=14, column=6)
            else:
                self.P1Haus=False
                labelHaus1=tk.Label(self,width=5,text="X")
                labelHaus1.grid(row=14,column=7)
                buttonHaus=tk.Button(self, bg='white',width=15, text= "25 Punkte", state='disabled')
                buttonHaus.grid(row=14, column=6)


        elif self.SP==2:
            if self.Einser==3 and (self.Zweier==2 or self.Dreier==2 or self.Vierer==2 or self.Fuenfer==2 or self.Sechser==2):
                self.P2Haus=False
                labelHaus2=tk.Label(self,width=5,text="25")
                labelHaus2.grid(row=14,column=8)
                buttonHaus=tk.Button(self, bg='white',width=15, text= "25 Punkte", state='disabled')
                buttonHaus.grid(row=14, column=6)
            elif self.Zweier==3 and (self.Einser==2 or self.Dreier==2 or self.Vierer==2 or self.Fuenfer==2 or self.Sechser==2):
                self.P2Haus=False
                labelHaus2=tk.Label(self,width=5,text="25")
                labelHaus2.grid(row=14,column=8)
                buttonHaus=tk.Button(self, bg='white',width=15, text= "25 Punkte", state='disabled')
                buttonHaus.grid(row=14, column=6)
            elif self.Dreier==3 and (self.Einser==2 or self.Zweier==2 or self.Vierer==2 or self.Fuenfer==2 or self.Sechser==2):
                self.P2Haus=False
                labelHaus2=tk.Label(self,width=5,text="25")
                labelHaus2.grid(row=14,column=8)
                buttonHaus=tk.Button(self, bg='white',width=15, text= "25 Punkte", state='disabled')
                buttonHaus.grid(row=14, column=6)
            elif self.Vierer==3 and (self.Einser==2 or self.Zweier==2 or self.Dreier==2 or self.Fuenfer==2 or self.Sechser==2):
                self.P2Haus=False
                labelHaus2=tk.Label(self,width=5,text="25")
                labelHaus2.grid(row=14,column=8)
                buttonHaus=tk.Button(self, bg='white',width=15, text= "25 Punkte", state='disabled')
                buttonHaus.grid(row=14, column=6)
            elif self.Fuenfer==3 and (self.Einser==2 or self.Zweier==2 or self.Dreier==2 or self.Vierer==2 or self.Sechser==2):
                self.P2Haus=False
                labelHaus2=tk.Label(self,width=5,text="25")
                labelHaus2.grid(row=14,column=8)
                buttonHaus=tk.Button(self, bg='white',width=15, text= "25 Punkte", state='disabled')
                buttonHaus.grid(row=14, column=6)
            elif self.Sechser==3 and (self.Einser==2 or self.Zweier==2 or self.Dreier==2 or self.Vierer==2 or self.Fuenfer==2):
                self.P2Haus=False
                labelHaus2=tk.Label(self,width=5,text="25")
                labelHaus2.grid(row=14,column=8)
                buttonHaus=tk.Button(self, bg='white',width=15, text= "25 Punkte", state='disabled')
                buttonHaus.grid(row=14, column=6)
            else:
                self.P1Haus=False
                labelHaus1=tk.Label(self,width=5,text="X")
                labelHaus1.grid(row=14,column=8)
                buttonHaus=tk.Button(self, bg='white',width=15, text= "25 Punkte", state='disabled')
                buttonHaus.grid(row=14, column=6)

        elif self.SP==3:
            if self.Einser==3 and (self.Zweier==2 or self.Dreier==2 or self.Vierer==2 or self.Fuenfer==2 or self.Sechser==2):
                self.P3Haus=False
                labelHaus3=tk.Label(self,width=5,text="25")
                labelHaus3.grid(row=14,column=9)
                buttonHaus=tk.Button(self, bg='white',width=15, text= "25 Punkte", state='disabled')
                buttonHaus.grid(row=14, column=6)
            elif self.Zweier==3 and (self.Einser==2 or self.Dreier==2 or self.Vierer==2 or self.Fuenfer==2 or self.Sechser==2):
                self.P3Haus=False
                labelHaus3=tk.Label(self,width=5,text="25")
                labelHaus3.grid(row=14,column=9)
                buttonHaus=tk.Button(self, bg='white',width=15, text= "25 Punkte", state='disabled')
                buttonHaus.grid(row=14, column=6)
            elif self.Dreier==3 and (self.Einser==2 or self.Zweier==2 or self.Vierer==2 or self.Fuenfer==2 or self.Sechser==2):
                self.P3Haus=False
                labelHaus3=tk.Label(self,width=5,text="25")
                labelHaus3.grid(row=14,column=9)
                buttonHaus=tk.Button(self, bg='white',width=15, text= "25 Punkte", state='disabled')
                buttonHaus.grid(row=14, column=6)
            elif self.Vierer==3 and (self.Einser==2 or self.Zweier==2 or self.Dreier==2 or self.Fuenfer==2 or self.Sechser==2):
                self.P3Haus=False
                labelHaus3=tk.Label(self,width=5,text="25")
                labelHaus3.grid(row=14,column=9)
                buttonHaus=tk.Button(self, bg='white',width=15, text= "25 Punkte", state='disabled')
                buttonHaus.grid(row=14, column=6)
            elif self.Fuenfer==3 and (self.Einser==2 or self.Zweier==2 or self.Dreier==2 or self.Vierer==2 or self.Sechser==2):
                self.P3Haus=False
                labelHaus3=tk.Label(self,width=5,text="25")
                labelHaus3.grid(row=14,column=9)
                buttonHaus=tk.Button(self, bg='white',width=15, text= "25 Punkte", state='disabled')
                buttonHaus.grid(row=14, column=6)
            elif self.Sechser==3 and (self.Einser==2 or self.Zweier==2 or self.Dreier==2 or self.Vierer==2 or self.Fuenfer==2):
                self.P3Haus=False
                labelHaus3=tk.Label(self,width=5,text="25")
                labelHaus3.grid(row=14,column=9)
                buttonHaus=tk.Button(self, bg='white',width=15, text= "25 Punkte", state='disabled')
                buttonHaus.grid(row=14, column=6)
            else:
                self.P1Haus=False
                labelHaus1=tk.Label(self,width=5,text="X")
                labelHaus1.grid(row=14,column=9)
                buttonHaus=tk.Button(self, bg='white',width=15, text= "25 Punkte", state='disabled')
                buttonHaus.grid(row=14, column=6)
        elif self.SP==4:
            if self.Einser==3 and (self.Zweier==2 or self.Dreier==2 or self.Vierer==2 or self.Fuenfer==2 or self.Sechser==2):
                self.P4Haus=False
                labelHaus4=tk.Label(self,width=5,text="25")
                labelHaus4.grid(row=14,column=10)
                buttonHaus=tk.Button(self, bg='white',width=15, text= "25 Punkte", state='disabled')
                buttonHaus.grid(row=14, column=6)
            elif self.Zweier==3 and (self.Einser==2 or self.Dreier==2 or self.Vierer==2 or self.Fuenfer==2 or self.Sechser==2):
                self.P4Haus=False
                labelHaus4=tk.Label(self,width=5,text="25")
                labelHaus4.grid(row=14,column=10)
                buttonHaus=tk.Button(self, bg='white',width=15, text= "25 Punkte", state='disabled')
                buttonHaus.grid(row=14, column=6)
            elif self.Dreier==3 and (self.Einser==2 or self.Zweier==2 or self.Vierer==2 or self.Fuenfer==2 or self.Sechser==2):
                self.P4Haus=False
                labelHaus4=tk.Label(self,width=5,text="25")
                labelHaus4.grid(row=14,column=10)
                buttonHaus=tk.Button(self, bg='white',width=15, text= "25 Punkte", state='disabled')
                buttonHaus.grid(row=14, column=6)
            elif self.Vierer==3 and (self.Einser==2 or self.Zweier==2 or self.Dreier==2 or self.Fuenfer==2 or self.Sechser==2):
                self.P4Haus=False
                labelHaus4=tk.Label(self,width=5,text="25")
                labelHaus4.grid(row=14,column=10)
                buttonHaus=tk.Button(self, bg='white',width=15, text= "25 Punkte", state='disabled')
                buttonHaus.grid(row=14, column=6)
            elif self.Fuenfer==3 and (self.Einser==2 or self.Zweier==2 or self.Dreier==2 or self.Vierer==2 or self.Sechser==2):
                self.P4Haus=False
                labelHaus4=tk.Label(self,width=5,text="25")
                labelHaus4.grid(row=14,column=10)
                buttonHaus=tk.Button(self, bg='white',width=15, text= "25 Punkte", state='disabled')
                buttonHaus.grid(row=14, column=6)
            elif self.Sechser==3 and (self.Einser==2 or self.Zweier==2 or self.Dreier==2 or self.Vierer==2 or self.Fuenfer==2):
                self.P4Haus=False
                labelHaus4=tk.Label(self,width=5,text="25")
                labelHaus8.grid(row=14,column=10)
                buttonHaus=tk.Button(self, bg='white',width=15, text= "25 Punkte", state='disabled')
                buttonHaus.grid(row=14, column=6)
            else:
                self.P1Haus=False
                labelHaus1=tk.Label(self,width=5,text="X")
                labelHaus1.grid(row=14,column=10)
                buttonHaus=tk.Button(self, bg='white',width=15, text= "25 Punkte", state='disabled')
                buttonHaus.grid(row=14, column=6)
        self.Sechser=0
        self.Fuenfer=0
        self.Vierer=0
        self.Dreier=0
        self.Zweier=0
        self.Einser=0

    def KStrasseClick(self):
        self.turn=1
        self.red1 == 'Nein'
        self.red2 == 'Nein'
        self.red3 == 'Nein'
        self.red4 == 'Nein'
        self.red5 == 'Nein'
        buttonWuerfel = tk.Button(self,text='Wuerfeln', command=self.buttonWuerfelnClick,state="disabled")
        buttonWuerfel.grid(row=6,column=2)
        buttonNaechster=tk.Button(self, width=20, text='naechster', command = self.buttonNaechsterClick)
        buttonNaechster.grid(row=19,column=2)
        if self.SP==1:
            if self.Einser>=1 and self.Zweier>=1 and self.Dreier>=1 and self.Vierer>=1:
                self.P1KStrasse = False
                labelKStrasse1=tk.Label(self, width=5, text="30")
                labelKStrasse1.grid(row=15, column=7)
                buttonKStrasse = tk.Button(self, bg='white',width=15, text= "30 Punkte", state='disabled')
                buttonKStrasse.grid(row=15, column=6 )
            elif self.Zweier>=1 and self.Dreier>=1 and self.Vierer>=1 and self.Fuenfer>=1 :
                self.P1KStrasse = False
                labelKStrasse1=tk.Label(self, width=5, text="30")
                labelKStrasse1.grid(row=15, column=7)
                buttonKStrasse = tk.Button(self, bg='white',width=15, text= "30 Punkte", state='disabled')
                buttonKStrasse.grid(row=15, column=6 )
            elif self.Dreier>=1 and self.Vierer>=1 and self.Fuenfer>=1 and self.Sechser>=1:
                self.P1KStrasse = False
                labelKStrasse1=tk.Label(self, width=5, text="30")
                labelKStrasse1.grid(row=15, column=7)
                buttonKStrasse = tk.Button(self, bg='white',width=15, text= "30 Punkte", state='disabled')
                buttonKStrasse.grid(row=15, column=6 )
            else:
                self.P1KStrasse = False
                labelKStrasse1=tk.Label(self, width=5, text="X")
                labelKStrasse1.grid(row=15, column=7)
                buttonKStrasse = tk.Button(self, bg='white',width=15, text= "30 Punkte", state='disabled')
                buttonKStrasse.grid(row=15, column=6 )

        elif self.SP==2:
            if self.Einser>=1 and self.Zweier>=1 and self.Dreier>=1 and self.Vierer>=1:
                self.P2KStrasse = False
                labelKStrasse2=tk.Label(self, width=5, text="30")
                labelKStrasse2.grid(row=15, column=8)
                buttonKStrasse = tk.Button(self, bg='white',width=15, text= "30 Punkte", state='disabled')
                buttonKStrasse.grid(row=15, column=6 )
            elif self.Zweier>=1 and self.Dreier>=1 and self.Vierer>=1 and self.Fuenfer>=1 :
                self.P2KStrasse = False
                labelKStrasse2=tk.Label(self, width=5, text="30")
                labelKStrasse2.grid(row=15, column=8)
                buttonKStrasse = tk.Button(self, bg='white',width=15, text= "30 Punkte", state='disabled')
                buttonKStrasse.grid(row=15, column=6 )
            elif self.Dreier>=1 and self.Vierer>=1 and self.Fuenfer>=1 and self.Sechser>=1:
                self.P2KStrasse = False
                labelKStrasse2=tk.Label(self, width=5, text="30")
                labelKStrasse2.grid(row=15, column=8)
                buttonKStrasse = tk.Button(self, bg='white',width=15, text= "30 Punkte", state='disabled')
                buttonKStrasse.grid(row=15, column=6 )
            else:
                self.P1KStrasse = False
                labelKStrasse1=tk.Label(self, width=5, text="X")
                labelKStrasse1.grid(row=15, column=8)
                buttonKStrasse = tk.Button(self, bg='white',width=15, text= "30 Punkte", state='disabled')
                buttonKStrasse.grid(row=15, column=6 )
        elif self.SP==3:
            if self.Einser>=1 and self.Zweier>=1 and self.Dreier>=1 and self.Vierer>=1:
                self.P3KStrasse = False
                labelKStrasse3=tk.Label(self, width=5, text="30")
                labelKStrasse3.grid(row=15, column=9)
                buttonKStrasse = tk.Button(self, bg='white',width=15, text= "30 Punkte", state='disabled')
                buttonKStrasse.grid(row=15, column=6 )
            elif self.Zweier>=1 and self.Dreier>=1 and self.Vierer>=1 and self.Fuenfer>=1 :
                self.P3KStrasse = False
                labelKStrasse3=tk.Label(self, width=5, text="30")
                labelKStrasse3.grid(row=15, column=9)
                buttonKStrasse = tk.Button(self, bg='white',width=15, text= "30 Punkte", state='disabled')
                buttonKStrasse.grid(row=15, column=6 )
            elif self.Dreier>=1 and self.Vierer>=1 and self.Fuenfer>=1 and self.Sechser>=1:
                self.P3KStrasse = False
                labelKStrasse3=tk.Label(self, width=5, text="30")
                labelKStrasse3.grid(row=15, column=9)
                buttonKStrasse = tk.Button(self, bg='white',width=15, text= "30 Punkte", state='disabled')
                buttonKStrasse.grid(row=15, column=6 )
            else:
                self.P1KStrasse = False
                labelKStrasse1=tk.Label(self, width=5, text="X")
                labelKStrasse1.grid(row=15, column=9)
                buttonKStrasse = tk.Button(self, bg='white',width=15, text= "30 Punkte", state='disabled')
                buttonKStrasse.grid(row=15, column=6 )
        elif self.SP==4:
            if self.Einser>=1 and self.Zweier>=1 and self.Dreier>=1 and self.Vierer>=1:
                self.P4Kstrasse = False
                labelKStrasse4=tk.Label(self, width=5, text="30")
                labelKStrasse4.grid(row=15, column=10)
                buttonKStrasse = tk.Button(self, bg='white',width=15, text= "30 Punkte", state='disabled')
                buttonKStrasse.grid(row=15, column=6 )
            elif self.Zweier>=1 and self.Dreier>=1 and self.Vierer>=1 and self.Fuenfer>=1 :
                self.P4KStrasse = False
                labelKStrasse4=tk.Label(self, width=5, text="30")
                labelKStrasse4.grid(row=15, column=10)
                buttonKStrasse = tk.Button(self, bg='white',width=15, text= "30 Punkte", state='disabled')
                buttonKStrasse.grid(row=15, column=6 )
            elif self.Dreier>=1 and self.Vierer>=1 and self.Fuenfer>=1 and self.Sechser>=1:
                self.P4KStrasse = False
                labelKStrasse4=tk.Label(self, width=5, text="30")
                labelKStrasse4.grid(row=15, column=10)
                buttonKStrasse = tk.Button(self, bg='white',width=15, text= "30 Punkte", state='disabled')
                buttonKStrasse.grid(row=15, column=6 )
            else:
                self.P1KStrasse = False
                labelKStrasse1=tk.Label(self, width=5, text="X")
                labelKStrasse1.grid(row=15, column=10)
                buttonKStrasse = tk.Button(self, bg='white',width=15, text= "30 Punkte", state='disabled')
                buttonKStrasse.grid(row=15, column=6 )
        self.Sechser=0
        self.Fuenfer=0
        self.Vierer=0
        self.Dreier=0
        self.Zweier=0
        self.Einser=0

    def GStrasseClick(self):
        self.turn=1
        self.red1 == 'Nein'
        self.red2 == 'Nein'
        self.red3 == 'Nein'
        self.red4 == 'Nein'
        self.red5 == 'Nein'
        buttonWuerfel = tk.Button(self,text='Wuerfeln', command=self.buttonWuerfelnClick,state="disabled")
        buttonWuerfel.grid(row=6,column=2)
        buttonNaechster=tk.Button(self, width=20, text='naechster', command = self.buttonNaechsterClick)
        buttonNaechster.grid(row=19,column=2)
        if self.SP==1:
            if self.Einser==1 and self.Zweier==1 and self.Dreier==1 and self.Vierer==1 and self.Fuenfer==1:
                self.P1GStrasse = False
                labelGStrasse2=tk.Label(self, width=5, text="40")
                labelGStrasse2.grid(row=16, column=7)
                buttonGStrasse = tk.Button(self, bg='white',width=15, text= "40 Punkte", state='disabled')
                buttonGStrasse.grid(row=16, column=6 )
            elif self.Zweier==1 and self.Dreier==1 and self.Vierer==1 and self.Fuenfer==1 and self.Sechser==1:
                self.P1GStrasse = False
                labelGStrasse2=tk.Label(self, width=5, text="40")
                labelGStrasse2.grid(row=16, column=7)
                buttonGStrasse = tk.Button(self, bg='white',width=15, text= "40 Punkte", state='disabled')
                buttonGStrasse.grid(row=16, column=6 )
            else:
                self.P1GStrasse = False
                labelGStrasse2=tk.Label(self, width=5, text="X")
                labelGStrasse2.grid(row=16, column=7)
                buttonGStrasse = tk.Button(self, bg='white',width=15, text= "40 Punkte", state='disabled')
                buttonGStrasse.grid(row=16, column=6 )
        elif self.SP==2:
            if self.Einser==1 and self.Zweier==1 and self.Dreier==1 and self.Vierer==1 and self.Fuenfer==1:
                self.P2GStrasse = False
                labelGStrasse2=tk.Label(self, width=5, text="40")
                labelGStrasse2.grid(row=16, column=8)
                buttonGStrasse = tk.Button(self, bg='white',width=15, text= "40 Punkte", state='disabled')
                buttonGStrasse.grid(row=16, column=6 )
            elif self.Zweier==1 and self.Dreier==1 and self.Vierer==1 and self.Fuenfer==1 and self.Sechser==1:
                self.P2GStrasse = False
                labelGStrasse2=tk.Label(self, width=5, text="40")
                labelGStrasse2.grid(row=16, column=8)
                buttonGStrasse = tk.Button(self, bg='white',width=15, text= "40 Punkte", state='disabled')
                buttonGStrasse.grid(row=16, column=6 )
            else:
                self.P1GStrasse = False
                labelGStrasse2=tk.Label(self, width=5, text="X")
                labelGStrasse2.grid(row=16, column=8)
                buttonGStrasse = tk.Button(self, bg='white',width=15, text= "40 Punkte", state='disabled')
                buttonGStrasse.grid(row=16, column=6 )
        elif self.SP==3:
            if self.Einser==1 and self.Zweier==1 and self.Dreier==1 and self.Vierer==1 and self.Fuenfer==1:
                self.P3GStrasse = False
                labelGStrasse3=tk.Label(self, width=5, text="40")
                labelGStrasse3.grid(row=16, column=9)
                buttonGStrasse = tk.Button(self, bg='white',width=15, text= "40 Punkte", state='disabled')
                buttonGStrasse.grid(row=16, column=6 )
            elif self.Zweier==1 and self.Dreier==1 and self.Vierer==1 and self.Fuenfer==1 and self.Sechser==1:
                self.P3GStrasse = False
                labelGStrasse3=tk.Label(self, width=5, text="40")
                labelGStrasse3.grid(row=16, column=9)
                buttonGStrasse = tk.Button(self, bg='white',width=15, text= "40 Punkte", state='disabled')
                buttonGStrasse.grid(row=16, column=6 )
            else:
                self.P1GStrasse = False
                labelGStrasse2=tk.Label(self, width=5, text="X")
                labelGStrasse2.grid(row=16, column=9)
                buttonGStrasse = tk.Button(self, bg='white',width=15, text= "40 Punkte", state='disabled')
                buttonGStrasse.grid(row=16, column=6 )
        elif self.SP==4:
            if self.Einser==1 and self.Zweier==1 and self.Dreier==1 and self.Vierer==1 and self.Fuenfer==1:
                self.P4GStrasse = False
                labelGStrasse4=tk.Label(self, width=5, text="40")
                labelGStrasse4.grid(row=16, column=10)
                buttonGStrasse = tk.Button(self, bg='white',width=15, text= "40 Punkte", state='disabled')
                buttonGStrasse.grid(row=16, column=6 )
            elif self.Zweier==1 and self.Dreier==1 and self.Vierer==1 and self.Fuenfer==1 and self.Sechser==1:
                self.P4GStrasse = False
                labelGStrasse4=tk.Label(self, width=5, text="40")
                labelGStrasse4.grid(row=16, column=10)
                buttonGStrasse = tk.Button(self, bg='white',width=15, text= "40 Punkte", state='disabled')
                buttonGStrasse.grid(row=16, column=6 )
            else:
                self.P1GStrasse = False
                labelGStrasse2=tk.Label(self, width=5, text="X")
                labelGStrasse2.grid(row=16, column=10)
                buttonGStrasse = tk.Button(self, bg='white',width=15, text= "40 Punkte", state='disabled')
                buttonGStrasse.grid(row=16, column=6 )
        self.Sechser=0
        self.Fuenfer=0
        self.Vierer=0
        self.Dreier=0
        self.Zweier=0
        self.Einser=0


    def KniffelClick(self):
        self.turn=1
        self.red1 == 'Nein'
        self.red2 == 'Nein'
        self.red3 == 'Nein'
        self.red4 == 'Nein'
        self.red5 == 'Nein'
        buttonWuerfel = tk.Button(self,text='Wuerfeln', command=self.buttonWuerfelnClick,state="disabled")
        buttonWuerfel.grid(row=6,column=2)
        buttonNaechster=tk.Button(self, width=20, text='naechster', command = self.buttonNaechsterClick)
        buttonNaechster.grid(row=19,column=2)

        if self.SP==1:
            if self.Einser==5 or self.Zweier==5 or self.Dreier==5 or self.Vierer==5 or self.Fuenfer==5 or self.Sechser==5:
                self.P1Kniffel = False
                labelKniffel1=tk.Label(self, width=5, text="50")
                labelKniffel1.grid(row=17, column=7)
                buttonKniffel = tk.Button(self, bg='white',width=15, text= "50 Punkte", state='disabled', command=self.button4PaschClick)
                buttonKniffel.grid(row=17, column=6)
            else:
                self.P1Kniffel = False
                labelKniffel1=tk.Label(self, width=5, text="X")
                labelKniffel1.grid(row=17, column=7)
                buttonKniffel = tk.Button(self, bg='white',width=15, text= "50 Punkte", state='disabled', command=self.button4PaschClick)
                buttonKniffel.grid(row=17, column=6)
        elif self.SP==2:
            if self.Einser==5 or self.Zweier==5 or self.Dreier==5 or self.Vierer==5 or self.Fuenfer==5 or self.Sechser==5:
                self.P2Kniffel = False
                labelKniffel2=tk.Label(self, width=5, text="50")
                labelKniffel2.grid(row=17, column=8)
                buttonKniffel = tk.Button(self, bg='white',width=15, text= "50 Punkte", state='disabled', command=self.button4PaschClick)
                buttonKniffel.grid(row=17, column=6)
            else:
                self.P1Kniffel = False
                labelKniffel1=tk.Label(self, width=5, text="X")
                labelKniffel1.grid(row=17, column=8)
                buttonKniffel = tk.Button(self, bg='white',width=15, text= "50 Punkte", state='disabled', command=self.button4PaschClick)
                buttonKniffel.grid(row=17, column=6)
        elif self.SP==3:
            if self.Einser==5 or self.Zweier==5 or self.Dreier==5 or self.Vierer==5 or self.Fuenfer==5 or self.Sechser==5:
                self.P3Kniffel = False
                labelKniffel3=tk.Label(self, width=5, text="50")
                labelKniffel3.grid(row=17, column=9)
                buttonKniffel = tk.Button(self, bg='white',width=15, text= "50 Punkte", state='disabled', command=self.button4PaschClick)
                buttonKniffel.grid(row=17, column=6)
            else:
                self.P1Kniffel = False
                labelKniffel1=tk.Label(self, width=5, text="X")
                labelKniffel1.grid(row=17, column=9)
                buttonKniffel = tk.Button(self, bg='white',width=15, text= "50 Punkte", state='disabled', command=self.button4PaschClick)
                buttonKniffel.grid(row=17, column=6)
        elif self.SP==4:
            if self.Einser==5 or self.Zweier==5 or self.Dreier==5 or self.Vierer==5 or self.Fuenfer==5 or self.Sechser==5:
                self.P4Kniffel = False
                labelKniffel4=tk.Label(self, width=5, text="50")
                labelKniffel4.grid(row=17, column=10)
                buttonKniffel = tk.Button(self, bg='white',width=15, text= "50 Punkte", state='disabled', command=self.button4PaschClick)
                buttonKniffel.grid(row=17, column=6)
            else:
                self.P1Kniffel = False
                labelKniffel1=tk.Label(self, width=5, text="X")
                labelKniffel1.grid(row=17, column=10)
                buttonKniffel = tk.Button(self, bg='white',width=15, text= "50 Punkte", state='disabled', command=self.button4PaschClick)
                buttonKniffel.grid(row=17, column=6)
        self.Sechser=0
        self.Fuenfer=0
        self.Vierer=0
        self.Dreier=0
        self.Zweier=0
        self.Einser=0
    def ChanceClick(self):
        self.turn=1
        self.red1 == 'Nein'
        self.red2 == 'Nein'
        self.red3 == 'Nein'
        self.red4 == 'Nein'
        self.red5 == 'Nein'
        buttonWuerfel = tk.Button(self,text='Wuerfeln', command=self.buttonWuerfelnClick,state="disabled")
        buttonWuerfel.grid(row=6,column=2)
        buttonNaechster=tk.Button(self, width=20, text='naechster', command = self.buttonNaechsterClick)
        buttonNaechster.grid(row=19,column=2)
        if self.SP==1:
            self.P1Chance = False
            self.werteChance1=((self.Einser)*1+(self.Zweier)*2+(self.Dreier)*3+(self.Vierer)*4+(self.Fuenfer)*5+(self.Sechser)*6)
            labelChance1=tk.Label(self, width=5, text=self.werteChance1)
            labelChance1.grid(row=18, column=7)
            buttonChance = tk.Button(self, bg='white',width=15, text= "Alle Augen Zaehlen", state='disabled', command=self.button4PaschClick)
            buttonChance.grid(row=18, column=6)
        elif self.SP==2:
            self.P2Chance = False
            self.werteChance2=((self.Einser)*1+(self.Zweier)*2+(self.Dreier)*3+(self.Vierer)*4+(self.Fuenfer)*5+(self.Sechser)*6)
            labelChance2=tk.Label(self, width=5, text=self.werteChance2)
            labelChance2.grid(row=18, column=8)
            buttonChance = tk.Button(self, bg='white',width=15, text= "Alle Augen Zaehlen", state='disabled', command=self.button4PaschClick)
            buttonChance.grid(row=18, column=6)
        elif self.SP==3:
            self.P3Chance = False
            self.werteChance3=((self.Einser)*1+(self.Zweier)*2+(self.Dreier)*3+(self.Vierer)*4+(self.Fuenfer)*5+(self.Sechser)*6)
            labelChance3=tk.Label(self, width=5, text=self.werteChance3)
            labelChance3.grid(row=18, column=9)
            buttonChance = tk.Button(self, bg='white',width=15, text= "Alle Augen Zaehlen", state='disabled', command=self.button4PaschClick)
            buttonChance.grid(row=18, column=6)
        elif self.SP==4:
            self.P4Chance = False
            self.werteChance4=((self.Einser)*1+(self.Zweier)*2+(self.Dreier)*3+(self.Vierer)*4+(self.Fuenfer)*5+(self.Sechser)*6)
            labelChance4=tk.Label(self, width=5, text=self.werteChance4)
            labelChance4.grid(row=18, column=10)
            buttonChance = tk.Button(self, bg='white',width=15, text= "Alle Augen Zaehlen", state='disabled', command=self.ChanceClick())
            buttonChance.grid(row=18, column=6)
        self.Sechser=0
        self.Fuenfer=0
        self.Vierer=0
        self.Dreier=0
        self.Zweier=0
        self.Einser=0
    def buttonWuerfelnClick(self):
        if self.turn==0:
            buttonEins = tk.Button(self, bg='white',width=15, text= "Einser Zaehlen", height=1, command=self.buttonEinsClick)
            buttonEins.grid(row=2, column=6)
            buttonZwei = tk.Button(self, bg='white',width=15, text= "Zweier Zaehlen", command=self.buttonZweiClick)
            buttonZwei.grid(row=3, column=6)
            buttonDrei = tk.Button(self, bg='white',width=15, text= "Dreier Zaehlen", command=self.buttonDreiClick)
            buttonDrei.grid(row=4, column=6)
            buttonVier = tk.Button(self, bg='white',width=15, text= "Vierer Zaehlen", command=self.buttonVierClick)
            buttonVier.grid(row=5, column=6)
            buttonFuenf = tk.Button(self, bg='white',width=15, text= "Fuenfer Zaehlen", command=self.buttonFuenfClick)
            buttonFuenf.grid(row=6, column=6)
            buttonSechs = tk.Button(self, bg='white',width=15, text= "Sechser Zaehlen", command=self.buttonSechsClick)
            buttonSechs.grid(row=7, column=6)
            buttonDreierpasch = tk.Button(self, bg='white',width=15, text= "Alle Augen Zaehlen", command=self.button3PaschClick)#
            buttonDreierpasch.grid(row=12, column=6)
            buttonViererpasch = tk.Button(self, bg='white',width=15, text= "Alle Augen Zaehlen", command=self.button4PaschClick)
            buttonViererpasch.grid(row=13, column=6)
            buttonHaus = tk.Button(self, bg='white',width=15, text= "25 Punkte", command=self.HouseClick)
            buttonHaus.grid(row=14, column=6)
            buttonKStrasse = tk.Button(self, bg='white',width=15, text= "30 Punkte", command=self.KStrasseClick)
            buttonKStrasse.grid(row=15,column=6)
            buttonGStrasse = tk.Button(self, bg='white',width=15, text= "40 Punkte", command=self.GStrasseClick)
            buttonGStrasse.grid(row=16, column=6 )
            buttonKniffel = tk.Button(self, bg='white',width=15, text= "50 Punkte", command=self.KniffelClick)
            buttonKniffel.grid(row=17, column=6)
            buttonChance = tk.Button(self, bg='white',width=15, text= "Alle Augen Zaehlen",command=self.ChanceClick)
            buttonChance.grid(row=18, column=6)
            self.turn=1



        if self.turn<=3:
            self.turn += 1
            for i in range(5):
                t=wuerfeln(self)
                if i ==0 and  self.red1 == 'Nein':


                    if t == 1:
                        self.augen1 = 1
                        buttonAuswaehlen1 = tk.Button(self, image = self.imageWuerfel1 , command = self.buttonAuswahl1Click)
                        buttonAuswaehlen1.grid(row=2,column=0,padx=20,pady=40, rowspan=5)
                    elif t == 2:
                        self.augen1 = 2
                        buttonAuswaehlen1 = tk.Button(self, image = self.imageWuerfel2 , command = self.buttonAuswahl1Click)
                        buttonAuswaehlen1.grid(row=2,column=0,padx=20,pady=40, rowspan=5)
                    elif t == 3:
                        self.augen1 = 3
                        buttonAuswaehlen1 = tk.Button(self, image = self.imageWuerfel3 , command = self.buttonAuswahl1Click)
                        buttonAuswaehlen1.grid(row=2,column=0,padx=20,pady=40, rowspan=5)
                    elif t == 4:
                        self.augen1 = 4
                        buttonAuswaehlen1 = tk.Button(self, image = self.imageWuerfel4 , command = self.buttonAuswahl1Click)
                        buttonAuswaehlen1.grid(row=2,column=0,padx=20,pady=40, rowspan=5)
                    elif t == 5:
                        self.augen1 = 5
                        buttonAuswaehlen1 = tk.Button(self, image = self.imageWuerfel5 , command = self.buttonAuswahl1Click)
                        buttonAuswaehlen1.grid(row=2,column=0,padx=20,pady=40, rowspan=5)
                    elif t == 6:
                        self.augen1 = 6
                        buttonAuswaehlen1 = tk.Button(self, image = self.imageWuerfel6 , command = self.buttonAuswahl1Click)
                        buttonAuswaehlen1.grid(row=2,column=0,padx=20,pady=40, rowspan=5)

                elif i==1 and  self.red2 == 'Nein':

                    if t == 1:
                        self.augen2 = 1
                        buttonAuswaehlen2 = tk.Button(self, image = self.imageWuerfel1 , command = self.buttonAuswahl2Click)
                        buttonAuswaehlen2.grid(row=2,column=1,padx=20,pady=40, rowspan=5)
                    elif t== 2:
                        self.augen2 = 2
                        buttonAuswaehlen2 = tk.Button(self, image = self.imageWuerfel2 , command = self.buttonAuswahl2Click)
                        buttonAuswaehlen2.grid(row=2,column=1,padx=20,pady=40, rowspan=5)
                    elif t == 3:
                        self.augen2 = 3
                        buttonAuswaehlen2 = tk.Button(self, image = self.imageWuerfel3 , command = self.buttonAuswahl2Click)
                        buttonAuswaehlen2.grid(row=2,column=1,padx=20,pady=40, rowspan=5)
                    elif t== 4:
                        self.augen2 = 4
                        buttonAuswaehlen2 = tk.Button(self, image = self.imageWuerfel4 , command = self.buttonAuswahl2Click)
                        buttonAuswaehlen2.grid(row=2,column=1,padx=20,pady=40, rowspan=5)
                    elif t == 5:
                        self.augen2 = 5
                        buttonAuswaehlen2 = tk.Button(self, image = self.imageWuerfel5 , command = self.buttonAuswahl2Click)
                        buttonAuswaehlen2.grid(row=2,column=1,padx=20,pady=40, rowspan=5)
                    elif t == 6:
                        self.augen2 = 6
                        buttonAuswaehlen2 = tk.Button(self, image = self.imageWuerfel6 , command = self.buttonAuswahl2Click)
                        buttonAuswaehlen2.grid(row=2,column=1,padx=20,pady=40, rowspan=5)

                elif i == 2 and  self.red3 == 'Nein':

                    if t == 1:
                        self.augen3 = 1
                        buttonAuswaehlen3 = tk.Button(self, image = self.imageWuerfel1 , command = self.buttonAuswahl3Click)
                        buttonAuswaehlen3.grid(row=2,column=2,padx=20,pady=40, rowspan=5)
                    elif t== 2:
                        self.augen3 = 2
                        buttonAuswaehlen3 = tk.Button(self, image = self.imageWuerfel2 , command = self.buttonAuswahl3Click)
                        buttonAuswaehlen3.grid(row=2,column=2,padx=20,pady=40, rowspan=5)
                    elif t== 3:
                        self.augen3 = 3
                        buttonAuswaehlen3 = tk.Button(self, image = self.imageWuerfel3 , command = self.buttonAuswahl3Click)
                        buttonAuswaehlen3.grid(row=2,column=2,padx=20,pady=40, rowspan=5)
                    elif t== 4:
                        self.augen3 = 4
                        buttonAuswaehlen3 = tk.Button(self, image = self.imageWuerfel4 , command = self.buttonAuswahl3Click)
                        buttonAuswaehlen3.grid(row=2,column=2,padx=20,pady=40, rowspan=5)
                    elif t == 5:
                        self.augen3 = 5
                        buttonAuswaehlen3 = tk.Button(self, image = self.imageWuerfel5 , command = self.buttonAuswahl3Click)
                        buttonAuswaehlen3.grid(row=2,column=2,padx=20,pady=40, rowspan=5)
                    elif t == 6:
                        self.augen3 = 6
                        buttonAuswaehlen3 = tk.Button(self, image = self.imageWuerfel6 , command = self.buttonAuswahl3Click)
                        buttonAuswaehlen3.grid(row=2,column=2,padx=20,pady=40, rowspan=5)

                elif i == 3 and  self.red4 == 'Nein':

                    if t == 1:
                        self.augen4 = 1
                        buttonAuswaehlen4 = tk.Button(self, image = self.imageWuerfel1 , command = self.buttonAuswahl4Click)
                        buttonAuswaehlen4.grid(row=2,column=3,padx=20,pady=40, rowspan=5)
                    elif t == 2:
                        self.augen4 = 2
                        buttonAuswaehlen4 = tk.Button(self, image = self.imageWuerfel2 , command = self.buttonAuswahl4Click)
                        buttonAuswaehlen4.grid(row=2,column=3,padx=20,pady=40, rowspan=5)
                    elif t == 3:
                        self.augen4 = 3
                        buttonAuswaehlen4 = tk.Button(self, image = self.imageWuerfel3 , command = self.buttonAuswahl4Click)
                        buttonAuswaehlen4.grid(row=2,column=3,padx=20,pady=40, rowspan=5)
                    elif t == 4:
                        self.augen4 = 4
                        buttonAuswaehlen4 = tk.Button(self, image = self.imageWuerfel4 , command = self.buttonAuswahl4Click)
                        buttonAuswaehlen4.grid(row=2,column=3,padx=20,pady=40, rowspan=5)
                    elif t == 5:
                        self.augen4 = 5
                        buttonAuswaehlen4 = tk.Button(self, image = self.imageWuerfel5 , command = self.buttonAuswahl4Click)
                        buttonAuswaehlen4.grid(row=2,column=3,padx=20,pady=40, rowspan=5)
                    elif t == 6:
                        self.augen4 = 6
                        buttonAuswaehlen4 = tk.Button(self, image = self.imageWuerfel6 , command = self.buttonAuswahl4Click)
                        buttonAuswaehlen4.grid(row=2,column=3,padx=20,pady=40, rowspan=5)

                elif i ==4 and  self.red5 == 'Nein':

                    if t == 1:
                        self.augen5 = 1
                        buttonAuswaehlen5 = tk.Button(self, image = self.imageWuerfel1 , command = self.buttonAuswahl5Click)
                        buttonAuswaehlen5.grid(row=2,column=4,padx=20,pady=40, rowspan=5)
                    elif t == 2:
                        self.augen5 = 2
                        buttonAuswaehlen5 = tk.Button(self, image = self.imageWuerfel2 , command = self.buttonAuswahl5Click)
                        buttonAuswaehlen5.grid(row=2,column=4,padx=20,pady=40, rowspan=5)
                    elif t == 3:
                        self.augen5 = 3
                        buttonAuswaehlen5 = tk.Button(self, image = self.imageWuerfel3 , command = self.buttonAuswahl5Click)
                        buttonAuswaehlen5.grid(row=2,column=4,padx=20,pady=40, rowspan=5)
                    elif t == 4:
                        self.augen5 = 4
                        buttonAuswaehlen5 = tk.Button(self, image = self.imageWuerfel4 , command = self.buttonAuswahl5Click)
                        buttonAuswaehlen5.grid(row=2,column=4,padx=20,pady=40, rowspan=5)
                    elif t == 5:
                        self.augen5 = 5
                        buttonAuswaehlen5 = tk.Button(self, image = self.imageWuerfel5 , command = self.buttonAuswahl5Click)
                        buttonAuswaehlen5.grid(row=2,column=4,padx=20,pady=40, rowspan=5)
                    elif t == 6:
                        self.augen5 = 6
                        buttonAuswaehlen5 = tk.Button(self, image = self.imageWuerfel6 , command = self.buttonAuswahl5Click)
                        buttonAuswaehlen5.grid(row=2,column=4,padx=20,pady=40, rowspan=5)

        if self.turn==4:
            self.turn=1

            buttonWuerfel = tk.Button(self,text='Wuerfeln', command=self.buttonWuerfelnClick,state="disabled")
            buttonWuerfel.grid(row=6,column=2)
            buttonNaechster=tk.Button(self, width=20, text='Naechster', command = self.buttonNaechsterClick)
            buttonNaechster.grid(row=19,column=2)







    def buttonAuswahl1Click(self):

        self.red1 = 'Ja'
        if self.augen1 == 1:
            buttonZurueck1 = tk.Button(self, image = self.imageWuerfel11 , command = self.buttonZurueck1Click)
            buttonZurueck1.grid(row=2,column=0,padx=20,pady=40, rowspan=5)
            self.Einser= self.Einser+1
        elif self.augen1 == 2:
            buttonZurueck1 = tk.Button(self, image = self.imageWuerfel22 , command = self.buttonZurueck1Click)
            buttonZurueck1.grid(row=2,column=0,padx=20,pady=40, rowspan=5)
            self.Zweier=self.Zweier+1
        elif self.augen1 == 3:
            buttonZurueck1 = tk.Button(self, image = self.imageWuerfel33 , command = self.buttonZurueck1Click)
            buttonZurueck1.grid(row=2,column=0,padx=20,pady=40, rowspan=5)
            self.Dreier = self.Dreier+1
        elif self.augen1 == 4:
            buttonZurueck1 = tk.Button(self, image = self.imageWuerfel44 , command = self.buttonZurueck1Click)
            buttonZurueck1.grid(row=2,column=0,padx=20,pady=40, rowspan=5)
            self.Vierer=self.Vierer+1
        elif self.augen1 == 5:
            buttonZurueck1 = tk.Button(self, image = self.imageWuerfel55 , command = self.buttonZurueck1Click)
            buttonZurueck1.grid(row=2,column=0,padx=20,pady=40, rowspan=5)
            self.Fuenfer=self.Fuenfer+1
        elif self.augen1 == 6:
            buttonZurueck1 = tk.Button(self, image = self.imageWuerfel66 , command = self.buttonZurueck1Click)
            buttonZurueck1.grid(row=2,column=0,padx=20,pady=40, rowspan=5)
            self.Sechser=self.Sechser+1


    def buttonAuswahl2Click(self):
        self.red2 = 'Ja'
        if self.augen2 == 1:
            buttonZurueck2 = tk.Button(self, image = self.imageWuerfel11 , command = self.buttonZurueck2Click)
            buttonZurueck2.grid(row=2,column=1,padx=20,pady=40, rowspan=5)
            self.Einser= self.Einser+1
        elif self.augen2 == 2:
            buttonZurueck2 = tk.Button(self, image = self.imageWuerfel22 , command = self.buttonZurueck2Click)
            buttonZurueck2.grid(row=2,column=1,padx=20,pady=40, rowspan=5)
            self.Zweier=self.Zweier+1
        elif self.augen2 == 3:
            buttonZurueck2 = tk.Button(self, image = self.imageWuerfel33 , command =self. buttonZurueck2Click)
            buttonZurueck2.grid(row=2,column=1,padx=20,pady=40, rowspan=5)
            self.Dreier = self.Dreier+1
        elif self.augen2 == 4:
            buttonZurueck2 = tk.Button(self, image = self.imageWuerfel44 , command = self.buttonZurueck2Click)
            buttonZurueck2.grid(row=2,column=1,padx=20,pady=40, rowspan=5)
            self.Vierer=self.Vierer+1
        elif self.augen2 == 5:
            buttonZurueck2 = tk.Button(self, image = self.imageWuerfel55 , command = self.buttonZurueck2Click)
            buttonZurueck2.grid(row=2,column=1,padx=20,pady=40, rowspan=5)
            self.Fuenfer=self.Fuenfer+1
        elif self.augen2 == 6:
            buttonZurueck2 = tk.Button(self, image = self.imageWuerfel66 , command = self.buttonZurueck2Click)
            buttonZurueck2.grid(row=2,column=1,padx=20,pady=40, rowspan=5)
            self.Sechser=self.Sechser+1

    def buttonAuswahl3Click(self):
        self.red3 = 'Ja'
        if self.augen3 == 1:
            buttonZurueck3 = tk.Button(self, image = self.imageWuerfel11 , command = self.buttonZurueck3Click)
            buttonZurueck3.grid(row=2,column=2,padx=20,pady=40, rowspan=5)
            self.Einser= self.Einser+1
        elif self.augen3 == 2:
            buttonZurueck3 = tk.Button(self, image = self.imageWuerfel22 , command = self.buttonZurueck3Click)
            buttonZurueck3.grid(row=2,column=2,padx=20,pady=40, rowspan=5)
            self.Zweier=self.Zweier+1
        elif self.augen3 == 3:
            buttonZurueck3 = tk.Button(self, image = self.imageWuerfel33 , command = self.buttonZurueck3Click)
            buttonZurueck3.grid(row=2,column=2,padx=20,pady=40, rowspan=5)
            self.Dreier = self.Dreier+1
        elif self.augen3 == 4:
            buttonZurueck3 = tk.Button(self, image = self.imageWuerfel44 , command = self.buttonZurueck3Click)
            buttonZurueck3.grid(row=2,column=2,padx=20,pady=40, rowspan=5)
            self.Vierer=self.Vierer+1
        elif self.augen3 == 5:
            buttonZurueck3 = tk.Button(self, image = self.imageWuerfel55 , command = self.buttonZurueck3Click)
            buttonZurueck3.grid(row=2,column=2,padx=20,pady=40, rowspan=5)
            self.Fuenfer=self.Fuenfer+1
        elif self.augen3 == 6:
            buttonZurueck3 = tk.Button(self, image = self.imageWuerfel66 , command = self.buttonZurueck3Click)
            buttonZurueck3.grid(row=2,column=2,padx=20,pady=40, rowspan=5)
            self.Sechser=self.Sechser+1

    def buttonAuswahl4Click(self):
        self.red4 = 'Ja'
        if self.augen4 == 1:
            buttonZurueck4 = tk.Button(self, image = self.imageWuerfel11 , command = self.buttonZurueck4Click)
            buttonZurueck4.grid(row=2,column=3,padx=20,pady=40, rowspan=5)
            self.Einser= self.Einser+1
        elif self.augen4 == 2:
            buttonZurueck4 = tk.Button(self, image = self.imageWuerfel22 , command = self.buttonZurueck4Click)
            buttonZurueck4.grid(row=2,column=3,padx=20,pady=40, rowspan=5)
            self.Zweier=self.Zweier+1
        elif self.augen4 == 3:
            buttonZurueck4 = tk.Button(self, image = self.imageWuerfel33 , command = self.buttonZurueck4Click)
            buttonZurueck4.grid(row=2,column=3,padx=20,pady=40, rowspan=5)
            self.Dreier = self.Dreier+1
        elif self.augen4 == 4:
            buttonZurueck4 = tk.Button(self, image = self.imageWuerfel44 , command = self.buttonZurueck4Click)
            buttonZurueck4.grid(row=2,column=3,padx=20,pady=40, rowspan=5)
            self.Vierer=self.Vierer+1
        elif self.augen4 == 5:
            buttonZurueck4 = tk.Button(self, image = self.imageWuerfel55 , command = self.buttonZurueck4Click)
            buttonZurueck4.grid(row=2,column=3,padx=20,pady=40, rowspan=5)
            self.Fuenfer=self.Fuenfer+1
        elif self.augen4 == 6:
            buttonZurueck4 = tk.Button(self, image = self.imageWuerfel66 , command = self.buttonZurueck4Click)
            buttonZurueck4.grid(row=2,column=3,padx=20,pady=40, rowspan=5)
            self.Sechser=self.Sechser+1

    def buttonAuswahl5Click(self):
        self.red5 = 'Ja'
        if self.augen5 == 1:
            buttonZurueck5 = tk.Button(self, image = self.imageWuerfel11 , command = self.buttonZurueck5Click)
            buttonZurueck5.grid(row=2,column=4,padx=20,pady=40, rowspan=5)
            self.Einser= self.Einser+1
        elif self.augen5 == 2:
            buttonZurueck5 = tk.Button(self, image = self.imageWuerfel22 , command = self.buttonZurueck5Click)
            buttonZurueck5.grid(row=2,column=4,padx=20,pady=40, rowspan=5)
            self.Zweier=self.Zweier+1
        elif self.augen5 == 3:
            buttonZurueck5 = tk.Button(self, image = self.imageWuerfel33 , command = self.buttonZurueck5Click)
            buttonZurueck5.grid(row=2,column=4,padx=20,pady=40, rowspan=5)
            self.Dreier = self.Dreier+1
        elif self.augen5 == 4:
            buttonZurueck5 = tk.Button(self, image = self.imageWuerfel44 , command = self.buttonZurueck5Click)
            buttonZurueck5.grid(row=2,column=4,padx=20,pady=40, rowspan=5)
            self.Vierer=self.Vierer+1
        elif self.augen5 == 5:
            buttonZurueck5 = tk.Button(self, image = self.imageWuerfel55 , command = self.buttonZurueck5Click)
            buttonZurueck5.grid(row=2,column=4,padx=20,pady=40, rowspan=5)
            self.Fuenfer=self.Fuenfer+1
        elif self.augen5== 6:
            buttonZurueck5 = tk.Button(self, image = self.imageWuerfel66 , command = self.buttonZurueck5Click)
            buttonZurueck5.grid(row=2,column=4,padx=20,pady=40, rowspan=5)
            self.Sechser=self.Sechser+1

    def buttonZurueck1Click(self):
        self.red1 = 'Nein'
        if self.augen1 == 1:
            buttonAuswaehlen1 = tk.Button(self, image = self.imageWuerfel1 , command = self.buttonAuswahl1Click)
            buttonAuswaehlen1.grid(row=2,column=0,padx=20,pady=40, rowspan=5)
            self.Einser= self.Einser-1
        elif self.augen1 == 2:
            buttonAuswaehlen1 = tk.Button(self, image = self.imageWuerfel2 , command = self.buttonAuswahl1Click)
            buttonAuswaehlen1.grid(row=2,column=0,padx=20,pady=40, rowspan=5)
            self.Zweier=self.Zweier-1
        elif self.augen1 == 3:
            buttonAuswaehlen1 = tk.Button(self, image = self.imageWuerfel3, command = self.buttonAuswahl1Click)
            buttonAuswaehlen1.grid(row=2,column=0,padx=20,pady=40, rowspan=5)
            self.Dreier = self.Dreier-1
        elif self.augen1 == 4:
            buttonAuswaehlen1 = tk.Button(self, image = self.imageWuerfel4 , command = self.buttonAuswahl1Click)
            buttonAuswaehlen1.grid(row=2,column=0,padx=20,pady=40, rowspan=5)
            self.Vierer=self.Vierer-1
        elif self.augen1 == 5:
            buttonAuswaehlen1 = tk.Button(self, image = self.imageWuerfel5 , command = self.buttonAuswahl1Click)
            buttonAuswaehlen1.grid(row=2,column=0,padx=20,pady=40, rowspan=5)
            self.Fuenfer=self.Fuenfer-1
        elif self.augen1 == 6:
            buttonAuswaehlen1 = tk.Button(self, image = self.imageWuerfel6 , command = self.buttonAuswahl1Click)
            buttonAuswaehlen1.grid(row=2,column=0,padx=20,pady=40, rowspan=5)
            self.Sechser=self.Sechser-1

    def buttonZurueck2Click(self):
        self.red2 = 'Nein'
        if self.augen2 == 1:
            buttonAuswaehlen2 = tk.Button(self, image = self.imageWuerfel1 , command = self.buttonAuswahl2Click)
            buttonAuswaehlen2.grid(row=2,column=1,padx=20,pady=40, rowspan=5)
            self.Einser= self.Einser-1
        elif self.augen2 == 2:
            buttonAuswaehlen2 = tk.Button(self, image = self.imageWuerfel2 , command = self.buttonAuswahl2Click)
            buttonAuswaehlen2.grid(row=2,column=1,padx=20,pady=40, rowspan=5)
            self.Zweier=self.Zweier-1
        elif self.augen2 == 3:
            buttonAuswaehlen2 = tk.Button(self, image = self.imageWuerfel3, command = self.buttonAuswahl2Click)
            buttonAuswaehlen2.grid(row=2,column=1,padx=20,pady=40, rowspan=5)
            self.Dreier=self.Dreier-1
        elif self.augen2 == 4:
            buttonAuswaehlen2 = tk.Button(self, image = self.imageWuerfel4 , command = self.buttonAuswahl2Click)
            buttonAuswaehlen2.grid(row=2,column=1,padx=20,pady=40, rowspan=5)
            self.Vierer=self.Vierer-1
        elif self.augen2 == 5:
            buttonAuswaehlen2 = tk.Button(self, image = self.imageWuerfel5 , command = self.buttonAuswahl2Click)
            buttonAuswaehlen2.grid(row=2,column=1,padx=20,pady=40, rowspan=5)
            self.Fuenfer=self.Fuenfer-1
        elif self.augen2 == 6:
            buttonAuswaehlen2 = tk.Button(self, image = self.imageWuerfel6 , command = self.buttonAuswahl2Click)
            buttonAuswaehlen2.grid(row=2,column=1,padx=20,pady=40, rowspan=5)
            self.Sechser=self.Sechser-1

    def buttonZurueck3Click(self):
        self.red3 = 'Nein'
        if self.augen3 == 1:
            buttonAuswaehlen3 = tk.Button(self, image = self.imageWuerfel1 , command = self.buttonAuswahl3Click)
            buttonAuswaehlen3.grid(row=2,column=2,padx=20,pady=40, rowspan=5)
            self.Einser= self.Einser-1
        elif self.augen3== 2:
            buttonAuswaehlen3 = tk.Button(self, image = self.imageWuerfel2 , command = self.buttonAuswahl3Click)
            buttonAuswaehlen3.grid(row=2,column=2,padx=20,pady=40, rowspan=5)
            self.Zweier=self.Zweier-1
        elif self.augen3 == 3:
            buttonAuswaehlen3 = tk.Button(self, image = self.imageWuerfel3, command = self.buttonAuswahl3Click)
            buttonAuswaehlen3.grid(row=2,column=2,padx=20,pady=40, rowspan=5)
            self.Dreier=self.Dreier-1
        elif self.augen3 == 4:
            buttonAuswaehlen3 = tk.Button(self, image = self.imageWuerfel4 , command = self.buttonAuswahl3Click)
            buttonAuswaehlen3.grid(row=2,column=2,padx=20,pady=40, rowspan=5)
            self.Vierer=self.Vierer-1
        elif self.augen3== 5:
            buttonAuswaehlen3 = tk.Button(self, image = self.imageWuerfel5 , command = self.buttonAuswahl3Click)
            buttonAuswaehlen3.grid(row=2,column=2,padx=20,pady=40, rowspan=5)
            self.Fuenfer=self.Fuenfer-1
        elif self.augen3 == 6:
            buttonAuswaehlen3 = tk.Button(self, image = self.imageWuerfel6 , command = self.buttonAuswahl3Click)
            buttonAuswaehlen3.grid(row=2,column=2,padx=20,pady=40, rowspan=5)
            self.Sechser=self.Sechser-1

    def buttonZurueck4Click(self):
        self.red4 = 'Nein'
        if self.augen4 == 1:
            buttonAuswaehlen4 = tk.Button(self, image = self.imageWuerfel1 , command = self.buttonAuswahl4Click)
            buttonAuswaehlen4.grid(row=2,column=3,padx=20,pady=40, rowspan=5)
            self.Einser= self.Einser-1
        elif self.augen4== 2:
            buttonAuswaehlen4 = tk.Button(self, image = self.imageWuerfel2 , command = self.buttonAuswahl4Click)
            buttonAuswaehlen4.grid(row=2,column=3,padx=20,pady=40, rowspan=5)
            self.Zweier=self.Zweier-1
        elif self.augen4 == 3:
            buttonAuswaehlen4= tk.Button(self, image = self.imageWuerfel3, command = self.buttonAuswahl4Click)
            buttonAuswaehlen4.grid(row=2,column=3,padx=20,pady=40, rowspan=5)
            self.Dreier=self.Dreier-1
        elif self.augen4 == 4:
            buttonAuswaehlen4 = tk.Button(self, image = self.imageWuerfel4 , command = self.buttonAuswahl4Click)
            buttonAuswaehlen4.grid(row=2,column=3,padx=20,pady=40, rowspan=5)
            self.Vierer=self.Vierer-1
        elif self.augen4== 5:
            buttonAuswaehlen4 = tk.Button(self, image = self.imageWuerfel5 , command = self.buttonAuswahl4Click)
            buttonAuswaehlen4.grid(row=2,column=3,padx=20,pady=40, rowspan=5)
            self.Fuenfer=self.Fuenfer-1
        elif self.augen4 == 6:
            buttonAuswaehlen4 = tk.Button(self, image = self.imageWuerfel6 , command = self.buttonAuswahl4Click)
            buttonAuswaehlen4.grid(row=2,column=3,padx=20,pady=40, rowspan=5)
            self.Sechser=self.Sechser-1

    def buttonZurueck5Click(self):
        self.red5 = 'Nein'
        if self.augen5 == 1:
            buttonAuswaehlen5 = tk.Button(self, image = self.imageWuerfel1 , command = self.buttonAuswahl5Click)
            buttonAuswaehlen5.grid(row=2,column=4,padx=20,pady=40, rowspan=5)
            self.Einser= self.Einser-1
        elif self.augen5== 2:
            buttonAuswaehlen5 = tk.Button(self, image = self.imageWuerfel2 , command = self.buttonAuswahl5Click)
            buttonAuswaehlen5.grid(row=2,column=4,padx=20,pady=40, rowspan=5)
            self.Zweier=self.Zweier-1
        elif self.augen5 == 3:
            buttonAuswaehlen5 = tk.Button(self, image = self.imageWuerfel3, command = self.buttonAuswahl5Click)
            buttonAuswaehlen5.grid(row=2,column=4,padx=20,pady=40, rowspan=5)
            self.Dreier=self.Dreier-1
        elif self.augen5 == 4:
            buttonAuswaehlen5 = tk.Button(self, image = self.imageWuerfel4 , command = self.buttonAuswahl5Click)
            buttonAuswaehlen5.grid(row=2,column=4,padx=20,pady=40, rowspan=5)
            self.Vierer=self.Vierer-1
        elif self.augen5== 5:
            buttonAuswaehlen5 = tk.Button(self, image = self.imageWuerfel5 , command = self.buttonAuswahl5Click)
            buttonAuswaehlen5.grid(row=2,column=4,padx=20,pady=40, rowspan=5)
            self.Fuenfer=self.Fuenfer-1
        elif self.augen5== 6:
            buttonAuswaehlen5 = tk.Button(self, image = self.imageWuerfel6 , command = self.buttonAuswahl5Click)
            buttonAuswaehlen5.grid(row=2,column=4,padx=20,pady=40, rowspan=5)
            self.Sechser=self.Sechser-1



class Highscore (tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        X = Datenbank()
        high1=tk.Label(self,text=X.Ausgeben())






app = Kniffel()
app.mainloop()
