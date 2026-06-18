class Solution:
    def largestRectangleArea(self, heights):
        stack = []
        max_area = 0
        n = len(heights)

        for i in range(n + 1):

            # Use 0 as extra height at the end
            current_height = 0 if i == n else heights[i]

            # Process all taller bars
            while stack and heights[stack[-1]] > current_height:
                
                height = heights[stack.pop()]

                # Calculate width
                if stack:
                    width = i - stack[-1] - 1
                else:
                    width = i

                # Calculate area
                area = height * width

                # Update max area
                if area > max_area:
                    max_area = area

            # Push current index
            stack.append(i)

        return max_area
