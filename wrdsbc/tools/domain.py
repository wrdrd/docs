#!/usr/bin/env python
# encoding: utf-8
from __future__ import print_function
"""
domain_tools

https://en.wikipedia.org/wiki/DNS
https://en.wikipedia.org/wiki/List_of_DNS_record_types
"""
import logging

import sh

log = logging.getLogger()

def nslookup(domain):
    if not domain.endswith('.'):
        domain = domain + '.'
    output = sh.nslookup(domain)
    return output

def whois(domain):
    output = sh.whois(domain)
    return output


def dig_all(domain):
    output = sh.dig(domain, "+cmd", "+nocomments", "+question", "+noidentify","+nostats")
    return output


def dig_ns(domain):
    output = sh.dig(domain, "ns", "+cmd", "+nocomments", "+question", "+noidentify","+nostats")
    return output


def dig_txt(domain):
    output = sh.dig(domain, "txt", "+cmd", "+nocomments", "+question", "+noidentify","+nostats")
    return output


def dig_spf(domain):
    """
    https://en.wikipedia.org/wiki/Sender_Policy_Framework
    """
    output = sh.dig(domain, "spf", "+cmd", "+nocomments", "+question", "+noidentify","+nostats")
    return output


def dig_mx(domain):
    """
    https://en.wikipedia.org/wiki/MX_record
    """
    mx_output = sh.dig(domain, "mx", "+cmd", "+nocomments", "+question", "+noidentify","+nostats")
    return mx_output


def dig_dnskey(zone):
    output = sh.dig('+dnssec', zone, 'dnskey', "+cmd", "+nocomments", "+question", "+noidentify","+nostats")
    return output


def check_google_mx(domain):
    output = sh.dig(domain, "mx", "+short").rstrip()
    log.debug(output)
    result = None
    check_domain = "aspmx.l.google.com."
    lines = output.split('\n')
    if not lines:
        log.debug("No MX records found for %r" % domain)
        result = False
    for l in lines:
        if not l.endswith(check_domain):
            result = False
            log.debug("%r does not end with %r" % (l, check_domain))
    if result is None:
        result = True
    return result


def check_google_spf(domain):
    output = sh.dig(domain, "txt", "+short").rstrip()
    log.debug(output)
    expected = u"v=spf1 include:_spf.google.com ~all"
    if output == expected:
        return True

    errmsg = "%r != %r" % (output, expected)
    log.debug(errmsg)
    return False


def domain_tools(domain):
    """
    mainfunc
    """
    print("## whois: %r" % domain)
    print(whois(domain))

    print("## dig: %r" % domain)
    print(dig_all(domain))

    print(dig_ns(domain))

    print(dig_mx(domain))

    print(dig_txt(domain))

    print(dig_spf(domain))

    print(dig_dnskey(domain.split(".")[-1])) # TODO: actual zone

    return 0


def google_domain_tools(domain):
    mx = check_google_mx(domain)
    spf = check_google_spf(domain)
    return int(not (mx and spf))


#import unittest
#class Test_domain_tools(unittest.TestCase):
#    def test_domain_tools(self):
#        pass


def main(*args):
    import logging
    import optparse
    import sys

    prs = optparse.OptionParser(
        usage="%prog <domain>",
        description="Collect DNS information with whois and dig"
    )

    prs.add_option('-g', '--google-domain-tools',
                    dest='google_domain_tools',
                    action='store_true',
                    help="Check Google MX and TXT SPF records")

    prs.add_option('-v', '--verbose',
                    dest='verbose',
                    action='store_true',)
    prs.add_option('-q', '--quiet',
                    dest='quiet',
                    action='store_true',)
    prs.add_option('-t', '--test',
                    dest='run_tests',
                    action='store_true',)

    args = args and list(args) or sys.argv[1:]
    (opts, args) = prs.parse_args()

    if len(args) != 1:
        raise Exception("Must specify a domain name")

    domain = args[0]

    if not opts.quiet:
        logging.basicConfig()

        if opts.verbose:
            logging.getLogger().setLevel(logging.DEBUG)

    if opts.run_tests:
        sys.argv = [sys.argv[0]] + args
        import unittest
        sys.exit(unittest.main())

    retcode = 0
    retcode = domain_tools(domain)

    if opts.google_domain_tools:
        print("## google_domain_tools: %r" % domain)
        retcode = retcode + google_domain_tools(domain)

    return retcode


if __name__ == "__main__":
    import sys
    sys.exit(main())
