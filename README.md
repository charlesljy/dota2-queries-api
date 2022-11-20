# Take Home Assignment
- name: charles
- email: charlesleejy@gmail.com


# API for Dota2 queries

As a part of the data team at Healint, you are tasked with coming up with an API for Dota2 queries that are frequently asked.

You can use the OpenDota API (https://docs.opendota.com/#) to build your own API.

The questions that your API must answer are:
1.	Given a list of player_ids (for example all the players in this match:https://www.opendota.com/matches/683764809 ) return a leaderboard of the players based on their win rate. The API can take two additional parameters
a.	a time period such as “last_week”, “last_month”, “last_year” 
b.	OR a date e.g. ‘2022-01-01’
2.	Given one player_id (for example: https://www.opendota.com/players/134784663 i.e. 134784663), return a suggestion of a hero that the player should play based on the player historical data.


# Launching the application

## Run the app

    FLASK_APP=app.py flask run


## Build docker image

    docker build -t dota2-queries-api .

## Run docker compose

    docker-compose up


# Write Up

A write-up detailing your answers to the below questions would also need to be submitted.

## 1.	Which tech stacks / frameworks did you consider for the development of this application?

This is a basic application built on flask API framework using python. Since it is simple API it just needs to be flexible, and lightweight, without the need to be feature rich. It is a small and simple application with little production specification and functionality, Flask would be sufficient. Flask is designed to enable us to scale web apps quickly and simply since this application, although simple could potentially be used by many users. To improve on the feature of the application, using Flask which uses Python programming language would allow for the application to handle activities as varied as data scraping, machine learning, and artificial intelligence more easily.


## 2.	What are some limitations of your application and how do you plan to work around them in the future?

The application does not have the ability to answer define the timeframe from which the answers are sought from.

## 3.	How would you ensure data required for the application stays up to date?

The data required for the application depends on the the external API, OpenDota API that is used in this application. In order to ensure that the data from the OpenDota API is up to date, we can check to make sure that the call for the OpenDota API with the latest date as a health check on a daily basis and assess the response to determine if the data is up to date.

## 4.	Why is your recommendation engine a good solution?

The recommendation engine depends only on the win rate of the hero (number of win/ number of games) by the particular user. It is possible to design a recommendation engine that better allow for better recommendation by looking at the ability 

## 5.	What are some features you would like to add to the application?

It would be useful to have features that allow us to answer more questions. 




