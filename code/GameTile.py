

from enum import Enum 

TILE_TYPE = Enum('TILE_TYPE', 'water mountain forest swamp desert')


class GameTile:
  def __init__(self, type, x, y):
    self.type = type # expected to be a TILE_TYPE
    self.y = y
    self.x = x  
  
  def getNeighbour(self, distance): # range is typically a number between 1 and 3
    result_set = [] 
    # terms out it is much easier to do this operation under
    # Cube coord, thus we will compute the result in cube coord then validate them at the end

    q_base, r_base = self.odd_q_to_axial(self.y, self.x)
    for i in range (-distance, distance+1, 1):  # i for q
        for j in range(max(-distance, -i - distance), min(distance, -i + distance) + 1, 1): # j for r
          result_set.append((i, j))
    
    odd_q_result_set = []
    for (q, r) in result_set:
      y, x = self.axial_to_odd_q(q_base + q, r_base + r)
      if self.validate(y, x):
        odd_q_result_set += [(y, x)]
      
    return odd_q_result_set

      
  def validate(self, y, x):
    return x >= 0 and x < 12 and y >= 0 and y < 12

  
  def odd_q_to_axial(self, y, x):
    q = y
    r = x - (y - (y&1))/2
    return (q, r)

  def axial_to_odd_q(self, q, r):
    y = q
    x = r + (q - (q&1)) / 2
    return (y, x)
  