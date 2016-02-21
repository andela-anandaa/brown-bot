import models
import botjr

import sys
import os

command = sys.argv[1]

if command == 'create-tables':
    models.create_tables()

if command == 'add-users':
    botjr.add_users_from_channel()

if command == 'refresh-db':
    # reset the whole db
    os.system('rm -f data/data.db')
    print "[status] DB dropped"

    os.system('touch data/data.db')
    print "[status] DB created"

    models.create_tables()
    print "[status] Tables created"

    botjr.add_users_from_channel()


if command == 'populate-brownbag':
    botjr.create_dummy_presenters()
