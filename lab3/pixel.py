class pixel:
    x = 0
    y = 0
    height = 0

    xRight = 0
    yLow = 0

    is_radar = False
    is_over = False

    length = 25
    width = 25
    color = (0, 0, 0)
    par = (0, 0, 0, 0)

    def __init__(self, x, y, height):
        self.x = x * self.length
        self.y = y * self.length
        self.height = height

        self.xRight = self.x + self.width
        self.yLow = self.y + self.length

        self.setColor(height)

        self.par = (self.x, self.y, self.length, self.width)


    def setColor(self, height = 1):
        if self.is_over == True and self.height == 1:
            self.color = (128, 128, 255)
            return
        if self.is_over == True and self.height == 2:
            self.color = (90, 90, 255)
            return
        if self.is_over == True and self.height == 3:
            self.color = (60, 60, 255)
            return
        if height == 1:
            self.color = (0, 128, 0)
            return
        if height == 2:
            self.color = (100, 128, 0)
            return
        if height == 3:
            self.color = (200, 128, 0)
            return

    def check_over(self, x, y):
        if x >= self.x and x <= self.xRight and y <= self.yLow and y >= self.y:
            return True
        else:
            return False



