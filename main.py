import argparse

import requests

from GandiAPI import GandiAPI
from Record import Record


def get_my_ip(ipv6 = True):
    if not ipv6:
        response = requests.get("https://api.ipify.org?format=json")
    else:
        response = requests.get("https://ipify.org?format=json")

    if response.ok:
        return response.json()["ip"]
    else:
        return None


def update_dns_with_my_ip(conn: GandiAPI, fqdn: str, rrset_name: str, rrset_type: str = "A",
                          create_if_not_exist: bool = False):
    """
    Update a DNS record with the actual IP, raise exception if errors occurred
    :param create_if_not_exist: If True, create the DNS record if it doesn't exist'
    :param conn: GandiAPI
    :param fqdn: Fully qualified domain name
    :param rrset_name: name of record
    :param rrset_type: type of record
    :return: False if record is not changed, True if it is updated
    """

    my_ip = get_my_ip(rrset_type == "AAAA")
    assert my_ip is not None, "cannot get current IP, myip.com API is maybe down"

    record = Record(rrset_name, rrset_type, [my_ip])

    result = conn.get_domain_record(fqdn, record)

    # If the status code is 404 (record does not exist.) and we want to create it, then we don't want to raise
    # exceptions
    if result.status_code != 404 and not create_if_not_exist:
        raise_status_code(result, result.status_code)
        current_record_ip = result.json()["rrset_values"][0]
    else:
        current_record_ip = None

    if current_record_ip == my_ip:
        return False
    else:
        result = conn.update_domain_records(fqdn, record)
        raise_status_code(result, result.status_code)
        return True


def raise_status_code(result, status_code):
    assert status_code != 403, "Access to the resource is denied. Mainly due to a lack of permissions to access it." \
                               "\n{}".format(result.json())
    assert status_code != 404, "the name/type pair does not exist"
    assert status_code != 401, "Bad authentication attempt because of a wrong API Key.\n{}".format(result.json())


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Update a Gandi DNS record (type A or AAAA) with current IP if the 2 values are different')
    parser.add_argument("--token", required=True, help="Api Key of your Gandi Account", type=str)
    parser.add_argument("--fqdn", required=True, help="Full qualified domain name", type=str)
    parser.add_argument("--rrset_name", required=True, help="Name of the record", type=str)
    parser.add_argument("--rrset_type", default="A", choices=['A', 'AAAA'], help="Choice the rrset type A -> IPv4, AAAA -> IPV6", type=str)
    parser.add_argument("--create_if_not_exist", help="If True, create the DNS record with current IP "
                                                      "address if it doesn't exist", action='store_true')
    parser.add_argument("--verbose", help="Print information if True", action='store_true')

    args = parser.parse_args()

    conn = GandiAPI(args.token)
    res = update_dns_with_my_ip(conn, args.fqdn, args.rrset_name, args.rrset_type, args.create_if_not_exist)

    if args.verbose:
        if res:
            print("The DNS record has been successfully changed")
        else:
            print("The DNS record has already the good value")
