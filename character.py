

#Dungeons and Dragons
class Character():
    def __init__(self, name, race, job_class, stats):
        self.name = name
        self.race = race
        self.job_class = job_class
        self.stats = stats

    def print_stats(self):
        print("Name = " + self.name)
        print("Race = " + self.race)
        print("Class = " + self.job_class)
        print("Strength = " + str(self.stats[0]))
        print("Dexterity = " + str(self.stats[1]))
        print("Consitution = " + str(self.stats[2]))
        print("Intelligence = " + str(self.stats[3]))
        print("Wisdomn = " + str(self.stats[4]))
        print("Charisma = " + str(self.stats[5]))

    

c1 = Character("Brobby", "Dwarf", "Paladin", [1,2,3,4,5,6])

#c2 = Character("Deejuce", "Orc", "Gunslinger", [3,4,1,6,4,2])
#c2.print_stats()

c1.stats = [0,0,0,0,0,0]
c1.print_stats()


