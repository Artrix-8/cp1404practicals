"""
Code to simulate using taxis.
"""

from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi


def main():
    total_fare = 0
    current_taxi = None
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    print("Let's Drive")
    print("q)uit, c)hoose taxi, d)rive)")
    menu_input = input('>>> ')

    while menu_input.lower() != 'q':

        if menu_input.lower() == 'c':
            print('Taxis available: ')
            for i, taxi in enumerate(taxis):
                print(f'{i} - {taxi}')
            try:
                taxi_input = int(input('Choose taxi: '))
                current_taxi = taxis[taxi_input]
            except ValueError:
                print('Invalid taxi choice')
            except IndexError:
                print('Invalid taxi choice')

        elif menu_input.lower() == 'd':
            if current_taxi:
                current_taxi.start_fare()
                distance = float(input('Drive how far? '))
                current_taxi.drive(distance)
                print(f'Your {current_taxi.name} trip cost you ${current_taxi.get_fare():.2f}')
                total_fare += current_taxi.get_fare()
            else:
                print('You need to choose a taxi before you can drive')

        else:
            print('Invalid option')

        print(f'Bill to date: ${total_fare:.2f}')
        print("q)uit, c)hoose taxi, d)rive)")
        menu_input = input('>>> ')

    print(f'Total trip cost: ${total_fare:.2f}')
    print("Taxis are now:")
    for i, taxi in enumerate(taxis):
        print(f'{i} - {taxi}')


main()
