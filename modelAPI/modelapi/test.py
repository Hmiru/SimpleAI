import os
from dotenv import load_dotenv

load_dotenv()
pythonpath = os.getenv('PYTHONPATH')
print(pythonpath)