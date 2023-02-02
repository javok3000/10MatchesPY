#!/usr/bin/env python3
import argparse
from argparse import RawTextHelpFormatter
import requests
import json
import pprint

parser = argparse.ArgumentParser(formatter_class=RawTextHelpFormatter, description='Little api challenge to see last 10 matches of a lol player.',prog='10 last martches')
parser.add_argument('-s','--summoner', type=str,help='Summoner name',required=True)
parser.add_argument('-r', '--region', type=str, required=True,help='Regions format:\n\t'
                                                                        '- br1\n\t'
                                                                        '- eun1\n\t'
                                                                        '- euw1\n\t'
                                                                        '- jp1\n\t'
                                                                        '- kr\n\t'
                                                                        '- la1\n\t'
                                                                        '- la2\n\t'
                                                                        '- na1\n\t'
                                                                        '- oc1\n\t'
                                                                        '- ph2\n\t'
                                                                        '- ru\n\t'
                                                                        '- sg2\n\t'
                                                                        '- th2\n\t'
                                                                        '- tr1\n\t'
                                                                        '- tw2\n\t'
                                                                        '- vn2\n')
                                                                        
parser.add_argument('-k','--key',type=str, required=True, help='Required LoL Dev key')
args = parser.parse_args()
region = vars(args)['region']
summonerName = vars(args)['summoner']
print(summonerName, 'Region = ', region)

key = vars(args)['key']
summoner = requests.get(f'https://{region}.api.riotgames.com/lol/summoner/v4/summoners/by-name/{summonerName}?api_key={key}')
continent = ['americas','europe','asia', 'sea']
index = -1
americas, europe, asia, sea = ['na1', 'la1', 'la2', 'br1'], ['euw1','eun1','ru','tr1'], ['jp1','kr'], ['oc1','ph2','sg2','th2','tw2','vn2']

if region in americas:
    index = 0 
elif region in europe:
    index = 1
elif region in asia:
    index = 2
elif region in sea :
    index = 3

summoner_info_manage = json.loads(summoner.text)['puuid']
matches = requests.get(f'https://{continent[index]}.api.riotgames.com/lol/match/v5/matches/by-puuid/{summoner_info_manage}/ids?start=0&count=10&api_key={key}')
matches_list = matches.text
matches_list = matches_list.replace('[','')
matches_list = matches_list.replace(',',' ')
matches_list = matches_list.replace('"','')
matches_list = matches_list.replace(']','')
matches_list = matches_list.split()

for match in range(0,len(matches_list)):
    match_info = requests.get(f'https://{continent[index]}.api.riotgames.com/lol/match/v5/matches/{matches_list[match]}?api_key={key}')
    match_info_manage = json.loads(match_info.text)
    info = match_info_manage['info']
    lista = info['participants']
    win = False
    for i in range(0,len(lista)):
        if lista[i]['summonerName'] == summonerName:
            win = lista[i]['win']
            if win == True:
                print (f'Match: {match+1}, Victory')
            else:
                print (f'Match: {match+1}, Defeat')