import sys

def parse_string(input_string):
    lines = input_string.strip().split('\n')
    for line in lines:
        if 'hold' in line:
            words = line.split()
            if len(words) > 1:
                return words[1]
    return None

if __name__ == "__main__":
    input_string = sys.argv[1]
    result = parse_string(input_string)
    if result:
        print(result)
    else:
        print("No 'hold' line found or not enough words in the line.")
