import logging
import re
from collections import Counter
from typing import List

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(name)s -   %(message)s',
                    datefmt='%m/%d/%Y %H:%M:%S',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

"""
주어진 Paragraph (String) 에서 금지된 단어를 제외한 가장 흔하게 등장하는 단어를 출력하자.
적어도 하나의 단어는 금지되지 않았고, 모든 정답 단어는 유니크하다.

Paragraph 에 있는 단어는 구두점을 무시하고 대소문자 구분을 하지 않는다.

# 819. Most Common Word (https://leetcode.com/problems/most-common-word/)
"""


class Solution:

  def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
    # r'[^\w]' -> 정규식에서 \w는 단어 문자를 뜻함.
    # str.isalnum() => 문자열이 알파벳([a-zA-Z])과 숫자([0-9])로만 구성되었는지 확인하는 파이썬 문자열 함수를 통하여
    # 정규식을 대체할 수 있음.
    words = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split() if word not in banned]
    return Counter(words).most_common(1)[0][0]


if __name__ == '__main__':
  paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
  banned = ["hit"]
  print(Solution().mostCommonWord(paragraph, banned))
