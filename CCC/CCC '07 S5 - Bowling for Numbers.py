input = __import__('sys').stdin.readline

for _ in range(int(input())):
    num_pins, num_balls, width = [int(data) for data in input().split()]
    pins = [int(input()) for _ in range(num_pins)]

    sums = [sum(pins[idx: idx + width]) for idx in range(num_pins)]
    dp = [[0] * num_pins for _ in range(num_balls + 1)]

    for ball in range(1, num_balls + 1):
        for pin in reversed(range(num_pins)):
            if pin >= num_pins - width:
                dp[ball][pin] = sums[pin]
            else:
                dp[ball][pin] = max(dp[ball - 1][pin + width] + sums[pin],
                                    dp[ball][pin + 1])

    print(dp[-1][0])
