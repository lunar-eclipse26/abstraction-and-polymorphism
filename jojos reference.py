from abc import ABC, abstractmethod
class stands(ABC):
    def stand_ability(self):
        pass
class star_platinum(stands):
    def stand_ability(self):
        print("i can punch things")
class the_world(stands):
    def stand_ability(self):
        print("i can stop time by saying ZA WARUDO")
class made_in_heaven(stands):
    def stand_ability(self):
        print("i can accelerate the flow of time for everything in the universe eventually casing a big bang and restart the universe")
class killer_queen(stands):
    def stand_ability(self):
        print("i can turn things into explosives by touching them and i have three types of bombs the primary bomb, sheer heart attack and bites the dust")
class gold_experience(stands):
    def stand_ability(self):
        print("i can give life to inorganic things and with my requim form send people into infinite death loops")
sp = star_platinum()
sp.stand_ability()
tw = the_world()
tw.stand_ability()
mih = made_in_heaven()
mih.stand_ability()
kq = killer_queen()
kq.stand_ability()
ger = gold_experience()
ger.stand_ability()