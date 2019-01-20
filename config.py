import os

from dotenv import load_dotenv

load_dotenv(verbose=True)
VIDEO_DIR = os.getenv("VIDEO_DIR")
GCID = os.getenv("GCID")
GCESS = os.getenv("GCESS")
CID = os.getenv("CID")
