# lessons

# types of recursion problems 
1. power set type problems (return all of set) / exhaustive search
    - number_pad
    - power_set
    - permutation_with_spaces
    - find_permutations
    - word_break
    - print_all_binary
2. recursive backtracking
    - description:
        + the above recursive algorithms essentially only return at the end 
        + whereas these backtrack repeatedly terminate the search 
        + particularly common strategy is set/if true return true/unset
            * the idea being that the recursive call returns true only if a solution is found, therefore as soon as you hit a true, you return it 
                - see 8 queens, boggle (in this case yield instead of return), euler path
    - recursive_backtracking_impl
        + recursive_backtracking_impl
            * cubic_decomp
            * shrink_word
            * 8_queens
        + boggle (in graphs dir)
        + euler path 
            * recursive backtracking from each node with set / unset 
3. recursion instead of iterative methods
    - strings
4. equation-based combinatorics
    - cutting_rectangles
    - stars and bars
5. compute nth term
    - product_sequence
    - print_pos_neg_seq
    - find_position
    - death_circle
6. graphs / trees
    - flood_fill
        + this is just bfs
    - flip_x_0
7. misc
    - decode_string


# problems to revist
- tree ones 
    + traversal etc
- water overflow