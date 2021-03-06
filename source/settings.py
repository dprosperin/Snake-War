from pygame import Color, font
import source.Resource as Resource

font.init()

BLACK = Color(0, 0, 0)
WHITE = Color(255, 255, 255)
RED = Color(255, 0, 0)
GREEN = Color(0, 255, 0)
BLUE = Color(0, 0, 255)
YELLOW = Color(255, 255, 0)

HEADING = font.Font(Resource.path('fonts\\Gameplay.ttf'), 40)
TEXT = font.Font(Resource.path('fonts\\Gameplay.ttf'), 20)
LOGO = font.Font(Resource.path('fonts\\Games.ttf'), 60)
