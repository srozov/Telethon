#!/usr/bin/env python3
# A simple script to print all updates received
#
# NOTE: To run this script you MUST have 'TG_API_ID' and 'TG_API_HASH' in
#       your environment variables. This is a good way to use these private
#       values. See https://superuser.com/q/284342.

from os import environ

# environ is used to get API information from environment variables
# You could also use a config file, pass them as arguments,
# or even hardcode them (not recommended)
from telethon import TelegramClient


def main():
    session_name = environ.get('TG_SESSION', 'session')
    client = TelegramClient(session_name,
                            int(environ['TG_API_ID']),
                            environ['TG_API_HASH'],
                            proxy=None,
                            update_workers=4,
                            spawn_read_thread=False)

    if 'TG_PHONE' in environ:
        client.start(phone=environ['TG_PHONE'])
    else:
        client.start()

    client.add_event_handler(update_handler)
    print('(Press Ctrl+C to stop this)')
    client.idle()


def update_handler(update):
    print(update)


if __name__ == '__main__':
    main()
