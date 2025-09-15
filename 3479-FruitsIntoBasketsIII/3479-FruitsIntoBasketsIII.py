class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        def insert(current, tree, fruits_amount, first_element):
            if current >= first_element:
                if tree[current] - fruits_amount >= 0:
                    tree[current] = 0
                    return 0

                else:
                    return 1

            left = 2*current + 1
            right = 2*current + 2

            if tree[left] >= fruits_amount:
                i = insert(left, tree, fruits_amount, first_element)
            else:
                i = insert(right, tree, fruits_amount, first_element)

            tree[current] = max(tree[left], tree[right])
            return i

        n = len(baskets)
        p = ceil(log2(n))
        tree = [0 for node in range(2**(p + 1) - 1)]
        first_element = 2**p - 1
        answer = 0

        for i in range(n):
            tree[first_element + i] = baskets[i]
        
        for i in range(first_element - 1, -1, -1):  
            tree[i] = max(tree[2 * i + 1], tree[2 * i + 2])

        for fruits_amount in fruits:
            answer += insert(0, tree, fruits_amount, first_element)

        return answer
