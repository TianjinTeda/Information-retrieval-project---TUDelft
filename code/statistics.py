import matplotlib.pyplot as plt


def document_statistics():
    sum_index = 0
    sum_len = 0
    max_len = 0
    min_len = 1000000000
    avg_len = 0
    length_list = 5*[0]
    stride = 2000
    with open('../data/msmarco-docs.tsv', encoding='utf-8') as f:
        line = f.readline()
        i= 1
        while line != '':
            sum_index += 1
            pid, url, title, content = line.split('\t')
            content = content.split(' ')
            length = len(content)
            sum_len += length
            if length > max_len:
                max_len = length
            if length < min_len:
                min_len = length
            if length < 10000:
                length_list[int(length / stride)] += 1
            if i % 10000 == 0:
                print(i)
            i += 1
            line = f.readline()
    avg_len = sum_len / i

    print('sum_index', sum_index)
    print('sum_len', sum_len)
    print('max_len', max_len)
    print('min_len', min_len)
    print('avg_len', avg_len)
    length = [str(i) for i in range(0, 5)]
    plt.bar(length, length_list)
    plt.show()


if __name__ == '__main__':
    document_statistics()