from colorama import Fore # Terminal colour
from tkinter import *

# Base variable establishment
root = Tk()
root.title("Wordle Assist")

e = Entry(root, width=50)
e.grid(row=0, column=0, columnspan=3, width=10, height=10)

def button_add():
	return

# Creating buttons
button_a = Button(root, text="A", width=40, height=20, bg="#787268", command=button_add)
button_b = Button(root, text="B", width=40, height=20, bg="#787268", command=button_add)
button_c = Button(root, text="C", width=40, height=20, bg="#787268", command=button_add)
button_d = Button(root, text="D", width=40, height=20, bg="#787268", command=button_add)
button_e = Button(root, text="E", width=40, height=20, bg="#787268", command=button_add)
button_f = Button(root, text="F", width=40, height=20, bg="#787268", command=button_add)
button_g = Button(root, text="G", width=40, height=20, bg="#787268", command=button_add)
button_h = Button(root, text="H", width=40, height=20, bg="#787268", command=button_add)
button_i = Button(root, text="I", width=40, height=20, bg="#787268", command=button_add)
button_j = Button(root, text="J", width=40, height=20, bg="#787268", command=button_add)
button_k = Button(root, text="K", width=40, height=20, bg="#787268", command=button_add)
button_l = Button(root, text="L", width=40, height=20, bg="#787268", command=button_add)
button_m = Button(root, text="M", width=40, height=20, bg="#787268", command=button_add)
button_n = Button(root, text="N", width=40, height=20, bg="#787268", command=button_add)
button_o = Button(root, text="O", width=40, height=20, bg="#787268", command=button_add)
button_p = Button(root, text="P", width=40, height=20, bg="#787268", command=button_add)
button_q = Button(root, text="Q", width=40, height=20, bg="#787268", command=button_add)
button_r = Button(root, text="R", width=40, height=20, bg="#787268", command=button_add)
button_s = Button(root, text="S", width=40, height=20, bg="#787268", command=button_add)
button_t = Button(root, text="T", width=40, height=20, bg="#787268", command=button_add)
button_u = Button(root, text="U", width=40, height=20, bg="#787268", command=button_add)
button_v = Button(root, text="V", width=40, height=20, bg="#787268", command=button_add)
button_w = Button(root, text="W", width=40, height=20, bg="#787268", command=button_add)
button_x = Button(root, text="X", width=40, height=20, bg="#787268", command=button_add)
button_y = Button(root, text="Y", width=40, height=20, bg="#787268", command=button_add)
button_z = Button(root, text="Z", width=40, height=20, bg="#787268", command=button_add)


# Buttons on screen

button_a.grid(row=1, column=0)
button_b.grid(row=1, column=1)
button_c.grid(row=1, column=2)
button_d.grid(row=1, column=3)
button_e.grid(row=1, column=4)
button_f.grid(row=1, column=5)

button_g.grid(row=2, column=0)
button_h.grid(row=2, column=1)
button_i.grid(row=2, column=2)
button_j.grid(row=2, column=3)
button_k.grid(row=2, column=4)
button_l.grid(row=2, column=5)

button_m.grid(row=3, column=0)
button_n.grid(row=3, column=1)
button_o.grid(row=3, column=2)
button_p.grid(row=3, column=3)
button_q.grid(row=3, column=4)
button_r.grid(row=3, column=5)

button_s.grid(row=4, column=1)
button_t.grid(row=4, column=2)
button_u.grid(row=4, column=3)
button_v.grid(row=4, column=4)

button_w.grid(row=5, column=1)
button_x.grid(row=5, column=2)
button_y.grid(row=5, column=3)
button_z.grid(row=5, column=4)














































wordlist = [] # The main list of possible words variable

try: # Using try statements for good error practise when opening file
	with open ('wordlist.txt') as f:
		for line in f:
			wordlist.append(line.strip()) # Appends each word into the wordlist variable above, stripping each line in between
except FileNotFoundError:
	print(Fore.RED,"[WORDLE-ASSIST] ERROR Wordlist file was unable to be imported. Please restart")

# Terminal visual
print(Fore.YELLOW,"\n[WORDLE-ASSIST] This is a wordle solver utility. Input words and the letter feedback, and approrpiate\nwords will be suggested.")
print("="*101)
print(Fore.YELLOW,"\n[WORDLE-ASSIST] Good starting words are crane, soare, adieu and argue.")


for num in range(6): # The amount of possible guesses to iterate over for main code body
	guess = input(Fore.YELLOW+"\n[WORDLE-ASSIST] Input word: ").lower() # Guess word
	for i in guess:
		if not (i in "abcdefghijklmnopqrstuvwxyz") or len(guess) != 5 or guess not in wordlist: # Checking if input word is valid or not
			print(Fore.RED, ("\n[WORDLE-ASSIST] Please input a 5 valid letter word as a guess with only letters included.\nOr, the word is unable to be the answer based off the letters known."))
			exit()
		else:
			pass


	print("[WORDLE-ASSIST] g - green, y - yellow, w - wrong / grey") # Feedback prompts
	feedback = input("[WORDLE-ASSIST] Feedback: ") # Feedback input
	for i in feedback:
		if not (i in "gyw") or len(feedback) != 5: # Checking if feedback input is valid or not
			print(Fore.RED, ("\n[WORDLE-ASSIST] Please ensure you are inputting 5 letters and following the feedback rule (g - green, y - yellow, w - wrong / grey)"))
			exit()
		else:
			pass

	if feedback == "ggggg": # If the word is found
		print(Fore.GREEN,"\n[WORDLE-ASSIST] Word found! The word was",guess)
		exit()

	for word in wordlist[:]: # The main body of the code. Iterating for each word in the wordlist

		for i in range(5): # For each letter in the word (5 letters)

			if feedback[i] == "g" and guess[i] != word[i]: # Removes word if correct letter isn't in same place as guess word
				wordlist.remove(word)
				break

			elif feedback[i] == "w" and guess[i] == word[i]: # Removes word if wrong letter is in it. guess[i] == word[i] in the event of multiple letters
					wordlist.remove(word)
					break

			elif feedback[i] == "y" and guess[i] not in word: # Removes word if yellow letter isn't in word
				wordlist.remove(word)
				break

			elif feedback[i] == "y" and guess[i] == word[i]: # Removes word if yellow letter is in the same place as guess word
				wordlist.remove(word)
				break

	#  Format code for suggestion words
	counter = 0
	print(Fore.LIGHTGREEN_EX+"[WORDLE-ASSIST] Possible Words: ")
	for word in wordlist:
		print(word,end=", ")
		counter+=1
		if counter == 8: # (Keeps max 8 words on one line in terminal)
			print("")
			counter = 0
