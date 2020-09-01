from collections import defaultdict

for case in range(int(input())):
    network = defaultdict(list)

    num_recipients = int(input())

    first_recipient = input()
    prev_recipient = first_recipient
    cur_recipient = first_recipient

    for recipient in range(num_recipients - 1):
        prev_recipient = cur_recipient
        cur_recipient = input()

        if not prev_recipient in network[cur_recipient]:
            network[prev_recipient].append(cur_recipient)

    if first_recipient != cur_recipient:
        network[first_recipient].remove(cur_recipient)
        network[cur_recipient].append(first_recipient)

    time = 0
    queue = [[recipient, 10] for recipient in network[cur_recipient]]
    while queue:
        recipient, cur_time = queue.pop(0)
        if cur_time > time:
            time = cur_time

        for other_recipient in network[recipient]:
            queue.append([other_recipient, time + 10])

    print(num_recipients * 10 - time * 2)
