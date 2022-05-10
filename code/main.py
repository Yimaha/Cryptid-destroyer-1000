


from .GameTile import *

def main():
  tile = GameTile(TILE_TYPE.water, 0, 0)
  print(tile.getNeighbour(1))
  print(tile.type)

  
main()