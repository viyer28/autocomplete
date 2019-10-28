#!/usr/bin/env python3

import time
from prompt_toolkit import prompt
from prompt_toolkit.key_binding import KeyBindings
import sys
# Simple tester that times users writing in the prompt


kb = KeyBindings()
# 	start_time = time.time()
# 	end_time = 0
linebreak = "="*100
t = "    "
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
	print('\n\n')
	print(linebreak)
	print("INSTRUCTIONS: For this test, there is no autocomplete functionality.")
	print("Look at the function below. Please recreate this function typing as you normally would.")
	print(linebreak)
	print("FUNCTION:")
	print("def function1():\n{}for i in range(0, 10):\n{}{}if i % 2 == 0:\n{}{}{}print(\"even\")\n{}{}else:\n{}{}{}print(\"odd\")".format(t,t,t,t,t,t,t,t,t,t,t))
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
		print("Please begin. \n")
		start_time = time.time()
		end_time = 0
		text = prompt('', key_bindings=kb, multiline=True)
		end_time = time.time()
		print("\nYour time: %f seconds"% (end_time-start_time))


if __name__ == '__main__':
    main()