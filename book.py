class Book:
    def __init__(self,title,author,year_published,price):
        self.title=title
        self.author=author
        self.year_published=year_published
        self.price=price
    def get_info(self):
        return f"{self.title} by {self.author} published in {self.year_published}"
    def apply_discount(self,discount):
        self.price-=self.price*(discount/100)

book1=Book("mrman","steve richards",2002,5000)
print(book1.get_info())
book1.apply_discount(10)
print(book1.price)
