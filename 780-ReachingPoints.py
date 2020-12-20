class Solution:
    # Consider the tree with root (sx, sy). Let's say by convention, (sx, sy+sx) is the left child, (sx+sy, sy) is the right child.
    # For any pair (x, y), if (x, y) is a node in the tree, its parent can either be
    # 1. (x, y-x) if y > x, in which case (x, y) is a right child
    # 2. (x-y, y) if x > y, in which case (x, y) is a left child
    # There are only these two possibilities, since every node must have positive value pairs.
    # Additionally, if x == y, (x, y) can't have a parent (i.e., it must be the root).

    # So the idea is to work backward/upward starting from (tx, ty), assuming (tx, ty) is in the tree, and iterate through its ancestors.
    # Return true IFF (sx, sy) is a node that can be reached from (tx, ty) following the parent chain.

    # The following implementation is an optimized version. Each iteration, we test tx > ty to see if (tx, ty) is a left child.
    # If yes, we update tx = tx % ty to get the first ancestor following the chain that is a right child (i.e., a "turning point").
    # Similarly, if ty > tx, we get the first ancestor that is a left child.

    # At each turning point, there are the following cases:
    # 1. If tx<sx and ty>sy (and its symetry case), (sx, sy) can't be an ancestor node, because tx will only get smaller as we go upwards
    # 2. Return true if the turning point is exactly (sx, sy)
    # 3. if tx == sx and ty < sy, then it might be the case that (sx, sy) is inbetween the current turning point and the previous turning point.
    # In otherwords, we might have skipped over (sx, sy) as we jump from the previous turning point. In this case, sy % tx == ty is true IFF
    # (sx, sy) is in between.
    # 4. Case 4 is symmetric to case 3
    # 5. In any other cases, we have tx >= sx and ty>=sy. In these cases, we will continue moving to the next ancestor turning point.

    # However, we might "skip" over the node (sx, sy) because we move up the tree too much.
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        if tx < sx or ty < sy:
            return False

        while True:
            if tx < sx and ty > sy or ty < sy and tx > sx:
                return False
            elif tx == sx and ty == sy:
                return True
            elif tx == sx and ty < sy:
                return sy % tx == ty
            elif ty == sy and tx < sx:
                return sx % ty == tx
            else:
                if tx > ty:
                    tx = tx % ty
                else:
                    ty = ty % tx