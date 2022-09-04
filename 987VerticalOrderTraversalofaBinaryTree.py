# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        results = defaultdict(list)
        # get coordinates of each node
        queue = [(root,0,0)]
        while queue:
            node, x, y = queue.pop(0)
            if not node: 
                continue
            results[(x,y)].append(node.val)
            results[(x,y)].sort()
            queue.extend([(node.left, x-1, y+1), (node.right, x+1, y+1)])
        # output values of nodes by increasing order of y-coordinate
        res = defaultdict(list)
        keys = sorted(list(results.keys()), key=lambda x: (x[0], x[1]))
        for k in keys:
            x, y = k
            res[x].extend(results[k])
        return res.values()
