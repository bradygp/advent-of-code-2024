import time

def parse(filename):
    f = open("data.txt", "rt")
    left = []
    right = []
    for line in f.readlines():
        tmp = line.split()
        left.append(int(tmp[0]))
        right.append(int(tmp[1]))
    left.sort()
    right.sort()
    return zip(left,right)

def compare(pairs):
    difference = 0
    for pair in parse('data.txt'):
        difference += abs(pair[0] - pair[1])
    return difference

def main():
    pairs = parse('data.txt')
    diff = compare(pairs)
    print(diff)

if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (round(time.time() - start_time,4)))