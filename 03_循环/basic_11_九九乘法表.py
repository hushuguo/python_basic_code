i = 0
k = 0
while i < 9:
    i += 1
    j = 0
    while j < i:
        j += 1
        k = i * j
        print("%d * %d = %d" % (j, i, k),  end="\t")
    print("")
