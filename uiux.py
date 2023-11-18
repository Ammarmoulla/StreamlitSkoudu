import pandas as pd
import numpy as np

#https://stackoverflow.com/questions/45471152/how-to-create-a-sudoku-puzzle-in-python

empty_board = """-------------------------
| 1 0 0 | 0 0 0 | 0 0 0 |
| 0 0 0 | 0 0 0 | 0 0 0 |
| 0 0 0 | 0 0 0 | 0 0 0 |
-------------------------
| 0 0 0 | 0 0 0 | 0 0 0 |
| 0 0 0 | 0 0 0 | 0 0 0 |
| 0 0 0 | 0 0 0 | 0 0 0 |
-------------------------
| 0 0 0 | 0 0 0 | 0 0 0 |
| 0 0 0 | 0 0 0 | 0 0 0 |
| 0 0 0 | 0 0 0 | 0 0 0 |
-------------------------"""


def board_matrix_to_dataframe(arr):
    df = pd.DataFrame(arr,
                      index=np.arange(1, 10), 
                      columns=np.arange(1, 10))
    return df