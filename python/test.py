
import re

import re


def stripComment(str):
    return re.sub(r'###.*?###', '', str, re.M, re.S)

# def stripComment(str):
#     count = 0
#     start = -1
#     end = -1
#     comments_blocks = []
#     in_string = False
#     for k, i in enumerate(str):
# print start, end, count
#         if i == '"':
#             if in_string:
#                 in_string = False
#             else:
#                 in_string = True
#         if not in_string:
# if i == '#':
#                 count += 1
#             else:
#                 count = 0

#             if count == 3:
#                 if start == -1:
#                     start = k - 3
#                 else:
#                     end = k + 1
#                     comments_blocks.append((start, end))
#                     start = -1
#                     end = -1
#                     count = 0
# print comments_blocks
#     if start > -1:
#         comments_blocks.append((start, -1))
#     deleted = 0
#     str_start = 0
#     results = []
#     for i in comments_blocks:
#         results.append(str[str_start: i[0]])
#         str_start = i[1]
#     results.append(str[str_start:])
#     return ''.join(results)

# print stripComment("int x; ### here is a comment ###")
a = """
int x; ### start of comment
comment continues
etc
### int y;"""
# a = "int x; ### here is a comment ###"
# a = '''###
# string s = "something###whatever";
#
# '''
print stripComment(a)
