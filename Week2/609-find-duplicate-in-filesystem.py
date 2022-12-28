class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:


        mp = {}
        # def helper(paths):
        res = []
        for path in paths:
            path = path.split(" ")
            curr = []
            for i in range(1, len(path)):
                dirctr = path[0] +'/'+ path[i][:path[i].index('(')]
                fl = path[i][path[i].index('(')+1:path[i].index(')')]
                mp[dirctr] = fl
        sorted_mp = sorted(mp.items(), key=lambda kv: kv[1])
        # print(sorted_mp)
        cnt = defaultdict(list)
        # print(cnt)
        for el in sorted_mp:
            cnt[el[1]].append(el[0])
        for itm in cnt.values():
            if len(itm) > 1:
                res.append(itm)
        return res



