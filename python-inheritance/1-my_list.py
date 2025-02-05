#!/usr/bin/python3
#!/usr/bin/python3
""" Module that defines a class MyList inheriting from list """


class MyList(list):
    """ Classe MyList qui hérite de list """

    def print_sorted(self):
        """ Affiche la liste triée en ordre croissant """
        print(sorted(self))
