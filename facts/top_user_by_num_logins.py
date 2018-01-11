'''
Get top user by number of logins

by @nathanperkins (GitHub)
https://github.com/nathanperkins/
'''

from facts.helpers.users import get_users


def fact():
    return {
        'top_user_by_num_logins': get_users(sorted_by='num_logins')[0],
    }


if __name__ == '__main__':
    print fact()
