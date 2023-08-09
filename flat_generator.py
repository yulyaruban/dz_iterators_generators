import types


def flat_generator(list_of_lists):
    lists = iter(list_of_lists)
    new = []
    for i in lists:
        new += i
    for el in new:
        if new == []:
            break
        yield (el)
    

list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]
def test_2():

    # list_of_lists_1 = [
    #     ['a', 'b', 'c'],
    #     ['d', 'e', 'f', 'h', False],
    #     [1, 2, None]
    # ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)


if __name__ == '__main__':
    test_2()
    el = [el for el in flat_generator(list_of_lists_1)]
    print(el)




