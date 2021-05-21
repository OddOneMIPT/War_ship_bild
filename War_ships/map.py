from Phrases import Phrases
from ship import Ship
from random import randint


from Phrases import Phrases

class Map():
    global dictinary
    dictinary = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9,
                 '1': 0, '2': 1, '3': 2, '4': 3, '5': 4, '6': 5, '7': 6, '8': 7, '9': 8, '10': 9}
    
    def __init__(self):
        self._ships = []
        self._shooten_cells = []
        self._busy_cells = []
        self._ship_cells = []
        self._shooten_ship_cells = []

    def make_ships(self, who):
        if who == 'user':
            flag = self.check_hand()
        else: 
            flag = 0
        if flag == 1:
            self.manual_input() #Реализую чуть позже
        else:
            self.random_input() # Попробуем реализовать для ускорения процесса


    #Реализовать!
    def manual_input(self):
        pass

    def random_input(self):
        order_of_ships = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
        for deckhand in order_of_ships:
            start_of_ship = [randint(0, 9), randint(0, 9)]
            free_place = self.check_free(start_of_ship, deckhand)
            while not free_place:
                start_of_ship = [randint(0, 9), randint(0, 9)]
                free_place = self.check_free(start_of_ship, deckhand)

            direction = free_place[randint(0, len(free_place)-1)]
            ship = Ship(start_of_ship, direction, deckhand)
            self._ships.append(ship)

            for coords in ship.busy_cells:
                self._busy_cells.append(coords)

            for coords in ship.ship_cells:
                self._ship_cells.append(coords)


    def check_free(self, start_of_ship, deckhand):
        free_place = []
        flag = True
        chek_right = [ [start_of_ship[0] + i, start_of_ship[1]] for i in range(deckhand)]
        for coord in chek_right:
            if coord in self._busy_cells or coord[0] > 9:
                flag = False
                break
        if flag:
            free_place.append("right")

        flag = True
        chek_left = [ [start_of_ship[0] - i, start_of_ship[1]] for i in range(deckhand)]
        for coord in chek_left:
            if coord in self._busy_cells or coord[0] < 0:
                flag = False
                break
        if flag:
            free_place.append('left')

        flag = True
        chek_up = [ [start_of_ship[0], start_of_ship[1] + i] for i in range(deckhand)]
        for coord in chek_up:
            if coord in self._busy_cells or coord[1] > 9:
                flag = False
                break
        if flag:
            free_place.append('up')

        flag = True
        chek_down = [ [start_of_ship[0], start_of_ship[1] - i] for i in range(deckhand)]
        for coord in chek_down:
            if coord in self._busy_cells or coord[1] < 0 :
                flag = False
                break
        if flag:
            free_place.append('down')

        return free_place
        

    def check_hand(self):
        print(Phrases.hand_or_nothand())
        input_answer = input()
        #Защита от дурака! 
        while input_answer != 'Y' and input_answer != 'N':
            print(Phrases.hand_or_nothand())
            input_answer = input()
        if input_answer == 'N':
            return 1
        else:
            return 0

    def ships(self):
        return self._ships



    def print(self):
        for y in range(10):
            string = []
            for x in range(10):
                if [x, y] in self._shooten_ship_cells:
                    string.append("X")
                elif [x, y] in self._shooten_cells:
                    string.append("*")
                elif [x, y] in self._ship_cells:
                    string.append("&")
                else:
                    string.append("0")
            print(*string)
    
    def check_user_input(self):
        user_input = input().lower()
        flag = -1
        while flag != 0:
            try:
                while not user_input[0] in dictinary.keys() or not user_input[1:] in dictinary.keys():
                    print(Phrases.wrong_step())
                    user_input = input().lower()
                else:
                    flag = 0
            except Exception:
                print(Phrases.wrong_step())
                user_input = input().lower()
        return [dictinary[user_input[0]], dictinary[user_input[1:]]]

    def user_step(self):
        if not self._ships:
            return 0 
        user_input = self.check_user_input()
        if user_input in self._shooten_cells:
            print(Phrases.repeted())
            return -1
        if user_input in self._ship_cells:
            for ship in self._ships:
                if user_input in ship.ship_cells:
                    break
            try:
                ship.ship_cells_for_shoot.remove(user_input)
            except Exception:
                print(Phrases.repeted())
                return -1
            self._shooten_ship_cells.append(user_input)
            if not ship.ship_cells_for_shoot:
                for coords in ship.busy_cells:
                    self._shooten_cells.append(coords)
                for coords in ship.ship_cells:
                    self._shooten_ship_cells.append(coords)
                self._ships.remove(ship)
            return 1
        self._shooten_cells.append(user_input)
        return 0

    def enemy_step(self):
        if not self._ships:
            return 0
        enemy_input = [randint(0, 9), randint(0, 9)]
        if enemy_input in self._shooten_cells:
            print(Phrases.repeted())
            return -1
        if enemy_input in self._ship_cells:
            for ship in self._ships:
                if enemy_input in ship.ship_cells:
                    break
            try:
                ship.ship_cells_for_shoot.remove(enemy_input)
            except Exception:
                print(Phrases.repeted())
                return -1
            self._shooten_ship_cells.append(enemy_input)
            if not ship.ship_cells_for_shoot:
                for coords in ship.busy_cells:
                    self._shooten_cells.append(coords)
                for coords in ship.ship_cells:
                    self._shooten_ship_cells.append(coords)
                self._ships.remove(ship)
            return 1
        self._shooten_cells.append(enemy_input)
        return 0

    @classmethod
    def print_maps(self, user_map, enemy_map, flag):
        if flag == -1:
            return

        string = [' ']
        for key in list(dictinary.keys())[:10]:
            string.append(key)
        string.append('      ')
        for key in list(dictinary.keys())[:10]:
            string.append(key)
        print(*string)
        for y in range(10):
            string = []
            string.append(y + 1)
            for x in range(10):
                if [x, y] in user_map._shooten_ship_cells:
                    string.append("X")
                elif [x, y] in user_map._shooten_cells:
                    string.append("*")
                elif [x, y] in user_map._ship_cells:
                    string.append("&")
                else:
                    string.append("0")
            string.append('    ')
            string.append(y + 1)
            for x in range(10):
                if [x, y] in enemy_map._shooten_ship_cells:
                    string.append("X")
                elif [x, y] in enemy_map._shooten_cells:
                    string.append("*")
                else:
                    string.append("0")
            print(*string)



# print(list(dictinary.keys())[:10])

# map = Map()
# map.make_ships()
# for _ in range(10):
#     for ship in map._ships:
#         print(ship.deckhand)
#     print(map._shooten_ship_cells)
#     map.user_step()
#     map.print()