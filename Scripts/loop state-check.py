from time import sleep
import json
from lcu_driver import Connector
while True:
    connector = Connector()



    @connector.ready
    async def connect(connection):
        
        summoner = await connection.request('get', '/lol-gameflow/v1/gameflow-phase') 
        
        phase = await summoner.json()
    #    print(summoner)
        if phase == 'ReadyCheck':
            answer = input("Accept 1 /n Decline 2")    
            if answer == "1":
                @connector.ready
                async def connect(connection):
                    summoner = await connection.request('post', '/lol-matchmaking/v1/ready-check/accept')
                    print("Accept")
                    
            else:
                @connector.ready
                async def connect(connection):
                    summoner = await connection.request('post', '/lol-matchmaking/v1/ready-check/decline')
                    print("Decline")
                                    
        elif phase == 'Lobby':
            print("I'm in Lobby")
        elif phase == 'ChampSelect':
            print("I'm in champ select")
        elif phase == 'Matchmaking':
            print("I'm searching for the game")
        else:
            print("I'm in game")
    sleep(1)




# starts the connector
    connector.start()