# --
# Copyright (c) 2008-2021 Net-ng.
# All rights reserved.
#
# This software is licensed under the BSD License, as described in
# the file LICENSE.txt, which you should have received as part of
# this distribution.
# --

from nagare.renderers import xml
from nagare.renderers import xsl, xsl2, xsl3


def test_namespaces():
    for s in (xsl.Renderer(), xsl2.Renderer(), xsl3.Renderer()):
        assert s.stylesheet(s.template).tostring() == b'<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"><xsl:template/></xsl:stylesheet>'

    for s in (xsl.Renderer(), xsl2.Renderer(), xsl3.Renderer()):
        s.default_namespace = None
        assert s.stylesheet(s.template).tostring() == b'<stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"><template/></stylesheet>'

    for s in (xsl.Renderer(), xsl2.Renderer(), xsl3.Renderer()):
        s.namespaces = None
        s.default_namespace = None
        assert s.stylesheet(s.template).tostring() == b'<stylesheet><template/></stylesheet>'

    for s in (xsl.Renderer(), xsl2.Renderer(), xsl3.Renderer()):
        x = xml.Renderer()
        root = x.content(x.section(s.stylesheet(s.template)), x.section(s.stylesheet(s.template)))
        assert root.tostring() == b'<content><section><xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"><xsl:template/></xsl:stylesheet></section><section><xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"><xsl:template/></xsl:stylesheet></section></content>'
