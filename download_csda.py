#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Print out all of the available links to CVVM Naše Společnost data and
documentation available in the Czech Social Science Data Archive.

These links are to be downloaded via Firefox's add-on
https://addons.mozilla.org/cs/firefox/addon/open-multiple-urls/ .

The partly-manual solution is used as the most time-effective.
"""


import os

link = "http://nesstar.soc.cas.cz/webview/velocity?format=CSV&includeDocumentation=on&execute=true&ddiformat=pdf&analysismode=table&study=http%3A%2F%2F147.231.52.118%3A80%2Fobj%2FfStudy%2FV0101&v=2&mode=download&onaccess=true"

for year in range(0, 100):
    year_str = "{0:02d}".format(year)
    for month in range(1, 13):
        month_str = "{0:02d}".format(month)
        path = "csda/V{0}{1}.zip".format(year_str, month_str)
        link = ("http://nesstar.soc.cas.cz/webview/velocity?format=CSV"
                "&includeDocumentation=on&execute=true&ddiformat=pdf"
                "&analysismode=table&study=http%3A%2F%2F147.231.52.118"
                "%3A80%2Fobj%2FfStudy%2FV{0}{1}&v=2"
                "&mode=download&onaccess=true").format(year_str, month_str)
        if not os.path.isfile(path):
            print(link)
