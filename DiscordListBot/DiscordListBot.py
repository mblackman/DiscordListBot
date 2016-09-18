import os
import sys
import time
import json

import discord
import asyncio
import configuration
import lists

class ListBot(discord.Client):
    def __init__(self):
        self.config = configuration.Config()
        self.notebook = lists.notebook()
        super().__init__()

    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

    def run(self):
        try:
            self.loop.run_until_complete(self.start(self.config.token))

        except discord.errors.LoginFailure:
            # Handle login failure
            raise Exception('login_failure', 'Failed to login do something')

        finally:
            self.loop.close()

    async def on_message(self, message):
        await self.wait_until_ready()

        message_content = message.content.strip()

        if not message_content.startswith(self.config.prefix):
            return

        if message.author == self.user:
            self.safe_print("Ignoring command from myself (%s)" % message.content)
            return

        command, *args = message_content.split()
        command = command[len(self.config.prefix):].lower().strip()

        if command == 'add':
            add_note(self, args)

    def add_note(self, args):
        argLen = len(args)

        if argLen == 0:
            return

        listName = args[0]
        args.pop(0)
        newLine = ' '.join(args)

        self.notebook.add_to_list(listName, newLine)


        return

if __name__ == '__main__':
    bot = ListBot()
    bot.run()