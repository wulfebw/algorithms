
# intro
- focus is on single-source shortest path 
    + but this can solve other problems 
        * single-destination
            - reverse edge directions
        * single-pair 
            - solving single-pair is the same as solving single-source 
        * all-pairs
            - though see chapter 25 for better ways 

- djikstra's is a greedy algorithm 
- floyd-warshall is a dp algorithm
- greedy and dp both share optimal substructure property

## optimal substructure
- v0 to vk with path p0k is shortest path 
- vi and vj on that path 
    + then pij (the subpath) is the shortest path from i to j

## cycles
- you can't have cycles
    + negative weight cycles mean shortest path ill-defined
    + positive weight cycles obviously shouldn't be used
    + 0 weight cycles can always just be not used

## shortest paths tree and predecessor graphs 
- how to get the path 
    + each vertex has a predecessor π
    + after running the algorithm following this path yields the shortest path, but during execution it may not 
    + the graph G_π is the predecessor graph
        * all the vertices with non nil π
        * all directed edges defined by π
        * the idea behind most of these algorithms is that after execution, G_π will be a rooted tree yielding shortest paths to all reachable vertices from the source
            - a "shortest paths tree"

## relaxation
- all nodes have a weight value d, which starts out as infinity and is "relaxed" during execution (i.e., it's an upper bound that's chilled the fuck out progressively in it's over estimation)
    + actual etymology is that 
        * there's a triangle inequality constraint that v.d <= u.d + w(u,v)
        * hmm I don't get this, and I like mine better
- relax function
    + takes two vertices u,v and a function w
    + if v.d > u.d + w(u,v):
        * # relax
        * v.d = u.d + w(u,v)
        * v.π = u 
- this is the key concept behind algorithms in this chapter
    + they differ in how they relax edges
        * djikstra's relaxes each edge once 
        * bellamn ford relaxes each edge |V| - 1 times

## properties 
- triangle inequality
    + s->v <= s->u + w(u,v)
- upper-bound
    + v.d > δ(s,v)
    + where δ is the weight of the shortest path 
- no-path
    + has weight infinity
- convergence
    + if s->u->v is a shortest path 
    + and s->u is a shortest path 
    + then s->u->v will always be a shortest path 
- path relaxation   
    + order doesn't matter
- predecessor graph 
    + gives shortest paths

# bellman-ford
- how does this work?
    + it initializes the source vertex to have 0 path weight and everything else to have infinite weight 
    + then it runs for |V| - 1 iterations
        * each iteration asks the question "if we allow for paths of this length, can we shorten the path from s to each vertex?"
            - if the answer is yes, it does it
    + the reason this works is that all shortest paths are simple paths (i.e., no cycles)
        * therefore the shortest path from s to u for all u is of length at most |V| - 1
        * this algorithm uses the optimal subtructure property in order to consider all possible best paths of up to length |V| - 1
- analysis
    + O(VE)
        * two for loops one over V one over E

# shortest paths in DAGs
- if the graph is a DAG you can toposort the vertices and then for each vertex relax each edge coming out of it 
    + initialize single source shortest path 
    + toposort 
    + for each vertex
        * for each outgoing edge
            - relax edge
- why does this work?
    + assume a path between v0 and vk
    + this path contains vertices (v0, v1, ..., vk)
        * if it's possible to move between these vertices arbitrarily, then you really have to look at all the paths 
        * but in this case, we know that you can only move between them in one order
        * in particular, we know we can move between them in the order (v0,v1) then (v1,v2), ..., (vk-1, vk) exactly because the toposorted ness of the vertices
            - basically, if you don't have cycles the set of paths you have to consider if highly simplified
- applications
    + scheduling jobs
        * a critical path is the longest path
            - maximum time to complete everything?
















