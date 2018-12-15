import sys


def get_freq_after_input(l):
    return sum([int(x) for x in l])


def get_repeated_freq(l):
    frequencies = set()
    current = 0
    repeated = None
    while repeated is None:
        for l in lines:
            current += int(l)
            if repeated is None and current in frequencies:
                repeated = current
                break
            frequencies.add(current)
    return repeated

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('One argument require: path to input file')
        exit(1)

    path = sys.argv[1]

    with open(path, 'rb') as fd:
        lines = fd.readlines()

    print('Frequency after input sequence: ' + str(get_freq_after_input(lines)))
    print('First repeated frequency: ' + str(get_repeated_freq(lines)))
