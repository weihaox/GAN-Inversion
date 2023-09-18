#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   save_cited_bib.py
@Time    :   2023/09/19 00:04:41
@Author  :   Weihao Xia (xiawh3@outlook.com)
@Version :   1.0
@Desc    :   This script is to create a .bib file containing only the references used in the present paper
             This can serve as an alternative to converting from .bbl to .bib.
'''

import re
import argparse

def extract_cite_content_from_file(filename):
    """Extract all citation keys from a .tex file."""
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()

    pattern = r'\\cite\{(.*?)\}'
    raw_matches = re.findall(pattern, content)
    matches = [ref.strip() for match in raw_matches for ref in match.split(',')]
    return set(matches)

def extract_bib_entries(bib_filename, cite_keys):
    """Extract relevant bib entries based on citation keys."""
    with open(bib_filename, 'r', encoding='utf-8') as file:
        content = file.readlines()

    inside_entry = False
    current_key = None
    saved_entries = []
    temp_entries = []

    for line in content:
        # Check if a new bib entry starts
        if line.startswith('@'):
            inside_entry = True
            current_key = line.split("{", 1)[1].split(",", 1)[0].strip()
            temp_entries = [line]
        elif inside_entry:
            temp_entries.append(line)

        # Check the end of the bib entry
        if inside_entry and line.strip() == "}":
            inside_entry = False
            if current_key in cite_keys:
                saved_entries.extend(temp_entries)
                saved_entries.append('\n')  # Add a newline after each entry

    return saved_entries

def main():
    parser = argparse.ArgumentParser(description="Extract cited bib entries from a larger bib file.")
    parser.add_argument("--tex_filename", default='main.tex', help="Path to the .tex file")
    parser.add_argument("--bib_filename", default='reference_full.bib', help="Path to the full .bib file")
    parser.add_argument("--out_filename", default='reference.bib', help="Path for the output .bib file with only cited entries")
    args = parser.parse_args()

    cite_keys = extract_cite_content_from_file(args.tex_filename)
    filtered_bib_entries = extract_bib_entries(args.bib_filename, cite_keys)

    with open(args.out_filename, 'w', encoding='utf-8') as out_file:
        out_file.writelines(filtered_bib_entries)

if __name__ == "__main__":
    main()