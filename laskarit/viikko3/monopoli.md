```mermaid
classDiagram
    class Monopolipeli {
        aloitusruudun_sijainti
        vankilan_sijainti
    }

    class Ruutu {
        seuraava
    }

    class Aloitusruutu {
        toiminto()
    }

    class Vankila {
        toiminto()
    }

    class Toimintokortti {
        toiminto()
    }

    class Asemat_ja_laitokset {
        toiminto()
    }

    class Katu {
        nimi
        talojen_maara
        hotelli
        toiminto()
    }

    class Pelaaja {
        rahaa
    }

    class Pelinappula
    class Pelilauta
    class Sattuma_ja_yhteismaa

    Monopolipeli "1" -- "2" Noppa
    Monopolipeli "1" -- "1" Pelilauta
    Pelilauta "1" -- "40" Ruutu
    Ruutu "1" -- "0..1" Aloitusruutu
    Ruutu "1" -- "0..1" Vankila
    Ruutu "6" -- "0..1" Sattuma_ja_yhteismaa
    Sattuma_ja_yhteismaa "1" -- "1" Toimintokortti
    Ruutu "6" -- "0..1" Asemat_ja_laitokset
    Ruutu "22" -- "0..1" Katu
    Ruutu "1" -- "0..8" Pelinappula
    Pelinappula "1" -- "1" Pelaaja
    Pelaaja "2..8" -- "1" Monopolipeli
    Pelaaja "1" -- "0..22" Katu
```