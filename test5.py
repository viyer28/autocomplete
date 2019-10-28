#!/usr/bin/env python3

import time
from prompt_toolkit import prompt
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.completion import Completer, Completion

# Press right key to complete word + dropdown
# word_list = ["def", "for", "range", "else", "print"]

kb = KeyBindings()
linebreak = "="*100
t = "    "
# start_time = time.time()
end_time = 0

# Dictionary of words to be replaced
completions = {
    'd': 'ef',
    'de': 'f',
    'f': 'or',
    'fo': 'r',
    'r': 'ange',
    'ra': 'nge',
    'ran': 'ge',
    'rang': 'e',
    'e': 'lse',
    'el': 'se',
    'els': 'e',
    'p': 'rint',
    'pr': 'int',
    'pri': 'nt',
    'prin': 't'
}
suggestions = {
    'd': 'def',
    'de': 'def',
    'f': 'for',
    'fo': 'for',
    'r': 'range',
    'ra': 'range',
    'ran': 'range',
    'rang': 'range',
    'e': 'else',
    'el': 'else',
    'els': 'else',
    'p': 'print',
    'pr': 'print',
    'pri': 'print',
    'prin': 'print'
}
autocompletes = 0

# Exit Test
@kb.add('c-c')
def _(event):
    event.app.exit()

# Tab spacing
@kb.add('c-i')
def _(event):
    b = event.app.current_buffer
    b.insert_text("    ")

# Complete with right-key
@kb.add('right')
def _(event):
    global autocompletes

    b = event.app.current_buffer
    w = b.document.get_word_before_cursor()

    if w in completions:
        b.insert_text(completions[w])
        autocompletes = autocompletes + 1

# Shift-tab
@kb.add('s-tab')
def _(event):
    b = event.app.current_buffer
    b.delete_before_cursor(count=4)

class MyCustomCompleter(Completer):
    def get_completions(self, document, complete_event):
        w = document.get_word_before_cursor()

        if w in suggestions:
            yield Completion(suggestions[w], start_position=-1*len(w))


def main():
    print('\n\n')
    print(linebreak)
    print("INSTRUCTIONS: For this test, suggested words will be displayed in a dropdown menu for certain keywords.")
    print("These keywords are def, for, range, else, and print.")
    print("Press the right arrow key to autocomplete a word.")
    print(linebreak)
    print("FUNCTION:")
    print("def function5():\n{}for i in range(0, 5):\n{}{}if i == 0:\n{}{}{}print(\"*\")\n{}{}else:\n{}{}{}print(\"#\")".format(t,t,t,t,t,t,t,t,t,t,t))
    print(linebreak)
    print("You will be timed, but timing will not start until you indicate you are ready to continue.")
    print("As soon as you are finished, please press ctrl+c to end the timing.")
    continue_ans = input('Do you wish to continue? y/n ?').lower()
    if continue_ans == "n":
        print("Goodbye!")
        sys.exit()
    elif continue_ans != "y":
        print("Input not recognized please restart and try again. Goodbye!")
        sys.exit()
    else:
        print("starting in ...")
        for i in range(5,0,-1):
            time.sleep(1)
            print(i)

        time.sleep(1)
        start_time = time.time()
        end_time = 0


        text = prompt('', key_bindings=kb, multiline=True, completer=MyCustomCompleter())
        end_time = time.time()
        print("\nYour time: %f seconds"% (end_time-start_time))
        print("Autocompletes: %d"% autocompletes)


if __name__ == '__main__':
    main()
