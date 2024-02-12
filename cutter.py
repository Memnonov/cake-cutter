"""
cutter.py - A Cutter class for cutting the Cake.

    Contains the Cutter class, with which you can cut the
    cake represented by Cake into squares that each have
    a single ornamental flower.

    It was probably unnecessarily complicated to split this
    cake and cutting thing into separate modules with all the
    static/class method trickery. I had been learning Java and
    wanted to try out some of the OOP features in Python too.

    I still don't think this is quite fast enough for large
    areas with plenty of flowers. Compared to the nasty nasty
    first version though, this is blazingly fast(er).

    @Author: Mikko Memonen, 2024

"""


class Cutter:
    """
    Cuts up a cake!
    """

    @staticmethod
    def get_updated_flowers_in_area(area, flowers):
        """
        Returns a new set of flowers with only the flowers present
        in given area.
        """
        updated_flowers = set()  # Original would be affected otherwise!
        for x in range(area[0], area[2] + 1):
            for y in range(area[1], area[3] + 1):
                if (x, y) in flowers:
                    updated_flowers.add((x, y))
        return updated_flowers

    @staticmethod
    def check_for_flowers(area, flowers):
        """
        Return True, if area contains one or more flowers.
        Otherwise False.
        """
        for x in range(area[0], area[2] + 1):
            for y in range(area[1], area[3] + 1):
                if (x, y) in flowers:
                    return True
        return False

    @staticmethod
    def get_furthest_flower_in_direction(area, flowers, direction):
        """
        Return the (x, y) of the flower furthes away from the initial
        cutting position of the area depending on the cut direction.
        """
        if direction == "vertical":
            for x in range(area[2], area[0] - 1, -1):
                for y in range(area[1], area[3] + 1):
                    if (x, y) in flowers:
                        return (x, y)
        else:
            for y in range(area[3], area[1] - 1, -1):
                for x in range(area[0], area[2] + 1):
                    if (x, y) in flowers:
                        return (x, y)

        return (0, 0)

    @staticmethod
    def get_cut_direction(area):
        """
        Decides the direction of the cut.
        """
        if area[2] - area[0] > area[3] - area[2]:
            return "vertical"
        return "horizontal"

    @staticmethod
    def switch_direction(direction):
        """
        Switches the cut direction: "vertical"/"horizontal"
        """
        return "vertical" if direction == "horizontal" else "horizontal"

    @staticmethod
    def split_area_halves(area, direction):
        """
        Splits the given area into halves in the given direction.
        Returns the cut halves.
        """
        if direction == "vertical":
            first_half = (area[0], area[1], area[0] + (area[2] - area[0]) // 2, area[3])
            second_half = (first_half[2] + 1, area[1], area[2], area[3])
        else:
            first_half = (area[0], area[1], area[2], area[1] + (area[3] - area[1]) // 2)
            second_half = (area[0], first_half[3] + 1, area[2], area[3])
        return first_half, second_half

    @classmethod
    def cut_the_cake(cls, cake):
        """
        Cuts the given cake object into pieces with a single flower.
        Pieces are stored in cake.pieces attribute.
        """
        area = (1, 1, cake.width, cake.height)
        flowers = cake.flowers
        direction = cls.get_cut_direction(area)
        pieces = set()
        cls.recursion_cut(area, flowers, direction, pieces)
        index = 1
        for piece in pieces:
            cake.pieces[piece] = index
            index += 1

    @classmethod
    def recursion_cut(cls, area, flowers, direction, pieces):
        """
        Cuts the cake using the power of RECURSION!
        Returns a dict containing the ready pieces (index): (x1, y1, x2, y2)
          pieces: an empty set for the flowers!
        """
        # print("Recursion cut called ------")
        # print("    area:", area, "pieces:", pieces, "direction:", direction)
        flowers_in_area = cls.get_updated_flowers_in_area(area, flowers)

        # Base case: piece ready --> return
        if len(flowers_in_area) == 1:
            # print("   DONE! 1 flower left in cut!")
            # print("   added piece:", area, "to pieces")
            pieces.add(area)
            # print("RETURN! Should be done! \n\n")
            return

        # Split in half
        first_half, second_half = cls.split_area_halves(area, direction)
        # print("    Split into:", first_half, second_half)

        # Halves OK --> it's recursion time!
        # print("     Calling recursion if both cuts are good")
        if cls.check_for_flowers(first_half, flowers) and cls.check_for_flowers(
            second_half, flowers
        ):
            cls.recursion_cut(
                first_half, flowers, cls.get_cut_direction(first_half), pieces
            )
            cls.recursion_cut(
                second_half, flowers, cls.get_cut_direction(second_half), pieces
            )
            return

        # A half was empty! Try a large cut!
        # print("    BAD! A half was empty!")
        target_flower = cls.get_furthest_flower_in_direction(area, flowers, direction)
        # print("   target_flower:", target_flower, "cut:", direction)
        if direction == "vertical":
            # print("        split is:", direction)
            first_half = (area[0], area[1], target_flower[0] - 1, area[3])
            second_half = (first_half[2] + 1, area[1], area[2], area[3])
        else:
            # print("        split is:", direction)
            first_half = (area[0], area[1], area[2], target_flower[1] - 1)
            second_half = (area[0], first_half[3] + 1, area[2], area[3])
        # print("    Cut adjusted")
        # print("    Halves are now:", first_half, second_half)

        # New cut OK!
        # print("    Checking if second adjusted cut was OK...")
        if cls.check_for_flowers(first_half, flowers) and cls.check_for_flowers(
            second_half, flowers
        ):
            cls.recursion_cut(
                first_half, flowers, cls.get_cut_direction(first_half), pieces
            )
            cls.recursion_cut(
                second_half, flowers, cls.get_cut_direction(second_half), pieces
            )
            return

        # Cut is SUPERBAD! Redo with a new direction
        # print("    SUPERBAD! Switching direction for area:", area)
        # print("    Cut is now", direction)
        cls.recursion_cut(area, flowers, cls.switch_direction(direction), pieces)
        return


if __name__ == "__main__":
    print("Hello Cutter!")
