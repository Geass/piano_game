import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Screen settings
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Piano Game")
clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GRAY = (100, 100, 100)
LIGHT_GREEN = (144, 238, 144)

# Note settings
NOTE_WIDTH = 100
NOTE_HEIGHT = 30
NOTE_SPEED = 5

# Paths and key bindings
lanes = [150, 300, 450, 600]
keys = [pygame.K_d, pygame.K_f, pygame.K_j, pygame.K_k]

# Load music
pygame.mixer.music.load("song.mp3")  # Replace with your music file
pygame.mixer.music.set_volume(0.7)
music_length = pygame.mixer.Sound("song.mp3").get_length() * 1000  # Convert to milliseconds

# Font settings
font = pygame.font.Font(None, 36)

# Game state
active_notes = []  # List of active notes as Note objects
pressed_keys = set()
score = 0
health = 100
flash_effects = []  # List to store flash effects

# Note class
class Note:
    def __init__(self, x, y, lane):
        self.rect = pygame.Rect(x, y, NOTE_WIDTH, NOTE_HEIGHT)
        self.lane = lane
        self.color = LIGHT_GREEN

    def update(self):
        self.rect.y += NOTE_SPEED

    def draw(self):
        gradient_rect = pygame.Surface((NOTE_WIDTH, NOTE_HEIGHT), pygame.SRCALPHA)
        for i in range(NOTE_HEIGHT):
            color = (self.color[0], self.color[1], self.color[2], 255 - int(255 * (i / NOTE_HEIGHT)))
            pygame.draw.line(gradient_rect, color, (0, i), (NOTE_WIDTH, i))
        screen.blit(gradient_rect, (self.rect.x, self.rect.y))

# Flash effect class
class FlashEffect:
    def __init__(self, x, y, width, height, color, duration):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.duration = duration
        self.start_time = pygame.time.get_ticks()

    def draw(self):
        elapsed_time = pygame.time.get_ticks() - self.start_time
        if elapsed_time < self.duration:
            alpha = max(255 - int(255 * (elapsed_time / self.duration)), 0)
            flash_surface = pygame.Surface((self.rect.width, self.rect.height), pygame.SRCALPHA)
            flash_surface.fill((*self.color, alpha))
            screen.blit(flash_surface, self.rect)
        else:
            flash_effects.remove(self)

# Create notes dynamically based on song length and rhythm
def generate_notes():
    global notes
    notes = []
    bpm = 120  # Beats per minute
    beat_interval = 60000 / bpm  # Interval between beats in milliseconds
    num_beats = int(music_length / beat_interval)

    for beat in range(num_beats):
        time = beat * beat_interval
        lane = random.choice(range(4))  # Random lane for simplicity
        notes.append((time, lane))

generate_notes()
note_index = 0

# Start the music
pygame.mixer.music.play()

# Main game loop
running = True
start_ticks = pygame.time.get_ticks()
while running:
    screen.fill(BLACK)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key in keys:
                pressed_keys.add(event.key)
        elif event.type == pygame.KEYUP:
            if event.key in keys:
                pressed_keys.discard(event.key)

    # Draw lanes
    for lane in lanes:
        pygame.draw.rect(screen, WHITE, (lane - NOTE_WIDTH // 2, 0, NOTE_WIDTH, SCREEN_HEIGHT), 1)

    # Draw target lines
    for lane in lanes:
        pygame.draw.line(screen, RED, (lane - NOTE_WIDTH // 2, SCREEN_HEIGHT - 100), (lane + NOTE_WIDTH // 2, SCREEN_HEIGHT - 100), 2)

    # Highlight pressed keys
    for i, key in enumerate(keys):
        if key in pressed_keys:
            pygame.draw.rect(screen, GRAY, (lanes[i] - NOTE_WIDTH // 2, SCREEN_HEIGHT - 100, NOTE_WIDTH, NOTE_HEIGHT))

    # Spawn notes based on timing
    current_time = pygame.time.get_ticks() - start_ticks
    while note_index < len(notes) and notes[note_index][0] <= current_time:
        _, lane = notes[note_index]
        x = lanes[lane] - NOTE_WIDTH // 2
        active_notes.append(Note(x, 0, lane))
        note_index += 1

    # Update and draw notes
    for note in active_notes[:]:
        note.update()
        note.draw()
        if note.rect.y > SCREEN_HEIGHT:
            active_notes.remove(note)
            health -= 10  # Missed note penalty

    # Handle key presses
    for i, key in enumerate(keys):
        if key in pressed_keys:
            for note in active_notes[:]:
                target_zone = pygame.Rect(lanes[i] - NOTE_WIDTH // 2, SCREEN_HEIGHT - 100, NOTE_WIDTH, NOTE_HEIGHT)
                if note.lane == i and target_zone.colliderect(note.rect):
                    active_notes.remove(note)
                    score += 10
                    flash_effects.append(FlashEffect(target_zone.x, target_zone.y, target_zone.width, target_zone.height, BLUE, 200))
                    break

    # Draw flash effects
    for flash in flash_effects:
        flash.draw()

    # Display score and health
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    health_text = font.render(f"Health: {health}", True, WHITE)
    screen.blit(health_text, (10, 50))

    # End game if health is 0
    if health <= 0:
        running = False

    pygame.display.flip()
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
sys.exit()
