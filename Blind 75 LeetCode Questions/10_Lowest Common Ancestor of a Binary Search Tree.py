class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        if p.val > q.val: 
            p, q = q, p
        while root:
            if p.val > root.val:
                root = root.right
            elif q.val < root.val:
                root = root.left
            else: 
                return root
        