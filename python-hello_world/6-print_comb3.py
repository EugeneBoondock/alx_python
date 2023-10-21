output = ""
for i in range(10):
    for j in range(i + 1, 10):
        output += "{:02d}, ".format(i * 10 + j) if i != 0 else "{:d}{:d}, ".format(i, j)
print(output[:-2])
