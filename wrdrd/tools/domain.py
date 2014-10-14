#!/usr/bin/env python
# encoding: utf-8
from __future__ import print_function
"""
domain_tools

https://en.wikipedia.org/wiki/DNS
https://en.wikipedia.org/wiki/List_of_DNS_record_types
"""
import logging

import sarge
import structlog

#log = logging.getLogger()
log = structlog.get_logger()

def nslookup(domain):
    if not domain.endswith('.'):
        domain = domain + '.'
    cmd = sarge.shell_format('nslookup {0}', domain)
    log.info('cmd', cmd=cmd)
    output = sarge.capture_both(cmd)
    return output

def whois(domain):
    cmd = sarge.shell_format('whois {0}', domain)
    log.info('cmd', cmd=cmd)
    output = sarge.capture_both(cmd)
    return output


def dig_all(domain):
    cmd = sarge.shell_format(
        "dig {0} +cmd +nocomments +question +noidentify +nostats",
        domain)
    log.info('cmd', cmd=cmd)
    output = sarge.capture_both(cmd)
    return output


def dig_ns(domain):
    cmd = sarge.shell_format(
        "dig {0} ns +cmd +nocomments +question +noidentify +nostats",
        domain)
    log.info('cmd', cmd=cmd)
    output = sarge.capture_both(cmd)
    return output


def dig_txt(domain):
    cmd = sarge.shell_format(
        "dig {0} txt +cmd +nocomments +question +noidentify +nostats",
        domain)
    log.info('cmd', cmd=cmd)
    output = sarge.capture_both(cmd)
    return output


def dig_spf(domain):
    """
    https://en.wikipedia.org/wiki/Sender_Policy_Framework
    """
    cmd = sarge.shell_format(
        "dig {0} spf +cmd +nocomments +question +noidentify +nostats",
        domain)
    log.info('cmd', cmd=cmd)
    output = sarge.capture_both(cmd)
    return output


def dig_mx(domain):
    """
    https://en.wikipedia.org/wiki/MX_record
    """
    cmd = sarge.shell_format(
        "dig {0} mx +cmd +nocomments +question +noidentify +nostats",
        domain)
    log.info('cmd', cmd=cmd)
    output = sarge.capture_both(cmd)
    return output


def dig_dnskey(zone):
    cmd = sarge.shell_format(
        "dig {0} +dnssec dnskey +cmd +nocomments +question +noidentify +nostats",
        zone)
    log.info('cmd', cmd=cmd)
    output = sarge.capture_both(cmd)
    return output


def check_google_mx(domain):
    """
    https://support.google.com/a/topic/2716885?hl=en&ref_topic=2426592
    """
    cmd = sarge.shell_format("dig {0} mx +short", domain)
    log.info('cmd', cmd=cmd)
    output = sarge.capture_both(cmd).stdout.text.rstrip()
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
    """
    https://support.google.com/a/answer/178723?hl=en
    """
    cmd = sarge.shell_format("dig {0} txt +short", domain)
    log.info('cmd', cmd=cmd)
    proc = sarge.capture_both(cmd)
    output = proc.stdout.text.rstrip()
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
    returncode = 0
    proc = whois(domain)
    returncode += proc.returncode
    print(proc.stdout.text)
    print('-')
    stderr = proc.stderr.text; stderr and print(stderr)
    print('--')

    proc = dig_all(domain)
    returncode += proc.returncode
    print(proc.stdout.text)
    print('-')
    stderr = proc.stderr.text; stderr and print(stderr)
    print('--')

    proc = dig_ns(domain)
    returncode += proc.returncode
    print(proc.stdout.text)
    print('-')
    stderr = proc.stderr.text; stderr and print(stderr)
    print('--')

    proc = dig_mx(domain)
    returncode += proc.returncode
    print(proc.stdout.text)
    print('-')
    stderr = proc.stderr.text; stderr and print(stderr)
    print('--')

    proc = dig_txt(domain)
    returncode += proc.returncode
    print(proc.stdout.text)
    print('-')
    stderr = proc.stderr.text; stderr and print(stderr)
    print('--')

    proc = dig_spf(domain)
    returncode += proc.returncode
    print(proc.stdout.text)
    print('-')
    stderr = proc.stderr.text; stderr and print(stderr)
    print('--')

    proc = dig_dnskey(domain.split(".")[-1])  # TODO: actual zone
    returncode += proc.returncode
    print(proc.stdout.text)
    print('-')
    stderr = proc.stderr.text; stderr and print(stderr)
    print('--')

    return returncode


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

    returncode = 0
    returncode += domain_tools(domain)
    print("domain_tools: %d" % returncode)

    if opts.google_domain_tools:
        print("## google_domain_tools: %r" % domain)
        returncode += google_domain_tools(domain)

    print("google_domain_tools: %d" % returncode)

    return returncode


if __name__ == "__main__":
    import sys
    sys.exit(main())
