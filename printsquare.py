"""
COMP.CS.100 Programming 1
Template for task: box printing
"""

def print_box(w, h, m):
    for i in range(1, h+1):
        print(f"{m*w}")



def main():
    width = int(input("Enter the width of a frame: "))
    height = int(input("Enter the height of a frame: "))
    mark = input("Enter a print mark: ")

    print()
    print_box(width, height, mark)


if __name__ == "__main__":
    main()
