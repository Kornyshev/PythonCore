import collections
import itertools
import os
import sys


# Example using os module
def explore_os():
    print("Current working directory:", os.getcwd())
    print("List of files and directories in the current directory:", os.listdir('.'))
    print("Environment variables:", os.environ.get('HOME'))  # example to get the HOME environment variable


# Example using sys module
def explore_sys():
    print("Python version information:", sys.version_info)
    print("Command line arguments passed to the script:", sys.argv)


# Example using collections module
def explore_collections():
    # Using namedtuple for more readable code
    Point = collections.namedtuple('Point', 'x y')
    p = Point(11, y=22)
    print("Namedtuple:", p.x, p.y)

    # Using Counter to count occurrences of elements
    cnt = collections.Counter('abracadabra')
    print("Counter:", cnt)
    print("Most common element:", cnt.most_common(1))


# Example using itertools module
def explore_itertools():
    # Infinite iterator: count
    for i in itertools.count(start=10, step=3):
        print("Count iterator:", i)
        if i > 20:
            break

    # Cycling through elements
    cycle_iter = itertools.cycle('ABCD')
    print("Cycle iterator:")
    for item in range(6):
        print(next(cycle_iter))

    # Combinations and permutations
    print("Combinations of ABC in groups of 2:", list(itertools.combinations('ABC', 2)))
    print("Permutations of ABC:", list(itertools.permutations('ABC')))


def main():
    print("OS Module Exploration:")
    explore_os()

    print("\nSYS Module Exploration:")
    explore_sys()

    print("\nCollections Module Exploration:")
    explore_collections()

    print("\nItertools Module Exploration:")
    explore_itertools()


if __name__ == "__main__":
    main()
