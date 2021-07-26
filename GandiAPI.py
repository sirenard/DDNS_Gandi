import requests

from Record import Record


class GandiAPI:
    """
    Class that directly use gandi API (https://api.gandi.net/docs/livedns/)
    """
    DOMAIN_RECORDS_URL = "https://api.gandi.net/v5/livedns/domains/{}/records"  # URL format to deal with DNS records
    DOMAIN_RECORD_BY_NAME_TYPE_URL = "https://api.gandi.net/v5/livedns/domains/{}/records/{}/{}"

    def __init__(self, api_key):
        self.api_key = api_key
        self.header = {"Authorization": "Apikey {}".format(self.api_key)}  # header for all HTTPS requests

    def get_all_domain_records(self, fqdn: str):
        """
        Get the list of all DNS records for the domain name
        https://api.gandi.net/docs/livedns/#v5-livedns-domains-fqdn-records
        for more information on return values
        :param fqdn: Full Qualified Domain Name
        :return: request response
        """
        url = self.DOMAIN_RECORDS_URL.format(fqdn)
        response = requests.get(url, headers=self.header)
        return response

    def get_domain_record(self, fqdn: str, record: Record):
        """
        Get the list of 1 DNS record for the domain name
        https://api.gandi.net/docs/livedns/#get-v5-livedns-domains-fqdn-records-rrset_name-rrset_type
        for more information on return values
        :param record: Record that will be get (dont need to have any values)
        :param fqdn: Full Qualified Domain Name
        :return: request response (code 404 if name/type pair does not exist)
        """
        url = self.DOMAIN_RECORD_BY_NAME_TYPE_URL.format(fqdn, record.get_rrset_name(), record.get_rrst_type())
        response = requests.get(url, headers=self.header)
        return response

    def update_domain_records(self, fqdn: str, record: Record):
        """
        Update/create DNS record
        https://api.gandi.net/docs/livedns/#get-v5-livedns-domains-fqdn-records-rrset_name-rrset_type
        for more information on return values
        :param fqdn: Full Qualified Domain Name
        :param record: Record Object that will be create
        :return: response request
        """
        url = self.DOMAIN_RECORD_BY_NAME_TYPE_URL.format(fqdn, record.get_rrset_name(), record.get_rrst_type())
        response = requests.put(url, json={"rrset_values": record.get_rrset_values()}, headers=self.header)

        return response

    def delete_domain_record(self, fqdn: str, record: Record):
        """
        UDelete a DNS record
        https://api.gandi.net/docs/livedns/#get-v5-livedns-domains-fqdn-records-rrset_name-rrset_type
        for more information on return values
        :param fqdn: Full Qualified Domain Name
        :param record: Record Object that will be deleted
        :return: response request
        """
        url = self.DOMAIN_RECORD_BY_NAME_TYPE_URL.format(fqdn, record.get_rrset_name(), record.get_rrst_type())
        response = requests.delete(url, headers=self.header)

        return response

