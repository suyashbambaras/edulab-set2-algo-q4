class suyash:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sumnumbers(root):
    def dfs(node, currentnumber):
        if not node:
            return 0
        currentnumber = currentnumber * 10 + node.val
        if not node.left and not node.right:
            return currentnumber
        leftsum = dfs(node.left, currentnumber)
        rightsum = dfs(node.right, currentnumber)
        return leftsum + rightsum

    return dfs(root, 0)


root = suyash(1)
root.left = suyash(2)
root.right = suyash(3)

print(sumnumbers(root)) 
