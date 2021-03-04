# task 5.44 page 27


def counter(A):
    '''counter how many numbers in list are greater than the adjacent numbers'''
    count = 0
    N = len(A)
    for i in range(N):
        if A[i - 1] < A[i] and A[i + 1] < A[i]:
            count += 1
    return count

def counter_test(count):
    '''preventive testing'''
    print('Testing', counter.__doc__)
    print('Testcase #1:', end=' ')
    A = [1, 2, 1, 44, 5, 1, 0]
    answer = 2
    count(A)
    print('Passed!' if count(A) == answer else 'Fail')

    print('Testcase #2:', end=' ')
    A = [1, 2, 1, 44, 5, 6, 0, 1, 0, 2, 5, 99, 1]
    answer = 5
    count(A)
    print('Passed!' if count(A) == answer else 'Fail')

    print('Testcase #3:', end=' ')
    A = [0, 0, 0, 0, 0, 0, 0]
    answer = 0
    count(A)
    print('Passed!' if count(A) == answer else 'Fail')

counter_test(counter)