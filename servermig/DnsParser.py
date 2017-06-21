from servermig.Parser import Parser
from servermig.Record import Record

import re


class DnsParser(Parser):
    """DNS Parser"""

    @staticmethod
    def _parse_record(record_string):
        zone_regex = re.compile(r"(\S*) {1,2}(?:\d*) {1,2}(?:IN\s{1,2}(A))\s{1,2}(.*)")
        match = zone_regex.match(record_string)
        if match:
            record = Record()
            record.name = match.group(1)
            record.record_type = match.group(2)
            record.record = match.group(3)
            return record
        else:
            return None