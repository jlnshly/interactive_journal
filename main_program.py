from journal_functions import InteractiveJournal
import time

def start_interactive_journal():
    journal = InteractiveJournal()
    print("What's on your mind?")
    active = True
    user_input = input()

