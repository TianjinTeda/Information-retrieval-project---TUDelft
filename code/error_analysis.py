def analyze_error(result_file_path, answer_file_path, extracted_file_path):
    qid_list = []
    with open(result_file_path, 'r', encoding='utf-8') as f:
        line = f.readline()
        while line != '':
            qid, _, _, _, _, _ = line.split('\t')
            if not qid in qid_list:
                qid_list.append(qid)
            line = f.readline()

    with open(answer_file_path, 'r', encoding='utf-8') as fr:
        with open(extracted_file_path, 'w', encoding='utf-8') as fw:
            line = fr.readline()
            i = 0
            while line != '':
                qid, _, _, _ = line.split(' ')
                if qid in qid_list:
                    fw.write(line)
                if i % 1000 == 0:
                    print(i)
                i += 1
                line = fr.readline()

if __name__ == "__main__":
    analyze_error('../result/result_train_bm25_top10.txt', '../data/msmarco-doctrain-qrels.tsv', '../data/train_compare.txt')