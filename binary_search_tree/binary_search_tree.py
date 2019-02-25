

class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if(value < self.value):
            if(self.left):
                self.left.insert(value)
            else:
                self.left = BinarySearchTree(value)
        elif(value > self.value):
            if(self.right):
                self.right.insert(value)
            else:
                self.right = BinarySearchTree(value)

    def contains(self, target):
        if(target is self.value):
            return True
        if(target < self.value):
            if(self.left is None):
                return False
            return self.left.contains(target)
        if(target > self.value):
            if(self.right is None):
                return False
            return self.right.contains(target)
        return False

    def get_max(self):
        if(self.right is None):
            return self.value
        return self.right.get_max()
