"""Lab4.5_wanderers"""

class Subject:
    """
    inform about subject
    >>> cheese = ("cheese", "A large and smelly block of cheese")
    >>> dining_hall.descript_subj
    "A really good book entitled 'Knitting for dummies'"
    """
    def __init__(self, name_subj, descript_subj) -> None:
        """Construct"""
        self.name_subj = name_subj
        self.descript_subj = descript_subj

class Enemy(Subject):
    """
    inform about character
    >>> tabitha = ('Tabitha', 'An enormous spider with countless eyes \
and furry legs.', "book","Sssss....I'm so bored...","cheese", "A large and smelly block of cheese")
    >>> dining_hall.name_pers
    'Dave'
    """
    def __init__(self, name_pers, descript_pers, weakness_pers, phrase_pers,\
        name_subj, descript_subj) -> None:
        """Constructor"""
        super().__init__(name_subj, descript_subj)
        self.name_pers = name_pers
        self.descript_pers = descript_pers
        self.weakness_pers = weakness_pers
        self.phrase_pers = phrase_pers
    def __str__(self) -> str:
        """write name and charecteristics of the character"""
        return f"\n{self.name_pers} is here!\n{self.descript_pers}"

class Room(Enemy):
    """
    inform about room
    >>> ballroom = Room('Ballroom', 'A vast room with a shiny wooden floor. Huge candlesticks guard \
the entrance.',{'east':'Dining Hall'}, 'Tabitha', 'An enormous spider with countless eyes \
and furry legs.', "book","Sssss....I'm so bored...","cheese", "A large and smelly block of cheese")
    >>> ballroom.name
    'Ballroom'
    >>> ballroom.directions
    {'east': 'Dining Hall'}
    """
    def __init__(self, name, description, directions={}, name_pers = None,\
        descript_pers = None, weakness_pers=None, phrase_pers = None,\
        name_subj = None, descript_subj=None) -> None:
        """constructor"""
        super().__init__(name_pers, descript_pers, weakness_pers,\
            phrase_pers, name_subj, descript_subj)
        self.name=name
        self.description=description
        self.directions=directions
    def __str__(self) -> str:
        """
        write the main bloc info about room
        """
        result = ""
        if self.directions != {}:
            for direction in self.directions:
                result += f"\nThe {direction} is {self.directions[direction]}"
        if self.name_pers is not None:
            result+=f"\n{self.name_pers} is here!\n{self.descript_pers}"
        if self.name_subj is not None:
            result+=f"\nThe [{self.name_subj}] is here - {self.descript_subj}"
        return f"\n\n{self.name}\n--------------------\n{self.description}{result}"



if __name__ == '__main__':
    #Create the game:
    # while True:
    #     print("\nDo you want create ome more room?(write 'Yes')\t")
    #     if input()!='Yes':
    #         break
    #     print("\nWrite name of the room:\t")
    #     room_name = str(input())
    #     print("\nWrite a description of the room:\t")
    #     room_descript = str(input())
    #     print("\nWrite a description of the room:\t")
    #     rooms_accommodation = {}
    #     direction
    kitchen = Room('Kitchen', 'A dank and dirty room buzzing with flies.', {'south':'Dining Hall'})
    dining_hall = Room('Dining Hall', 'A large room with ornate golden decorations on each wall.',\
{'north':'Kitchen', 'west':'Ballroom'}, 'Dave', 'A smelly zombie', "cheese",\
"What's up, dude! I'm hungry.", "book", "A really good book entitled 'Knitting for dummies'")
    ballroom = Room('Ballroom', 'A vast room with a shiny wooden floor. Huge candlesticks guard \
the entrance.',{'east':'Dining Hall'}, 'Tabitha', 'An enormous spider with countless eyes \
and furry legs.', "book","Sssss....I'm so bored...","cheese", "A large and smelly block of cheese")
    # print(kitchen)
    room = kitchen
    rooms = {kitchen.name:kitchen, dining_hall.name:dining_hall, ballroom.name:ballroom}
    backpack, beats_enemy= {}, 0
    while True:
        print(room)
        comand = input("> ")
        if comand in room.directions:
            room = rooms[room.directions[comand]]
        elif comand == 'talk':
            if room.name_pers is not None:
                print(f"[{room.name_pers} says]: {room.phrase_pers}")
            else:
                print()
        elif comand == 'fight':
            if room.name_pers is None:
                print("There is no one here to fight with")
            else:
                subject_to_use = str(input("What will you fight with?\n"))
                if subject_to_use not in backpack:
                    print("You have no these oject")
                    continue
                elif subject_to_use != room.weakness_pers:
                    print(f"{room.name_pers} crushes you, puny adventurer\
                    !\nOh dear, you lost the fight.\nThat's the end of the game")
                    break
                print(f"You fend {room.name_pers} off with the {subject_to_use}\
\nHooray, you won the fight!")
                room.name_pers, room.descript_pers = None, None
                room.weakness_pers, room.phrase_pers = None, None
                beats_enemy+=1
        elif comand == 'take':
            if room.name_pers is None:
                print("There's nothing here to take!")
            else:
                print(f"You put the {room.name_subj} in your backpack")
                backpack[room.name_subj] = room.descript_subj
                room.name_subj, room.descript_subj = None, None
        elif comand == "exit":
            break
        if beats_enemy >= 2:
            print("You won this game!!!")
            break
    import doctest
    print(doctest.testmod())
