with open("unformatted.txt") as f:
    lines = f.read()
    lines = lines.replace('\n', ' ')
    for word in lines.split(" "):
        if (len(word) > 2):
            lines = lines.replace(word,"")
    print(lines)
    