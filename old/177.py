dictionary = input().lower().split()
dictionary_s = ["".join(sorted(list(i))) for i in dictionary]
text = input().lower().split()
mass = []
for i in text:
    if any([sorted(list(i)) == sorted(list(w)) and i != w for w in dictionary]):
        if "".join(sorted(list(i))) in dictionary_s:
            mass.append("".join(["#" for r in range(len(i))]))
        else:
            mass.append(i)
    else:
        mass.append(i)
print(" ".join(mass))
