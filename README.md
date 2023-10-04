``` python
from random import sample
from solver import *
```
### Generate a sudoku game
``` python
solution = full_grid()
show(solution)
```

```
     3  8  2 | 6  5  4 | 1  7  9 
     9  7  4 | 3  2  1 | 6  8  5 
     5  6  1 | 9  7  8 | 4  2  3 
    ---------+---------+---------
     7  4  8 | 1  9  3 | 2  5  6 
     2  9  6 | 4  8  5 | 7  3  1 
     1  3  5 | 7  6  2 | 8  9  4 
    ---------+---------+---------
     6  2  7 | 5  4  9 | 3  1  8 
     4  5  3 | 8  1  7 | 9  6  2 
     8  1  9 | 2  3  6 | 5  4  7 
```

``` python
grid = new_partial_grid(18, solution)
show(grid)
```

```
     3  8  _ | _  _  _ | _  7  _ 
     _  _  4 | _  2  _ | _  _  _ 
     _  _  _ | _  _  _ | _  _  3 
    ---------+---------+---------
     _  4  _ | _  9  _ | _  _  _ 
     2  9  _ | _  8  _ | _  _  _ 
     _  3  _ | _  _  _ | 8  _  4 
    ---------+---------+---------
     _  _  _ | _  _  9 | _  _  _ 
     _  _  _ | 8  _  _ | 9  _  _ 
     _  _  9 | _  _  _ | _  _  _ 
```

### Solve

Confusingly enough, both generating and solving the puzzle make use of
`fill_grid` which recursively searches and backtracks.

``` python
full_grid(grid)
show(grid)
```

```
     3  8  2 | 1  5  4 | 6  7  9 
     9  6  4 | 3  2  7 | 1  5  8 
     5  7  1 | 9  6  8 | 4  2  3 
    ---------+---------+---------
     7  4  8 | 6  9  3 | 5  1  2 
     2  9  5 | 4  8  1 | 3  6  7 
     1  3  6 | 5  7  2 | 8  9  4 
    ---------+---------+---------
     6  5  3 | 2  4  9 | 7  8  1 
     4  2  7 | 8  1  5 | 9  3  6 
     8  1  9 | 7  3  6 | 2  4  5 
```

### Check

``` python
validate_grid(grid)
```

```
    True
```

