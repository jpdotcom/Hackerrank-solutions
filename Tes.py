import random
import sys
import time
sys.setrecursionlimit(10**6)
class Node():
    def __init__(self, key):
        self.key = key
        self.left = None 
        self.right = None 




class AVLTree():
    def __init__(self, *args):
        self.node = None 
        self.height = -1  
        self.balance = 0; 
        
        if len(args) == 1: 
            for i in args[0]: 
                self.insert(i)
                
    def height(self):
        if self.node: 
            return self.node.height 
        else: 
            return 0 
    
    def is_leaf(self):
        return (self.height == 0) 
    
    def insert(self, key,arr):
        tree = self.node
        
        newnode = Node(key)
        
        if tree == None:
            self.root=newnode
            self.node = newnode 
            self.node.left = AVLTree() 
            self.node.right = AVLTree()
            
        
        elif arr[key[0]] < tree.key: 
            self.node.left.insert(key)
            
        else: 
            self.node.right.insert(key)
        
        
            
        self.rebalance() 
        
    def rebalance(self):
        ''' 
        Rebalance a particular (sub)tree
        ''' 
        # key inserted. Let's check if we're balanced
        self.update_heights(False)
        self.update_balances(False)
        while self.balance < -1 or self.balance > 1: 
            if self.balance > 1:
                if self.node.left.balance < 0:  
                    self.node.left.lrotate() # we're in case II
                    self.update_heights()
                    self.update_balances()
                self.rrotate()
                self.update_heights()
                self.update_balances()
                
            if self.balance < -1:
                if self.node.right.balance > 0:  
                    self.node.right.rrotate() # we're in case III
                    self.update_heights()
                    self.update_balances()
                self.lrotate()
                self.update_heights()
                self.update_balances()


            
    def rrotate(self):
        # Rotate left pivoting on self
       
        A = self.node 
        B = self.node.left.node 
        T = B.right.node 
        
        self.node = B 
        B.right.node = A 
        A.left.node = T 

    
    def lrotate(self):
        # Rotate left pivoting on self
        debug ('Rotating ' + str(self.node.key) + ' left') 
        A = self.node 
        B = self.node.right.node 
        T = B.left.node 
        
        self.node = B 
        B.left.node = A 
        A.right.node = T 
        
    def getRoot(self):
        return self.root  
    def update_heights(self, recurse=True):
        if not self.node == None: 
            if recurse: 
                if self.node.left != None: 
                    self.node.left.update_heights()
                if self.node.right != None:
                    self.node.right.update_heights()
            
            self.height = max(self.node.left.height,
                              self.node.right.height) + 1 
        else: 
            self.height = -1 
            
    def update_balances(self, recurse=True):
        if not self.node == None: 
            if recurse: 
                if self.node.left != None: 
                    self.node.left.update_balances()
                if self.node.right != None:
                    self.node.right.update_balances()

            self.balance = self.node.left.height - self.node.right.height 
        else: 
            self.balance = 0 
    def traverse(self,arr_idx,node,arr,mod):
        print(node)
        if node is not None:
            a,b=self.node.key 
            if arr[a]>=arr[arr_idx]:
                return self.traverse(arr_idx,self.node.left,arr,mod)%mod
            elif a<arr_idx:
                return (b%mod+self.traverse(arr_idx,self.node.left,arr,mod)%mod+self.traverse(arr_idx,self.node.right,arr,mod)%mod)%mod
       
        return 0
    def sum(self,node):
        if node is not None:
            a,b=self.node.key
            return b+self.sum(self.node.left)+self.sum(self.node.right)
        return 0

def candles(arr):
    s=time.time()
    tree= AVLTree()
    tree.insert((0,1),arr)
    root=tree.getRoot()
    
    mod=10**9+7
    for i in range(1,len(arr)):
        
        j=1
        j+=tree.traverse(i,root,arr,mod)
        
        tree.add((i,j),arr)
    
    return tree.sum(root),time.time()-s
arr=[1,2,3,4]
print(candles(arr))