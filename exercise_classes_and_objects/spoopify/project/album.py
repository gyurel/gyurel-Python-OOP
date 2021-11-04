from spoopify.project.song import Song


class Album:

    def __init__(self, name, *songs):
        self.name = name
        self.songs = list(songs)
        self.published = False

    def add_song(self, song: Song):
        if song.single:
            return f"Cannot add {song.name}. It's a single"

        if self.published:
            return "Cannot add songs. Album is published."

        for piece in self.songs:
            if song.name == piece.name:
                return "Song is already in the album."

        self.songs.append(song)
        return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, name):

        if self.published:
            return "Cannot remove songs. Album is published."

        for song in self.songs:
            if song.name == name:
                self.songs.remove(song)
                return f"Removed song {song.name} from album {self.name}."

        return "Song is not in the album."

    def publish(self):
        if self.published:
            return f"Album {self.name} is already published."

        self.published = True
        return f"Album {self.name} has been published."

    def details(self):
        result = f"Album {self.name}\n"

        for song in self.songs:
            result += f"== {song.get_info()}\n"

        return result