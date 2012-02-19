from analogous import *

code = open("my_code.py", "r")
exec code

while 1:
  for event in pygame.event.get():
    if event.type == pygame.QUIT: sys.exit()
