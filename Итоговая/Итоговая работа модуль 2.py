import doctest

if __name__ == "__main__":
    class Tablet:
        """
        Базовый класс Планшетный ПК
        :param name - фирма производитель
        :param system - операционная система, на которой работает планшетный ПК
        Например:
        >>> test_tablet = Tablet ("Amazon", "Android")
        """
        def __init__(self, name: str, system: str):
            self.name = name
            self.system = system

        def __str__(self):
            """
            :return Возвращает основную информацию о планшетном ПК
            Например:
            >>> test_tablet = Tablet ("Amazon", "Android")
            >>> print(test_tablet)
            Планшет фирмы Amazon, под управлением операционной системы Android
            """
            return f"Планшет фирмы {self.name}, под управлением операционной системы {self.system}"

        def __repr__(self):
            """
            :return: информативное или официальное строковое представление объекта.
            Например:
            >>> test_tablet = Tablet ("Amazon", "Android")
            >>> print("__repr__", repr(test_tablet))
            __repr__ Tablet(name='Amazon', system='Android')
            """
            return f"{self.__class__.__name__}(name={self.name!r}, system={self.system!r})"

        def add_year (self, year: int):
            """
            Метод, позволяющий указать год выхода планшетного ПК на рынок
            :param year: год выхода на рынок
            :return: возвращает год выхода планшета на рынок
            Например:
            >>> test_tablet = Tablet ("Amazon", "Android")
            >>> test_tablet.add_year(2019)
            """
            self._year = year


    class Eink_book (Tablet):
        """
        Например:
        >>> test_Ebook = Eink_book ("Amazon", "Android", "FullHD")
        """
        def __init__(self, name: str, system: str, screen_resolution: str):
            super(Eink_book, self).__init__(name, system)
            self.name = name
            self.system = system
            self.screen_resolution = screen_resolution

        def __str__(self):
            return f"Электронная книга фирмы {self.name}, под управлением операционной системы {self.system}. "

        def __repr__(self):
            return f"{self.__class__.__name__}(name={self.name!r}, system={self.system!r})"

        def add_year(self, year: int):
            return self.add_year(2019) + 3
        
    doctest.testmod()
    print("results")
    pass

