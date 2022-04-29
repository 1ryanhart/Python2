import os

from QuoteEngine import Ingestor

directory = './_data/DogQuotes/'

for file in os.listdir(directory):
    Ingestor.parse(f'{directory}/{file}')
