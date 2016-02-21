from slackbot.bot import Bot
from slackbot.bot import respond_to, listen_to
import botjr
import re


def main():	
	bot = Bot()
	# retrieve members in brown-bag-channel
	members = botjr.get_members_in_the_nairobi_brown_bag_channel()
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

@listen_to('Brown_Bag', re.IGNORECASE)
def brown_bag(message):
    message.reply('yoooo yadoi yadi')

# @listen_to('sup', re.IGNORECASE)
# def brown_bag(message):
#     message.reply('Hey PUNK!!! Back off')

if __name__ == "__main__":
    print "==> I'm Up"
    main()
