import pygame 
from tiles import Tile 
from settings import tile_size, screen_width


class Level:
	def __init__(self,level_data,surface):
		
		# level setup
		self.display_surface = surface 
		self.setup_level(level_data)


	def setup_level(self,layout):
		self.tiles = pygame.sprite.Group()

		for row_index,row in enumerate(layout):
			for col_index,cell in enumerate(row):
				x = col_index * tile_size
				y = row_index * tile_size
				
				if cell == 'X':
					tile = Tile((x,y),tile_size)
					self.tiles.add(tile)
				# if cell == 'P':
				# 	player_sprite = Player((x,y),self.display_surface,self.create_jump_particles)
				# 	self.player.add(player_sprite)
					pass

	def run(self):
		self.tiles
		self.tiles.draw(self.display_surface)




