"""
1. Balanced Parentheses or Brackets
Problem: Check if a string of parentheses/brackets is balanced (e.g., {[()]} is balanced, but {[(])} is not).
Approach: Use a stack to keep track of opening brackets. When a closing bracket is encountered, check if it matches the top of the stack.
Key Operations: Push for opening brackets, pop and compare for closing brackets.
2. Evaluate Postfix Expressions
Problem: Evaluate mathematical expressions written in postfix (Reverse Polish Notation), e.g., 231*+9-.
Approach: Use a stack to store operands. For every operator, pop two operands, apply the operator, and push the result back.
Key Operations: Push operands, pop operands for operators, push the result.
3. Convert Infix to Postfix/Prefix
Problem: Convert an infix expression (e.g., A + B * C) to postfix (e.g., A B C * +) or prefix (e.g., + A * B C).
Approach: Use a stack to manage operators, respecting operator precedence and associativity.
4. Next Greater Element
Problem: Given an array, find the next greater element for each element. If no greater element exists, return -1.
Approach: Traverse the array from right to left. Use a stack to keep track of potential next greater elements.
Key Operations: Push elements, pop smaller elements, and compare.
5. Stock Span Problem
Problem: For each day, find the number of consecutive days the stock price was less than or equal to the current day's price.
Approach: Use a stack to store indices of days. Pop indices of days with smaller prices while iterating through the array.
Key Operations: Push and pop based on comparison.
6. Largest Rectangle in Histogram
Problem: Find the largest rectangular area in a histogram represented by an array of heights.
Approach: Use a stack to keep track of bars. For each bar, calculate areas with the bars popped from the stack as the smallest (or minimum height) bar.
Key Operations: Push bar indices, pop and calculate areas.
7. Design a Min Stack
Problem: Implement a stack that supports push, pop, top, and retrieving the minimum element in constant time.
Approach: Use an auxiliary stack to keep track of the minimum value at each state.
Key Operations: Maintain two stacks (main and min).
8. Check for Palindrome Using Stack
Problem: Check if a string is a palindrome.
Approach: Push the first half of the string onto a stack, then compare the stack's contents with the second half.
Key Operations: Push characters, pop and compare.
9. Depth-First Search (DFS)
Problem: Traverse a graph using Depth-First Search without recursion.
Approach: Use a stack to keep track of the vertices to visit.
Key Operations: Push and pop vertices as you explore.
10. Sort a Stack
Problem: Sort a stack without using an additional data structure.
Approach: Use recursion or an auxiliary stack to reorder elements.
Key Operations: Push and pop elements with comparisons.
11. Celebrity Problem
Problem: In a party of n people, find the celebrity (a person who is known by everyone but knows no one).
Approach: Use a stack to compare pairs of people and narrow down the potential celebrity.
Key Operations: Push candidates, pop and compare.
12. Trapping Rain Water
Problem: Given an array of heights, find the amount of water that can be trapped between the bars.
Approach: Use a stack to track the indices of the bars and calculate water trapped as you iterate.
Key Operations: Push bar indices, pop and calculate trapped water.
13. Undo/Redo Operations
Problem: Implement undo and redo functionality in a text editor.
Approach: Use two stacks, one for the undo operations and another for redo operations.
Key Operations: Push commands, pop for undo, and push into redo stack.
14. Flatten Nested List Iterator
Problem: Given a nested list, implement an iterator to flatten it.
Approach: Use a stack to store the nested list and process elements in a controlled order.
Key Operations: Push sublists, pop and yield values.
15. Binary Tree Traversals
Problem: Implement non-recursive inorder, preorder, or postorder traversal of a binary tree.
Approach: Use a stack to keep track of nodes during traversal.
Key Operations: Push and pop nodes.
"""