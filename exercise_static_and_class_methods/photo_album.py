from math import ceil


class PhotoAlbum:
    def __init__(self, pages):
        self.pages = pages
        self.photos = [[] for _ in range(self.pages)]

    @classmethod
    def from_photos_count(cls, photos_count):
        pages = ceil(photos_count / 4)
        return cls(pages)

    def add_photo(self, label):
        page_nbr = 0
        for page in self.photos:
            page_nbr += 1
            slot_nbr = len(page) + 1
            if len(page) < 4:
                page.append(label)
                return f"{label} photo added successfully on page {page_nbr} slot {slot_nbr}"
        return "No more free slots"

    def display(self):
        result = '-' * 11
        result += '\n'
        for page in self.photos:
            for _ in page:
                result += '[]'
                result += ' '
            result = result.strip()
            result += '\n'
            if len(page) == 0:
                result += '\n'
            result += '-' * 11
            result += '\n'

        return result.strip()


album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())
