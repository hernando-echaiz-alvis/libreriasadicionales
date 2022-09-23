API Documentation - Pokédex documentation    body { --color-code-background: #f8f8f8; --color-code-foreground: black; } @media not print { body\[data-theme="dark"\] { --color-code-background: #202020; --color-code-foreground: #d0d0d0; } @media (prefers-color-scheme: dark) { body:not(\[data-theme="light"\]) { --color-code-background: #202020; --color-code-foreground: #d0d0d0; } } } document.body.dataset.theme = localStorage.getItem("theme") || "auto"; Contents Menu Expand Light mode Dark mode Auto light/dark mode  

Hide navigation sidebar

Hide table of contents sidebar

Toggle site navigation sidebar

[

Pokédex documentation

](index.html)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

[Pokédex documentation](index.html)

  

Contents:

*   [Quickstart](quickstart.html)
*   [API Documentation](#)

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

API Documentation[#](#module-pokedex "Permalink to this heading")
=================================================================

_class_ pokedex.Bulbasaur[#](#pokedex.Bulbasaur "Permalink to this definition")

Bulbasaur is a dual-type Grass/Poison Pokémon introduced in Generation I.

It evolves into Ivysaur starting at level 16, which evolves into Venusaur starting at level 32.

Along with [`Charmander`](#pokedex.Charmander "pokedex.Charmander") and [`Squirtle`](#pokedex.Squirtle "pokedex.Squirtle"), Bulbasaur is one of three starter Pokémon of Kanto available at the beginning of Pokémon Red, Green, Blue, FireRed, and LeafGreen.

_class_ pokedex.Charmander[#](#pokedex.Charmander "Permalink to this definition")

Charmander is a Fire-type Pokémon introduced in Generation I.

It evolves into Charmeleon starting at level 16, which evolves into Charizard starting at level 36.

Along with [`Bulbasaur`](#pokedex.Bulbasaur "pokedex.Bulbasaur") and [`Squirtle`](#pokedex.Squirtle "pokedex.Squirtle"), Charmander is one of three starter Pokémon of Kanto available at the beginning of Pokémon Red, Green, Blue, FireRed, and LeafGreen.

Note

Charmeleon and Charizard are fire-type Pokémon, but Mega Charizard X and Gigantamax Charizard are also Flying Pokémon, while Mega Charizard Y is a Dragon-type Pokémon.

_class_ pokedex.Squirtle[#](#pokedex.Squirtle "Permalink to this definition")

Squirtle is a Water-type Pokémon introduced in Generation I.

It evolves into Wartortle starting at level 16, which evolves into Blastoise starting at level 36.

Along with [`Bulbasaur`](#pokedex.Bulbasaur "pokedex.Bulbasaur") and [`Charmander`](#pokedex.Charmander "pokedex.Charmander"), Squirtle is one of three starter Pokémon of Kanto available at the beginning of Pokémon Red, Green, Blue, FireRed, and LeafGreen.

_class_ pokedex.StarterPokemon[#](#pokedex.StarterPokemon "Permalink to this definition")

This class defined one of the starter Pokémon given to the player by Professor Oak at the start of Pokémon Red, Green, Blue, FireRed, and LeafGreen.

Actual Pokémon can be created by calling the specific classes defining the starter Pokémon types. You can see more details about them at [About starter Pokémon](quickstart.html#starter).

who\_is\_that\_pokemon()[#](#pokedex.StarterPokemon.who_is_that_pokemon "Permalink to this definition")

Shows the Pokémon name and its evolution.

Usage:

\>>> import pokedex
\>>> friend \= pokedex.Bulbasaur()
\>>> friend.who\_is\_that\_pokemon()
This pokemon is Bulbasaur.
It will evolve into Ivysaur, Venusaur, Mega Venusaur, Gigantamax Venusaur.
\>>>

[

Previous

Quickstart



](quickstart.html)

Copyright © 2021, melissawm

Made with [Sphinx](https://www.sphinx-doc.org/) and [@pradyunsg](https://pradyunsg.me)'s [Furo](https://github.com/pradyunsg/furo)