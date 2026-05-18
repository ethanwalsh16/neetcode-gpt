from typing import List


class Solution:
    def get_merges(self, corpus: str, num_merges: int) -> List[List[str]]:
        # 1. Split corpus into a list of individual characters
        # 2. For each merge step:
        #    a. Count frequency of all adjacent token pairs
        #    b. Find the most frequent pair (break ties lexicographically)
        #    c. Merge all non-overlapping occurrences left to right
        #    d. Record the merge as [token_a, token_b]
        # 3. Return the list of merges performed

        tokens = list(corpus)
        merges = []
        for _ in range(num_merges):
            if len(tokens) < 2:
                break
            
            frequency_map = {}
            for i in range(1, len(tokens)):
                pair = (tokens[i-1], tokens[i])
                frequency_map[pair] = frequency_map.get(pair, 0) + 1
            
            if not frequency_map:
                break

            # sort by highest count, then lexicographically for tiebreak
            highest_count = max(frequency_map.values())
            candidates = sorted(p for p, c in frequency_map.items() if c == highest_count)
            best = candidates[0]

            merges.append([best[0], best[1]])

            new_tokens = []
            i = 0
            while i < len(tokens):
                if i < len(tokens) - 1 and tokens[i] == best[0] and tokens[i + 1] == best[1]:
                    new_tokens.append(best[0] + best[1])
                    i += 2
                else:
                    new_tokens.append(tokens[i])
                    i += 1
            tokens = new_tokens
        
        return merges

                



        return merges
