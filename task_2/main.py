from src.decorators import handle_errors
from src.handlers import parse_rec_depth, draw_koch_snowflake, koch_line

@handle_errors
def main():
    rec_depth = parse_rec_depth(input("Hello! "
    "Please, enter the recursion level to build the Koch snowflake: "))

    draw_koch_snowflake(rec_depth)

    print("The Koch snowflake is built.")

if __name__ == "__main__":
    main()
