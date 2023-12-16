# # import cv2 as cv

# # imagePaths = [
# #     './mazes/maze1.png',
# #     './mazes/maze2.png',
# #     './mazes/maze3.png'
# # ]


# # def readImage(imagePath: str) -> cv.Mat:
# #     img = cv.imread(imagePath)
# #     ret, img = cv.threshold(img, 127, 255, cv.THRESH_BINARY)
# #     return img


# # image = readImage(imagePaths[0])

# # CELL_SIZE = 6

# # cv.imshow("Maze", image)
# # cv.waitKey(0)


# # Author List:		Om Rastogi
# # Filename:			finder.py
# # Functions:		readImage, solveMaze, blockwork
# # Global variables:	CELL_SIZE


# # Import necessary modules
# # Do not import any other modules
# import cv2
# import numpy as np
# import os


# # To enhance the maze image
# # import image_enhancer


# # Maze images in mazes folder have cell size of 20 pixels
# # In my case I was able to get a fixes size for cells, for other cases one may have to do this dynamically
# CELL_SIZE = 20


# # def blockwork(img,coordinate)

# def readImage(img_file_path: str) -> cv2.Mat:
#     img = cv2.imread(img_file_path, 0)
#     ret, img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
#     return img


# def solveMaze(original_binary_img: cv2.Mat, initial_point, final_point, no_cells_height, no_cells_width):
#     shortestPath = []
#     img = original_binary_img.copy()
#     sp = []
#     rec = [0]
#     p = 0
#     sp.append(list(initial_point))
#     edgearray = []
#     for i in range(no_cells_height):
#         edgearray.append([])
#         for j in range(no_cells_width):
#             sz = [i, j]
#             edge, block = blockwork(img, sz)
#             edgearray[i].append(edge)

#     edge = edgearray

#     while True:
#         h, w = sp[p][0], sp[p][1]
#         if sp[-1] == list(final_point):
#             break

#         if edge[h][w] > 0:
#             rec.append(len(sp))

#         if edge[h][w] > 999:
#             edge[h][w] = edge[h][w]-1000
#             h = h-1
#             sp.append([h, w])
#             edge[h][w] = edge[h][w]-100

#             p = p+1
#             continue

#         if edge[h][w] > 99:
#             edge[h][w] = edge[h][w]-100
#             h = h+1
#             sp.append([h, w])
#             edge[h][w] = edge[h][w]-1000
#             p = p+1
#             continue

#         if edge[h][w] > 9:
#             edge[h][w] = edge[h][w]-10
#             w = w-1
#             sp.append([h, w])
#             edge[h][w] = edge[h][w]-1
#             p = p+1
#             continue

#         if edge[h][w] == 1:
#             edge[h][w] = edge[h][w]-1
#             w = w+1
#             sp.append([h, w])
#             edge[h][w] = edge[h][w]-10
#             p = p+1
#             continue

#         else:
#             sp.pop()
#             rec.pop()
#             p = rec[-1]

#     for i in sp:
#         shortestPath.append(tuple(i))

#     return shortestPath


# def blockwork(img, coordinate):
#     # coordinate is a list consisting for dimension of block to be processesd
#     # coordinate = [y-axis, x-axis]
#     # the first block is coordinate = [0,0]
#     size = CELL_SIZE
#     h = CELL_SIZE * (coordinate[0] + 1)
#     w = CELL_SIZE * (coordinate[1] + 1)
#     h0 = CELL_SIZE * coordinate[0]
#     w0 = CELL_SIZE * coordinate[1]

#     block = img[h0:h, w0:w]

#     up = bool(block[0, int(size/2)]) * 1000
#     down = bool(block[int(size-1), int(size/2)])*100
#     left = bool(block[int(size/2), 0]) * 10
#     right = bool(block[int(size/2), int(size-1)])*1

#     # edge = [up, down, left, right] in the form of 1111
#     edge = up+down+left+right
#     return edge, block


# def main():
#     file_num = 0
#     img_file_path = "./mazes/maze01.jpg"

#     try:
#         original_binary_img = readImage(img_file_path)
#         height, width = original_binary_img.shape
#     except AttributeError as attr_error:
#         print('\n[ERROR] readImage function is not returning binary form of original image in expected format !\n')
#         exit()

#     # number of cells in height of maze image
#     numberOfVerticalCells = int(height/CELL_SIZE)
#     # number of cells in width of maze image
#     numberOfHorizontalCells = int(width/CELL_SIZE)
#     initalPoint = (0, 0)
#     finalPoint = (numberOfVerticalCells - 1, numberOfVerticalCells - 1)

#     try:
#         shortestPath = solveMaze(original_binary_img, initalPoint,
#                                  finalPoint, numberOfVerticalCells, numberOfHorizontalCells)

#         if len(shortestPath) > 2:
#             # img = image_enhancer.highlightPath(
#             #     original_binary_img, initial_point, final_point, shortestPath)
#             pass
#         else:
#             print(
#                 '\n[ERROR] shortestPath returned by solveMaze function is not complete !\n')
#             exit()

#     except TypeError as type_err:
#         print('\n[ERROR] solveMaze function is not returning shortest path in maze image in expected format !\n')
#         exit()

#     # print('\nShortest Path = %s \n\nLength of Path = %d' %
#     #       (shortestPath, len(shortestPath)))
#     # print('\n============================================')

#     return shortestPath


# if __name__ == "__main__":
#     print(main())

# # if __name__ == '__main__':
# #     file_num = 0
# #     img_file_path = "./mazes/maze00.jpg"

# #     try:
# #         original_binary_img = readImage(img_file_path)
# #         height, width = original_binary_img.shape
# #     except AttributeError as attr_error:
# #         print('\n[ERROR] readImage function is not returning binary form of original image in expected format !\n')
# #         exit()

# #     # number of cells in height of maze image
# #     no_cells_height = int(height/CELL_SIZE)
# #     # number of cells in width of maze image
# #     no_cells_width = int(width/CELL_SIZE)
# #     initial_point = (0, 0)
# #     final_point = (no_cells_height - 1, no_cells_height - 1)

# #     try:
# #         shortestPath = solveMaze(original_binary_img, initial_point,
# #                                  final_point, no_cells_height, no_cells_width)

# #         if len(shortestPath) > 2:
# #             # img = image_enhancer.highlightPath(
# #             #     original_binary_img, initial_point, final_point, shortestPath)
# #             pass
# #         else:
# #             print(
# #                 '\n[ERROR] shortestPath returned by solveMaze function is not complete !\n')
# #             exit()

# #     except TypeError as type_err:
# #         print('\n[ERROR] solveMaze function is not returning shortest path in maze image in expected format !\n')
# #         exit()

# #     print('\nShortest Path = %s \n\nLength of Path = %d' %
# #           (shortestPath, len(shortestPath)))
# #     print('\n============================================')

# #     return shortestPath

#     # cv2.imshow('canvas0' + str(file_num), original_binary_img)
#     # cv2.waitKey(0)
#     # cv2.destroyAllWindows()

#     # choice = input(
#     #     '\nWant to run your script on all maze images ? ==>> "y" or "n": ')

#     # if choice == 'y':

#     #     file_count = len(os.listdir(img_dir_path))

#     #     for file_num in range(file_count):

#     #         img_file_path = img_dir_path + 'maze0' + str(file_num) + '.jpg'

#     #         print('\n============================================')

#     #         print('\nFor maze0' + str(file_num) + '.jpg')

#     #         try:

#     #             original_binary_img = readImage(img_file_path)
#     #             height, width = original_binary_img.shape

#     #         except AttributeError as attr_error:

#     #             print(
#     #                 '\n[ERROR] readImage function is not returning binary form of original image in expected format !\n')
#     #             exit()

#     #         # number of cells in height of maze image
#     #         no_cells_height = int(height/CELL_SIZE)
#     #         # number of cells in width of maze image
#     #         no_cells_width = int(width/CELL_SIZE)
#     #         initial_point = (0, 0)											# start point coordinates of maze
#     #         # end point coordinates of maze
#     #         final_point = ((no_cells_height-1), (no_cells_width-1))

#     #         try:

#     #             shortestPath = solveMaze(
#     #                 original_binary_img, initial_point, final_point, no_cells_height, no_cells_width)

#     #             if len(shortestPath) > 2:

#     #                 img = image_enhancer.highlightPath(
#     #                     original_binary_img, initial_point, final_point, shortestPath)

#     #             else:

#     #                 print(
#     #                     '\n[ERROR] shortestPath returned by solveMaze function is not complete !\n')
#     #                 exit()

#     #         except TypeError as type_err:

#     #             print(
#     #                 '\n[ERROR] solveMaze function is not returning shortest path in maze image in expected format !\n')
#     #             exit()

#     #         print('\nShortest Path = %s \n\nLength of Path = %d' %
#     #               (shortestPath, len(shortestPath)))

#     #         print('\n============================================')

#     #         cv2.imshow('canvas0' + str(file_num), img)
#     #         cv2.waitKey(0)
#     #         cv2.destroyAllWindows()

#     # else:

#     #     print('')

# graph = {'A': set(['B', 'C']),
#          'B': set(['A', 'D', 'E']),
#          'C': set(['A', 'F']),
#          'D': set(['B']),
#          'E': set(['B', 'F']),
#          'F': set(['C', 'E'])}


# def dfs_paths(graph, start, goal):
#     stack = [(start, [start])]
#     visited = set()
#     while stack:
#         (vertex, path) = stack.pop()
#         if vertex not in visited:
#             if vertex == goal:
#                 return path
#             visited.add(vertex)
#             for neighbor in graph[vertex]:
#                 stack.append((neighbor, path + [neighbor]))


# print(dfs_paths(graph, 'A', 'F'))  # ['A', 'B', 'E', 'F']

import asyncio
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/connect")
async def connect():
    await asyncio.sleep(3)
    return {"message": "Connected"}

@app.get("/disconnect")
async def disconnect():
    return {"message": "CYKA BLYAT"}