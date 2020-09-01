while True:
  u_input = int(input())
  if u_input == 99:
    stream = int(input()) - 1
    percent = int(input()) / 100
    streams[stream: stream + 1] = [round(streams[stream] * percent),
                                   round(streams[stream] * (1 - percent))]
  elif u_input == 88:
    stream = int(input()) - 1
    streams[stream: stream + 2] = [streams[stream] + streams[stream + 1]]
  elif u_input == 77:
    break

print(" ".join(str(flow) for flow in streams))
