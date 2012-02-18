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

import os
import sys
sys.path.append('../src/')
os.chdir('../src/')
from analogous import *

# draw a simple triangle
def triangle(size):
  for i in range(3):
    forward(size)
    turn_left(120)

# draw three triangles (the whole of them forming another triangle)
def three_triangles (size):
  triangle(size)
  forward(size)
  triangle(size)
  turn_left(120)
  forward(size)
  turn_left(240)
  triangle(size)
  turn_left(240)
  forward(size)
  turn_left(120)

# recursive sierpinski triangle drawing function
def sierpinski (size, depth):
  if not depth:
    return;
  change_color((255 / (depth + 1), 0, 100))
  three_triangles (size)
  sierpinski (size / 2, depth - 1)
  if depth - 1:
    forward(size)
  sierpinski (size / 2, depth - 1)
  if depth - 1:
    turn_left(120)
    forward(size)
    turn_left(240)
  sierpinski (size / 2, depth - 1)
  if depth - 1:
    turn_left(240)
    forward(size)
    turn_left(120)

sierpinski(100, 4)

# wait for windows to be closed
while 1:
  for event in pygame.event.get():
    if event.type == pygame.QUIT: sys.exit()
