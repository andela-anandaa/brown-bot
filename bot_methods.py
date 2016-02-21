import random

import models

session = models.create_session()

def select_brownbag_user():
    '''
    Selects the next person doing Brown Bag.
    Then announces that person in the #brown-bag-nairobi channel
    plus the #nairobi (private channel).
    '''

    users = session.query(models.User).filter(models.User.done == 0).all()
    # import ipdb;ipdb.set_trace()
    
    if len(users) > 0:
        user = random.choice(users)
        # mark the person as 'done'
        mark_brownbag_selected(user.username)
    else:
        user = None

    return user
    

def mark_brownbag_selected(username):
    '''
    Mark the user as done
    '''
    session.query(models.User).filter_by(username=username).update({'done': 1})
    session.commit()

def undo_brownbag_select(username):
    '''
    Unselect done user
    '''
    session.query(models.User).filter_by(username=username).update({'done': 0})
    session.commit()

def mark_brownbag_done(username=''):
    '''
    Called when the last presenter selected has already presented.
    '''
    pass

def hack_mark_brownbag_done():
    for i in range(1, 5):
        session.query(models.User).filter_by(id=i).update({'done': 1})
        session.commit()
