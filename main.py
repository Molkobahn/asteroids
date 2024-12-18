import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	clock = pygame.time.Clock()
	
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	shots = pygame.sprite.Group()

	Asteroid.containers = (asteroids, updatable, drawable)
	Shot.containers = (shots, updatable, drawable)
	AsteroidField.containers = (updatable)
	asteroid_field = AsteroidField()
	
	Player.containers = (updatable, drawable)

	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
	
	dt = 0
	seconds = 0
	kill_count = 0

	while True:
		for event in pygame.event.get():
				if event.type == pygame.QUIT:
					return 
		
		for obj in updatable:
			obj.update(dt)
		
		for asteroid in asteroids:
			if asteroid.collision(player):
				print ("Game Over!")
				print (f"Time: {round(seconds)} seconds")
				print (f"Kills: {kill_count}")
				print(f"Score: {kill_count * round(seconds)}")
				sys.exit()

			for shot in shots:
				if shot.collision(asteroid):
					asteroid.split()
					shot.kill()
					kill_count += 1

		screen.fill("black")
		
		for obj in drawable:
			obj.draw(screen)
		
		seconds += clock.get_time() / 1000
		
		pygame.display.flip()
		
		# limit the framerate to 60 FPS
		dt = clock.tick(60) / 1000


if __name__=="__main__":
	main()
	