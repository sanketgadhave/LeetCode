class Solution:
    def compress(self, chars: List[str]) -> int:
        if not chars:
            return 0

        output_list = []
        count = 1  # Since the first occurrence is counted as 1
        for i in range(1, len(chars) + 1):  # Add +1 to handle the last character
            if i < len(chars) and chars[i] == chars[i-1]:
                count += 1
            else:
                output_list.append(chars[i-1])
                if count > 1:
                    for c in str(count):  # This handles numbers greater than 9 correctly
                        output_list.append(c)
                if i < len(chars):  # Reset count for the next new character
                    count = 1

        # Now, overwrite chars with output_list
        chars.clear()  # Clear the original list
        chars.extend(output_list)  # Extend the list with the new values

        return len(chars)