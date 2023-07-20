combinations = []
for i in range(10):
    for j in range(i + 1, 10):
        combinations.append("{:02}".format(i * 10 + j))
print(", ".join(combinations))
