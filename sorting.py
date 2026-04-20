import random
import matplotlib.pyplot as plt


def bubble_sort(numbers):
    n = len(numbers)

    for i in range(n):
        for j in range(n - 1 - i):
            plt.ion()
            plt.show()

            index_highlight1 = j
            index_highlight2 = j + 1
            colors = ["steelblue"] * len(numbers)
            colors[index_highlight1] = "tomato"
            colors[index_highlight2] = "tomato"
            plt.clf()
            plt.bar(range(len(numbers)), numbers, color=colors)
            plt.title("Bubble Sort")
            plt.pause(0.1)

            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

    return numbers





def selection_sort(my_list):
    n = len(my_list)

    for i in range(n):
        min_index = i

        for j in range(i + 1, n):
            if my_list[j] < my_list[min_index]:
                min_index = j

        my_list[i], my_list[min_index] = my_list[min_index], my_list[i]

    return my_list




def random_numbers(count, low=0, high=100):
    return [random.randint(low, high) for _ in range(count)]


