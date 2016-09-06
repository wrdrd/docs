#!/usr/bin/env python
# encoding: utf-8
from __future__ import print_function
"""
wrdrd.tools.domain

* nslookup, whois, and dig command wrappers
* check_google_domain (_mx, _spf, _dkim, _dmarc)

| https://en.wikipedia.org/wiki/DNS
| https://en.wikipedia.org/wiki/List_of_DNS_record_types
"""

import sarge
import structlog

log = structlog.get_logger()


def nslookup(domain, nameserver=''):
    """
    Get nslookup information with nslookup (resolve a domainname to an IP)

    Args:
        domain (str): DNS domain
        nameserver (str): DNS domain name server to query (default: ``''``)
    Returns:
        str: nslookup output
    """
    if not domain.endswith('.'):
        domain = domain + '.'
    cmd = sarge.shell_format('nslookup {0} {1}', domain, nameserver)
    log.info('cmd', cmd=cmd)
    output = sarge.capture_both(cmd)
    return output


def whois(domain):
    """
    Get whois information with whois

    Args:
        domain (str): DNS domain
    Returns:
        str: whois output
    """
    cmd = sarge.shell_format('whois {0}', domain)
    log.info('cmd', cmd=cmd)
    output = sarge.capture_both(cmd)
    return output


def dig_all(domain):
    """
    Get all DNS records with dig

    Args:
        domain (str): DNS domain
    Returns:
        str: dig output
    """
    cmd = sarge.shell_format(
        "dig {0} +cmd +nocomments +question +noidentify +nostats +dnssec",
        domain)
    log.info('cmd', cmd=cmd)
    output = sarge.capture_both(cmd)
    return output


def dig_ns(domain):
    """
    Get DNS NS records with dig

    Args:
        domain (str): DNS domain
    Returns:
        str: dig output
    """
    cmd = sarge.shell_format(
        "dig {0} ns +cmd +nocomments +question +noidentify +nostats",
        domain)
    log.info('cmd', cmd=cmd)
    output = sarge.capture_both(cmd)
    return output


def dig_txt(domain):
    """
    Get DNS TXT records with dig

    Args:
        domain (str): DNS domain
    Returns:
        str: dig output
    """
    cmd = sarge.shell_format(
        "dig {0} txt +cmd +nocomments +question +noidentify +nostats",
        domain)
    log.info('cmd', cmd=cmd)
    output = sarge.capture_both(cmd)
    return output


def dig_spf(domain):
    """
    Get SPF DNS TXT records with dig

    Args:
        domain (str): DNS domain
    Returns:
        str: dig output

    | https://en.wikipedia.org/wiki/Sender_Policy_Framework
    """
    output = dig_txt(domain)
    # TODO: look for "v=spf1"
    return output


def dig_mx(domain):
    """
    Get MX DNS records with dig

    Args:
        domain (str): DNS domain
    Returns:
        str: dig output

    | https://en.wikipedia.org/wiki/MX_record
    """
    cmd = sarge.shell_format(
        "dig {0} mx +cmd +nocomments +question +noidentify +nostats",
        domain)
    log.info('cmd', cmd=cmd)
    output = sarge.capture_both(cmd)
    return output


def dig_dnskey(zone):
    """
    Get DNSSEC DNS records with dig

    Args:
        zone (str): DNS zone
    Returns:
        str: dig output
    """
    cmd = sarge.shell_format(
        "dig {0} +dnssec dnskey +cmd +nocomments +question +noidentify +nostats",
        zone)
    log.info('cmd', cmd=cmd)
    output = sarge.capture_both(cmd)
    return output


def check_google_mx(domain):
    """
    Check Google MX DNS records

    Args:
        domain (str): DNS domain name

    Returns:
        int: 0 if OK, 1 on error

    | https://support.google.com/a/topic/2716885?hl=en&ref_topic=2426592
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
    Check a Google SPF DNS TXT record

    Args:
        domain (str): DNS domain name

    Returns:
        int: 0 if OK, 1 on error

    | https://support.google.com/a/answer/178723?hl=en
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
    Check a Google DMARC DNS TXT record

    Args:
        domain (str): DNS domain name

    Returns:
        int: 0 if OK, 1 on error

    | https://support.google.com/a/answer/2466580
    | https://support.google.com/a/answer/2466563
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


DEFAULT_GOOGLE_DKIM_PREFIX = 'google'


def check_google_dkim(domain, prefix=DEFAULT_GOOGLE_DKIM_PREFIX):
    """
    Check a Google DKIM DNS TXT record

    Args:
        domain (str): DNS domain name
        prefix (str): DKIM ``s=`` selector ('DKIM prefix')

    Returns:
        int: 0 if OK, 1 on error

    | https://support.google.com/a/answer/174126
    | https://admin.google.com/AdminHome?fral=1#AppDetails:service=email&flyout=dkim

    .. note:: This check function only finds "v=DKIM1" TXT records;
       it defaults to the default ``google`` prefix
       and **does not validate DKIM signatures**.

    | http://dkim.org/specs/rfc4871-dkimbase.html#rfc.section.3.6.2.1
    | http://dkim.org/specs/rfc4871-dkimbase.html#rfc.section.A.3

    """
    dkim_record_name = "%s._domainkey.%s" % (prefix, domain)
    cmd = sarge.shell_format("dig {0} txt +short", dkim_record_name)
    log.info('cmd', op='check_google_dkim', cmd=cmd)
    proc = sarge.capture_both(cmd)
    output = proc.stdout.text.rstrip().split('\n')
    for line in output:
        log.debug('TXT', record=line)
        expected = u"\"v=DKIM1"  # ... "\; p=none\; rua=mailto:"
        if line.startswith(expected):
            if 'k=' in line and 'p=' in line:
                return 0

    errmsg = "%s is not a valid DKIM record" % (output)
    log.error('err', msg=errmsg)
    return 1


def domain_tools(domain):
    """
    Get whois and DNS information for a domain.

    Args:
        domain (str): DNS domain name

    Returns:
        int: nonzero returncode on failure (sum of returncodes)
    """
    returncode = 0
    proc = whois(domain)
    returncode += proc.returncode
    print(proc.stdout.text)
    print('-')
    stderr = proc.stderr.text
    stderr and print(stderr)
    print('--')

    proc = dig_all(domain)
    returncode += proc.returncode
    print(proc.stdout.text)
    print('-')
    stderr = proc.stderr.text
    stderr and print(stderr)
    print('--')

    proc = dig_ns(domain)
    returncode += proc.returncode
    print(proc.stdout.text)
    print('-')
    stderr = proc.stderr.text
    stderr and print(stderr)
    print('--')

    proc = dig_mx(domain)
    returncode += proc.returncode
    print(proc.stdout.text)
    print('-')
    stderr = proc.stderr.text
    stderr and print(stderr)
    print('--')

    proc = dig_txt(domain)
    returncode += proc.returncode
    print(proc.stdout.text)
    print('-')
    stderr = proc.stderr.text
    stderr and print(stderr)
    print('--')

    # See: dig_txt
    #proc = dig_spf(domain)
    #returncode += proc.returncode
    # print(proc.stdout.text)
    # print('-')
    #stderr = proc.stderr.text; stderr and print(stderr)
    # print('--')

    dmarc_domain = "_dmarc." + domain
    proc = dig_txt(dmarc_domain)
    returncode += proc.returncode
    print(proc.stdout.text)
    print('-')
    stderr = proc.stderr.text
    stderr and print(stderr)
    print('--')

    # Would need to specify a DKIM prefix (DKIM s= selector)
    #dkim_record_name = "%s._domainkey.%s" % (dkim_prefix, domain)
    #proc = dig_txt(dkim_record_name)
    #returncode += proc.returncode
    # print(proc.stdout.text)
    # print('-')
    #stderr = proc.stderr.text; stderr and print(stderr)
    # print('--')

    proc = dig_dnskey(domain.split(".")[-1])  # TODO: actual zone
    returncode += proc.returncode
    print(proc.stdout.text)
    print('-')
    stderr = proc.stderr.text
    stderr and print(stderr)
    print('--')

    return returncode


def check_google_domain(domain, dkim_prefix=DEFAULT_GOOGLE_DKIM_PREFIX):
    """
    Check DNS MX, SPF, DMARC, and DKIM records for a Google Apps domain

    Args:
        domain (str): DNS domain
        dkim_prefix (str): DKIM prefix (``<prefix>._domainkey``)
    Returns:
        int: nonzero returncode on failure (sum of returncodes)

    | https://support.google.com/a/answer/2716802
    """
    mx = check_google_mx(domain)
    spf = check_google_spf(domain)
    dmarc = check_google_dmarc(domain)
    dkim = check_google_dkim(domain, prefix=dkim_prefix)

    returncode = mx + spf + dmarc + dkim
    if returncode:
        log.error('err', mx=mx, spf=spf, dmarc=dmarc, dkim=dkim)
    else:
        log.info('OK', mx=mx, spf=spf, dmarc=dmarc, dkim=dkim)

    return returncode


#import unittest
# class Test_domain_tools(unittest.TestCase):
#    def test_domain_tools(self):
#        pass


def main(*args):
    """
    :py:mod:`wrdrd.tools.domain` main method

    Args:
        args (list): commandline arguments
    Returns:
        int: nonzero returncode on failure (sum of returncodes)
    """
    import logging
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
