# execution of derivative pricer 
import model
import argparse

def main():
    pass


def _parser():
    """ CLI args """
    parser = argparse.ArgumentParser(description="options")

    parser.add_argument("-s", dest="spot0", type=float, help="spot price")
    return parser.parse_args()


kwargs = vars(_parser())
if __name__ == "__main__":
    main()
