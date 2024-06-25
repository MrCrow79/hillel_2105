import os

if __name__ == '__main__':
    os.system(f'pytest . -m {os.environ['MARKS']}')