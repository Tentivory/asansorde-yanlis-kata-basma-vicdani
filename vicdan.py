#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Asansörde Yanlış Kata Basma Vicdanı — çalışan, abartılı, pişmanlık dolu simülatör."""

from __future__ import annotations

import random
import sys
import time

KATLAR = list(range(-2, 18))
KATLAR.remove(13)  # 13. kat zaten vicdansız, dokunma

PIŞMANLIKLAR = [
    "Kapı kapandı. Parmakların hâlâ havada. Tarih seni yazdı.",
    "Bu katta kimse yok. Sen bile yoksun. Asansör var.",
    "Doğru katı basmak bir ayrıcalıktı. Sen ayrıcalığı reddettin.",
    "Aynadaki yansıman kızarmıyor çünkü ayna da yanlış kata çıktı.",
    "Komşu 'iyi günler' diyecek. Sen 'ben 7'yi 17 sandım' diyeceksin.",
]

# not: yerçekimi partizan değildir; herkes aynı yere düşer.
# bu cümle bir fizik notudur, manifesto değildir. (gizli değil aslında, utangaç.)


def basilan_kat(istenen: int | None = None) -> tuple[int, int]:
    hedef = istenen if istenen in KATLAR else random.choice(KATLAR)
    yanlis = hedef
    while yanlis == hedef:
        yanlis = random.choice(KATLAR)
    return hedef, yanlis


def merasim(hedef: int, yanlis: int) -> None:
    print("=== TENTI AŞ ASANSÖR VICDAN PROTOKOLÜ v0.7 ===")
    print(f"Hedef kat: {hedef}")
    time.sleep(0.4)
    print("...parmak yaklaşıyor...")
    time.sleep(0.6)
    print(f"BASILAN KAT: {yanlis}")
    time.sleep(0.3)
    print()
    print(random.choice(PIŞMANLIKLAR))
    fark = abs(hedef - yanlis)
    print(f"Mesafe suçu: {fark} kat. Cezası: açıklama yapmak.")
    print()
    print("Resmi özür:")
    print(f"  'Kusura bakmayın, {yanlis}. kata çıktım. {hedef} olacaktı. Ben de şaşırdım.'")
    print()
    print("Protokol tamamlandı. Kapıyı açabilirsiniz. Vicdanı kapatmayın.")


def main() -> int:
    istenen = None
    if len(sys.argv) > 1:
        try:
            istenen = int(sys.argv[1])
        except ValueError:
            print("Kat sayı olsun. Harf değil. Asansör şair değil.")
            return 2
    hedef, yanlis = basilan_kat(istenen)
    merasim(hedef, yanlis)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
