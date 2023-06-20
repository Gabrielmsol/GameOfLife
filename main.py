import numpy as np
import pygame as pg


# Colors
Black = (0, 0, 0)
White = (255, 255, 255)


# Gets the grid specifications
def grid_size(width_and_height_size, rows_and_cols_size):

    cell_size = width_and_height_size // rows_and_cols_size

    width, height = width_and_height_size, width_and_height_size

    rows, cols = rows_and_cols_size, rows_and_cols_size

    return width, height, rows, cols, cell_size


# Creates a grid with probability P of having a cell alive
def create_grid(rows_and_cols_size, P):
    return np.random.choice([0, 1], size=(rows_and_cols_size, rows_and_cols_size), p=[1-P, P])


# Updates the grid following Conway's game of life rules
def update_grid(grid):
    neighbours = np.zeros_like(grid)
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            neighbours += np.roll(np.roll(grid, i, axis=0), j, axis=1)
            # Smart trick to count neighbours we roll the grid summing values over a point

    new_grid = np.where((grid == 1) & ((neighbours < 2) | (neighbours > 3)), 0, grid)
    new_grid = np.where((grid == 0) & (neighbours == 3), 1, new_grid)
    # This makes, so we update our grid according to Conway's law
    return new_grid


def draw_grid(screen, grid, cell_size):
    screen.fill(Black)
    indices = np.where(grid == 1)
    for row, col in zip(indices[0], indices[1]):
        pg.draw.rect(screen, White, (col*cell_size, row*cell_size, cell_size, cell_size))


def run_game(width_and_height_size, rows_and_cols_size, P, t):

    width, height, rows, cols, cell_size = grid_size(width_and_height_size, rows_and_cols_size)

    pg.init()
    screen = pg.display.set_mode((width, height))
    clock = pg.time.Clock()

    grid = create_grid(rows_and_cols_size, P)

    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        draw_grid(screen, grid, cell_size)
        grid = update_grid(grid)

        pg.display.flip()
        clock.tick(t)

    pg.quit()


def see_grid(width_and_height_size, rows_and_cols_size, P):

    width, height, rows, cols, cell_size = grid_size(width_and_height_size, rows_and_cols_size)

    pg.init()
    screen = pg.display.set_mode((width, height))
    clock = pg.time.Clock()

    grid = create_grid(rows_and_cols_size, P)

    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        draw_grid(screen, grid, cell_size)

        pg.display.flip()
        clock.tick(1)

    pg.quit()

run_game(600, 100, 0.2, 50)
