class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        mp = {}
        for domain in cpdomains:
            domcnt, domName = domain.split(" ")
            domcnt = int(domcnt)
            mp[domName] = mp.get(domName, 0) + domcnt
            dom12 = domName.split(".")
            if len(dom12) == 3:
                wrd = dom12[1]+"."+dom12[2]
                mp[wrd] = mp.get(wrd, 0) + domcnt
            mp[dom12[-1]] = mp.get(dom12[-1], 0) + domcnt
        res = []
        for key, val in mp.items():
            # print(key, val)
            string = ""
            string += str(val)+ " " + key
            res.append(string)
        return res
