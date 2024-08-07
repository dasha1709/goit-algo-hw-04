import sys
from pathlib import Path
from log import log_file, log_folger


def main():

    p = Path(sys.argv[1])
    for path in p.rglob('*'):
        if path.is_dir():
            print(log_folger(path))
        else:
            print(log_file(path))

if __name__ == "__main__":
    main()