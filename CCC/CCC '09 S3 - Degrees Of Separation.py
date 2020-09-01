from math import inf
network = {'1': ['6'], '2': ['6'], '3': ['4', '5', '6', '15'], '4': ['3', '5', '6'], '5': ['3', '4', '6'], '6': ['1', '2', '3', '4', '5', '7'], '7': ['6', '8'], '8': ['7', '9'], '9': ['8', '10', '12'], '10': ['9', '11'], '11': ['10', '12'], '12': ['9', '11', '13'], '13': ['12', '14', '15'], '14': ['13'], '15': ['3', '13'], '16': ['17', '18'], '17': ['16', '18'], '18': ['16', '17']}

while True:
    comm = input()
    if comm == 'i':
        user1, user2 = input(), input()
        if user1 not in network:
            network[user1] = []
        if user2 not in network:
            network[user2] = []
        if user1 not in network[user2]:
            network[user2].append(user1)
        if user2 not in network[user1]:
            network[user1].append(user2)

    if comm == 'd':
        user1, user2 = input(), input()
        if user1 in network[user2]:
            network[user2].remove(user1)
        if user2 in network[user1]:
            network[user1].remove(user2)

    if comm == 'n':
        user = input()
        print(len(network[user]))

    if comm == 'f':
        user = input()
        friends_friends = set()
        for friend in network[user]:
            for friend_friend in network[friend]:
                if not friend_friend in network[user]and friend_friend != user:
                    friends_friends.add(friend_friend)
        print(len(friends_friends))

    if comm == 's':
        user1, user2 = input(), input()
        min_sepr = {key: inf for key in network}
        queue = [(user1, 0)]
        while queue:
            cur_user, cur_sepr = queue.pop(0)
            if cur_sepr >= min_sepr[cur_user]:
                continue
            min_sepr[cur_user] = cur_sepr
            if cur_user == user2:
                break
            for oth_user in network[cur_user]:
                queue.append((oth_user, cur_sepr + 1))

        print("Not connected" if not user2 in min_sepr or min_sepr[user2] == inf else min_sepr[user2])

    if comm == 'q':
        break
