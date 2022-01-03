from lcu_driver import Connector

connector = Connector()




    
# fired when LCU API is ready to be used

@connector.ready
async def connect(connection):
    summoner = await connection.request('post', '/lol-matchmaking/v1/ready-check/accept')   






connector.start()