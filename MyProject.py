def bubble_sort(data):
    n = len(data)

    for i in range(n):
        # Last i elements are already sorted, so we don't need to check them
        for j in range(0, n-i-1):
            # Swap if the element found is greater than the next element
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]

# Example usage with a dataset of 30 numbers
dataset = [64, 34, 25, 12, 22, 11, 90, 88, 73, 66, 44, 19, 84, 38, 97, 45, 52, 63, 71, 10, 5, 29, 82, 16, 42, 60, 78, 54, 31, 70]

bubble_sort(dataset)

print("Sorted dataset:", dataset)
