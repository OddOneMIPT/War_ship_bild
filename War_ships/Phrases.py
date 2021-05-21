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

        

