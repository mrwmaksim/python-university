import pygame
import math
from pixel import pixel

class Map:
    win = 0
    event = 0

    radarIcon = 0
    radarX = 0
    radarY = 0
    radarI = 0
    radarJ = 0
    radarRange = 0
    radarHeight = 0

    num = 20

    heights = [
               [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
               [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
               [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
               [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
               [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
               [1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
               [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
               [1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
               [1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1],
               [1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1],
               [1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1],
               [1, 1, 1, 1, 1, 1, 1, 2, 3, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1],
               [1, 1, 1, 1, 1, 1, 1, 2, 3, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1],
               [1, 1, 1, 1, 1, 1, 1, 2, 3, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1],
               [1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1],
               [1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
               [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1],
               [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1],
               [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1],
               [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

    pixels = [[0] * 20 for i in range(20)]

    def __init__(self):

        run = True
        while run:
            self.radarX = input("Введите X радара: ")
            self.radarY = input("Введите Y радара: ")
            self.radarRange = input("Введите радиус действия радара: ")


            if self.radarX.isnumeric() and self.radarY.isnumeric():
                if int(self.radarX) < 20 and int(self.radarX) >= 0:
                    if int(self.radarY) < 20 and int(self.radarY) >= 0:
                        if int(self.radarRange) <= 400 and int(self.radarRange) > 0:
                            self.radarX = int(self.radarX)
                            self.radarY = int(self.radarY)
                            self.radarRange = int(self.radarRange)
                            run = False

        pygame.init()
        self.win = pygame.display.set_mode((500, 500))
        pygame.display.set_caption("radar")

        self.radarIcon = pygame.image.load('radar.png')

        for i in range(self.num):
            for j in range(self.num):
                self.pixels[i][j] = pixel(j, i, self.heights[i][j])

        self.pixels[self.radarY][self.radarX].is_radar = True
        self.radarI = self.radarX
        self.radarJ = self.radarY
        self.radarHeight = self.pixels[self.radarY][self.radarX].height

        self.calculateRadarNew()



    def calculateRange(self):
        currentI = self.radarI
        currentJ = self.radarJ


        self.pixels[self.radarY][self.radarX].is_over = True
        self.pixels[currentI][currentJ].setColor()

        step = 5
        numSteps = self.radarRange / step

        for angle in range(0, 360, 10):
            radianAngle = math.radians(angle)
            stepX = int(step * math.cos(radianAngle))
            stepY = int(step * math.sin(radianAngle))

            currentX = (self.pixels[self.radarI][self.radarJ].x + self.pixels[self.radarI][self.radarJ].xRight) / 2
            currentY = (self.pixels[self.radarI][self.radarJ].y + self.pixels[self.radarI][self.radarJ].yLow) / 2

            for len in range(0, self.radarRange, step):
                currentX += stepX
                currentY += stepY

                if (angle == 180):
                    print("x = ", currentX, "y = ", currentY)
                    print(currentI, currentJ)
                    if self.pixels[10][7].check_over(232.5, 262.5):
                        print("x = ", self.pixels[10][7].x," xRight = ", self.pixels[10][7].xRight ," y = ", self.pixels[10][7].y, " yLow = ", self.pixels[10][7].yLow)
                        print("yes")
                    else:
                        print("no")


                if self.pixels[currentI][currentJ].check_over(currentX, currentY):
                    self.pixels[currentI][currentJ].is_over = True
                    continue

                if currentI < 19:
                    if self.pixels[currentI + 1][currentJ].check_over(currentX, currentY):
                        currentI = currentI + 1
                        self.pixels[currentI][currentJ].is_over = True
                        continue

                if currentI > 0:
                    if self.pixels[currentI - 1][currentJ].check_over(currentX, currentY):
                        currentI = currentI - 1
                        self.pixels[currentI][currentJ].is_over = True
                        continue

                if currentJ < 19:
                    if self.pixels[currentI][currentJ + 1].check_over(currentX, currentY):
                        currentJ = currentJ + 1
                        self.pixels[currentI][currentJ].is_over = True
                        continue

                if currentJ > 0:
                    if self.pixels[currentI][currentJ - 1].check_over(currentX, currentY):
                        currentJ = currentJ - 1
                        self.pixels[currentI][currentJ].is_over = True
                        continue

                if currentJ > 0 and currentI > 0:
                    if self.pixels[currentI - 1][currentJ - 1].check_over(currentX, currentY):
                        currentI = currentI - 1
                        currentJ = currentJ - 1
                        self.pixels[currentI][currentJ].is_over = True
                        continue

                if currentJ < 19 and currentI > 0:
                    if self.pixels[currentI - 1][currentJ + 1].check_over(currentX, currentY):
                        currentI = currentI - 1
                        currentJ = currentJ + 1
                        self.pixels[currentI][currentJ].is_over = True
                        continue

                if currentJ > 0 and currentI < 19:
                    if self.pixels[currentI + 1][currentJ - 1].check_over(currentX, currentY):
                        currentI = currentI + 1
                        currentJ = currentJ - 1
                        self.pixels[currentI][currentJ].is_over = True
                        continue

                if currentJ < 19 and currentI < 19:
                    if self.pixels[currentI + 1][currentJ + 1].check_over(currentX, currentY):
                        currentI = currentI + 1
                        currentJ = currentJ + 1
                        self.pixels[currentI][currentJ].is_over = True
                        continue
                if self.pixels[9][10].is_over:
                    print("yes")

    def getTg(self, pixelHeight, stepX, stepY):
        sum = math.pow(stepX, 2) + math.pow(stepY, 2)
        sum = math.pow(sum, 1/2)
        resolve = pixelHeight - self.radarHeight
        resolve = resolve / sum

        return resolve


    def calculateRadarNew(self):
        currentI = self.radarI
        currentJ = self.radarJ

        angleK = [0] * 36

        self.pixels[self.radarY][self.radarX].is_over = True
        self.pixels[currentI][currentJ].setColor()

        step = 5
        for step in range(5, self.radarRange, step):
            for angle in range(0, 360, 10):


                currentX = (self.pixels[self.radarI][self.radarJ].x + self.pixels[self.radarI][self.radarJ].xRight) / 2
                currentY = (self.pixels[self.radarI][self.radarJ].y + self.pixels[self.radarI][self.radarJ].yLow) / 2
                radianAngle = math.radians(angle)
                stepX = int(step * math.cos(radianAngle))
                stepY = int(step * math.sin(radianAngle))
                currentX += stepX
                currentY += stepY

                for i in range(20):
                    for j in range(20):
                        if self.pixels[i][j].check_over(currentX, currentY):
                            num = int(angle * 0.1)

                            tan = self.getTg(self.pixels[i][j].height, stepX, stepY)

                            posX = math.pow(stepX, 2) + math.pow(stepY, 2)
                            posX = math.pow(posX, 1 / 2)

                            posY = angleK[num] * float(posX)


                            if angleK[num] == 0:
                                angleK[num] = tan

                            self.pixels[i][j].is_over = True

        print(angleK)

    def show(self):


        run = True
        while run:
            pygame.time.delay(1000)

            keys = pygame.key.get_pressed()

            for self.event in pygame.event.get():
                if self.event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
                    run = False

            for i in range(self.num):
                for j in range(self.num):
                    self.pixels[i][j].setColor(self.pixels[i][j].height)
                    pygame.draw.rect(self.win, self.pixels[i][j].color, self.pixels[i][j].par)

            self.win.blit(self.radarIcon, (self.radarX*25, self.radarY*25))
            pygame.display.update()

        pygame.quit()
        return