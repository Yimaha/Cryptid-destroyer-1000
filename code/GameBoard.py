

CONTINENTS = [
  [
    [
      [GameTile(TILE_TYPE.water, 0, 0), GameTile(TILE_TYPE.water, 1, 0), GameTile(TILE_TYPE.water, 2, 0), GameTile(TILE_TYPE.water, 3, 0), GameTile(TILE_TYPE.forest, 4, 0), GameTile(TILE_TYPE.forest, 5, 0)],
      [GameTile(TILE_TYPE.swamp, 0, 1), GameTile(TILE_TYPE.swamp, 1, 1), GameTile(TILE_TYPE.water, 2, 1), GameTile(TILE_TYPE.sand, 3, 1), GameTile(TILE_TYPE.forest, 4, 1), GameTile(TILE_TYPE.forest, 5, 1)],
      [GameTile(TILE_TYPE.swamp, 0, 2), GameTile(TILE_TYPE.swamp, 1, 2), GameTile(TILE_TYPE.sand, 2, 1), GameTile(TILE_TYPE.sand, 3, 1, ANIMAL_TYPE.bear), GameTile(TILE_TYPE.sand, 4, 2, ANIMAL_TYPE.bear), GameTile(TILE_TYPE.forest, 5, 2, ANIMAL_TYPE.bear)],
    ]
  ],[

  ],[

  ],[

  ],[

  ],[

  ]
]

TOP_LEFT_CORNER = [(0, 0), (6, 0), (3, 0), (3, 6), (6, 0), (6, 6)]

STRUCTURES = [(STRUCTURE_TYPE.standing_stone, COLOR_TYPE.blue), (STRUCTURE_TYPE.shack, COLOR_TYPE.blue),
(STRUCTURE_TYPE.standing_stone, COLOR_TYPE.white),(STRUCTURE_TYPE.shack, COLOR_TYPE.white),
(STRUCTURE_TYPE.standing_stone, COLOR_TYPE.green), (STRUCTURE_TYPE.shack, COLOR_TYPE.green)]

class GameBoard:
  def __init__(self, 
  ids, 
  orientations, 
  # structures have a pre-assumed order: blue stone, blue shack, white stone, white shack, green stone, green shack
  structures
  ):

  computed_map = [[None*9]*12] ## this is the final 2D map that is suppose to represent the entire board after fully computed inputs
  for i in range(6)
    continent = CONTINENTS[ids[i]] # identify which block is in this location
    orientation = orientations[i] # a boolean value that either true (top left) or false (bottom right)
    top_left_y, top_left_x = TOP_LEFT_CORNER[i]
    if orientation:
      for j in range(6):
        for k in range(6):
          computed_map[top_left_y + j][top_left_x + k] = continent[j][k]
          computed_map[top_left_y + j][top_left_x + k].y = top_left_y + j
          computed_map[top_left_y + j][top_left_x + k].x = top_left_x + k
          self.update_continent_if_has_structure(self, computed_map[top_left_y + j][top_left_x + k], structures)s


  def update_continent_if_has_structure(self, tile, structures):
    y = tile.y 
    x = tile.x 
    for i in range(len(structure)):
      s_y, s_x = structure[i]
      if y is s_y and x is s_x:
        tile.structure, tile.color = STRUCTURES[i]
      






