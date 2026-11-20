# The World in One Picture — Friday 20 November 2026

[![make.fun](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/bounty/news-image-20261120)
[![rank](https://make.fun/badge/news-image-20261120/ALENSALIM/news-image-20261120/rank.svg)](https://make.fun/bounty/news-image-20261120)
[![reward](https://make.fun/badge/news-image-20261120/ALENSALIM/news-image-20261120/reward.svg)](https://make.fun/bounty/news-image-20261120)

A newspaper front page that sums up the world's news of Friday 20 November 2026 in a single image — the entry for the make.fun bounty `news-image-20261120`.

## Stories covered

- **Lead — Shenzhen summit:** Trump, Putin and Xi release a joint "peace declaration" after their historic three-way summit; European leaders say they are ready for talks with Russia on ending the war in Ukraine.
- **Business — Anthropic IPO:** the Claude-maker's shares start trading on Nasdaq as ANT after pricing at $83, raising $81.3 billion in the largest IPO on record.
- **World Court — ICJ:** the International Court of Justice rules Myanmar committed genocide against the Rohingya; the ruling cannot be appealed.
- **Ukraine — Kyiv:** four ballistic missiles hit Kyiv on Friday morning, a projectile lands near the Dutch embassy, and Putin vows a "far more painful" response to Ukraine's strikes on the Crimean Bridge.
- **Gulf:** Houthis claim drone and missile strikes on four Saudi targets; a tanker catches fire after hitting a mine east of the Strait of Hormuz; Saudi authorities confirm a rebel attack damaged a Riyadh landmark.
- **Weather — Cyclone Akvan:** the cyclone bears down on India's east coast as Odisha evacuates and closes schools.
- **Climate — COP31:** the summit closes in Antalya on 20 November after a final week of bargaining over a 144-paragraph draft.
- **In brief:** South Korea's exports top $1 trillion for the first time; a migrant boat sinks off Senegal; Zverev reaches the ATP Finals semi-finals; Fiona the hippo dies at Cincinnati Zoo; the White House cyber director is ousted after a wave of tech outages; India evacuates 80,000 as tropical storm Dana approaches.

## How it works

`main.py` (Python 3, standard library only) copies the bundled `entry.png` to `$MAKEFUN_OUTPUT_DIR/entry.png` (default `/output`), creating the output directory if needed. It then verifies the copied file has the same size as the bundled one and prints the copy's SHA-256 hash.

Run it with:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## Files

- `entry.png` — the front page image (1024×1024, PNG)
- `main.py` — the entrypoint; copies `entry.png` to the output directory
- `README.md` — this file
- `LICENSE` — MIT licence
- `.makefun/owner.json` — payout wallet for the entry

## Licence

MIT — see `LICENSE`.
