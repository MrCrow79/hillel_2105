import configparser
import pathlib
from os.path import join
import load_dotenv

ROOT_PATH = str(pathlib.Path(__file__).parent.parent.resolve())

load_dotenv.load_dotenv(join(ROOT_PATH, '.env'))


settings = configparser.ConfigParser()
settings.read(join(ROOT_PATH, 'config_file.ini'))

# join(r'D:\asd', 'file.txt') =>D:\asd\file.txt  for win and //D/asd/file.txt

