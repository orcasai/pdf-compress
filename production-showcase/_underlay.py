#!/usr/bin/env python3
"""Underlay a solid color rectangle on every page of a PDF.

Usage: _underlay.py <in.pdf> <out.pdf> <#hex>
"""
import sys
import fitz


def main():
    inp, out, hex_color = sys.argv[1], sys.argv[2], sys.argv[3]
    h = hex_color.lstrip("#")
    r, g, b = (int(h[i:i+2], 16) / 255 for i in (0, 2, 4))
    doc = fitz.open(inp)
    for page in doc:
        page.draw_rect(
            page.rect,
            color=(r, g, b),
            fill=(r, g, b),
            overlay=False,
            width=0,
        )
    doc.save(out, incremental=False, deflate=True)


if __name__ == "__main__":
    main()
