#!/usr/bin/python3
"""Disconnect VPN Site to VPN Gateway."""
import os
from azure.mgmt.network import NetworkManagementClient
from azure.common.credentials import ServicePrincipalCredentials

# setup Azure Login Credentials from Environmental Variables
credentials = ServicePrincipalCredentials(
    client_id=os.environ.get('ARM_CLIENT_ID'),
    secret=os.environ.get('ARM_CLIENT_SECRET'),
    tenant=os.environ.get('ARM_TENANT_ID')
)

# Connect to Azure APIs and get session details
network_client = NetworkManagementClient(credentials, os.environ.get('ARM_SUBSCRIPTION_ID'))

# Delete VPN Site Connection to VPNG
async_vpn_site_connection_deletion = network_client.vpn_connections.delete(
    os.environ.get('GROUP_NAME'),
    os.environ.get('VPNG_NAME'),
    'CONNECTION_' + os.environ.get('VPN_SITE_NAME'),
    custom_headers=None,
    raw=False,
    polling=True
)
async_vpn_site_connection_deletion.wait()
print(async_vpn_site_connection_deletion.result())
print('VPN Site Connection to VPNG Deleted')
