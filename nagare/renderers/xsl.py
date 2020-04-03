# --
# Copyright (c) 2008-2020 Net-ng.
# All rights reserved.
#
# This software is licensed under the BSD License, as described in
# the file LICENSE.txt, which you should have received as part of
# this distribution.
# --

"""XSL v1 renderer"""

from nagare.renderers import xml
from nagare.renderers.xml import TagProp


class Renderer(xml.XmlRenderer):
    """ The XSL renderer
    """

    content_type = 'text/xsl'
    namespace = 'http://www.w3.org/1999/XSL/Transform'

    def __init__(self, parent=None):
        super(Renderer, self).__init__(parent)

        self.namespaces = {'xsl': self.namespace}
        self.default_namespace = 'xsl'

    # The XSL tags
    # ------------

    apply_imports = TagProp('apply-imports')
    apply_templates = TagProp('apply-templates', {'select', 'mode'})
    attribute = TagProp('attribute', {'name', 'namespace'})
    attribute_set = TagProp('attribute-set', {'name', 'use-attribute-sets'})
    call_template = TagProp('call-template', {'name'})
    choose = TagProp('choose')
    comment = TagProp('comment')
    copy = TagProp('copy', {'use-attribute-sets'})
    copy_of = TagProp('copy-of', {'select'})
    decimal_format = TagProp('decimal-format', {
        'name', 'decimal-separator', 'grouping-separator', 'infinity',
        'minus-sign', 'NaN', 'percent', 'per-mille', 'zero-digit',
        'digit', 'pattern-separator'
    })
    element = TagProp('element', {'name', 'namespace', 'use-attribute-sets'})
    fallback = TagProp('fallback', {'select'})
    for_each = TagProp('for-each', {'select'})
    if_ = TagProp('if', {'test'})
    import_ = TagProp('import', {'href'})
    include = TagProp('include', {'href'})
    key = TagProp('key', {'name', 'match', 'use'})
    message = TagProp('message', {'select', 'terminate'})
    namespace_alias = TagProp('namespace-alias', {'stylesheet-prefix'})
    number = TagProp('number', {
        'level', 'count', 'from', 'value', 'format',
        'lang', 'letter-value', 'grouping-separator',
        'grouping-size', 'select', 'ordinal'
    })
    otherwise = TagProp('otherwise')
    output = TagProp('output', {
        'method', 'version', 'encoding',
        'omit-xml-declaration', 'standalone',
        'doctype-public', 'doctype-system',
        'cdata-section-elements', 'indent',
        'media-type'
    })
    param = TagProp('param', {'name', 'select'})
    preserve_space = TagProp('preserve-space', {'elements'})
    processing_instruction = TagProp('processing-instruction', {'name'})
    sort = TagProp('sort', {'select', 'lang', 'data-type', 'order', 'case-order'})
    strip_space = TagProp('strip-space', {'elements'})
    stylesheet = TagProp('stylesheet', {
        'version', 'id',
        'extension-element-prefixes',
        'exclude-result-prefixes'
    })
    template = TagProp('template', {'match', 'name', 'priority', 'mode'})
    text = TagProp('text')
    transform = TagProp('transform', {
        'version', 'id',
        'extension-element-prefixes',
        'exclude-result-prefixes'
    })
    value_of = TagProp('value-of', {'select', 'disable-output-escaping'})
    variable = TagProp('variable', {'name', 'select'})
    when = TagProp('when', {'test'})
    with_param = TagProp('with-param', {'name', 'select'})
