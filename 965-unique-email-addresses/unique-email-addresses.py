class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        res = []
        for email in emails:
            name, domain = email.split('@')
            name = name.replace('.', '')
            if name.find('+') != -1:
                name = name[:name.find('+')]
            res.append(name + '@' + domain)
        return len(set(res))