import time, collections

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
    counter = collections.Counter(right)

    return zip(left,right), left, counter

def compare(pairs):
    difference = 0
    for left, right in pairs:
        difference += abs(left - right)
    return difference

def similarity(left, right_count):
    similarity = 0
    for id in left:
        similarity += (id * right_count[id])
    return similarity
    

def main():
    pairs, left, right_count = parse('data.txt')
    diff = compare(pairs)
    similar = similarity(left, right_count)
    print("Difference: %s" % (diff))
    print("Similarity: %s" % (similar))
    
    

if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (round(time.time() - start_time,4)))