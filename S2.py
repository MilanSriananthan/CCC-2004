contest = input()
contest = contest.split(" ")
people = int(contest[0])
rounds = int(contest[1])

def ranking(seq):
    new = seq.copy()
    final = []
    for i in range(len(seq)):
        save = new.index(max(new))
        final.append(save+1)
        new[save] = -100000007
    return final

def makenum(seq):
    for i in range(len(seq)):
        seq[i] = int(seq[i])
    return seq

all = input()
all = all.split(" ")
all = makenum(all)

grand = []
#print(all)
grand.append(ranking(all))
for i in range(rounds - 1):
#    print(all)
#    print(grand)
    hold = input()
    hold = hold.split(" ")
    hold = makenum(hold)
#    print(hold)
    for x in range(people):
        all[x] += hold[x]
    grand.append(ranking(all))

ties = all.count(max(all))
#print(all)
#print(ties)
score = max(all)
for x in range(ties):
    firstplace = grand[-1][x]
    losing = 0
    for i in grand:
        current = i.index(firstplace)
        if current > losing:
            losing = current

    print("Yodeller " + str(firstplace) + " is the TopYodeller: score " + str(score) + ", worst rank " + str(losing + 1))