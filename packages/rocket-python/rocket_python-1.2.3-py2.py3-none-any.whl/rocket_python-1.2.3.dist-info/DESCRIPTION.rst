#### RocketChat API

Python API wrapper for the [Rocket chat API](https://rocket.chat/docs/developer-guides/rest-api)

[Documentation](http://rocket-python.readthedocs.io/en/latest/)

#### Install

    pip install rocket-python

#### Usage

Initialize the client with a username and password.  This user *must* have Admin privs::

    from rocketchat.api import RocketChatAPI

    api = RocketChatAPI(settings={'username': 'someuser', 'password': 'somepassword',
                                  'domain': 'https://myrockethchatdomain.com'})

##### Available Calls
    api.send_message('message', 'room_id')
    api.get_private_rooms()
    api.get_private_room_history('room_id', oldest=date)
    api.get_public_rooms()
    api.get_room_info('room_id')
    api.get_private_room_info('room_id')
    api.get_room_history('room_id')
    api.get_my_info()

check /rocketchat/calls/api.py for more.

#### Running Tests

    py.test tests rocketchat

##### Sending a message

You'll first need to get the _id of the room you want to send a message to.  Currently, Rocket
can only send messages to *public* rooms.

    api.send_message('Your message', room_id)


