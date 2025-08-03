class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        if len(queryIP.split('.')) == 4:
            ipv4 = queryIP.split('.')
            for i, xi in enumerate(ipv4):
                if len(xi) == 0:
                    return "Neither"
                for char in xi:
                    if char.isalpha():
                        return "Neither"
                if not (0 <= int(xi) <= 255):
                    return "Neither"
                # leading zero
                if len(xi) != len(str(int(xi))):
                    return "Neither"
            return "IPv4"
        elif len(queryIP.split(':')) == 8:
            ipv6 = queryIP.split(':')
            for i, xi in enumerate(ipv6):
                if not (1 <= len(xi) <= 4):
                    return "Neither"
                for char in xi:
                    if not (char.isnumeric() or char in 'ABCDEFabcdef'):
                        return "Neither"
            return "IPv6"
        else:
            return "Neither"