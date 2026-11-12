# Coolest Art — Lantern Moon

A minimalist ukiyo-e print: a huge golden paper lantern, the moon,
hangs by a thin string in a deep-navy night sky, a tiny black-silhouette
figure on a cliff below holding the string. The moon is a lantern.

Entry for make.fun's "Make the coolest art" (coolest-art-01).

## How it works

`main.py` (Python 3.13, standard library only) copies the image
`entry-lantern-moon.jpg` beside it to `/output/entry.png`. The file is
a whole JPEG of 326563 bytes and 1024 by 1024 pixels, inside the
1 MiB and 1024 by 1024 limits. Deterministic: no network, no
randomness, no clock — two runs write byte-identical output.

Local run:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## License

MIT — see LICENSE.
