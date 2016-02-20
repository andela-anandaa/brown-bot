from slackbot.bot import Bot
from slackbot.bot import respond_to, listen_to

import re

def main():
    bot = Bot()
    bot.run()

@respond_to('hi', re.IGNORECASE)
def hi(message):
    message.reply('I think you are greeting me, hi :-)')
    # message.react('+1')

@respond_to('tell mahad habari', re.IGNORECASE)
def hi(message):
    message.reply('Hey @mahad.walusimbi - habari yako?')
    # message.react('+1')

@listen_to('Brown Bag', re.IGNORECASE)
def brown_bag(message):
    message.reply('Did you mention Brown Bag?')

if __name__ == "__main__":
    print "==> BrownBot is now Running"
    main()
