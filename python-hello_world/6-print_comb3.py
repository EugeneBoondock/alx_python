for i in range(10):
    for j in range(i + 1, 10):
        print(f"{i}{j:02}" if i != 0 else f"{i}{j}", end=", " if i != 8 else "\n")
