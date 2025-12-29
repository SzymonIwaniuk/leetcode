from collections import defaultdict


class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        n = len(bottom)
        triples = defaultdict(set)

        for triple in allowed:
            triples[triple[:2]].add(triple[2:])

        def rec(h, w, layer, new_layer):
            if h == n:
                return True

            if new_layer and len(new_layer) == n - h:
                return rec(h+1, 0, new_layer, [])

            pair = layer[w] + layer[w+1]
            can_build = False
            for c in triples[pair]:
                new_layer.append(c)
                can_build = can_build or rec(h, w + 1, layer, new_layer)
                new_layer.pop()

            return can_build

        return rec(1, 0, list(bottom), [])

            
            
