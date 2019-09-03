from pokemon_handbook import pokemon_crawler
import pandas as pd

pokemon_list = pokemon_crawler()
df= pd.DataFrame(pokemon_list)
df.to_csv('pokemon.csv')