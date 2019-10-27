#!/usr/bin/env python3

import time
from prompt_toolkit import prompt
from prompt_toolkit.key_binding import KeyBindings

# Simple tester that times users writing in the prompt

kb = KeyBindings()
start_time = time.time()
end_time = 0

# Finish test
@kb.add('s-tab')
def _(event):
    end_time = time.time()
    print("\nYour time: %f seconds"% (end_time-start_time))

# Exit Test
@kb.add('c-c')
def _(event):
    event.app.exit()

# Tab spacing
@kb.add('c-i')
def _(event):
    b = event.app.current_buffer
    b.insert_text("    ")

# Shift-tab
@kb.add('s-tab')
def _(event):
    b = event.app.current_buffer
    b.delete_before_cursor(count=4)
    
def main():
    text = prompt('', key_bindings=kb, multiline=True)


if __name__ == '__main__':
    main()