from time import sleep
import json
from lcu_driver import Connector

connector = Connector()



@connector.ready
async def connect(connection):
    while True:
        summoner = await connection.request('get', '/lol-gameflow/v1/gameflow-phase') 
        
        phase = await summoner.json()
    #    print(summoner)
        if phase == 'ReadyCheck':
            answer = input("Accept 1 /n Decline 2")    
            if answer == 1:
                async def connect(connection):
                    summoner = await connection.request('post', '/lol-matchmaking/v1/ready-check/accept')
                    
            else:
                 async def connect(connection):
                    summoner = await connection.request('post', '/lol-matchmaking/v1/ready-check/decline')
            break                       
        elif phase == 'Lobby':
            print("I'm in Lobby")
        elif phase == 'ChampSelect':
            print("I'm in champ select")
        elif phase == 'Matchmaking':
            print("I'm searching for the game")
        sleep(1)




# starts the connector
connector.start()