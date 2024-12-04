import time, re

def parse(filename):
    f = open(filename, "rt")
    return f.read()

def identify_records(file):
    matches = re.findall(r'mul\(\d{1,3},\d{1,3}\)', file)
    return matches

def multiply(record):
    matches = re.findall(r'\d{1,3}', record)
    return int(matches[0]) * int(matches[1])

def clean(file):
    cleaned = re.sub(r'don\'t\(\).*do\(\)', '', file)
    return cleaned

def main():
    safe_reports = 0
    file = parse('data.txt')
    cleaned = clean(file)
    records = identify_records(cleaned)
    sum = 0
    for r in records:
        sum += multiply(r)
    print("Multiplication Sum: %s" % (sum))    
    

if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (round(time.time() - start_time,4)))