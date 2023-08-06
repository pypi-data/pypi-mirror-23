# -*- coding: utf-8 -*-

# Copyright 2017 Mike Fährmann
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as
# published by the Free Software Foundation.

"""Extract manga-chapters and entire manga from https://mangazuki.co/"""

from .common import Extractor, MangaExtractor, Message
from .. import text, util, exception


class MangazukiChapterExtractor(Extractor):
    """Extractor for manga-chapters from mangazuki.co"""
    category = "mangazuki"
    subcategory = "chapter"
    directory_fmt = ["{category}", "{manga}", "c{chapter:>03}"]
    filename_fmt = ("{manga}_c{chapter:>03}_{page:>03}.{extension}")
    pattern = [r"(?:https?://)?((raws\.)?mangazuki\.co/read/[^/]+/\d+)"]
    test = [
        ("https://mangazuki.co/read/Double-Casting/59", {
            "url": "47b4102da3ee1bd28459848904e8b7ff48e1ac5e",
            "keyword": "b4cac50b3a3a1dd06451d1917a0faae2c6a51b95",
        }),
        ("https://raws.mangazuki.co/read/Rakujitsu-no-Pathos/25", {
            "url": "c1c95d9954185f53a8449f497239aee181bea4af",
            "keyword": "7554ca641f10e84fa5594e5ff8bd3925a5ff2e80",
        }),
        ("https://mangazuki.co/read/Double-Casting/999", {
            "exception": exception.NotFoundError,
        }),
    ]

    def __init__(self, match):
        Extractor.__init__(self)
        self.url = "https://" + match.group(1)
        self.lang = "" if match.group(2) else "en"

    def items(self):
        response = self.request(self.url)
        if response.history:
            raise exception.NotFoundError("chapter")
        page = response.text
        data = self.get_metadata(page)
        imgs = self.get_images(page)
        data["count"] = len(imgs)

        yield Message.Version, 1
        yield Message.Directory, data
        for data["page"], url in enumerate(imgs, 1):
            yield Message.Url, url, text.nameext_from_url(url, data)

    def get_metadata(self, page):
        """Collect metadata for extractor-job"""
        data = {
            "lang": self.lang,
            "language": util.code_to_language(self.lang, self.lang),
        }
        return text.extract_all(page, (
            (None     , "<title>Mangazuki", ""),
            ("manga"  , " - ", " - Chapter "),
            ("chapter", "", "</title>"),
        ), values=data)[0]

    @staticmethod
    def get_images(page):
        """Return a list of all image-urls"""
        return list(text.extract_iter(page, 'data-src="', '"'))


class MangazukiMangaExtractor(MangaExtractor):
    """Extractor for manga from mangazuki.co"""
    category = "mangazuki"
    pattern = [r"(?:https?://)?((?:raws\.)?mangazuki\.co/series/[^/?&#]+)"]
    scheme = "https"
    test = [
        ("https://mangazuki.co/series/Double-Casting", {
            "url": "aab747414191b14e768f4a1eb148448d83ef2e14",
        }),
        ("https://raws.mangazuki.co/series/Rakujitsu-no-Pathos", {
            "url": "4c5fcee4ad306faa3cfe952f7474293a99d11787",
        }),
    ]

    def chapters(self, page):
        params = {"page": 1}
        chlist = []

        while True:
            chlist.extend(
                text.extract_iter(page, '<li class="media"><a href="', '"'))
            if 'class="next disabled"' in page:
                break
            params["page"] += 1
            page = self.request(self.url, params=params).text

        return chlist
