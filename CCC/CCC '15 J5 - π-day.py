num_pie = int(input())
num_people = int(input())

cache = {}
def pie_day(pie_left, people_left, min_give = 1):
    if (pie_left, people_left, min_give) in cache:
        return cache[(pie_left, people_left, min_give)]

    if people_left == 1:
        return int(pie_left >= min_give)

    max_give = pie_left // people_left + 1
    result = sum(pie_day(pie_left - i, people_left - 1, max(min_give, i)) for i in range(min_give, max_give))
    cache[(pie_left, people_left, min_give)] = result
    return result

print(pie_day(num_pie, num_people))
