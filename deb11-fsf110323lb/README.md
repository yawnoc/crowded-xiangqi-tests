# (Debian 11, XBoard 4.9.1, Fairy-Stockfish 110323 LB)

- Debian 11 (Linux metabox 5.10.0-21-amd64 #1 SMP Debian 5.10.162-1 (2023-01-21) x86_64 GNU/Linux)
- Xboard 4.9.1 installed by running `sudo apt install xboard`
- "Fairy-Stockfish 110323 LB" compiled from [Fairy-Stockfish @ ea83afa] (with `crowdedxiangqi` added to `variants.ini`) by running `make net; make build ARCH=x86-64-avx512 largeboards=yes all=yes`

[Fairy-Stockfish @ ea83afa]: https://github.com/fairy-stockfish/Fairy-Stockfish/commit/ea83afa32df00530b331934c257f3599e44912b0
