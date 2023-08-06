""" rhcephcompose CLI """

from argparse import ArgumentParser
import kobo.conf
from rhcephcompose.compose import Compose


class RHCephCompose(object):
    """ Main class for rhcephcompose CLI. """

    def __init__(self):

        parser = ArgumentParser(description='Generate a compose for RHCS.')
        parser.add_argument('config_file', metavar='config',
                            help='main configuration file for this release.')
        parser.add_argument('--insecure', action='store_const', const=True,
                            default=False, help='skip SSL verification')
        parser.add_argument('--compose-type', metavar='TYPE', default='test',
                            help='choose compose type to determine suffix: '
                            'production, nightly, test, ci (default: test)')
        args = parser.parse_args()

        conf = kobo.conf.PyConfigParser()
        conf.load_from_file(args.config_file)
        if args.insecure:
            conf['chacra_ssl_verify'] = False
            import requests
            from requests.packages.urllib3.exceptions\
                import InsecureRequestWarning
            requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        conf['compose_type'] = args.compose_type

        compose = Compose(conf)
        compose.run()
