#!/usr/bin/env python3
"""Machinale stijlcontrole op AI-tells (zie guides/anti-ai-style.md).

Gebruik:  python scripts/check_style.py weeks/2026-43/video-01/caption.txt [meer bestanden]
Exitcode 0 = geen fouten, 1 = fouten gevonden. Waarschuwingen blokkeren niet.
"""
import re
import sys
from pathlib import Path

VERBODEN = [
    # Engels
    r"\bunlock", r"\bdive into\b", r"\bdelve", r"game[- ]changer", r"\belevate",
    r"\bunleash", r"\bseamless", r"\blevel up\b", r"\bready to\b", r"\blet'?s\b.*!",
    r"look no further", r"whether you'?re", r"fast-paced world", r"next level",
    r"\bthe ultimate\b", r"\brevolutioni[sz]e", r"\bembark", r"\bvibrant\b",
    # Nederlands
    r"ontdek de wereld van", r"\bduik in\b", r"naar een hoger niveau", r"\bklaar om\b",
    r"\blaten we\b.*!", r"\bde ultieme\b", r"\bnaadloos", r"\bontgrendel",
    r"ben jij er klaar voor", r"het is tijd om", r"in een wereld waar",
    r"niet alleen .{1,40} maar ook", r"\bof je nu\b", r"\bboordevol\b",
    r"unieke ervaring", r"\bmust-have\b", r"\biconisch",
]

EMOJI = re.compile(
    "[\U0001F300-\U0001FAFF\U00002600-\U000027BF\U0001F000-\U0001F2FF]", flags=re.UNICODE
)


def controleer(pad: Path) -> tuple[list[str], list[str]]:
    tekst = pad.read_text(encoding="utf-8")
    laag = tekst.lower()
    fouten, waarschuwingen = [], []

    for patroon in VERBODEN:
        m = re.search(patroon, laag)
        if m:
            fouten.append(f"AI-cliché: '{m.group(0)}'")

    if "—" in tekst:
        fouten.append("lang gedachtestreepje (—)")

    emoji = EMOJI.findall(tekst)
    if len(emoji) > 2:
        fouten.append(f"{len(emoji)} emoji (max 2)")

    if tekst.count("!") > 1:
        fouten.append(f"{tekst.count('!')} uitroeptekens (max 1)")

    hashtags = re.findall(r"#\w+", tekst)
    if len(hashtags) > 5:
        fouten.append(f"{len(hashtags)} hashtags (max 5)")

    # Drieslag: "x, y en z" met korte woorden, of drie korte zinnen met punt.
    if re.search(r"\b\w+, \w+ en \w+\b", laag):
        waarschuwingen.append("mogelijke drieslag ('x, y en z'): bewust?")
    if re.search(r"(?:^|\n)\s*\w+\.\s+\w+\.\s+\w+\.", tekst):
        waarschuwingen.append("drie korte zinnen na elkaar ('Snel. Simpel. Sociaal.')")

    regels = [r for r in tekst.splitlines() if r.strip() and not r.strip().startswith("#")]
    if len(regels) > 4:
        waarschuwingen.append(f"{len(regels)} regels tekst: kan het korter?")

    return fouten, waarschuwingen


def main() -> int:
    sys.stdout.reconfigure(encoding="utf-8")  # Windows-console
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    totaal = 0
    for arg in sys.argv[1:]:
        pad = Path(arg)
        fouten, waarschuwingen = controleer(pad)
        status = "OK" if not fouten else "FOUT"
        print(f"[{status}] {pad}")
        for f in fouten:
            print(f"   ✗ {f}")
        for w in waarschuwingen:
            print(f"   ! {w}")
        totaal += len(fouten)
    return 1 if totaal else 0


if __name__ == "__main__":
    sys.exit(main())
