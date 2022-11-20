# -*- coding: utf-8 -*-

from flask import Flask, render_template
import json
import os
import requests

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Welcome to Dota2 Queries!</p>"

@app.route("/rankings")
def rankings(date: int = None):
    """Player hero rankings"""
    players = ['134784663', '6832287527']
    url = 'https://api.opendota.com/api/players/'
    player_win_rate_dict = {}
    for player in players:
        data = requests.get(url + player + '/wl', date)
        data = data.json()
        try: 
            win_rate = data['win']/(data['win'] + data['lose'])
        except:
            win_rate = 0
        player_win_rate_dict[player] = win_rate
    sorted_player_win_rate_list = sorted(player_win_rate_dict, key=player_win_rate_dict.get, reverse=True)
    return str(sorted_player_win_rate_list) 


@app.route("/recommended")
def heroes():
    """
    Suggestion of a hero that the player should play based on the player historical win rate
    """
    player = '134784663'
    url = 'https://api.opendota.com/api/players/'
    data = requests.get(url + player + '/heroes')
    data = json.loads(data.text)
    data = sorted(data, key = lambda x: x['win']/x['games'] if x['games'] else 0, reverse = True)
    recommended_hero_id = [x['hero_id'] for x in data][0]
    #convert hero_id to hero name
    hero = requests.get('https://api.opendota.com/api/heroes/')
    hero = json.loads(hero.text)
    recommended_hero = [x['name'] for x in hero if x['id']== int(recommended_hero_id)][0]
    return recommended_hero


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
