class Phrases:
    """
    Spechial class for phrases
    With future adaptation to other language)))
    """
    @classmethod
    def wrong_coords(self, Language):
        if Language == 'Ru':
            pass
        else:
            return "You entered the wrong coordinates"

    @classmethod
    def hello_world(self):
        # if Language == 'Ru':
        #     pass
        # else:
        #     return "You entered the wrong coordinates"
        return "Привет, дорогой Пользователь!, расставь, пожалуйста, свои корабли)"

    @classmethod
    def enemy_congrats(self):
        # if Language == 'Ru':
        #     pass
        # else:
        #     return "You entered the wrong coordinates"
        return "Проигрышь"

    @classmethod
    def user_congrats(self):
        # if Language == 'Ru':
        #     pass
        # else:
        #     return "You entered the wrong coordinates"
        return "Победа!"

    @classmethod
    def hand_or_nothand(self):
        return "Хотите расставить корабли рандомно? Y/N"

    @classmethod
    def wrong_step(self):
        return "Введите, пожалуйста, корректную ячейку! Например: A2 или b3"
    
    @classmethod
    def repeted(self):
        return "Вы уже ходили в эту клетку"

    @classmethod
    def deckhand_ship(self, deckhand):
        if deckhand == 4:
            return "Введите начало 4-х палубника"
        if deckhand == 3:
            return "Введите начало 3-х палубника"
        if deckhand == 2:
            return "Введите начало 2-х палубника"
        if deckhand == 1:
            return "Введите координаты 1-палубника"

        return "Что-то пошло не так, с нумерацией количества палуб"


    @classmethod
    def blocked(self):
        return "Эта позиция занята или вы пытаетесь играть не по правилам"

    @classmethod
    def direction(self):
        return "Выберите направление"

        

