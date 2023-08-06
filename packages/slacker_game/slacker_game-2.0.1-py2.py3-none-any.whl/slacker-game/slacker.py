#!/usr/bin/env python
# -*- coding: utf-8 -*-
# slacker-game - A clone of the arcade game Stacker
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Copyright (C) 2007 Clint Herron
# Copyright (C) 2017 Nguyễn Gia Phong

from math import sin
from random import choice, randint

import pygame
from pkg_resources import resource_filename


class SlackerMissedTile:
    """SlackerMissedTile(x, y, time) => SlackerMissedTile
    Slacker object for storing missed tiles.
    """
    def __init__(self, x, y, time):
        self.x, self.y, self.time = x, y, time

    def get_time_delta(self):
        """Return the duration the missed tile has been falling in."""
        return (pygame.time.get_ticks() - self.time) / 125.0


class Slacker:
    """This class provides functions to run the game Slacker, a clone of
    the popular arcade game Stacker.
    """
    BOARD_SIZE = BOARD_WIDTH, BOARD_HEIGHT = 7, 15
    SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = 280, 600
    TILE_SIZE = TILE_WIDTH, TILE_HEIGHT = 40, 40

    TILE_COLOR = 127, 127, 255
    TILE_COLOR_ALT = 255, 127, 127
    TILE_COLOR_LOSE = 64, 64, 128
    TILE_COLOR_ALT_LOSE = 127, 64, 64
    BG_COLOR = 0, 0, 0

    LEVEL_SPEED = 80, 80, 75, 75, 70, 70, 65, 60, 55, 50, 45, 40, 35, 30, 32
    MAX_WIDTH = (3,)*4 + (2,)*4 + (1,)*7

    COLOR_CHANGE_Y = 5  # blocks below which are displayed in the alternate color
    WIN_LEVEL = 15
    WIN_SPEED = 100
    INTRO, PLAYING, LOSE, WIN = range(4)

    BG_IMAGES = [pygame.image.load(resource_filename('slacker-game', i))
                 for i in ('intro.png', 'game.png', 'lose.png', 'win.png')]
    BG_IMAGES[WIN].set_colorkey(BG_COLOR)
    BG_IMAGES[LOSE].set_colorkey(BG_COLOR)

    def __init__(self):
        self.board = [[False] * self.BOARD_WIDTH for _ in range(self.BOARD_HEIGHT)]
        self.direction = choice([1, -1])
        self.game_state = self.INTRO
        self.level = 0
        self.last_time = 0
        self.missed_tiles = []
        self.screen = pygame.display.set_mode(self.SCREEN_SIZE)
        self.speed = self.LEVEL_SPEED[0]
        self.speed_ratio = 1.0
        self.width = self.MAX_WIDTH[0]
        self.x = randint(0, self.BOARD_WIDTH - self.width)
        self.y = self.BOARD_HEIGHT - 1

    def draw_tile(self, x, y):
        """Draw the tile at position (x, y)."""
        if self.game_state == self.LOSE:
            if y < self.COLOR_CHANGE_Y:
                color = self.TILE_COLOR_ALT_LOSE
            else:
                color = self.TILE_COLOR_LOSE
        else:
            if y < self.COLOR_CHANGE_Y:
                color = self.TILE_COLOR_ALT
            else:
                color = self.TILE_COLOR

        # XOffset is used to draw some wiggle in the tower when you win
        if self.game_state == self.WIN:
            xoffset = (sin(pygame.time.get_ticks()*0.004 + y*0.5)
                       * (self.SCREEN_WIDTH / 4))
        else:
            xoffset = 0

        rect = pygame.Rect(x*self.TILE_WIDTH + xoffset, y * self.TILE_HEIGHT,
                           self.TILE_WIDTH, self.TILE_HEIGHT)
        pygame.draw.rect(self.screen, color, rect)
        pygame.draw.rect(self.screen, self.BG_COLOR, rect, 2)

    def draw_board(self):
        """Draw the board and the tiles inside."""
        for x in range(self.BOARD_WIDTH):
            for y in range(self.BOARD_HEIGHT):
                if self.board[y][x]: self.draw_tile(x, y)

        # Draw the missed tiles
        for mt in self.missed_tiles:
            x = mt.x * self.TILE_WIDTH
            y = mt.y*self.TILE_HEIGHT + mt.get_time_delta()**2

            if mt.y < self.COLOR_CHANGE_Y:
                color = self.TILE_COLOR_ALT_LOSE
            else:
                color = self.TILE_COLOR_LOSE

            if y > self.SCREEN_HEIGHT:
                self.missed_tiles.remove(mt)
            else:
                pygame.draw.rect(
                    self.screen, color,
                    pygame.Rect(x + 2, y + 2, self.TILE_WIDTH - 3, self.TILE_HEIGHT - 3))

    def draw_background(self):
        """Draw the background image according to current game_state."""
        self.screen.blit(self.BG_IMAGES[self.game_state],
                         (0, 0, self.SCREEN_WIDTH, self.SCREEN_HEIGHT))

    def update_screen(self):
        """Draw the whole screen and everything inside."""
        if self.game_state == self.PLAYING:
            self.draw_background()
            self.draw_board()
        elif self.game_state == self.INTRO:
            self.draw_background()
        elif self.game_state in (self.LOSE, self.WIN):
            self.screen.fill(self.BG_COLOR)
            self.draw_board()
            self.draw_background()
        pygame.display.flip()

    def update_movement(self):
        """Update the direction the blocks are moving in."""
        self.time = pygame.time.get_ticks()
        if self.last_time + self.speed * self.speed_ratio <= self.time:
            if not -self.width < self.x + self.direction < self.BOARD_WIDTH:
                self.direction *= -1
            self.x += self.direction
            self.last_time = self.time
        self.board[self.y] = [0 <= x - self.x < self.width
                              for x in range(self.BOARD_WIDTH)]

    def key_hit(self):
        """Process the current position of the blocks relatively to the
        ones underneath when user hit the switch, then decide if the
        user will win, lose or go to the next level of the tower.
        """
        if self.y < self.BOARD_HEIGHT - 1:
            for x in range(max(0, self.x),
                           min(self.x + self.width, self.BOARD_WIDTH)):
                # If there isn't any block underneath
                if not self.board[self.y + 1][x]:
                    # Get rid of the block not standing on solid ground
                    self.board[self.y][x] = False
                    # Then, add that missed block to missed_tiles
                    self.missed_tiles.append(
                        SlackerMissedTile(x, self.y, pygame.time.get_ticks()))
        self.width = sum(self.board[self.y])
        if not self.width:
            self.game_state = self.LOSE
        elif self.level + 1 == self.WIN_LEVEL:
            self.speed, self.game_state = self.WIN_SPEED, self.WIN
        else:
            self.direction = choice([1, -1])
            self.level += 1
            self.speed = self.LEVEL_SPEED[self.level]
            self.width = min(self.width, self.MAX_WIDTH[self.level])
            self.x = randint(0, self.BOARD_WIDTH - self.width)
            self.y -= 1

    def main_loop(self, loop=True):
        """The main loop."""
        while loop:
            self.update_screen()
            if self.game_state == self.INTRO:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        loop = False
                    elif event.type == pygame.KEYDOWN:
                        if event.key in (pygame.K_RETURN, pygame.K_SPACE):
                            self.game_state = self.PLAYING
                        elif event.key in (pygame.K_ESCAPE, pygame.K_q):
                            loop = False
            elif self.game_state == self.PLAYING:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        loop = False
                    elif event.type == pygame.KEYDOWN:
                        if event.key in (pygame.K_RETURN, pygame.K_SPACE):
                            self.key_hit()
                        elif event.key in (pygame.K_ESCAPE, pygame.K_q):
                            self.__init__()
                        # Yes, this is a cheat.
                        elif event.key == pygame.K_0 and self.width < self.BOARD_WIDTH:
                            self.x -= self.direction
                            self.width += 1
                        elif event.key in range(pygame.K_1, pygame.K_9 + 1):
                            self.speed_ratio = (pygame.K_9 - event.key + 1) / 5.0
                self.update_movement()
            elif self.game_state in (self.LOSE, self.WIN):
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        loop = False
                    elif event.type == pygame.KEYDOWN:
                        self.__init__()


def main():
    pygame.init()
    slacker = Slacker()
    slacker.main_loop()
    pygame.display.quit()


if __name__ == '__main__':
    main()
