import pygame

MASTID = ["Poti", "Ärtu", "Risti", "Ruutu"]
kaardid = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
väärtused = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 11, "Q": 12, "K": 13, "A": 14}

PAKK = []
class Pakk():
    def __init__(self, mast, väärtus):
        self.mast = mast
        self.väärtus = väärtus
        self.tugevus = väärtused[self.väärtus]

def tee_pakk():
    i=0
    for mast in MASTID:
        for kaart1 in kaardid:
            PAKK.append(Pakk(mast, kaart1))
            
tee_pakk()
