from slacker import Slacker

from models import create_user

slack = Slacker('xoxb-22334709665-8GDIEcmTVRMUKqQFUuTPB76p')

def get_members_in_the_nairobi_brown_bag_channel():
	# retrieve info from the #brown-bag-nairobi channel
	response = slack.channels.info('C0NBFQSG1')
	# Strip out members in that channel
	channel_members = response.body['channel']['members']
	return channel_members
	# code for sending a message to a particular user
	# Use the @ symbol for a user and the # symbol for a channel
	# slack.chat.post_message('@nandaa', 'This is your id: U071T5TJ6', as_user=True)

def add_users_from_channel():
	members = get_members_in_the_nairobi_brown_bag_channel()
	print "[status] Members fetched"

	for slackid in members:
		response = slack.users.info(slackid)
		print "[status] User fetched: {}".format(response.body['user']['name'])
		# Strip out members in that channel
		username = response.body['user']['name']
		first_name = response.body['user']['profile']['first_name']
		last_name = response.body['user']['profile']['last_name']
		email = response.body['user']['profile']['email']
		phone = response.body['user']['profile'].get('phone', '')

		create_user(username=username, slackid=slackid,
				first_name=first_name, last_name=last_name,
				email=email, phone=phone)
