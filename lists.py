"""SKILLS: LISTS

Complete the following functions.
"""


def print_indices(items):
    """Print each item in the list, followed by its index.

    Do this without using a "counting variable" --- in other words,
    DON'T do this:

        >>> count = 0
        >>> for item in list:
        ...     print(count)
        ...     count = count + 1
        ...

    The output should look like this:

        >>> print_indices(['apple', 'berry', 'cherry'])
        apple 0
        berry 1
        cherry 2
    """

    for index in range(len(items)):
        item = items[index]
        
        print(f'{item} {index}')


def words_in_common(words1, words2):
    """Return words that are shared between `words1` and `words2`.

    The returned words are sorted alphabetically.

    NOTE: For this problem, feel free to use other data structures we've
    learned about in this class.

    For example:

        >>> words_in_common(
        ...     ['Python', 'Python', 'Python'],
        ...     ['Lizard', 'Turtle', 'Python']
        ... )
        ['Python']

    The returned list should not have any duplicates:

        >>> words_in_common(
        ...     ['cheese', 'cheese', 'cheese', 'cake'],
        ...     ['cheese', 'hummus', 'beets', 'cake']
        ... )
        ['cake', 'cheese']

    If there are no words in common, return an empty list:

        >>> words_in_common(
        ...     ['lamb', 'chili', 'cheese'],
        ...     ['cake', 'ice cream']
        ... )
        []
    """

    # Convert each input list into a set
    words1_set = set(words1)
    words2_set = set(words2)
    
    #Take the intersection of the sets
    intersection = words1_set & words2_set

    #Save the intersection as a list
    intersection_list = list(intersection)

    #Sort the list
    intersection_sorted = sorted(intersection_list)

    return intersection_sorted


def every_other_item(items):
    """Return every other item in `items`, starting at first item.

    For example:

       >>> every_other_item(['a', 400, True, 'b', 0])
       ['a', True, 0]
    """

    return items[::2]


def smallest_n_items(items, n):
    """Return the `n` smallest integers in list in descending order.

    You can assume that `n` will be less than the length of the list.

    For example:

        >>> smallest_n_items([2, 6006, 700, 42, 6, 59], 3)
        [42, 6, 2]

    If `n` is 0, return an empty list:

        >>> smallest_n_items([3, 4, 5], 0)
        []

    Duplicates are OK:

        >>> smallest_n_items([1, 1, 1, 1, 1, 1], 2)
        [1, 1]
    """

    return []


"""Developer test code is below."""

fruits = ['apple', 'cherry', 'berry']
#print_indices(fruits)

fav_foods = ['berry', 'cherry', 'whipped cream']

#intersection_output = words_in_common(fruits, fav_foods)
#print(intersection_output)

long_list = fruits + fav_foods + [1, 2, 3, 4, 5, 6]
#print(long_list)

#every_other_output = every_other_item(long_list)
#print(every_other_output)