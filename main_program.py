from journal_functions import InteractiveJournal
import time

def start_interactive_journal():
    journal = InteractiveJournal()
    print('What is on your mind?')
    active = True
    while active:
        user_input = input('Enter line: ')
        journal.add_entry = user_input
        choice = input('Would you like to add more lines (y/n): ').lower().strip()
        if choice == 'n':
            active = False
        elif choice != 'y':
            print('Invalid input. Exiting...')
            exit()
    print('Let me finalize your entries...')
    time.sleep(1)
    if journal.save_entry():
        print('Entry saved.')
    else:
        print('Entry not saved.')

if __name__ == '__main__':
    start_interactive_journal()




