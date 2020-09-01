mother = input()
father = input()

for baby in range(int(input())):
  genes = input() 
  if all((genes[i].isupper()
          and (any(mother[i * 2 + j].isupper() for j in range(2))
            or any(father[i * 2 + j].isupper() for j in range(2))))
      or (genes[i].islower()
          and (any(mother[i * 2 + j].islower() for j in range(2))
          and  any(father[i * 2 + j].islower() for j in range(2))))
          for i in range(5)):
    print("Possible baby.")
  else:
    print("Not their baby!")
