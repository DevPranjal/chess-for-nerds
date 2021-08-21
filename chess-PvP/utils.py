def parse_position(pos):
    if pos == "out":
        return (-1, -1)
    if pos == None:
        return (None, None)

    x = ord(pos[0])
    y = ord(pos[1])
    return 56 - y, x - 97
