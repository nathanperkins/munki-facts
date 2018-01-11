'''
Get top user by connect time.

by @nathanperkins (GitHub)
https://github.com/nathanperkins/
'''

from facts.helpers.users import get_users


def fact():
    return {
        'top_user_by_connect_time': get_users(sorted_by='connect_time')[0],
    }


if __name__ == '__main__':
    print fact()
