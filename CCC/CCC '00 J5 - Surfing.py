links_here = []
links_there = []
page_num = int(input())
for page in range(page_num):
  here = input()
  while True:
    line = input()
    while '<A HREF="' in line:
      start = line.find('<A HREF="')
      end = line[start:].find('">') + start
      there = line[start + 9: end]
      line = line[end + 2:]
      print("Link from", here, "to", there)
      links_here.append(here)
      links_there.append(there)
    if '</HTML>' in line:
      break

while True:
  here = input()
  if here == "The End":
    break
  there = input()
  can_surf = False
  checked_links = []
  links = [here]
  for link in links:
    for i in range(len(links_here)):
      if link == links_here[i] and not i in checked_links:
        checked_links.append(i)
        if there == links_there[i]:
          can_surf = True
          break
        links.append(links_there[i])

  if can_surf:
    print("Can surf from {} to {}.".format(here, there))
  else:
    print("Can't surf from {} to {}.".format(here, there))
