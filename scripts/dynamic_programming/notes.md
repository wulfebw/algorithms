
# notes on dynamic programming
- four steps 
    1. characterize optimal solution
    2. recursively define value of optimal solution
    3. compute value of optimal solution in bottom up manner
    4. construct optimal solution from what's been computed

# experience notes

## types of DP problems 
1. min/max cost single-step
    - max_cost_path_only_down_and_right
    - min_cost_path_only_down_and_right
    - max_all_one_submat
    - edit_dist
    - longest_common_subsequence
        + space optimized
    - longest_common_subsequence_3_seq
    - longest_common_substring
    - longest_increasing_subseq
    - maze_path_count
    - longest_palindromic_subsequence
2. generic optimization
    - assembly_line_opt
    - choice_of_area
    - optimal_strategy
3. constraint problems (e.g., sum as axis of array) (similar to min/max cost single-step, but are multi-step) (also include / exclude problems)
    - coin_change
    - min_cost_weight
    - subset_sum
    - zero_one_knapsack
    - weighted_job_scheduling
    - floyd-warshall
    - partition equal sum
    - bellman-ford
    - recursion/sum_as_pow
4. recursive definition (w/ recurring substructure) (also count problems)
    - fib
    - binomial_coef
    - n_by_2_tiling
    - friend_pairing
5. 1d opt
    - rod_cutting_revisited
    - min_jump
    - max_product_cutting
    - expectd_rolls
6. misc
    - ugly_numbers

## problems I skipped but should do 
- box stacking
- dice throw
- tree problems 
    + largest independent set
    + vertex cover
    + optimal binary search tree
- shortest path with exactly k edges
- lot's of count problems 
    + revisit after recursion overview
















