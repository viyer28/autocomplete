#!/usr/bin/env python3

import time
from prompt_toolkit import prompt
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.auto_suggest import AutoSuggest, Suggestion

# Press tab to complete word + grayed out in-place
# word_list = ["def", "for", "range", "else", "print"]

kb = KeyBindings()
start_time = time.time()
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
autocompletes = 0

# Exit Test
@kb.add('c-c')
def _(event):
    event.app.exit()

# Tab spacing and complete
@kb.add('c-i')
def _(event):
    global autocompletes

    b = event.app.current_buffer
    w = b.document.get_word_before_cursor()

    if w in completions:
        b.insert_text(completions[w])
        autocompletes = autocompletes + 1
    else:
        b.insert_text("    ")

# Disable right key completion
@kb.add('right')
def _(event):
    return

# Shift-tab
@kb.add('s-tab')
def _(event):
    b = event.app.current_buffer
    b.delete_before_cursor(count=4)

class MyCustomSuggester(AutoSuggest):
    def get_suggestion(self, buffer, document):
        w = document.get_word_before_cursor()

        if w in completions:
            return Suggestion(completions[w])

        return None


def main():
    text = prompt('', key_bindings=kb, multiline=True, auto_suggest=MyCustomSuggester())
    end_time = time.time()
    print("\nYour time: %f seconds"% (end_time-start_time))
    print("Autocompletes: %d"% autocompletes)


if __name__ == '__main__':
    main()