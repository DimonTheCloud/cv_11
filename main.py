from hodnoceni_studentu import HodnoceniStudentu
from sorting import random_numbers

def main():
    results = HodnoceniStudentu([85, 42, 91, 67, 50, 73, 100, 38, 58])

    print(results.count())

    for i in range(results.count()):
        print(f"Student {i}: {results.get_by_index(i)} points - {results.get_grade(i)}")

    print(results.find(100))
    print(results.get_sorted())
    print(results.scores)

    print(results.find_sorted(91))
    print(results.find_sorted(50))
    print(results.find_sorted(77))

    random_results = HodnoceniStudentu(random_numbers(30, 0, 100))
    print(random_results.count())
    print(random_results.get_sorted())

if __name__ == "__main__":
    main()