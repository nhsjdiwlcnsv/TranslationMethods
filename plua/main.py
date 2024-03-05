import re


token_patterns = [
    ('MULTI_LINE_COMMENT', re.compile(r'--\s*\[\[.*?\]\]\s*(--)?', re.DOTALL)),
    ('SINGLE_LINE_COMMENT', re.compile(r'--.*')),
    ('KEYWORD', re.compile(r'\b(and|break|do|else|elseif|end|false|for|function|if|in|local|nil|not|or|repeat|return|then|true|until|while)\b')),
    ('IDENTIFIER', re.compile(r'[a-zA-Z_][a-zA-Z0-9_]*')),
    ('STRING_LITERAL', re.compile(r'(\'[^\']*\'|\"[^\"]*\")')),
    ('NUMBER_LITERAL', re.compile(r'\d+(\.\d+)?')),
    ('BOOLEAN_LITERAL', re.compile(r'\b(true|false)\b')),
    ('NIL_LITERAL', re.compile(r'\bnil\b')),
    ('OPERATOR', re.compile(r'[+\-*/^%=|<|>|~]')),
    ('LOGICAL_OPERATOR', re.compile(r'\b(and|or|not)\b')),
    ('UNARY_OPERATOR', re.compile(r'[\-#]')),
    ('PUNCTUATION', re.compile(r'[(),;.]')),
]


def tokenize(source_code: str) -> list[tuple[str, str]]:
    tokens: list[tuple[str, str]] = []
    lines: list[str] = source_code.split("\n")
    line_index: int = 0
    pos: int = 0

    while pos < len(source_code):
        match_found: bool = False

        for token_type, regex in token_patterns:
            match: re.Match | None = regex.match(source_code, pos)

            if match:
                match_found = True
                pos = match.end(0)
                tokens.append((token_type, match.group(0)))
                break

        if not match_found:
            print("---------------------------------------")
            print("Line index:", line_index)
            print("Position:", pos)
            print("Lengths of the lines passed:", list(map(len, lines[:line_index])))
            print()

            print(f"INVALID TOKEN AT POSITION {line_index}:{pos - sum(map(len, lines[:line_index]))}: {source_code[pos]}")
            pos += 1

        while pos > sum(map(len, lines[:line_index])):
            line_index += 1


# ПЯТЬ ТЫСЯЧ (ТРИТОН) И ПЯТЬ ТЫСЯЧ ДВА (РАГ)


    return tokens

if __name__ == "__main__":
    with open("test_program.lua") as f:
        source_code: str = f.read().strip("\n")

    for token_type, value in tokenize(source_code):
        print(f"{token_type}: {value}")

"""
[ 1,  2,  3,  4,  5,  6],
[ 7,  8,  9, 10, 11, 12],
[13, 14, 15, 16, 17, 18],
[19, 20, 21, 22, 23, 24],
[25, 26, 27, 28, 29, 30],
"""
