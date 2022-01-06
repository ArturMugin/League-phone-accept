from random import randint

from lcu_driver import Connector

connector = Connector()


async def set_random_icon(connection):
    # random number of a chinese icon
    random_number = randint(1, 10)

    # make the request to set the icon
    icon = await connection.request('put', '/lol-summoner/v1/current-summoner/icon',
                                    data={'profileIconId': random_number})

    # if HTTP status code is 201 the icon was applied successfully
    if icon.status == 201:
        print(f'Chinese icon number {random_number} was set correctly.')
    else:
        print('Unknown problem, the icon was not set.')


# fired when LCU API is ready to be used
@connector.ready
async def connect(connection):
    print('LCU API is ready to be used.')

    # check if the user is already logged into his account
    summoner = await connection.request('get', '/lol-summoner/v1/current-summoner')
    if summoner.status != 200:
        print('Please login into your account to change your icon and restart the script...')
    else:
        print('Setting new icon...')
        await set_random_icon(connection)


# fired when League Client is closed (or disconnected from websocket)
@connector.close
async def disconnect(connection):
    print('The client was closed')
    await connector.stop()




# subscribe to '/lol-summoner/v1/current-summoner' endpoint for the UPDATE event
# when an update to the user happen (e.g. name change, profile icon change, level, ...) the function will be called
@connector.ws.register('/lol-summoner/v1/current-summoner', event_types=('UPDATE',))
async def icon_changed(connection, event):
    print(f'The summoner {event.data["displayName"]} was updated.')

# starts the connector
connector.start()
