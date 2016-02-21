import re

from slacker import Slacker

from slackbot.bot import Bot
from slackbot.bot import respond_to, listen_to

import bot_methods as bm

slack = Slacker('xoxb-22328931106-tACwqKP1LwOuwfvGcYD9qHyP')

def main():
	bot = Bot()
	bot.run()

@respond_to('sup', re.IGNORECASE)
@listen_to('sup', re.IGNORECASE)
def hi(message):
    message.reply('I think you are greeting me, hi :-)')
    # message.react('+1')

@respond_to('story kyi', re.IGNORECASE)
def hi(message):
    message.reply('Hey @mahad.walusimbi - habari yako?')
    # message.react('+1')

# select next Brown Bag person
# find regex for this!
@respond_to('who is the next presenter', re.IGNORECASE)
@respond_to('who is the next presenter\?', re.IGNORECASE)
@listen_to('who is the next presenter\?', re.IGNORECASE)
@listen_to('who is the next presenter', re.IGNORECASE)
def select_user(message):
    user = bm.select_brownbag_user()
    if user:
        print "[status] {} selected for BB".format(user.username)
        message.reply('The next presenter is _[drum-roll]_ @{}!!!'.format(user.username))
    	# junior bot DM's the user :)
    	slack.chat.post_message('@{}'.format(user.username), 'You are the one presenting in the next Brown Bag, ha :-D', as_user=True)
    else:
        message.reply('There is no one on the waiting list :( ')
        message.reply('But I think, in that case, Mahad can present about Uganda Elections :-D')

if __name__ == "__main__":
    print "==> I'm up and running :-D"
    main()
