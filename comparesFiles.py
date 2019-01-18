IDENTICAL = -1

def singleline_diff(line1, line2):
    if len(line1) < len(line2):
        shorter = line1
    else:
        shorter = line2

    for index in range(len(shorter)):
        if (line1[index] != line2[index]):
            return index

    if len(line1) == len(line2):
        return IDENTICAL
    else:
        return len(shorter)

def singleline_diff_format(line1, line2, index):
    if "\r" in line1 or "\n" in line1 or "\r" in line2 or "\n" in line2:
        return ""
    if index > min(len(line1), len(line2)):
        return ""

    separator = "="*index + "^"

    return line1 + "\n" + separator + "\n" + line2


def multiline_diff(lines1, lines2):
    if len(lines1) < len(lines2):
        shorter = lines1
    else:
        shorter = lines2

    for index in range(len(shorter)):
        pos = singleline_diff(lines1[index], lines2[index])
        if pos != IDENTICAL:
            return (index, pos)

    if len(lines1) == len(lines2):
        return (IDENTICAL, IDENTICAL)
    else:
        return (len(shorter), 0)

def get_file_lines(filename):
    file = open(filename, "rt")
    data = file.read()
    file.close()
    return data.split("\n")

def file_diff_format(filename1, filename2):
    lines1 = get_file_lines(filename1)
    lines2 = get_file_lines(filename2)
    tup = multiline_diff(lines1, lines2)
    line = tup[0]
    pos = tup[1]
    msg = "Line "

    if line != IDENTICAL:
        msg += str(line) + ":\n"
        msg += singleline_diff_format(lines1[line], lines2[line], pos)
        return msg
    else:
        return "No differences\n"


diff = file_diff_format("himno_nacional.txt", "himno2.txt")
print(diff)

#print(singleline_diff_format("ni se tiñe con sangre de hermanos", "ni se tiñe con sangre de ermanos", 10))

lines1 = get_file_lines("himno2.txt")
print(lines1)
# print(singleline_diff("hola mundo", "hola mundo"))
# print(singleline_diff("hola mundo", "hola mundo!"))
# print(singleline_diff("holax mundo", "hola mundo"))
# print(singleline_diff("hola mundo", "hola mund"))

#print(singleline_diff_format("hola mundo", "hola mundo!", 15))

#lines1 = ["hello", "world", "!"]
#lines2 = ["hello", "world", "!"]
#tup = multiline_diff(lines1, lines2)
#print(tup)
