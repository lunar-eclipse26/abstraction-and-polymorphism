class part_5():
    def set_in(self):
        print("part 5 of jojos is set in italy")
    def language(self):
        print("jojos is japanese anime so it is in japanese not italian")
    def mc(self):
        print("the main character of part 5 is giorna giovanna the new leader passione")
class part_9():
    def set_in(self):
        print("part 9 of jojos is set in hawaii")
    def language(self):
        print("jojos is japanese anime so it is in japanese not hawaiian but part 9 is still in the manga but it is still japanese, english if we're talking about the fan translation")
    def mc(self):
        print("the main character of part 9 is jodio joestar just a guy who wants to be rich with his crew")
obj_part5 = part_5()
obj_part9 = part_9()
for location in (obj_part5, obj_part9):
    location.set_in()
    location.language()
    location.mc()