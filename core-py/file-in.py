import sys


def read_series1(filename):
    try:
        f = open(filename, mode='rt', encoding='utf-8')
        return [int(line.strip()) for line in f]
    finally:
        f.close()


def read_series(filename):
    with open(filename, mode='rt', encoding='utf-8') as f:
        return [int(line.strip()) for line in f]


def main(filename):
    series = read_series(filename)
    print(series)


def _int32_to_bytes(i):
    return bytes((i & 0xff,
                  i >> 8 & 0xff,
                  i >> 16 & 0xff,
                  i >> 24 & 0xff))


# ran from the cli the command would look like:
# $
if __name__ == '__main__':
    main(sys.argv[1])
