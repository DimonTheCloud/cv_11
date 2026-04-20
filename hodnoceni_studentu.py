from sorting import random_numbers


class HodnoceniStudentu:
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
















