import requests
from bs4 import BeautifulSoup
import re
import csv

def pokemon_crawler():
    url ="https://pokemondb.net/pokedex/all"
    r = requests.get(url)
    html = r.text
    soup = BeautifulSoup(html, features='html.parser')
    pokemon_list = []

    #add order number
    numbers = soup.find_all("span", {"class":"infocard-cell-data"})
    for number in numbers:
        pokemon_dictionary = {}
        pokemon_dictionary["Number"] = number.get_text()
        pokemon_list.append(pokemon_dictionary)

    #add name
    names = soup.find_all("a", {"class":"ent-name"})
    counter = 0
    for name in names:
        pokemon_list[counter]["Name"] = name.get_text()
        counter += 1

    #add type
    counter = 0
    kinds = soup.find_all("td", {"class":"cell-icon"})
    for kind in kinds:
        kind_list = []
        personal_kinds = kind.find_all("a")
        for personal_kind in personal_kinds:
            kind_list.append(personal_kind.get_text())
        pokemon_list[counter]["Type"] = kind_list
        counter += 1

    #add total ability
    counter = 0
    total_abilities = soup.find_all("td", {"class":"cell-total"})
    for single_total in total_abilities:
        pokemon_list[counter]["Total"] = single_total.get_text()
        counter += 1

    #add ability details
    counter = 0
    items = soup.find_all("tr")
    for item in items:
        abilities = item.find_all("td", {"data-sort-value":'', "class":"cell-num"})  
        if abilities:   
            pokemon_list[counter]["HP"] = abilities[0].get_text()
            pokemon_list[counter]["Attack"] = abilities[1].get_text()
            pokemon_list[counter]["Defence"] = abilities[2].get_text()
            pokemon_list[counter]["Sp.Atk"] = abilities[3].get_text()
            pokemon_list[counter]["Sp.Def"] = abilities[4].get_text()
            pokemon_list[counter]["Speed"] = abilities[5].get_text()
            counter += 1
    return pokemon_list
