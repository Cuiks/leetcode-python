# -*- coding: utf-8 -*-

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.val)


# [1,2,3,4,null,null,5]
def zigzagLevelOrder(root: TreeNode):
    if not root:
        return []
    res = []
    queue = list()
    queue.insert(0, root)
    left_to_right = False
    while queue:
        node_res = []
        queue_bak = queue[:]
        queue.clear()
        for node in queue_bak:
            node_res.append(node.val)
            if not left_to_right:
                if node.left:
                    queue.insert(0, node.left)
                if node.right:
                    queue.insert(0, node.right)
            else:
                if node.right:
                    queue.insert(0, node.right)
                if node.left:
                    queue.insert(0, node.left)
        left_to_right = not left_to_right
        res.append(node_res)

    return res


node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(None)
node6 = TreeNode(None)
node7 = TreeNode(5)

root = node1
root.left = node2
root.right = node3
node2.left = node4
node3.right = node7

res = zigzagLevelOrder(root)

print(res)
