import { loadFont } from "@remotion/fonts";
import { staticFile } from "remotion";

// Lettertypes staan lokaal in public/fonts (OFL-licentie). Nooit van internet laden tijdens
// het renderen: in de cloud vertrouwt de headless browser de proxy-certificaten niet.
const bestanden = [
  { family: "IBM Plex Sans", weight: "400", file: "ibm-plex-sans-latin-400-normal.woff2" },
  { family: "IBM Plex Sans", weight: "600", file: "ibm-plex-sans-latin-600-normal.woff2" },
  { family: "IBM Plex Sans", weight: "700", file: "ibm-plex-sans-latin-700-normal.woff2" },
  { family: "Noto Sans", weight: "400", file: "noto-sans-latin-400-normal.woff2" },
  { family: "Noto Sans", weight: "600", file: "noto-sans-latin-600-normal.woff2" },
  { family: "Noto Sans", weight: "700", file: "noto-sans-latin-700-normal.woff2" },
];

for (const f of bestanden) {
  loadFont({ family: f.family, url: staticFile(`fonts/${f.file}`), weight: f.weight });
}

export const titelFont = "IBM Plex Sans";
export const tekstFont = "Noto Sans";
