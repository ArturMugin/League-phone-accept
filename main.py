from lcu_driver import Connector

connector = Connector()


@connector.ready
async def connect(connection):
    print('LCU API is ready to be used.')



@connector.ready
async def connect(connection):
    summoner = await connection.request('get', '/lol-summoner/v1/current-summoner')
    print(await summoner.json())

    
@connector.ws.register('/lol-summoner/v1/current-summoner', event_types=('UPDATE',))
async def icon_changed(connection, event):
    print(f'The summoner {event.data["displayName"]} was updated.')


@connector.close
async def disconnect(connection):
    print('The client was closed')
    await connector.stop()

    
connector.start()