sheet = []

for i in range(10):
    hold = input()
    hold = hold.split(" ")
    sheet.append(hold)



def location(value):
    spot = value[0]
    if spot == "A":
        spot = 0
    elif spot == "B":
        spot = 1
    elif spot == "C":
        spot = 2
    elif spot == "D":
        spot = 3
    elif spot == "E":
        spot = 4
    elif spot == "F":
        spot = 5
    elif spot == "G":
        spot = 6
    elif spot == "H":
        spot = 7
    elif spot == "I":
        spot = 8
    else:
        spot = 9
    return [spot, int(value[1])]

def receive(directions):
    send = location(directions)
    send = sheet[send[0]][send[1]-1]
#    print(send)
    if send[0].isalpha() is True:
        return False
    return send

def add_cell(value):
    look = list(value)
    cells = look.count("+") + 1
    command = 0
    for i in range(cells):
        result = receive(value[i*3:i*3+2])
        if result is False:
            return False
        command += int(result)
    return command
count = 1
while count != 0:
    count = 0
    for i in range(len(sheet)):
        for x in range(len(sheet[i])):
            if sheet[i][x][0].isalpha() is True:
                run = add_cell(sheet[i][x])
#                print(run)
                if run is not False:

                    sheet[i][x] = str(run)
                    count += 1
#    print(count)
 #   print(sheet)

for i in range(len(sheet)):
    for x in range(len(sheet[i])):
        if sheet[i][x][0].isalpha() is True:
            sheet[i][x] = '*'

for i in sheet:
    print(*i, sep = " ")




