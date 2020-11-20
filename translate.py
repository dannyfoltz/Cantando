import json
import googletrans
import pandas as pd

class Translator():
	def __init__(self):
		pass

	def load_data(self):
		path = input(f'Please enter the desired song\'s json file path: ')
		with open(path) as f:
			data = json.load(f)
		lyrics = data['Lyrics'][0]
		return lyrics

	def translate_song(self, lyrics):
		translator = googletrans.Translator()
		translations = pd.DataFrame(columns=['Line','Translation'])
		for line in lyrics:
			translation = translator.translate(line).text
			translations = translations.append({'Line':line,'Translation':translation}, ignore_index=True)
		file_path = input('\nPlease enter a name for the output (include .csv): ')
		translations.to_csv(file_path, mode='w', header=True, index=False)

	def print_song(self, lyrics):
		translator = googletrans.Translator()
		for line in lyrics:
			translation = translator.translate(line).text
			print(line)
			print(translation)
			print('\n')