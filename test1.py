from itertools import chain
import urllib.request
import json


def main():
    # get input
    input_id = input('type search id: ')
    # get friend list
    friendList = showFriend(input_id)
    # get friends' friends, chain function to flat list
    friendList.extend(list(chain.from_iterable([showFriend(x) for x in friendList])))
    # print name list
    print([showName(x) for x in friendList])

# return name by id
def showName(search_id):
    return request(search_id)['name']

# return friend list by id
def showFriend(search_id):
    return request(search_id)['friends']


def request(search_id):
    URL = 'http://fg-69c8cbcd.herokuapp.com/user/'
    response = urllib.request.urlopen(URL + str(search_id))
    data = json.loads(response.read().decode('utf-8'))
    return data


if __name__ == "__main__":
    main()