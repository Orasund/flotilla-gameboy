import flotilla


class MyMatrix:
    def __init__(self, matrix):
        self.matrix = matrix
        
    def display_image(self, image):
        for x in range(0,8):
          for y in range(0,8):
              self.matrix.set_pixel(x, y, image[y][x])
        self.matrix.update()

def get_matrix(dock):
    matrix = dock.first(flotilla.Matrix)
    if not matrix:
        print("no matrix module found...")
        dock.stop()
        sys.exit(1)       
    else:
        print("found matrix")
        return MyMatrix(matrix)

