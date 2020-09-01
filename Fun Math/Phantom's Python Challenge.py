(lambda N:(lambda P:[print(f"{i}{'*'if not i-2 in P or not i+2 in P else''}") for i in range(2,N) if not i in P])({0}|set(p for n in range(2,int(N**0.5)+1) for p in range(n*2,N,n))))(int(input()))
