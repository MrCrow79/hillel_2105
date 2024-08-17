import configparser
import pathlib
from os.path import join

ROOT_PATH = str(pathlib.Path(__file__).parent.parent.resolve())


settings = configparser.ConfigParser()
settings.read(join(ROOT_PATH, 'config_file.ini'))

# join(r'D:\asd', 'file.txt') =>D:\asd\file.txt  for win and //D/asd/file.txt

