import time, collections

def identify_safe_reports(filename):
    f = open(filename, "rt")
    count = 0
    for report in f.readlines():
        levels = report.split()
        i = 0
        while i < len(levels):
            try:
                current = int(levels[i])
                next = int(levels[i+1])
                i = i + 1
                if is_jumping_or_stale(current, next):
                    break
            except IndexError:
                if is_ordered(list(map(int, report.split()))):
                    count += 1
                break
    return count

def is_jumping_or_stale(left, right):
    diff = abs(left-right)
    # return true if the difference is higher than 3
    return (diff > 3) or (diff == 0)
    
def is_ordered(report):
    sort = sorted(report)
    sortr = sorted(report, reverse=True)
    if report == sort:
        return True
    if report == sortr:
        return True
    return False

def main():
    safe_reports = identify_safe_reports('reports.txt')
    print("Number of Safe Reports: %s" % (safe_reports))    
    

if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (round(time.time() - start_time,4)))