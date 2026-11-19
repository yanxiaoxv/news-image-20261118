"""News image of Wednesday 18 November 2026 - entry program.

The image lives beside this file as entry.png: a one-page newspaper
summary of the day's world news, drawn procedurally in this session
(PIL, fixed text and geometry, no external assets). This program's whole
job is to deliver those exact bytes, unchanged, to /output/entry.png on
every run, so two runs write byte-identical files. It uses only the
Python standard library, needs no network, and reads nothing outside
its own directory.

Local check:  mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))

OUT_DIR.mkdir(parents=True, exist_ok=True)
shutil.copyfile(HERE / "entry.png", OUT_DIR / "entry.png")
