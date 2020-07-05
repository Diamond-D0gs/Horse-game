class Horse:
    _horseList = []

    def __init__(self, name, phrase, death):
        self.horseName = str(name)
        self.horsePhrase = str(phrase)
        self.horseDeath = str(death)
        print(self.horseName + ' has entered the arena!')
        print()

    def GetName(self):
        return self.horseName
    
    def GetPhrase(self):
        return self.horsePhrase

    def UpdatePhrase(self, phrase):
        self.horsePhrase = phrase

    def GetDeathPhrase(self):
        return self.horseDeath

    @classmethod
    def ListHorses(cls):
        print('Number of horses: ' + str(len(Horse._horseList)))
        for i in Horse._horseList:
            print(i.GetName())
        print ()

    @classmethod
    def FightHorses(cls):
        horse1 = str(input('Enter the name of the first horse: '))
        horse2 = str(input('Enter the name of the second horse: '))
        #print(len(Horse._horseList))

        i = None
        for i in Horse._horseList:              # Iterate over horseList, if a horse with the same name is located, break the loop.
            if str(i.GetName()) == horse1:
                break
        if i.GetName() != horse1:               # If the horse is not located, return to main. (Is there a less janky solution?)
            print("The first horse cannot be located. Try Again.")
            print()
            return

        j = None
        for j in Horse._horseList:
            if str(j.GetName()) == horse2:
                break
        if j.GetName() != horse2:
            print("The second horse cannot be located. Try Again.")
            print()
            return
        
        if isinstance(i, SuperHorse) == True:   # Check if attacking horse, horse 1, is a superhorse.
            print(i.GetName() + " attacks and kills " + j.GetName() + " using their " + i.GetAttack() + " attack!")
            print(j.GetName() + ": " + j.GetDeathPhrase())
            Horse._horseList.remove(j)          # Horse is killed by being removed from horseList.
            print()
        else:
            print(i.GetName() + " is not a super horse, therefore it cannot attack.")
            print()

    @classmethod
    def MakeHorse(cls):
        name = input("Enter your horse's name: ")
        phrase = input("Enter your horse's phrase: ")
        death = input("Enter your horse's death phrase: ")
        Horse._horseList.append(Horse(name, phrase, death))

class SuperHorse(Horse):
    def __init__(self, name, phrase, death, attack):
        super(SuperHorse, self).__init__(name, phrase, death)
        self.attackName = str(attack)

    def GetAttack(self):
        return self.attackName

    @classmethod
    def MakeSuperHorse(cls):
        name = input("Enter your horse's name: ")
        phrase = input("Enter your horse's phrase: ")
        death = input("Enter your horse's death phrase: ")
        attack = input("Enter your horse's attack name: ")
        Horse._horseList.append(SuperHorse(name, phrase, death, attack))

def Main():
    x = None
    while (x != 0):
        print('1) Make a regular horse')
        print('2) Make a super horse')
        print('3) List horses')
        print('4) Fight two horses')
        print('0) Quit')
        print()

        x = int(input('Enter your selection: '))
        print ()

        if x == 1:
            Horse.MakeHorse()
        elif x == 2:
            SuperHorse.MakeSuperHorse()
        elif x == 3:
            Horse.ListHorses()
        elif x == 4:
            Horse.FightHorses()
        elif x == 0:
            print("Goodbye.")
        else:
            print('Please enter a valid selection.')

if __name__ == '__main__':
    Main()




