import time, collections

def parse_levels(filename):
    f = open(filename, "rt")
    out = []
    for report in f.readlines():
        levels = list(map(int,report.split()))
        out.append(levels)
    return out

def is_ordered(level):
    sort = sorted(level)
    sortr = sorted(level, reverse=True)
    if level == sort:
        return True
    if level == sortr:
        return True
    return False

def is_dampened_ordered(level):
    if is_ordered(level):
        return True
    i = 0
    while i < len(level):
        if is_ordered(level[:i] + level[i+1 :]):
            if has_jump_or_stale_dampened(level[:i] + level[i+1 :]):
                #print("Dampened level: %s" % (level))
                return True
            else:
                return False
        i += 1

def has_jump_or_stale_dampened(level):
    i = 0
    dampened = False
    while i < len(level) - 1:
        current = level[i]
        next = level[i+1]
        i = i + 1
        if is_jumping_or_stale(current, next):
            if dampened:
                return False
            else:
                dampened = True
                print("Dampened Report: %s" % (level))    
                continue
    if is_dampened_ordered(level):
        return True


def is_jumping_or_stale(left, right):
    diff = abs(left-right)
    # return true if the difference is higher than 3
    return (diff > 3) or (diff == 0)

def main():
    report = parse_levels('reports.txt')
    report[:] = [level for level in report if is_dampened_ordered(level)]
    report[:] = [level for level in report if has_jump_or_stale_dampened(level)]
    print("Number of Safe Reports: %s" % (len(report)))
    #for level in report:
    #    print(level)  
    

if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (round(time.time() - start_time,4)))