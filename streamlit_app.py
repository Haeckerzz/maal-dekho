import streamlit as st
from typing import List
from itertools import permutations

def minimize_bars(required_lengths: List[int], bar_length: int):
    best_solution = None
    min_bars = float('inf')
    
    # Try all permutations to find the optimal solution
    for perm in permutations(required_lengths):
        bars = []
        for length in perm:
            if length > bar_length:
                # If a single required length is greater than bar_length, split it across multiple bars
                needed_bars = -(-length // bar_length)  # Ceiling division
                split_lengths = [bar_length] * (needed_bars - 1) + [length % bar_length]
                for split_length in split_lengths:
                    bars.append([split_length])
            else:
                placed = False
                for bar in bars:
                    if sum(bar) + length <= bar_length:
                        bar.append(length)
                        placed = True
                        break
                if not placed:
                    bars.append([length])
        
        if len(bars) < min_bars:
            min_bars = len(bars)
            best_solution = bars
    
    return best_solution

def main():
    st.title("Maal Dekho")
    
    max_length = st.number_input("Enter maximum bar length:", min_value=1, value=15)
    input_lengths = st.text_area("Enter required lengths (comma-separated):", "5, 4, 2, 14, 7, 8, 6, 3, 1, 2")
    
    if st.button("Optimize"): 
        required_lengths = list(map(int, input_lengths.split(',')))
        bars = minimize_bars(required_lengths, max_length)
        
        st.write(f"### Minimum number of bars needed: {len(bars)}")
        for i, bar in enumerate(bars, start=1):
            st.write(f"**Bar {i}:** {bar} (Total used: {sum(bar)}/{max_length})")

if __name__ == "__main__":
    main()
