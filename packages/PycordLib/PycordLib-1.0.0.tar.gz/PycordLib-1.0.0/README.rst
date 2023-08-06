Pycord
======

Super simple Discord API layer. If you want something full-featured,
this isn't it. Try
`discord.py <https://github.com/Rapptz/discord.py>`__.

This library is suitable for simple bots that allow users to send
commands.

Installation
------------

1. Clone from GitHub
2. Setup virtual environment: ``virtualenv env -p python3.6``
3. Activate: ``source env/bin/activate``
4. Install libraries: ``pip install -r requirements.txt``

Making a bot
------------

Import the Pycord object and instantiate it, passing in your bot token
(`need a token? <https://discordapp.com/developers/applications/me>`__):

.. code:: python

    from pycord import Pycord


    pycord = Pycord('your.token.here')

From there, you'll want to start the websocket connection:

.. code:: python

    pycord.connect_to_websocket()

Next, you'll want to register some command callbacks. There are two ways
to do this, depending on how you want to lay out your code (you can mix
and match):

.. code:: python

    # immediate registeration via decorator

    @pycord.command('hello')
    def hello(data):
        # do stuff


    # delayed registeration
    def hello(data):
        # do stuff

    # later
    pycord.register_command('hello', hello)

The method names don't matter; the string you register the callback with
is what determines what the bot listens for.

All commands start with ``!``. Examples:

    !hello bob

.. code:: python

    @pycord.command('hello')
    def do_hello_command(data):
        pycord.send_message(data['channel_id'], 'Hello '+ data['author']['username'])

Adding your bot to your Discord server
--------------------------------------

Per `the OAuth2
documentation <https://discordapp.com/developers/docs/topics/oauth2#adding-bots-to-guilds>`__,
you'll need to generate a link and then have someone who is an admin on
the desired server click it, log in, and accept the bot.

The link will look like this:

https://discordapp.com/api/oauth2/authorize?client\_id=[id]&scope=bot&permissions=[perms]

-  [id] is the bot's "Client Id", accessible on `your app's
   page <https://discordapp.com/developers/applications/me>`__
-  [perms] is the bot's required permissions.

For bots made with this library, you'll likely need the "Read Messages"
and "Send Messages" permissions. That's permission code ``3072``.

There's a super-handy `permissions calculator
here <https://discordapi.com/permissions.html>`__ if I add more to the
library and you want to use it.
