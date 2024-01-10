from PIL import Image

def generate_colored_image(width, height, color):
    # Creează o nouă imagine cu dimensiunile specificate
    image = Image.new("RGB", (width, height), color)
    
    # Salvează imaginea cu numele specificat
    image.save("verde.png")

# Culorile sunt reprezentate sub forma de tupluri (R, G, B), unde R, G și B sunt valorile între 0 și 255.
# De exemplu, (255, 0, 0) reprezintă roșu, (0, 255, 0) reprezintă verde, iar (0, 0, 255) reprezintă albastru.
color = (136, 171, 142)  # Culoare portocaliu în exemplu

generate_colored_image(512, 512, color)
