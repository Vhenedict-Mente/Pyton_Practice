class Singer:
    def __init__(self, name, song):
        self.name = name
        self.song = song

    def info(self):
        print(f"I am a singer. My name is {self.name}. I sing the song {self.song} .")

    def make_sound(self):
        print("HeeHee!")


class Actor:
    def __init__(self, name, character):
        self.name = name
        self.character = character

    def info(self):
        print(f"I am an actor. My name is {self.name}. I play as {self.character} in the Marvel Cinematic Universe.")

    def make_sound(self):
        print("Motherfather!")


artist1 = Singer("Michael Jackson", "Billy Jeans")
artist2 = Actor("Samuel L. Jackson", "Nick Fury")

for animal in (artist1, artist2):
    animal.info()
    animal.make_sound()