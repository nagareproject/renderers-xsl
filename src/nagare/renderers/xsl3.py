# --
# Copyright (c) 2008-2024 Net-ng.
# All rights reserved.
#
# This software is licensed under the BSD License, as described in
# the file LICENSE.txt, which you should have received as part of
# this distribution.
# --

"""XSL v3 renderer."""

from nagare.renderers.xml import TagProp

from . import xsl2


class Renderer(xsl2.Renderer):
    """The XSL renderer."""

    accept = TagProp('accept', {'component', 'names', 'visibility'})
    accumulator = TagProp('accumulator', {'name', 'initial-value', 'as', 'streamable'})
    accumulator_rule = TagProp('accumulator-rule', {'match', 'phase', 'select'})
    assert_ = TagProp('assert', {'test', 'select', 'error-code'})
    attribute_set = TagProp('attribute-set', {'name', 'use-attribute-sets', 'visibility', 'streamable'})
    break_ = TagProp('break', {'select'})
    catch = TagProp('catch', {'errors', 'select'})
    context_item = TagProp('context-item', {'as', 'use'})
    copy_of = TagProp('copy-of', {'select', 'copy-accumulator', 'copy-namespaces', 'type', 'validation'})
    evaluate = TagProp(
        'evaluate', {'xpath', 'as', 'base-uri', 'with-params', 'context-item', 'namespace-context', 'schema-aware'}
    )
    expose = TagProp('expose', {'component', 'names', 'visibility'})
    fork = TagProp('fork')
    function = TagProp(
        'function',
        {'name', 'as', 'visibility', 'streamability', 'override-extension-function', 'new-each-time', 'cache'},
    )
    global_context_item = TagProp('global-context-item', {'as', 'use'})
    iterate = TagProp('iterate', {'select'})
    key = TagProp('key', {'name', 'match', 'use', 'composite', 'collation'})
    map = TagProp('map')
    map_entry = TagProp('map-entry', {'key', 'select'})
    merge = TagProp('merge')
    merge_action = TagProp('merge-action')
    merge_key = TagProp('merge-key', {'select', 'lang', 'order', 'collation', 'case-order', 'data-type'})
    merge_source = TagProp(
        'merge-source',
        {
            'name',
            'for-each-item',
            'for-each-source',
            'select',
            'streamable',
            'use-accumulators',
            'sort-before-merge',
            'validation',
            'type',
        },
    )
    message = TagProp('message', {'select', 'terminate', 'error-code'})
    mode = TagProp(
        'mode',
        {
            'name',
            'streamable',
            'use-accumulators',
            'on-no-match',
            'on-multiple-match',
            'warning-on-no-match',
            'warning-on-multiple-match',
            'typed',
            'visibility',
        },
    )
    namespace_alias = TagProp('namespace-alias', {'stylesheet-prefix', 'result-prefix'})
    next_iteration = TagProp('next-iteration')
    number = TagProp(
        'number',
        {
            'value',
            'select',
            'level',
            'count',
            'from',
            'format',
            'lang',
            'letter-value',
            'ordinal',
            'start-at',
            'grouping-separator',
            'grouping-size',
        },
    )
    on_completion = TagProp('on-completion', {'select'})
    on_empty = TagProp('on-empty', {'select'})
    on_non_empty = TagProp('on-non-empty', {'select'})
    output = TagProp(
        'output',
        {
            'name',
            'method',
            'allow-duplicate-names',
            'build-tree',
            'byte-order-mark',
            'cdata-section-elements',
            'doctype-public',
            'doctype-system',
            'encoding',
            'escape-uri-attributes',
            'html-version',
            'include-content-type',
            'indent',
            'item-separator',
            'json-node-output-method',
            'media-type',
            'normalization-form',
            'omit-xml-declaration',
            'parameter-document',
            'standalone',
            'suppress-indentation',
            'undeclare-prefixes',
            'use-character-maps',
            'version',
        },
    )
    override = TagProp('override')
    package = TagProp(
        'package',
        {
            'id',
            'name',
            'package-version',
            'version',
            'input-type-annotations',
            'declared-modes',
            'default-mode',
            'default-validation',
            'default-collation',
            'extension-element-prefixes',
            'exclude-result-prefixes',
            'expand-text',
            'use-when',
            'xpath-default-namespace',
        },
    )
    param = TagProp('param', {'name', 'select', 'as', 'required', 'tunnel', 'static'})
    result_document = TagProp(
        'result-document',
        {
            'format',
            'href',
            'validation',
            'type',
            'method',
            'allow-duplicate-names',
            'build-tree',
            'byte-order-mark',
            'cdata-section-elements',
            'doctype-public',
            'doctype-system',
            'encoding',
            'escape-uri-attributes',
            'html-version',
            'include-content-type',
            'indent',
            'item-separator',
            'json-node-output-method',
            'media-type',
            'normalization-form',
            'omit-xml-declaration',
            'parameter-document',
            'standalone',
            'suppress-indentation',
            'undeclare-prefixes',
            'use-character-maps',
            'output-version',
        },
    )
    source_document = TagProp('source-document', {'href', 'streamable', 'use-accumulators', 'validation', 'type'})
    stylesheet = TagProp(
        'stylesheet',
        {
            'id',
            'version',
            'default-mode',
            'default-validation',
            'input-type-annotations',
            'default-collation',
            'extension-element-prefixes',
            'exclude-result-prefixes',
            'expand-text',
            'use-when',
            'xpath-default-namespace',
        },
    )
    template = TagProp('template', {'match', 'name', 'priority', 'mode', 'as', 'visibility'})
    transform = TagProp(
        'transform',
        {
            'id',
            'version',
            'default-mode',
            'default-validation',
            'input-type-annotations',
            'default-collation',
            'extension-element-prefixes',
            'exclude-result-prefixes',
            'expand-text',
            'use-when',
            'xpath-default-namespace',
        },
    )
    try_ = TagProp('try', {'select', 'rollback-output'})
    use_package = TagProp('use-package', {'name', 'package-version'})
    variable = TagProp('variable', {'name', 'select', 'as', 'static', 'visibility'})
    where_populated = TagProp('where-populated')
