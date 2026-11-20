#!/usr/bin/env python3
"""Copy the bundled front-page image to the output directory.

The repository holds entry.png, a newspaper front page summing up the
world news of Friday 20 November 2026. This program copies it to
$MAKEFUN_OUTPUT_DIR/entry.png (default /output), creating the output
directory if it does not exist yet.
"""

import hashlib
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.png")


def sha256_of(path):
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dest = os.path.join(out_dir, "entry.png")
    shutil.copyfile(SOURCE, dest)
    src_size = os.path.getsize(SOURCE)
    dst_size = os.path.getsize(dest)
    if dst_size != src_size:
        raise SystemExit(
            "size mismatch: copied %d bytes, expected %d" % (dst_size, src_size)
        )
    print("wrote", dest, "%d bytes" % dst_size)
    print("sha256", sha256_of(dest))


if __name__ == "__main__":
    main()
