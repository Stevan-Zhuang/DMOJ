import sys
input = sys.stdin.readline

freqs_readings = {}
for sensor in range(int(input())):
  reading = int(input())
  if not reading in freqs_readings:
    freqs_readings[reading] = 0
  freqs_readings[reading] += 1

freqs_readings = sorted([[freqs_readings[reading], reading]
                        for reading in freqs_readings],
                       reverse = True)

if freqs_readings[0][0] == freqs_readings[1][0]:
  print(freqs_readings[0][1] - min(reading for freq, reading in freqs_readings
                                   if freq == freqs_readings[0][0]))
else:
  if freqs_readings[1][0] == freqs_readings[2][0]:
    print(max(abs(freqs_readings[0][1] - reading) for freq, reading in freqs_readings
              if freq == freqs_readings[1][0]))
  else:
    print(abs(freqs_readings[0][1] - freqs_readings[1][1]))
