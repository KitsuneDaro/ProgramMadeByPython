import json
import random


def common_list(list1, list2):
    common = []
    i = 0
    j = 0
    if len(list1) * len(list2) == 0:
        return []

    while True:
        if list1[i] > list2[j]:
            j += 1

            if j >= len(list2):
                break
        elif list1[i] < list2[j]:
            i += 1

            if i >= len(list1):
                break
        else:
            common.append(list1[i])

            i += 1
            j += 1

            if i >= len(list1) or j >= len(list2):
                break

    return common


with open('dialogue.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

name = '霊夢'
sta_chr = data['sta_chr']
end_chr = data['end_chr']
rank = data['rank']

dictionary = data['data'][name]


n = int(input('何回？>'))

while n > 0:
    for loop_i in range(n):
        words = [sta_chr]
        words_i = 0

        while words[-1] != end_chr:
            common = dictionary[words[words_i]][0]

            for i in range(1, rank):
                if i > words_i:
                    break

                next_common = common_list(common, dictionary[words[words_i - i]][i])

                if len(next_common) > 0:
                    common = next_common
                else:
                    break

            random_i = random.randrange(len(common))
            words.append(common[random_i])

            words_i += 1

        text = ''
        for words_i in range(1, len(words) - 1):
            text += words[words_i]

        print(text)
    
    n = int(input('何回？'))
