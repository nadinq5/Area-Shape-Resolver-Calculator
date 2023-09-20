class Shape:
    def get_area(self):
        print("Subclass has to implement this method.")

    def __str__(self):
        return(f'{self.get_area()}')

    def get_perimeter(self):
        print("Subclass has to implement this method.")
