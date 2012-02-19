# Copyright (C) 2012  Cleymans Sylvain
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program. If not, see <http://www.gnu.org/licenses/>.

import sys, pygame, math

class Game:
  def __init__(self):
    self.screen_size = 1000, 800
    self.player_pos = self.screen_size[0] / 2, self.screen_size[1] / 2
    self.player_angle = 0.
    self.brush_color = 255, 255, 255
    self.brush_size = 1
    self.brush_visible = True

    # initialization of the screen
    pygame.init ()
    self.screen = pygame.display.set_mode (self.screen_size)

    # initialization of the drawing surface
    self.drawing_surface = pygame.Surface (self.screen_size)

    # loading the cursor
    self.cursor = pygame.sprite.Sprite ()
    self.cursor.image = pygame.image.load("roundcursor.png").convert()

  def forward(self, length):
    dest = ((self.player_pos[0] + length * math.cos(self.player_angle)),
        (self.player_pos[1] + length * math.sin(self.player_angle)))

    # Smooth effect on moving : intermediate points are computed and traced
    while abs(self.player_pos[0] - dest[0]) > 2 or abs(self.player_pos[1] - dest[1]) > 2:
      tmp_dest = (self.player_pos[0] + (dest[0] - self.player_pos[0]) / 5.,
          (self.player_pos[1] + (dest[1] - self.player_pos[1]) / 5.))
      self.draw_line((int(self.player_pos[0]), int(self.player_pos[1])),
          (int(tmp_dest[0]), int(tmp_dest[1])))
      self.player_pos = tmp_dest
      self.render()

    # We draw the last portion of line
    self.draw_line((int(self.player_pos[0]), int(self.player_pos[1])),
        (int(dest[0]), int(dest[1])))
    self.player_pos = dest
    self.render()

  def turn_left(self, angle):
    self.player_angle -= angle * (math.pi / 180.)

  def turn_right(self, angle):
    self.player_angle += angle * (math.pi / 180.)

  def change_color(self, color):
    self.brush_color = color

  def change_brush_size(self, size):
    self.brush_size = size

  def hide_brush(self):
    self.brush_visible = False

  def show_brush(self):
    self.brush_visible = True

  def toggle_brush(self):
    self.brush_visible = not self.brush_visible

  def draw_line(self, orig, end):
    if self.brush_visible:
      pygame.draw.line (self.drawing_surface, self.brush_color, orig, end,
                        self.brush_size)

  def render(self):
    self.screen.blit(self.drawing_surface, (0, 0))
    self.screen.blit(self.cursor.image, (self.player_pos[0] - 10,
                                         self.player_pos[1] - 10))
    pygame.display.update()

  def reset_all(self):
    self.player_pos = self.screen_size[0] / 2, self.screen_size[1] / 2
    self.player_angle = 0.
    self.brush_color = 255, 255, 255
    self.drawing_surface = pygame.Surface (self.screen_size)

game = Game ()
