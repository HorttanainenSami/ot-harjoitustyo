import os
from dotenv import load_dotenv

dirname = os.path.dirname(__file__)
load_dotenv(dotenv_path=os.path.join(dirname, '..', '.env'))


DATABASE_FILENAME = os.getenv('DATABASE_FILENAME')
DATABASE_FILE_PATH = os.path.join(dirname, '..', 'data', DATABASE_FILENAME)
