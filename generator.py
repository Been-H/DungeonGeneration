import random as r

class Room:

    allRooms = []

    def __init__(self, row, column):

        self.row = row
        self.column = column
        self.weight = 1
        self.posNeighbors = [
            [self.row, self.column - 1],
            [self.row - 1, self.column],
            [self.row, self.column + 1],
            [self.row + 1, self.column]
        ]
        Room.allRooms.append(self)

    @classmethod
    def shuffleRooms(cls):
        r.shuffle(Room.allRooms)

    def show(self):
        print("R      ", end="")

class Dungeon:

    def __init__(self):
        self.dungeon = [[' ' for i in range(20)] for i in range(20)]

    def show_dungeon(self):
        for row in self.dungeon:
            for room in row:
                if isinstance(room, Room):
                    room.show()
                else:
                    print(room + "      ", end="")
            print('\n')

    def generate_dungeon(self, numRooms):
        for i in range(numRooms):
            Room.shuffleRooms()
            while True:
                roomInd = r.randint(0, len(Room.allRooms) - 1)
                chosenParent = Room.allRooms[roomInd]
                possibleNewRooms = []
                for neighbor in chosenParent.posNeighbors:
                    if self.dungeon[neighbor[0]][neighbor[1]] == ' ':
                        possibleNewRooms.append(neighbor)
                if len(possibleNewRooms) == 0:
                    continue
                else:
                    break
            newRoomPositionInd = r.randint(0, len(possibleNewRooms) - 1)
            newRoomPosition = possibleNewRooms[newRoomPositionInd]
            self.dungeon[newRoomPosition[0]][newRoomPosition[1]] = Room(newRoomPosition[0], newRoomPosition[1])


dungeon = Dungeon()


start_room = Room(5,5)
dungeon.dungeon[5][5] = start_room


dungeon.generate_dungeon(12)
dungeon.show_dungeon()