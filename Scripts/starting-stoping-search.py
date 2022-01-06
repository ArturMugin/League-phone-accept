from time import sleep
import json
from lcu_driver import Connector
while True:
    connector = Connector()



    @connector.ready
    async def connect(connection):
        
        answer = input("Accept 1 \nDecline 2\n") 

        if answer == "1":
            @connector.ready
            async def connect(connection):
                summoner = await connection.request('post', '/lol-lobby/v2/lobby/matchmaking/search')
                
                print("ACCEPTED")
                
                

        elif answer =="2":
            @connector.ready
            async def connect(connection):
                summoner = await connection.request('delete', '/lol-lobby/v2/lobby/matchmaking/search')
                
                print("DECLINED")
                

# starts the connector
    connector.start()