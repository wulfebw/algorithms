'''
https://en.wikipedia.org/wiki/Stars_and_bars_(combinatorics)
'''

'''
theorem 1
1. how many k-tuples of _positive_ integers with sum n exist?
for positive integers n and k 
the number of k-tuples of _positive_ integers with sum n 
is equal to the number of subsets from n-1 of size k-1
which is given by choose(n-1, k-1)

why?
because
line up the stars, of which there are n 
how many ways are there to place k-1 (k-1 because you have to have one on the left)
bars in between these stars?

well the bars define n-1 valid gaps for the bars
because no bars can be adjacent
and you have k-1 bars (one on the left)
so basically choose(n-1, k-1)
'''


'''
theorem 2
1. how many k-tuples of _non-zero_ integers with sum n exist?
it's the same logic as before, except now you can have empty bins 

i.e., now there are n - 1 + k possible locations for the bars 
however, since you lose the previous restrictions you could just as well use 
the stars now as the insertion objects 
so either of choose(n - 1 + k, n) = choose(n - 1 + k, k - 1) works

here's the logic recapped
- you have n stars 
- you have k bars 
- no matter what, the left position will be a bar
    + a star must be in a bin
    + therefore you really have k-1 bars 
- with that out the way, note that placing all the bars or placing all the stars fully defines an ordering 
    + so you can place either, but we'll place bars (of which we have k-1)
- so how many ways are there of placing these objects when we have no other constraints?
    + noting that the order of the stars within bins doesn't matter (again)
- the answer is the number of objects (n + k - 1) and the number of objects whose position defines an order (k)
- this gives choose(n + k - 1, k)


'''