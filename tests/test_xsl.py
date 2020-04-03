# --
# Copyright (c) 2008-2020 Net-ng.
# All rights reserved.
#
# This software is licensed under the BSD License, as described in
# the file LICENSE.txt, which you should have received as part of
# this distribution.
# --

import os

from lxml import etree

from nagare.renderers import xml
from nagare.renderers import xsl, xsl2, xsl3


def create_stylesheet(x):
    h = xml.Renderer()

    return x.stylesheet(
        x.output(encoding='utf-8', method='html'),
        x.template(x.copy(x.apply_templates(select='@*|node()')), match='@*|node()'),
        x.template(x.copy(x.apply_templates), match='world'),
        x.template(
            h.html(
                h.head,
                h.body(
                    x.apply_templates(select='@*|node()')
                )
            ),
            match='hello'
        ),
        x.template(
            x.element(x.value_of(select="@language"), ' : ', x.value_of(select="."), name="h1"),
            match="world"
        ),
        version='1.0'
    )


def test1():
    for x in (xsl.Renderer(), xsl2.Renderer(), xsl3.Renderer()):
        style_sheet = create_stylesheet(x)
        root = x.fromfile(os.path.join(os.path.dirname(__file__), 'test_xmlns_1.xml'))
        r = root.getroottree().xslt(style_sheet)

        r = etree.tostring(r, pretty_print=True, encoding='utf-8')
        r = [l.strip() for l in r.splitlines()]

        with open(os.path.join(os.path.dirname(__file__), 'helloworld.html'), 'rb') as f:
            xml_to_compare = [l.strip() for l in f]

        assert r == xml_to_compare


def test2():
    for x in (xsl.Renderer(), xsl2.Renderer(), xsl3.Renderer()):
        style_sheet = x.stylesheet(
            x.output(encoding='utf-8'),
            x.template(
                x.copy_of(select='.'), match='/'
            )
        )

        h = xml.Renderer()
        page = h.html(h.h1('Hello'), h.h2('World'))

        r = page.getroottree().xslt(style_sheet)

        assert r.xpath('//html/h1')[0].text == 'Hello'
        assert r.xpath('//html/h2')[0].text == 'World'


def test_identity():
    for x in (xsl.Renderer(), xsl2.Renderer(), xsl3.Renderer()):
        style_sheet = x.stylesheet(
            x.output(encoding='utf-8'),
            x.template(
                x.copy_of(select='.'), match='/'
            )
        )

        h = xml.Renderer()

        page = h.html(h.h1('Hello'), h.h2('world'))

        r = page.getroottree().xslt(style_sheet)

        assert etree.tostring(r) == page.tostring()
