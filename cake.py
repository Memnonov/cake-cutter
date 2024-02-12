"""
cake.py - Return of the cake...

  Represents a rectangle cake that can only be cut following a ready made
  square grid (i.e. horizontal and vertical cuts only). Some of the squares
  contain ornamental flowers, which are coveted by the cake enjoyers.

  Contains the Cake class, which contains methods for visualizing
  the solution.

  @Author: Mikko Memonen, 2024

"""


class Cake:

    def __init__(self, width, height, flowers):
        self.width = width
        self.height = height
        self.flowers = set(flowers)
        self.pieces = {}

    def belongs_to_piece(self, square_x, square_y):
        """
        Checks if the given square is inside an already cut piece.
        Returns the index of the piece or 0.
        """
        for piece, index in self.pieces.items():
            if square_x in range(piece[0], piece[2] + 1) and square_y in range(
                piece[1], piece[3] + 1
            ):
                return index
        return 0

    def print_cake(self):
        """
        Prints the cake with '@' representing flowers, numbers
        squares belonging to certain pieces and '·' unassigned squares.
        """
        print()
        for row in range(self.height, 0, -1):
            for column in range(1, self.width + 1):
                if (column, row) in self.flowers:
                    print("@ ", end="")
                elif piece_nbr := self.belongs_to_piece(column, row):
                    print(piece_nbr, "", end="")
                else:
                    print("· ", end="")
            print()
        print()

    def print_pieces(self):
        """
        Outputs the coordinates of cut pieces and leftover cake in the
        format defined in the problem description.
        """
        if len(self.pieces):
            for piece in self.pieces:
                print(piece[1], piece[0], piece[3], piece[2])
            print(0)  # Should be no leftovers with this method.
        else:
            print("The cake is uncut!")

    def get_area(self):
        """
        Returns a list representing two opposite corners of the cake
        i.e. the area of the cake.
        """
        return [1, 1, self.width, self.height]


if __name__ == "__main__":
    print("Cake is good.")
