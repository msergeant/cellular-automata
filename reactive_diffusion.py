class World(object):
    DA = 1
    DB = 0.5
    FEED = 0.055
    K = 0.062

    def __init__(self, cells = [], width = 200, height = 200):
        self.width = width
        self.height = height
        self.grid = [(1, 0) for i in range(width * height)]
        self.next = [(1, 0) for i in range(width * height)]
        self.minX = 1
        self.minY = 1
        self.maxX = self.width - 1
        self.maxY = self.height - 1

        for cell in cells:
            self.grid[cell[0] + width * cell[1]] = (0, 1)

    def get_color(self, x, y):
        cell =  self.grid[x + self.width * y]

        color = max(0, 255 - int(cell[1] * 255))
        return (color, color, color)

    def update(self):
        lowerX = max(1, self.minX)
        upperX = min(self.width - 1, self.maxX)
        lowerY = max(1, self.minY)
        upperY = min(self.height - 1, self.maxY)
        self.minX = self.width
        self.minY = self.height
        self.maxX = 1
        self.maxY = 1

        for x in range(lowerX, upperX):
            for y in range(lowerY, upperY):
                a = self.grid[x + self.width * y][0]
                b = self.grid[x + self.width * y][1]
                nextA = (a +
                         self.DA * self._laplaceA(x, y) -
                         a * b * b +
                         self.FEED * (1 - a))
                nextB = (b +
                         self.DB * self._laplaceB(x, y) +
                         a * b * b -
                         (self.K + self.FEED) * b)

                # Find a boundary for next update
                if (nextA < 0.99999 and
                    nextB > 0.00001):
                    print((nextA,nextB))
                    self.minX = min(x - 2, self.minX)
                    self.minY = min(y - 2, self.minY)
                    self.maxX = max(x + 2, self.maxX)
                    self.maxY = max(y + 2, self.maxY)

                self.next[x + self.width * y] = (min(nextA, 1), min(nextB, 1))

        self.grid = self.next

    def _laplaceA(self, x, y):
        return self._laplace(0, x, y)

    def _laplaceB(self, x, y):
        return self._laplace(1, x, y)

    def _laplace(self, index, x, y):
        sum = 0
        sum += self.grid[(x + 0) + self.width * (y - 1)][index] * 0.2
        sum += self.grid[(x + 0) + self.width * (y + 0)][index] * -1
        sum += self.grid[(x + 0) + self.width * (y + 1)][index] * 0.2
        sum += self.grid[(x - 1) + self.width * (y - 1)][index] * 0.05
        sum += self.grid[(x - 1) + self.width * (y + 0)][index] * 0.2
        sum += self.grid[(x - 1) + self.width * (y + 1)][index] * 0.05
        sum += self.grid[(x + 1) + self.width * (y - 1)][index] * 0.05
        sum += self.grid[(x + 1) + self.width * (y + 0)][index] * 0.2
        sum += self.grid[(x + 1) + self.width * (y + 1)][index] * 0.05
        return sum
