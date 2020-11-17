import scraper
import translate
import sys

scraper = scraper.Scraper()
translator = translate.Translator()
actions = ['\nScrape Data (1)','Translate Song to CSV (2)','Print Song in Command Line (3)','Exit (4)']

while True:
	while True:
		try:
			print('\nPlease select an action:')
			for i in actions:
				print(i)
			action = int(input('\n'))
			if action in [1,2,3,4]:
				break
			else:
				print('Please enter a valid action.')
		except:
			print('Please enter a valid action.')

	if action == 1:
		scraper.scrape_data()
	if action == 2:
		lyrics = translator.load_data()
		translator.translate_song(lyrics)
	if action == 3:
		lyrics = translator.load_data()
		translator.print_song(lyrics)
	if action == 4:
		sys.exit()





def main():
	pass

# if __main__ = 'main':
# 	main()