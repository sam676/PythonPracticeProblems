"""
Compute the length of single-link list without a cycle.

A pointer is called a linked list if:

it is an empty pointer (it is then called a terminator or an empty list); or
it points to a structure (called a node or the head) that contains a value and a linked list (called the tail).
The length of a list is defined as the total number of nodes it contains. In particular, an empty list has length 0.

For example, consider the following linked list:

  A -> B -> C -> D ->
This list contains four nodes: A, B, C and D. Node D is the last node and its tail is the terminator. The length of this list is 4.

Assume that the following declarations are given:

class IntList(object):
  value = 0
  next = None

Write a function:

def solution(L)

that, given a non-empty linked list L consisting of N nodes, returns its length.

For example, given list L shown in the example above, the function should return 4.

Assume that:

N is an integer within the range [1..5,000];
list L does not have a cycle (each non-empty pointer points to a different structure).
In your solution, focus on correctness. The performance of your solution will not be the focus of the assessment.

"""


def solution(L):
    count = 0
    while L:
        count += 1
        L = L.next
    return count
