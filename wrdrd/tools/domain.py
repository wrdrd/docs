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
        "dig {0} txt +cmd +nocomments +question +noidentify +nostats",
        domain)
    log.info('cmd', cmd=cmd)
    output = sarge.capture_both(cmd)
    # look for "v=spf1"
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
    log.debug('MX', record=output)
    result = 0
    check_domain1 = "aspmx.l.google.com."
    check_domain2 = "googlemail.com."
    lines = output.split('\n')
    if not lines:
        log.error('err', msg="No MX records found for %r" % domain)
        result += 1
    for l in lines:
        l = l.lower()
        if not (l.endswith(check_domain1) or l.endswith(check_domain2)):
            result += 1
            log.error('err', msg="%r does not end with %r or %r" %
                      (l, check_domain1, check_domain2))
    if result is None:
        result += 1
    return result


def check_google_spf(domain):
    """
    https://support.google.com/a/answer/178723?hl=en
    """
    cmd = sarge.shell_format("dig {0} txt +short", domain)
    log.info('cmd', op='check_google_spf', cmd=cmd)
    proc = sarge.capture_both(cmd)
    output = proc.stdout.text.rstrip().split('\n')
    for line in output:
        log.debug('TXT', record=line)
        expected = u"\"v=spf1 include:_spf.google.com ~all\""
        if line == expected:
            return 0

    errmsg = "%r != %r" % (output, expected)
    log.error('err', msg=errmsg)
    return 1


def check_google_dmarc(domain):
    """
    https://support.google.com/a/answer/2466580
    https://support.google.com/a/answer/2466563
    """
    dmarc_domain = "_dmarc." + domain
    cmd = sarge.shell_format("dig {0} txt +short", dmarc_domain)
    log.info('cmd', op='check_google_dmarc', cmd=cmd)
    proc = sarge.capture_both(cmd)
    output = proc.stdout.text.rstrip().split('\n')
    for line in output:
        log.debug('TXT', record=line)
        expected = u"\"v=DMARC1"  # ... "\; p=none\; rua=mailto:"
        if line.startswith(expected):
            if 'p=' in line:
                return 0

    errmsg = "%r != %r" % (output, expected)
    log.error('err', msg=errmsg)
    return 1


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

    ## See: dig_txt
    #proc = dig_spf(domain)
    #returncode += proc.returncode
    #print(proc.stdout.text)
    #print('-')
    #stderr = proc.stderr.text; stderr and print(stderr)
    #print('--')

    dmarc_domain = "_dmarc." + domain
    proc = dig_txt(dmarc_domain)
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


def check_google_domain(domain):
    """
    https://support.google.com/a/answer/2716802
    """
    mx = check_google_mx(domain)
    spf = check_google_spf(domain)
    dmarc = check_google_dmarc(domain)

    returncode = mx + spf + dmarc  # TODO: + dkim
    if returncode:
        log.error('err', mx=mx, spf=spf, dmarc=dmarc)
    else:
        log.info('OK', mx=mx, spf=spf, dmarc=dmarc)

    return returncode


#import unittest
#class Test_domain_tools(unittest.TestCase):
#    def test_domain_tools(self):
#        pass


def main(*args):
    import optparse
    import sys

    prs = optparse.OptionParser(
        usage="%prog <domain>",
        description="Collect DNS information with whois and dig"
    )

    prs.add_option('-g', '--check-google-domain',
                    dest='check_google_domain',
                    action='store_true',
                    help="Check Google MX, SPF, DMARC records")

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

    if opts.check_google_domain:
        print("## check_google_domain: %r" % domain)
        returncode += check_google_domain(domain)

    print("check_google_domain: %d" % returncode)

    return returncode


if __name__ == "__main__":
    import sys
    sys.exit(main())
