import re
import streamlit as st
import pandas as pd
import numpy as np
from solver import astar
from uiux import empty_board, board_matrix_to_dataframe

np.random.seed(0)

st.title("Sudoku Solver 🥳")

st.subheader("Use A* to solve a Sudoku puzzle. 😎")

input_board= st.text_area(
    label="Enter the random number 0 to 9 of the board.", value=empty_board, height=400
)

values = []
board = []
for line in input_board.split("\n"):
    if not "-" in line:
        vals = re.findall("[0-9]", line.rstrip())
        temp = [int(x) for x in vals]
        values += temp
        board.append(temp)


rows = np.repeat(np.arange(1, 10), 9)
cols = np.tile(np.arange(1, 10), 9)

if len(rows) == len(cols) == len(values):

    df = pd.DataFrame({"i": rows, "j": cols, "k": values})
    
    board_empty = df.copy()

    df = df[df["k"] != 0]

    board_empty.k = ["" if x == 0 else str(x) for x in board_empty.k]
    board_empty = board_empty.pivot(index="i", columns="j", values="k")

    if st.button("Solve!"):

        solution = astar(board)

        if solution:

            st.markdown("**Solution**")
            df = board_matrix_to_dataframe(solution)
            st.write(df)
        
    else:
        
        st.markdown("**Board layout**")
        st.write(board_empty)

else:
    st.write("Something is wrong with the layout of the board. Please try again.")

if st.button("Reset!"):

    st.cache_resource.clear()