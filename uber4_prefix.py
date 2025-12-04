def solution(paragraphs, width):
    def framed_center(line: str) -> str:
        gap = width - len(line)
        left = gap // 2
        right = gap - left  # extra space (if any) goes to the right
        return "*" + " " * left + line + " " * right + "*"

    page = ["*" * (width + 2)]

    for words in paragraphs:
        cur = ""
        for w in words:
            if not cur:
                cur = w
            elif len(cur) + 1 + len(w) <= width:
                cur += " " + w
            else:
                page.append(framed_center(cur))
                cur = w
        if cur:
            page.append(framed_center(cur))

    page.append("*" * (width + 2))
    return page


# quick example
if __name__ == "__main__":
    paragraphs = [["hello", "world"],
                  ["How", "areYou", "doing"],
                  ["Please look", "and align", "to center"]]
    width = 16
    print("\n".join(solution(paragraphs, width)))
