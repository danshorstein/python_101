# Priority List!

from datetime import datetime
import csv
from pathlib import Path


# Make loop and basic user interface

# Neeed to refactor into more functions!
def main():
    print('\n'*20)
    list_name = input('What list would you like to use? ')

    list_loc = create_or_load_priority_file(list_name)

    error = None

    while True:
        print('\n' * 20)
        if error:
            print(error)
            print('-'*30)
            error = None
        print(f'{list_name} list. What would you like to do?')
        print('(a)dd a priority')
        print('(p)rint the list of priorities')
        print('(q)uit')
        selection = input('>> ').lower()

        if selection not in 'apq':
            error = f'Error! "{selection}" not recognized. Please select from the menu.'

        if selection == 'a':
            print('Add a priority.')
            time = str(datetime.now())
            desc = input('Provide a description ')
            priority = input('What is the priority? (1, 2, 3) ')

            with open(list_loc, 'r') as list_file:
                list_items = csv.DictReader(list_file)
                next_item = '0'
                max_item = 0

                for item in list_items:
                    num = int(item['item_number'])
                    if num >= max_item:
                        next_item = str(num + 1)
                        
            with open(list_loc, 'a') as list_file:
                list_file.write(','.join([next_item, time, desc, priority + '\n']))
                print('Added one item to your list!')
                input('Press enter to continue...')


        if selection == 'p':
            print('Here\'s your current list of priorities:')
            with open(list_loc, 'r') as list_file:
                list_items = csv.DictReader(list_file)
                for item in list_items:
                    if item['complete'] == 'False':
                        print(item)
                input('press enter to continue..')

        if selection == 'q':
            quit()

def create_or_load_priority_file(list_name):
    base_path = Path.cwd()
    lists_path = Path(base_path, 'lists')
    if not Path.exists(lists_path):
        Path.mkdir(lists_path)

    list_path = Path(lists_path, (list_name + '.csv'))

    if not Path.exists(list_path):
        with open(list_path, 'a') as list_file:
            list_file.write('item_number,timestamp,description,priority' + '\n')
    
    return list_path
    
if __name__ == '__main__':
    main()