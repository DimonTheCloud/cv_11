from sorting import random_numbers


class StudentsGrades:
    def __init__(self, scores):
        self.scores = scores
        self._sorted_scores = None

    def get_by_index(self, index):
        return self.scores[index]

    def count(self):
        return len(self.scores)

    def get_grade(self, index):
        score = self.scores[index]

        if score >= 90:
            return "A"
        elif score >= 80:
            return "B"
        elif score >= 70:
            return "C"
        elif score >= 60:
            return "D"
        elif score >= 50:
            return "E"
        else:
            return "F"

    def find(self, points):
        result = []

        for i in range(len(self.scores)):
            if self.scores[i] == points:
                result.append(i)

        return result

    def get_sorted(self):
        scores = self.scores.copy()
        n = len(scores)

        for i in range(n):
            for j in range(n - 1 - i):
                if scores[j] > scores[j + 1]:
                    scores[j], scores[j + 1] = scores[j + 1], scores[j]

        return scores

    def find_sorted(self, score):
        if self._sorted_scores is None:
            print("sorting...")
            self._sorted_scores = self.get_sorted()

        left = 0
        right = len(self._sorted_scores) - 1

        while left <= right:
            middle = (left + right) // 2
            current = self._sorted_scores[middle]

            if current == score:
                return middle
            elif current < score:
                left = middle + 1
            else:
                right = middle - 1

        return None


def main():
    results = StudentsGrades([85, 42, 91, 67, 50, 73, 100, 38, 58])

    print(results.count())

    for i in range(results.count()):
        print(f"Student {i}: {results.get_by_index(i)} points - {results.get_grade(i)}")

    print(results.find(100))
    print(results.get_sorted())
    print(results.scores)

    print(results.find_sorted(91))
    print(results.find_sorted(50))
    print(results.find_sorted(77))

    random_results = StudentsGrades(random_numbers(30, 0, 100))
    print(random_results.count())
    print(random_results.get_sorted())


if __name__ == "__main__":
    main()












