class UnionFind:

    def __init__(self, size):
        self.size = size
        self.id = list(range(size))
        self.depth = [1] * size

    def union(self,node1,node2):
        i = self.root(node1)
        j = self.root(node2)
        if self.depth[node1] < self.depth[node2]:
            self.id[node1]=node2
            self.depth[node2] += self.depth[node1]
        else:
            self.id[j]=node1
            self.depth[node1] += self.depth[node2]

    def root(self, node):
        while node != self.id[node]:
            self.id[node] = self.id[self.id[node]]
            node=self.id[node]
        return node       

    def find(self, node1, node2):
        return self.root(node1) == self.root(node2)

if __name__=="__main__":
    uf=UF(8)
    root(6)
    #print(find(3,5))
    union(3,7)