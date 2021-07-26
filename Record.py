class Record:
    """
    Simple class that store a DNS record
    """

    def __init__(self, rrset_name: str, rrset_type: str, rrset_values: list, rrset_ttl: int = None):
        """

        :param rrset_name: name of the record
        :param rrset_type: record type, One of: "A", "AAAA", "ALIAS", "CAA", "CDS", "CNAME", "DNAME", "DS", "KEY", "LOC", "MX", "NAPTR", "NS", "OPENPGPKEY", "PTR", "RP", "SPF", "SRV", "SSHFP", "TLSA", "TXT", "WKS"
        :param rrset_values: list of string that are the value for the record
        :param rrset_ttl: time to live of the record Minimum: 300 Maximum: 2592000
        """

        self.rrset_name = rrset_name
        self.rrset_type = rrset_type
        self.rrset_values = rrset_values
        self.rrset_ttl = rrset_ttl

    def json(self):
        """
        format the record to be set in http body (in json)
        :return: json string
        """
        result = {
            "rrset_name": self.rrset_name,
            "rrset_type": self.rrset_type,
            "rrset_values": self.rrset_values
        }

        if self.rrset_ttl is not None:
            result["rrset_ttl"] = self.rrset_ttl

        return result

    def get_rrset_name(self):
        return self.rrset_name

    def get_rrst_type(self):
        return self.rrset_type

    def get_rrset_values(self):
        return self.rrset_values



