The binary representation of a 30-bit unsigned integer Q is denoted by the sequence [Q[29], Q[28], ..., Q[2], Q[1], Q[0]], where Q[29] corresponds to the most significant bit of Q. Leading zeros may appear.

A 30-bit unsigned integer N is given. The *right cyclic shift of N by one bit* is the 30-bit unsigned integer whose binary representation is [N[0], N[29], N[28], ..., N[2], N[1]]. A *right cyclic shift of N by K bits* is the result of performing a right cyclic shift of N by one bit K times.

For example:
- the right cyclic shift of 9,736 by one bit is 4,868;
- the right cyclic shift of 9,736 by two bits is 2,434;
- the right cyclic shift of 9,736 by three bits is 1,217;
- the right cyclic shift of 9,736 by five bits is 268,435,760;
- the right cyclic shift of 9,736 by eleven bits is 809,500,676;

The number 809,500,676 is the largest value that can be obtained by performing a right cyclic shift of 9,736.

You are give an implementation of a function:
```py
def solution(N)
```
that, given a 30-bit unsigned integer N, returns any integer K such that the right cyclic shift of N by K bits yields the largest possible value. If there are several integers K fulfilling this condition, the function may return any of them.

For example, given N = 9,736, the function may return 11, as explained above.

The attached code is still **incorrect** for some inputs. Despite the error(s), the code may produce a correct answer for the example test cases. The goal of the exercise is to find and fix the bug(s) in the implementation. You can modify at most **two** lines.

Assume that:
- N is an integer within the range [0 .. 1,073,741,823].

In your solution, focus on **correctness**. The performance of your solution will not be the focus of the assessment.

## Code Template
```py
def solution(N):
    largest = 0
    shift = 0
    temp = N
    for i in range(1, 30):
        index = (temp & 1)
        temp = (temp >> 1) | (index << 29)
        if (temp > largest):
            largest = temp
            shift = i
    return shift
```

## Test Data
System defined:
- 9736
