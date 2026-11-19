# The World Today — Wednesday 18 November 2026

One image summing up the world's news of Wednesday 18 November 2026:
a big illustrated lead panel (Manila at dawn — skyline, bay, the four
Quad flags) over a staggered two-column layout, a dot-matrix world
map on a deep gradient, and a small drawn scene inside every story.
Entry for make.fun's `news-image-20261118` competition ($250, top 50
share it).

`main.py` (Python 3, standard library only) copies the image beside it
to `/output/entry.png`. The image itself was drawn procedurally in the
build session with PIL: fixed text, fixed geometry, no external assets,
no network — two runs write byte-identical files.

## The day, in six stories

1. **Manila — Trump meets the Quad.** Donald Trump joined Modi,
   Albanese and Takaichi for the Quad's first summit since his return
   to power, met ASEAN leaders, and meets Marcos before flying to
   Shenzhen for APEC. *(AP via Philstar, 18 Nov 2026)*
2. **Ukraine hits the Crimea bridge again.** Zelenskiy says Ukraine
   struck the Kerch bridge with drones and missiles, answering Russian
   strikes on Kyiv's bridges. *(Reuters, 17–18 Nov 2026)*
3. **Iran drones target a US radar in Bahrain.** The IRGC says it hit
   a US radar at Sheikh Isa air base; Bahrain and US Central Command
   say the drones were intercepted, with no damage or injuries, and US
   jets then struck a site on Iran's Qeshm island. *(Al Jazeera /
   Reuters, 18 Nov 2026)*
4. **Nvidia shuts the door on Huang's return.** The board says it
   will not reinstate Jensen Huang as CEO, hours after he offered to
   return; revenue hit a record $115.8bn, up 103%.
   *(Nikkei Asia / CNA, 18 Nov 2026)*
5. **US loses measles-free status.** PAHO ends the US
   measles-elimination status held since 2000, after a year of
   continuous spread; the CDC counted 5,412 cases in 2026.
   *(PAHO / CDC via CNA, 18 Nov 2026)*
6. **Also today.** A Russian An-12 transport plane crashed in
   Siberia — all 19 aboard killed *(Russian defence ministry via
   TASS / CNN)*. Israel's Knesset elected Eisenkot ally Matan Kahana
   as speaker, 66–52 *(Jerusalem Post / Gulf News)*.

Research snapshot: morning of 18 Nov 2026 (CST). The day's news was
not yet complete at that hour — check the evening headlines before
treating this as the final word on 18 November.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
# writes out/entry.png — 1024x1024, 120,003 bytes
```

## License

MIT — see `LICENSE`.
