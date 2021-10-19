# Task 1

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

-----
# Task 2

Write a function:
```py
def solution(A, B)
```
that, given two non-negative integers A and B, returns the number of bits set to 1 in the binary representation of the number A * B.

For example, given A = 3 and B = 7 the function should return 3, because the binary representation of A * B = 3 * 7 = 21 is `10101` and it contains three bits set to 1.

Assume that:
- A and B are integers within the range [0 .. 100,000,000].

In your solution, focus on **correctness**. The performance of your solution will not be the focus of the assessment.

## Code Template
```py
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, B):
    # write your code in Python 3.6
    pass

```

## Test Data
System defined:
- (3, 7)

-------
# Task 3

You are given two tables, `players` and `matches`, with the following structure:
```sql
create table players (
    player_id integer not null unique,
    group_id integer not null
);

create table matches (
    match_id integer not null unique,
    first_player integer not null,
    second_player integer not null,
    first_score integer not null,
    second_score integer not null
);
```

Each record in the table `players` represents a single player in the tournament. The column `player_id` contains the ID of each player. The column `group_id` contains the ID of the group that each player belongs to.

Each record in the table `matches` represents a single match in the group stage. The column `first_player (second_player)` contains the ID of the first player (second player) in each match. The column `first_score(second_score)` contains the number of points scored by the first player (second player) in each match. You may assume that, in each match, players belong to the same group.

You would like to compute the winner in each group. The winner in each group is the player who scored the maximum total number of points within the group. If there is more than one such player, the winner is the one with the lowest ID.

Write an SQL query that returns a table containing the winner of each group. Each record should contain the ID of the group and the ID of the winner in this group. Records should be ordered by increasing ID number of the group.

For example, given:

`players`:

| player_id | group_id |
|-----------|----------|
| 20        | 2        |
| 30        | 1        |
| 40        | 3        |
| 45        | 1        |
| 50        | 2        |
| 65        | 1        |

`matches`:

| match_id | first_player | second_player | first_score | second_score |
|----------|--------------|---------------|-------------|--------------|
| 1        | 30           | 45            | 10          | 12           |
| 2        | 20           | 50            | 5           | 5            |
| 13       | 65           | 45            | 10          | 10           |
| 5        | 30           | 65            | 3           | 15           |
| 42       | 45           | 65            | 8           | 4            |

your query should return:

| group_id | winner_id |
|----------|-----------|
| 1        | 45        |
| 2        | 20        |
| 3        | 40        |

In group 1 the winner is player 45 with the total score of 30 points. In group 2 both players scored 5 points, but player 20 has lower ID and is a winner. In group 3 there is only one player, and although she didn't play any matches, she is a winner.

Assume that:
- groups are numbered with consecutive integers beginning from 1;
- every player from table `matches` occurs in table `players`;
- in each match players belong to the same group;
- score is a value between 0 and 1000000;
- there is at most 100 players;
- there is at most 100 matches;

## Code Template
```sql
-- write your code in PostgreSQL 9.4
SELECT ...

```

## Test Data
```
insert into players values(20, 2);
insert into players values(30, 1);
insert into players values(40, 3);
insert into players values(45, 1);
insert into players values(50, 2);
insert into players values(65, 1);
insert into matches values(1, 30, 45, 10, 12);
insert into matches values(2, 20, 50, 5, 5);
insert into matches values(13, 65, 45, 10, 10);
insert into matches values(5, 30, 65, 3, 15);
insert into matches values(42, 45, 65, 8, 4);
```
