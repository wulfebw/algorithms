
- brief recap of big theta / O / Omega 
- if g ∈ Θ(f), then there exist constants c1, c2 s.t. c1g <= f <= c2f for n > n0
    + this is by definition an asymptotically tight bound
- g ∈ O(f), then there exists constants c and n0 s.t. cg <= f for n > n0
    + i.e., f is an upper bound on performance
- g ∈ Ω(f) then there exist constants c and n0 s.t. f <= cg for n > n0
    + i.e., f is a lower bound
- the lower case o and ω just mean that the bound is explictly not tight 
    + so n ∈ O(n^2) but n ∉ O(n) because this second bound is tight

- all these are worst case bounds 
    + it's just a question of determining the function describing the worst case run time
