"""Coolest-art-01 entry (Python 3.13, standard library only).

The art is entry-lantern-moon.jpg beside this file: a minimalist
ukiyo-e print of a huge golden paper lantern, the moon, hanging by a
thin string in a deep-navy night sky, a tiny black-silhouette figure
on a cliff below holding the string. The moon is a lantern.
The program copies it to /output/entry.png.

The gate accepts a PNG or a JPEG at /output/entry.png, told apart by
its first bytes; the name stays entry.png either way. The file is a
whole JPEG of 326563 bytes and 1024 by 1024 pixels, inside the
1 MiB and 1024 by 1024 limits.

Deterministic: no network, no randomness, no clock. It copies the
same bytes every run, so two runs write byte-identical output.

Local run: mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import hashlib
import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
ARTWORK = "entry-lantern-moon.jpg"
SRC = HERE / ARTWORK
OUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
DST = OUT_DIR / "entry.png"


def main():
    if not SRC.is_file():
        raise FileNotFoundError(f"artwork missing: {SRC}")
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SRC, DST)
    # Byte-exact copy: the judge sees exactly the bytes in the file,
    # so refuse to leave a partial or mismatched output behind.
    if DST.stat().st_size != SRC.stat().st_size:
        raise RuntimeError("output does not match the source image")
    if hashlib.sha256(DST.read_bytes()).hexdigest() != hashlib.sha256(
        SRC.read_bytes()
    ).hexdigest():
        raise RuntimeError("output hash does not match the source image")


if __name__ == "__main__":
    main()
