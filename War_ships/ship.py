from Phrases import Phrases

class Ship:
    def __init__(self, coord_1, direction, deckhand):
        self._start = coord_1
        self._direction = direction
        self.busy_cells = []
        self.deckhand = deckhand
        self.make_busy_cells()
        self.ship_cells = []
        self.make_ship_cells()
        self.ship_cells_for_shoot = self.ship_cells.copy()


    def make_busy_cells(self):
        if self._direction == 'up':
            for deck in range(-1, self.deckhand + 1):
                for i in range(-1, 2):
                    self.busy_cells.append([self._start[0] + i, self._start[1] + deck])
        
        if self._direction == 'down':
            for deck in range(-1, self.deckhand + 1):
                for i in range(-1, 2):
                    self.busy_cells.append([self._start[0] + i, self._start[1] - deck])

        if self._direction == 'right':
            for deck in range(-1, self.deckhand + 1):
                for i in range(-1, 2):
                    self.busy_cells.append([self._start[0] + deck, self._start[1] + i])


        if self._direction == 'left':
            for deck in range(-1, self.deckhand + 1):
                for i in range(-1, 2):
                    self.busy_cells.append([self._start[0] - deck, self._start[1] + i])

    def make_ship_cells(self):
        if self._direction == 'up':
            for deck in range(self.deckhand):
                    self.ship_cells.append([self._start[0], self._start[1] + deck])
        
        if self._direction == 'down':
            for deck in range(self.deckhand):
                    self.ship_cells.append([self._start[0], self._start[1] - deck])

        if self._direction == 'right':
            for deck in range(self.deckhand):
                    self.ship_cells.append([self._start[0] + deck, self._start[1]])


        if self._direction == 'left':
            for deck in range(self.deckhand):
                    self.ship_cells.append([self._start[0] - deck, self._start[1]])  

# ship = Ship([5,5], 'right', 4)
# print(ship.busy_cells)












