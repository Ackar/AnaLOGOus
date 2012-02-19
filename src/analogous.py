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

from game import *

# Forward definitions (allow direct call of the methods)
forward = game.forward
turn_left = game.turn_left
turn_right = game.turn_right
change_color = game.change_color
change_brush_size = game.change_brush_size
hide_brush = game.hide_brush
show_brush = game.show_brush
toggle_brush = game.toggle_brush

# Colors definitions
red = 189, 26, 58
green = 61, 161, 65
blue = 112, 190, 229



#  ** French translations **

# functions
avancer = forward
tourner_gauche = turn_left
tourner_droite = turn_right
changer_couleur = change_color
changer_taille = change_brush_size
lever_crayon = hide_brush
poser_crayon = show_brush
basculer_crayon = toggle_brush

# colors
rouge = red
vert = green
bleu = blue
