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
sys.path.append(sys.path[0] + '/../src/')
os.chdir(sys.path[0] + '/../src/')
from analogous import *

def spiral():
  angle = 2
  n = 3500

  for i in range(n):
    # compute a new color
    c = int(i * 255. / n)
    change_color((100, c, 50))

    # draw the line and change slightly widen the angle
    forward(2)
    turn_left(angle)
    angle *= 0.9995

def square(size):
  for i in range(4):
    forward(size)
    turn_left(90)

spiral()
for i in range (20, 50, 5):
  square(i)
  square(-i)

# wait for windows to be closed
while 1:
  for event in pygame.event.get():
    if event.type == pygame.QUIT: sys.exit()
