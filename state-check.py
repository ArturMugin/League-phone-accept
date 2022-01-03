import json
from lcu_driver import Connector

connector = Connector()


@connector.ready
async def connect(connection):
    summoner = await connection.request('get', '/lol-gameflow/v1/gameflow-phase') 
    
    phase = await summoner.json()
#    print(summoner)
    if phase == 'ReadyCheck':    
        print("kek")
        @connector.ready
        async def connect(connection):
            summoner = await connection.request('post', '/lol-matchmaking/v1/ready-check/accept') 

# starts the connector
connector.start()