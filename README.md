[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/EU06KJG-)

# MazeProblem

## Objective

Your task is to implement an algorithm that finds the shortest path from the start to the exit in a maze in the **MazeProblem.py** file included in the repo.

## Maze Representation

The maze is given as a 2D matrix of integers:

```python
maze = [
  [1, 1, 1, 1, 1],
  [1, 0, 0, 1, 1],
  [1, 1, 0, 1, 1],
  [1, 1, 0, 0, 0],
  [1, 1, 1, 1, 1],
```

- 1 represents a valid cell (walkable)

- 0 represents a wall (blocked)

- The start point is at the top-left corner (0, 0)

- The destination is the bottom-right corner (n-1, n-1)


## Goal

Your algorithm should find the **shortest path from the start to the destination** and return the path as a new matrix where:

- Each step in the path is marked with S
- All other cells can remain as - or unchanged

### Example output:
```
[
  [S, -, -, -, -],
  [S, -, -, -, -],
  [S, -, -, -, -],
  [S, -, -, -, -],
  [S, S, S, S, S],
]
```

### Requirements

  - Implement the solution using BFS or DFS

  - Clearly mark the path found

  - Your code must solve the 4 examples included in the ****MazeProblem.py file

  - Keep your code modular and readable


### Resource
You can follow the link bellow to set your SSH keys to your github account:
https://www.theserverside.com/blog/Coffee-Talk-Java-News-Stories-and-Opinions/GitHub-SSH-Windows-Example 
