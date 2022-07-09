import glob
import MeCab
import json


def list_of_empty_lists(rank):
    lists = []
    for i in range(rank):
        lists.append([])
    return lists


def arrange(line, value):
    line.append(value)

    for i in range(len(line) - 1, 0, -1):
        if value < line[i - 1]:
            line[i - 1], line[i] = value, line[i - 1]
        else:
            break

    return line


target = '霊夢'
sta_chr = '\t'
end_chr = '\n'
sep_chr = '：'
rank = 3

tagger = MeCab.Tagger('-Owakati')
file_names = glob.glob('dialogues/*')

save_file_name = 'dialogue.json'
chr_i = 0

json_file = {}
json_file['sta_chr'] = sta_chr
json_file['end_chr'] = end_chr
json_file['rank'] = rank
json_file['data'] = {}
json_file['data'][target] = {}

for file_name in file_names:
    with open(file_name, 'r') as file:
        lines = file.readlines()

    for line in lines:
        if line.find(target + sep_chr) == 0:
            line = line.rsplit('\n', 1)[0]
            line = line.split(sep_chr, 1)[1]
            words = [sta_chr] + tagger.parse(line).split() + [end_chr]

            for i in range(len(words)):
                word = words[i]
                chr_i += 1

                try:
                    json_file['data'][target][word]
                except KeyError:
                    json_file['data'][target][word] = list_of_empty_lists(rank)

                for j in range(rank):
                    if i + j + 1 < len(words):
                        json_file['data'][target][word][j] = arrange(
                            json_file['data'][target][word][j], words[i + j + 1])
                    else:
                        break

print('分かち書きの単語数:{0}'.format(chr_i))

with open(save_file_name, 'w', encoding='utf-8') as save_file:
    json.dump(json_file, save_file, indent=4, ensure_ascii=False)
