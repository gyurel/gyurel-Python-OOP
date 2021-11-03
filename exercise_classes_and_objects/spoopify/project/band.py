from spoopify.project.album import Album


class Band:

    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album: Album):
        for el in self.albums:
            if album.name == el.name:
                return f"Band {self.name} already has {album.name} in their library."

        self.albums.append(album)
        return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, name):
        for el in self.albums:
            if el.name == name:
                if el.published:
                    return "Album has been published. It cannot be removed."
                self.albums.remove(el)
                return f"Album {name} has been removed."

        return f"Album {name} is not found."

    def details(self):
        result = f"Band {self.name}\n"

        for album in self.albums:
            result += f"{album.details()}\n"

        return result
