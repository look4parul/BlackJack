class Error:
    @staticmethod
    def in_Error():
        while True:
            hit_status = input()
            if hit_status == "y" or hit_status == "Y" or hit_status == "n" or hit_status == "N":
                return hit_status
            else:
                print("Please enter (Y/N) ")
                # return hit_status
    
    @staticmethod
    def chip_error(have_Chip):
        while True:
            try:
                x = int(input())
            except:
                print("need to be int ")
            else:
                if x > have_Chip:
                    print(
                        "Sorry, You do not have enough Chips , you have {} ".format(
                            have_Chip
                        )
                    )
                elif x <= 0:
                    print("num need to be > 0")
                else:
                    return x
            finally:
                print("")
