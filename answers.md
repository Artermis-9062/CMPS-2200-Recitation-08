# CMPS 2200 Recitation 08 Answers

**Name:** Chuong Hoang Pham
_________________________


Place all written answers from `recitation-10.md` here for easier grading.



- **2) (2 pts)** What is the work of `reachable`, assuming $n$ nodes and $m$ edges?

    - Since we need to check at most $n$ nodes and $m$ edges, then the work is $O(m + n)$

- **4) (1 pt)** What is the worst case number of times we need to call `reachable` to determine if a graph is connected?

    - We only need to call `reachable` once. Checking connectivity only requires picking a single arbitrary start node and seeing whether the set returned by `reachable` contains all $n$ nodes in the graph. If it does, the graph is connected; if not, it is disconnected. This is true regardless of which node we pick, so one call always suffices.

- **5) (2 pts)** What is the work of `connected`, assuming $n$ nodes and $m$ edges?

    The work of `connected` is based on the work of `reachable`, and the work of `reachable` is $O(m + n)$, so the work for `connected` is also $O(m + n)$

- **7) (1 pt)** What if we switched the graph representation to an adjacency matrix? Would the work of `reachable` change? If so, what would it be? If not, why not?

    Yes, the work would change. With an adjacency matrix, finding the neighbors of a single node requires scanning its entire row, which takes $O(n)$ time, and we do this for each of the $n$ nodes in the worst case. This gives a total work of $O(n^2)$, regardless of $m$, since the matrix itself has $\Theta(n^2)$ entries. This is worse than $O(m + n)$ for sparse graphs (where $m$ is much smaller than $n^2$).