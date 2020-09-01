start_day, days = [int(num) for num in input().split()]
calendar = [[] for row in range(6)]

week = -1
print("Sun Mon Tue Wed Thr Fri Sat")
for day in range(days + start_day - 1):
  date = day - start_day + 2
  if day % 7 == 0: week += 1
  if date < 1: calendar[week].append("   ")
  else: calendar[week].append("{:>3}".format(date))

print("\n".join(" ".join(row) for row in calendar
                if not all(day == "   " for day in row)))
