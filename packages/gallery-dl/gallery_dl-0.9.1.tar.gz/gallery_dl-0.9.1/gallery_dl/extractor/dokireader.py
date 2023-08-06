# -*- coding: utf-8 -*-

# Copyright 2016-2017 Mike Fährmann
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as
# published by the Free Software Foundation.

"""Extractors for https://kobato.hologfx.com/"""

from . import foolslide


class DokireaderChapterExtractor(foolslide.FoolslideChapterExtractor):
    """Extractor for manga-chapters from kobato.hologfx.com"""
    category = "dokireader"
    pattern = foolslide.chapter_pattern(r"kobato\.hologfx\.com/reader")
    test = [(("https://kobato.hologfx.com/reader/read/"
              "hitoribocchi_no_oo_seikatsu/en/3/34"), {
        "keyword": "1dc1ec8264df4126552dbe53f42c5643fd2a4cf3",
    })]


class DokireaderMangaExtractor(foolslide.FoolslideMangaExtractor):
    """Extractor for manga from kobato.hologfx.com"""
    category = "dokireader"
    pattern = foolslide.manga_pattern(r"kobato\.hologfx\.com/reader")
    test = [(("https://kobato.hologfx.com/reader/series/"
              "boku_ha_ohimesama_ni_narenai/"), {
        "url": "1c1f5a7258ce4f631f5fc32be548d78a6a57990d",
    })]
