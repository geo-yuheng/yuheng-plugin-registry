import os

def main():
    return os.listdir(os.path.dirname(__file__),"..")

if __name__ == "__main__":
    main()