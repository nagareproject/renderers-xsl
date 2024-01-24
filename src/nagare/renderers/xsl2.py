# --
# Copyright (c) 2008-2024 Net-ng.
# All rights reserved.
#
# This software is licensed under the BSD License, as described in
# the file LICENSE.txt, which you should have received as part of
# this distribution.
# --

"""XSL v2 renderer."""

from nagare.renderers.xml import TagProp

from . import xsl


class Renderer(xsl.Renderer):
    """The XSL renderer."""

    # The XSL tags
    # ------------

    analyse_string = TagProp('analyse-string', {'select', 'regex', 'flags'})
    attribute = TagProp('attribute', {'name', 'namespace', 'select', 'separator', 'type', 'validation'})
    character_map = TagProp('character-map', {'name', 'use-character-maps'})
    copy = TagProp('copy', {'copy-namespaces', 'inherit-namespaces', 'use-attribute-sets', 'type', 'validation'})
    copy_of = TagProp('copy-of', {'select', 'copy-namespaces', 'type', 'validation'})
    document = TagProp('document', {'type', 'validation'})
    element = TagProp(
        'element', {'name', 'namespace', 'inherit-namespaces', 'use-attribute-sets', 'type', 'validation'}
    )
    for_each_group = TagProp(
        'for-each-group',
        {'select', 'group-by', 'group-adjacent', 'group-starting-with', 'group-ending-with', 'collation'},
    )
    function = TagProp('function', {'name', 'override', 'as'})
    import_schema = TagProp('import-schema', {'namespace', 'schema-location'})
    key = TagProp('key', {'name', 'match', 'use', 'collation'})
    matching_substring = TagProp('matching-substring', {'select', 'terminate'})
    namespace_ = TagProp('namespace', {'name', 'select'})
    next_match = TagProp('next-match')
    non_matching_substring = TagProp('non-matching-substring')
    output = TagProp(
        'output',
        {
            'name',
            'method',
            'byte-order-mark',
            'cdata-section-elements',
            'doctype-public',
            'doctype-system',
            'encoding',
            'escape-uri-attributes',
            'include-content-type',
            'indent',
            'media-type',
            'normalization-form',
            'omit-xml-declaration',
            'standalone',
            'use-character-maps',
            'version',
        },
    )
    output_character = TagProp('output-character', {'character', 'string'})
    param = TagProp('param', {'name', 'select', 'as', 'required', 'tunnel'})
    perform_sort = TagProp('perform-sort', {'select'})
    processing_instruction = TagProp('processing-instruction', {'name', 'select'})
    result_document = TagProp(
        'result-document',
        {
            'format',
            'href',
            'type',
            'validation',
            'method',
            'byte-order-mark',
            'cdata-section-elements',
            'doctype-public',
            'doctype-system',
            'encoding',
            'escape-uri-attributes',
            'include-content-type',
            'indent',
            'media-type',
            'normalization-form',
            'omit-xml-declaration',
            'standalone',
            'undeclare-prefixes',
            'use-character-maps',
            'output-version',
        },
    )
    sequence = TagProp('sequence', {'select'})
    sort = TagProp('sort', {'select', 'lang', 'data-type', 'order', 'case-order', 'collation', 'stable'})
    template = TagProp('template', {'match', 'name', 'priority', 'mode', 'as'})
    text_element_base_type = TagProp('text-element-base-type')
    text = TagProp('text', {'disable-output-escaping'})
    transform_element_base_type = TagProp('transform-element-base-type', {'version'})
    transform = TagProp('transform', {'id', 'default-validation', 'input-type-annotations'})
    value_of = TagProp('value-of', {'select', 'separator', 'disable-output-escaping'})
    variable = TagProp('variable', {'name', 'select', 'as'})
    when = TagProp('when', {'test'})
    with_param = TagProp('with-param', {'name', 'select', 'as', 'tunnel'})
