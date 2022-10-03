def solution(numbers, A, B):
    """

    >>> solution(2, [5, 6], [0,0,1,0])
    (30, 30)
    """
    global results
    results = []
    strings = str(A[0])
    remaining = A[1:]
    num_to_exec = {0: '+', 1: '-', 2: '*', 3: '/'}

    def find_next(remains, remain_exec, strings):
        bool_exec = list(map(bool, remain_exec))
        # breakpoint()
        if len(remains):
            for num, ele in enumerate(bool_exec):
                if ele:
                    string_to_exec = strings + num_to_exec[num] + str(remains[0])
                    remain_exec[num] -= 1
                    find_next(remains[1:], remain_exec, str(eval(string_to_exec)))
                    remain_exec[num] += 1

        else:
            results.append(eval(strings))

    find_next(remaining, B, strings)
    return max(results), min(results)


if __name__ == '__main__':
    numbers = input()
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    solution(numbers, A, B)
