#!/usr/bin/env python3

import argparse
import rich.table
import rich.console
import digikey
import sys
import logging
from digikey.v3.productinformation import KeywordSearchRequest

digikey.logger.setLevel(logging.CRITICAL)

SANE_MIN_ORDER_PRICE=20.0

class Part:
    pass

def search_parts(query, sane_min_order=True, sort_by_price=True, hide_broken=True):
    search_request = KeywordSearchRequest(keywords=query, record_count=50)
    result = digikey.keyword_search(body=search_request)

    parts = []

    for product in result.products:
        part = Part()

        part.name = product.manufacturer_part_number
        part.digikey_part = product.digi_key_part_number
        part.desc = product.product_description
        part.price = product.unit_price
        part.min_order = product.minimum_order_quantity
        part.quantity = product.quantity_available
        part.manufacturer = product.manufacturer.value
        part.stock = not product.non_stock
        part.packaging = product.packaging.value

        if hide_broken:
            if part.price <= 0.0 or part.quantity <= 0 or not part.stock:
                continue

        if sane_min_order:
            if part.min_order * part.price > SANE_MIN_ORDER_PRICE:
                continue

        parts.append(part)

    if sort_by_price:
        parts.sort(key=lambda x: x.price)

    return parts

def present_parts(console, parts):
    table = rich.table.Table(title='Results')
    table.add_column('Name')
    table.add_column('Description')
    table.add_column('Manufacturer')
    table.add_column('Quantity')
    table.add_column('M/O')
    table.add_column('Price')
    table.add_column('Packaging')
    table.add_column('DigiKey part number')

    for p in parts:
        table.add_row(p.name, p.desc, p.manufacturer, str(p.quantity),
                str(p.min_order), str(p.price), p.packaging, p.digikey_part)

    console.print(table)

def parse_arguments():
    parser = argparse.ArgumentParser(description='Search DigiKey')
    parser.add_argument('request', help='search request')
    parser.add_argument('--dont-hide-broken', action='store_true',
            help='don\'t hide non available parts')

    return parser.parse_args()

def main():
    args = parse_arguments()
    console = rich.console.Console()

    hide_broken = not args.dont_hide_broken
    parts = search_parts(args.request, hide_broken=hide_broken)
    present_parts(console, parts)

if __name__ == '__main__':
    main()
