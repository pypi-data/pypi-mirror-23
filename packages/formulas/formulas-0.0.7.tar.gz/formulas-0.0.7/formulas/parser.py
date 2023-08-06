#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# Copyright 2016-2017 European Commission (JRC);
# Licensed under the EUPL (the 'Licence');
# You may not use this work except in compliance with the Licence.
# You may obtain a copy of the Licence at: http://ec.europa.eu/idabc/eupl

"""
It provides formula parser class.
"""

# noinspection PyCompatibility
import regex
from .errors import TokenError, FormulaError, ParenthesesError
from .tokens.operand import String, Error, Number, Range
from .tokens.operator import OperatorToken, Separator, Intersect
from .tokens.function import Function, Array
from .tokens.parenthesis import Parenthesis
from .builder import AstBuilder


class Parser(object):
    formula_check = regex.compile(
        r"""
        (?P<array>^\s*{\s*=\s*(?P<formula>\S.*)\s*}\s*$)
        |
        (?P<value>^\s*=\s*(?P<formula>\S.*))
        """, regex.IGNORECASE | regex.X | regex.DOTALL
    )
    ast_builder = AstBuilder
    filters = [
        String, Error, Range, Number, OperatorToken, Separator, Function, Array,
        Parenthesis, Intersect
    ]

    def ast(self, expression, context=None):
        try:
            match = self.formula_check.match(expression).groupdict()
            expr = match['formula']
        except (AttributeError, KeyError):
            raise FormulaError(expression)
        builder = self.ast_builder(match=match)
        filters, tokens, stack = self.filters, [], []
        Parenthesis('(').ast(tokens, stack, builder)
        while expr:
            for f in filters:
                try:
                    token = f(expr, context)
                    token.ast(tokens, stack, builder)
                    expr = expr[token.match.end(0):]
                    break
                except TokenError:
                    pass
            else:
                raise FormulaError(expression)
        Parenthesis(')').ast(tokens, stack, builder)
        tokens = tokens[1:-1]
        while stack:
            if isinstance(stack[-1], Parenthesis):
                raise ParenthesesError()
            builder.append(stack.pop())
        if len(builder) != 1:
            FormulaError(expression)
        builder.finish()
        return tokens, builder
