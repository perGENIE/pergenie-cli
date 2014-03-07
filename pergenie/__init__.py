#!/usr/bin/env python

import argparse
from lib.riskreport.cui import RiskReportCUI


def main():
    r = RiskReportCUI()

    parser = argparse.ArgumentParser(description='')
    subparsers = parser.add_subparsers(help='')
    parser_riskreport = subparsers.add_parser('riskreport', help='')
    parser_riskreport.add_argument('-I', '--infile', help='', required=True)
    parser_riskreport.add_argument('-O', '--outfile', help='', default=None)
    parser_riskreport.add_argument('-F', '--file-format', help='', required=True, choices=[x['name'] for x in r.FILEFORMATS])
    parser_riskreport.add_argument('-P', '--population', help='', default='unknown', choices=r.POPULATION)
    parser_riskreport.add_argument('--compress', help='Compress type of infile (-I/--infile)', choices=['gzip'])
    args = parser.parse_args()

    r.load_gwascatalog(args.population)
    r.load_genome(args.infile, args.file_format, compress=args.compress)
    r.write_riskreport(outfile=args.outfile)

if __name__ == '__main__':
    main()
