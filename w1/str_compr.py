class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0
        write = 0

        while i < len(chars):
            char = chars[i]
            count = 1

            while i + 1 < len(chars) and chars[i + 1] == char:
                i += 1
                count += 1

            chars[write] = char
            write += 1

            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1

            i += 1

        return write
