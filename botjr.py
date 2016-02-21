from slacker import Slacker


def get_members_in_the_nairobi_brown_bag_channel():
	slack = Slacker('xoxb-22334709665-8GDIEcmTVRMUKqQFUuTPB76p')
	# retrieve info from the #brown-bag-nairobi channel
	response = slack.channels.info('C0NBFQSG1')
	# Strip out members in that channel
	channel_members = response.body['channel']['members']
	return channel_members
	# code for sending a message to a particular user
	# Use the @ symbol for a user and the # symbol for a channel
	# slack.chat.post_message('@nandaa', 'This is your id: U071T5TJ6', as_user=True)

