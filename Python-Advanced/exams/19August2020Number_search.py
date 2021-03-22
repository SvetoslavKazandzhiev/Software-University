def find_missing(args):
    return [x for x in range(min(args), max(args) + 1)
            if x not in args]


def sorting_numbers(args):
    args = sorted(set([x for x in args if args.count(x) > 1]))
    return args


def numbers_searching(*args):
    missing = find_missing(args)[0]
    sorting = sorting_numbers(args)
    return [missing, sorting]



print(numbers_searching(1, 2, 4, 2, 5, 4))
print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))
print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))