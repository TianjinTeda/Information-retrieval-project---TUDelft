def check_the_document(file_path):
    with open(file_path, 'r') as f:
        data = f.readline()
        pid, url, title, content = data.split('\t')
        print(pid)
        print(url)
        print(title)
        print(content)


if __name__ == '__main__':
    check_the_document('../data/msmarco-docs.tsv')