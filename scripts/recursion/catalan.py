'''
catalan numbers come up a bunch in combinatorics
https://en.wikipedia.org/wiki/Catalan_number

# examples:

1. X-Y words
- how many ways to order n Xs and n Ys such that no initial substring has more ys than xs 

2. how many expressions containing n pairs of parentheses?
- same idea, the open parens must proceed the close parens

3. number of ways to parenthesize n+1 factors
- ((ab)c)d, etc 

4. Cn is the number of full binary trees with n+1 leaves
- equivalently, the number of binary trees with n internal nodes

5. Cn is number of monotonic lattice paths along grid with nxn cells that don't cross the diagonal

6. Cn is number of ways convex polygon with n+2 sides can be cut into triangles by connecting vertices without crossing line segments

# formula and explanation
- for the case where the relevant value is n 
    + Cn = 1/(n+1) * choose(2n, n)
    + also satisfy recurrence relation Cn+1 = ∑-=0^n Ci * Cn-i
    
'''