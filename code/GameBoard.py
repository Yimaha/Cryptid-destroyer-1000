


class GameBoard:
  def __init__(self, 
  ids, 
  orientations, 
  blues,
  whites,
  greens
  ):
  map_coord_dict = [
    [
      [
        [GameTile(TILE_TYPE.water, 0, 0), GameTile(TILE_TYPE.water, 1, 0), GameTile(TILE_TYPE.water, 2, 0), GameTile(TILE_TYPE.water, 3, 0), GameTile(TILE_TYPE.forest, 4, 0), GameTile(TILE_TYPE.forest, 5, 0)],
        [GameTile(TILE_TYPE.swamp, 0, 1), GameTile(TILE_TYPE.swamp, 1, 1), GameTile(TILE_TYPE.water, 2, 1), GameTile(TILE_TYPE.sand, 3, 1), GameTile(TILE_TYPE.forest, 4, 1), GameTile(TILE_TYPE.forest, 5, 1)],
        [GameTile(TILE_TYPE.swamp, 0, 2), GameTile(TILE_TYPE.swamp, 1, 2), GameTile(TILE_TYPE.sand, 2, 1), GameTile(TILE_TYPE.sand, 3, 1), GameTile(TILE_TYPE.sand, 4, 2), GameTile(TILE_TYPE.forest, 5, 2)],
      ]
    ],[

    ],[

    ],[

    ],[

    ],[

    ]
  ]

  
