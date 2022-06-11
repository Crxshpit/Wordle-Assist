from colorama import Fore # Terminal colour

# Triple speech marks below indicate to format the string as is (terminal visual)
print(Fore.GREEN + r""" 
((((((((((((((((((((((((((((((((((((((((((((((((\
(((((((((((((((((((((((((((((((((((((((((((((((((((((((\
((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((\
(((((((((*      ((((((((((((.      (((((((((((((      ((((((((
(((((((((        #(((((((((         ((((((((((,      ,(((((((( 
(((((((((#        ((((((((           (((((((((       ((((((((( 
((((((((((.        (((((((            (((((((       (((((((((( 
(((((((((((        #(((((              (((((       #(((((((((( 
((((((((((((        ((((               ((((#       ((((((((((( 
((((((((((((#        ((        /\       (((       (((((((((((( 
(((((((((((((        ((       /((\       (        ((((((((((((
((((((((((((((               /((((\              .(((((((((((( 
(((((((((((((((             /((((((\             ((((((((((((( 
((((((((((((((((           /((((((((\           (((((((((((((( 
((((((((((((((((          /((((((((((\         /(((((((((((((( 
(((((((((((((((((        /#(((((((((((\       ((((((((((((((((  
((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((/
((((((((((((((((((((((((((((((((((((((((((((((((((((((((/
((((((((((((((((((((((((((((((((((((((((((((((((/
 """)

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
