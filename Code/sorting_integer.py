#!python


def counting_sort(numbers):
    """Sort given numbers (integers) by counting occurrences of each number,
    then looping over counts and copying that many numbers into output list.
    TODO: Running time: O(n+range) Why and under what conditions?
    where range is the differece between the minimum and maximum values in the list
    TODO: Memory usage: O(n) Why and under what conditions? we are creating a new 
    place in memory for each element in the list"""
    if len(numbers) == 0:
        return numbers
    # TODO: Find range of given numbers (minimum and maximum integer values)
    numbers_range = max(numbers) - min(numbers) + 1
    offset = min(numbers)
    # TODO: Create list of counts with a slot for each number in input range
    counts = [0 for _ in range(numbers_range)]
    # TODO: Loop over given numbers and increment each number's count
    for num in numbers:
        counts[num - offset] += 1
    # TODO: Loop over counts and append that many numbers into output list
    # FIXME: Improve this to mutate input instead of creating new output list
    output = []
    for index, value in enumerate(counts):
        for _ in range(value):
            output.append(index + offset)
    return output


def bucket_sort(numbers, num_buckets=10):
    """Sort given numbers by distributing into buckets representing subranges,
    then sorting each bucket and concatenating all buckets in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    if num_buckets <= 0:
        num_buckets = len(numbers)
    # TODO: Find range of given numbers (minimum and maximum values)
    # TODO: Create list of buckets to store numbers in subranges of input range
    buckets = [[] for _ in range(num_buckets + 1)]
    # TODO: Loop over given numbers and place each item in appropriate bucket
    maximum = max(numbers)
    for num in numbers:
        bucket_index = num * num_buckets // maximum
        buckets[bucket_index].append(num)
    # TODO: Sort each bucket using any sorting algorithm (recursive or another)
    for index, bucket in enumerate(buckets):
        buckets[index] = counting_sort(bucket)
    # TODO: Loop over buckets and append each bucket's numbers into output list
    # FIXME: Improve this to mutate input instead of creating new output list
    count = 0
    for bucket in buckets:
        for value in bucket:
            numbers[count] = value
            count += 1
    return numbers
