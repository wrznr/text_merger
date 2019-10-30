
def lines(stream):
    lines = []
    for line in stream:
        text = []
        word = ""
        line = line.strip()
        if line:
            for c in line:
                if not c or c == " ":
                    if len(word) > 0:
                        text.append(word)
                    word = u""
                    continue
                word += c
            if word:
                text.append(word)
            lines.append(text)
    return lines
