# Cantando
 Warm up those vocal chords! This command line app scrapes foreign song lyrics from Genius.com and translates them to English.

 Code for the Genius.com scraper was obtained from a blog post by Abhisek Roy on PromptCloud.com ('Scraping Song Lyrics using Python from Genius' https://www.promptcloud.com/blog/scraping-song-lyrics-using-python-from-genius/).

 The main.py file uses two modules - the scraper module and the translate module. There are four actions that can be performed using the app:
 * Scrape Data - input a URL from Genius.com of a song you would like translated. It will return a json file with the lyrics and any comments from the website (as well as the scraped html in a separate file).
 * Translate Song - this command takes a json file of a song you have scraped, translates it to english, and returns a csv file (idea being to then load it into a pandas dataframe).
 * Print Song - this command takes a json file and prints the original lyrics and translation to the command line.
 * Exit - this command exits the application.
