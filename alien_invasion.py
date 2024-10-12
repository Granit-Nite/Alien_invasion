import sys                                                   # "C:/Program Files/Python312/python.exe" "C:/Code/Alien_invasion/alien_invasion/alien_invasion.py"
import pygame
from settings import Settings                                # från filen "settings" importera klassen Settings
from ship import Ship


class AlienInvasion:
    """Overall class to manage game assets and behavior"""   #  MAN KAN SÄGA ATT __INIT__ ÄR LAGRET DÄR ALL INFO SKA HÄMTAS OCH ALLA ANDRA KODER ÄR ARBETARNA SOM SKA GÖRA JOBBET.
    
    def __init__(self):
        """Initialize the game, and create game resources""" #### GRUNDEN ELLER BASEN TILL SPELET
        pygame.init()                                        # Denna funktion ger oss skärmen på spelet
        self.clock = pygame.time.Clock()                     # Denna funktion gör att framen följer klockan och blir smooth
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        #self.screen = pygame.display.set_mode ((1200,800))
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)
        self.bg_color = (194,194,194)                        # OBS!! EFTEROM __INIT__ BARA ÄR BASEN SÅ ÄR DET SENARE BYTET TILLKALLAS, men väljer vi vilken färg som skall användas 
        
        
        
        
    def run_game(self):                                      ### SJÄLVA SPELET OCH VAD DEN GÖR/ HUR DEN KONTROLLERAS      
        """Start the main loop for the game"""
        while True:                                          # En while loop, så länge denna är True är spelet igång
            for event in pygame.event.get():                 # Event är det actions/ spelaren trycker på
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill(self.settings.bg_color)                  # EFTERSOM __INIT__ BARA ÄR BASEN ÄR DET, FÖRST HÄR DET FÖRÄNDRAS OCH SKÄRMEN BYTER FÄRG
            self.ship.blitme()
            pygame.display.flip()                            # Vad denna gör är att den uppdaterar skärmen, så en bild försvinner och en ny kommer, så det ser ut som saker rör sig
            self.clock.tick(60)
            

            
if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()



