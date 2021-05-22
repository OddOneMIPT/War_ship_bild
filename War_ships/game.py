from map import Map
from Phrases import Phrases

def main():
    print(Phrases.hello_world())

    user_map = Map()
    enemy_map = Map()
    user_map.make_ships('user', enemy_map)
    enemy_map.make_ships('enemy', enemy_map)

    user_ships = user_map.ships()
    enemy_ships = enemy_map.ships()

    while user_ships and enemy_ships:
        # user_map.print()
        # print('/n')
        # enemy_map.print()
        Map.print_maps(user_map, enemy_map, flag=0)
        flag = enemy_map.user_step()
        while flag != 0:
            # user_map.print()
            # print('/n')
            # enemy_map.print()
            Map.print_maps(user_map, enemy_map, flag)
            flag = enemy_map.user_step()

        
        flag = user_map.enemy_step()
        while flag != 0:
            # user_map.print()
            # print('/n')
            # enemy_map.print()
            Map.print_maps(user_map, enemy_map, flag)
            flag = user_map.enemy_step()


        user_ships = user_map.ships()
        enemy_ships = enemy_map.ships()

        # Map.print_maps(user_map.show_map('user'), enemy_map.show_map('enemy'))

    if user_ships:
        print(Phrases.user_congrats())
    else:
        print(Phrases.enemy_congrats())

if __name__ == "__main__":
    main()