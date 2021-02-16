def top3(count):
    tier = list()
    for c in count:
        tier.append((c, count[c]["number"]))
    tier.sort(key=lambda tup: tup[1])
    print("TOP 3 - ", end="")
    print(tier[-1][0], end=" ")
    if len(tier) > 1:
        print(tier[-2][0], end=" ")
        if len(tier) > 2:
            print(tier[-3][0])
        else: print()
    else: print()

f = open("voters.txt", "r")
count = dict()
for line in f:
    if(line[-1]=="\n"):
        voter_id, candidate_id = map(int, line[:-1].split(','))
    else:
        voter_id, candidate_id = map(int, line[:].split(','))
    # print(voter_id, candidate_id)
    if candidate_id not in count:
        count[candidate_id] = dict()
        count[candidate_id]["number"] = 1
        count[candidate_id]["voters"] = [voter_id]
    else:
        if voter_id in count[candidate_id]["voters"]:
            print("FRAUD!!! %d voted more than 1 time" % (voter_id))
        else:
            count[candidate_id]["voters"].append(voter_id)
            count[candidate_id]["number"] += 1
    top3(count)