print((lambda text, string: "yes" if any(cyclic_shift in text for cyclic_shift in [string[idx:] + string[:idx] for idx in range(len(string))]) else "no")(input(), input()))
