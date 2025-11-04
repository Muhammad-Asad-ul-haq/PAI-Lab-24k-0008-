originalPixels = [[10, 20, 30], [40, 50, 60]]

class Image:
    def __init__(self, pixelList):
        self.pixels = pixelList

    def applyTransformation(self, func):
        self.pixels = func(self.pixels)

    def getCopy(self):
        return [row[:] for row in self.pixels]


def flipHorizontal(pixels):
    return [row[::-1] for row in pixels]


def adjustBrightness(pixels, value):
    for i in range(len(pixels)):
        for j in range(len(pixels[0])):
            pixels[i][j] += value
    return pixels


def rotateNinetyDegrees(pixels):
    rows = len(pixels)
    cols = len(pixels[0])
    rotated = []
    for i in range(cols):
        new_row = []
        for j in range(rows):
            new_row.append(pixels[rows - j - 1][i])
        rotated.append(new_row)
    return rotated


class AugmentationPipeline:
    def __init__(self):
        self.steps = []

    def addStep(self, func):
        self.steps.append(func)

    def processImage(self, image):
        result = []
        for step in self.steps:
            temp = Image(image.getCopy())
            temp.applyTransformation(step)
            result.append(temp.pixels)
        return result


img = Image(originalPixels)
pipeline = AugmentationPipeline()

pipeline.addStep(flipHorizontal)
pipeline.addStep(lambda p: adjustBrightness(p, 10))
pipeline.addStep(rotateNinetyDegrees)

augmentedImages = pipeline.processImage(img)

for i in range(len(augmentedImages)):
    print("Transformation", i + 1)
    for row in augmentedImages[i]:
        print(row)
    print()
