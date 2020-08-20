#!/usr/bin/python3
"""Delete a network in a given environment."""
from os import environ
import nf_token as nft
import nf_network as nfn


def network_delete():
    """Delete a network based on environments variables."""
    nft.clear_log()
    token = nft.get_token(environ.get('ENVIRONMENT'),
                          environ.get('SMOKE_TEST_USER'),
                          environ.get('SMOKE_TEST_PASS'))
    nfn_url = nfn.find_network(environ.get('ENVIRONMENT'),
                               environ.get('NFN_NAME'),
                               token)
    nfn.delete_network(nfn_url, token)
    print(nfn_url)


if __name__ == '__main__':
    network_delete()
