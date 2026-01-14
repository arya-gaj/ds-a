class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        events = []
        for x, y, l in squares:
            events.append((y, 1, x, x + l))
            events.append((y + l, -1, x, x + l))

        events.sort()
        active = []
        prev_y = events[0][0]
        slabs = []

        area_so_far = 0

        def merged_width(intervals):
            intervals.sort()
            total = 0
            cur_l, cur_r = intervals[0]
            for l, r in intervals[1:]:
                if l > cur_r:
                    total += cur_r - cur_l
                    cur_l, cur_r = l, r
                else:
                    cur_r = max(cur_r, r)
            total += cur_r - cur_l
            return total

        for y, typ, x1, x2 in events:
            if y > prev_y and active:
                width = merged_width(active)
                dy = y - prev_y
                slabs.append((prev_y, y, width, area_so_far))
                area_so_far += width * dy

            if typ == 1:
                active.append((x1, x2))
            else:
                active.remove((x1, x2))

            prev_y = y

        total_area = area_so_far
        half = total_area / 2

        for y1, y2, width, area_before in slabs:
            slab_area = width * (y2 - y1)
            if area_before + slab_area >= half:
                return y1 + (half - area_before) / width

        return prev_y      