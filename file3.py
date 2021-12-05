class Book:
    def init(self, bid, autor, name, year):
        self.id = bid
        self.autor = autor
        self.name = name
        try:
            self.year = int(year)
        except ValueError:
            raise ValueError('...')

    def str(self):
         return f'{self.id}, {self.autor}, {self.name}, {self.year}'
 
class Library:
    def init(self):
        self._storage = {}
 
    def str(self):
        result = []
        for item in self._storage.values():
            result.append(f'{str(item[0])} - {str(item[1])} экз.')
        return str(result)
 
    def add(self, book):
        if not isinstance(book, Book):
            raise ValueError('...')
        bid = book.id
        if bid in self._storage:
            self._storage[bid][1] += 1
        else:
            self._storage[bid] = [book, 1]
 
    def see(self, bid):
        item = self._storage.get(bid)
        if item:
            return item[0]
        return None
 
    def pop(self, bid):
        item = self._storage.get(bid)
        if item:
            item[1] -= 1
            if not item[1]:
                self._storage.pop(bid)
            return item[0]
        else:
            raise ValueError('...')
 
    def find(self, autor='', name='', year=0):
        result = []
        for item in self._storage.values():
            book = item[0]
            if (not autor or autor == book.autor) and \
               (not name or book.name.startswith(name)) and \
               (not year or year == book.year):
                result.append(book.id)
        return result
 
 
book1 = Book(1, 'Підмогильний', 'Місто', 1927)
book2 = Book(5, 'Івана Семеновича Нечуя-Левицького', 'Кайдаше́ва семья', 1878)
book3 = Book(7, 'Карпенко-Карий Іван', 'Мартин Боруля', 1886)
book4 = Book(9, 'Іван Франко', 'Захар Беркут', 1883)
book5 = Book(12, 'Юрій Яновський', 'Майстер корабля', 1928)
lib = Library()


lib.add(book1)
lib.add(book2)
lib.add(book3)
print(lib)
print()
print(lib.find(year=2000))
 
print()
lib.add(book4)
lib.add(book5)
print(lib.pop(1))
print(lib.pop(1))
print()
print(lib)
print()
print(lib.find(name='Как'))