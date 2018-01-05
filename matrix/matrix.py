class Matrix:

    def __init__(self, m):
        self.m = m
        self.i = len(self.m)
        self.j = len(self.m[0])

    # elementart row operations
    def switch(self, r1, r2):
        self.m[r1 - 1], self.m[r2 - 1] = self.m[r2 - 1], self.m[r1 - 1]

    def multiply(self, r1, c):
        self.m[r1 - 1] = [(c * j) for j in self.m[r1 - 1]]

    def addRow(self, r1, r2 , c):
        r2m = [(c * j) for j in self.m[r2 - 1]]
        self.m[r1 - 1] = [(self.m[r1 - 1][j] + r2m[j]) for j in range(self.j)]

    def isSquare(self):
        return self.i == self.j

    def isDiagonal(self):
        if (self.isSquare):
            for i in range(3):
                for j in range(3):
                    if (self.m[i][j] != 0 and i != j): 
                        return False

            return True

        return False

    def __str__(self):
        return "\n".join(str(r) for r in self.m)

def main():

    A = Matrix([
        [1, 2 ,3],
        [2, 4, 6],
        [0, 0, 0]
    ])

    A.addRow(2, 1, -2)
    print(A)

main()
