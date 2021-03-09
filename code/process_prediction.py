def process_raw_prediction(prediction_file_path, test_file_path, output_path):
    with open(prediction_file_path, 'r', encoding='utf-8') as f1:
        with open(test_file_path, 'r', encoding='utf-8') as f2:
            with open(output_path, 'w', encoding='utf-8') as f3:
                for i in range(0, 200):
                    list = []
                    qid = ''
                    for j in range(0, 100):
                        line = f1.readline()[:-1]
                        print(line)
                        score = float(line)
                        qid, pid, _, _, _, _, _ = f2.readline().split('\t')
                        list.append((score, pid))
                    list.sort()
                    list = list[::-1]
                    rank = 1
                    for item in list:
                        f3.write(qid + "\t"
                                 + "Q0\t"
                                 + item[1] + "\t"
                                 + str(rank) + "\t"
                                 + str(item[0]) + "\t"
                                 + "IndriQueryLikelihood" + "\n")
                        rank += 1


if __name__ == '__main__':
    process_raw_prediction('../data/prediction_8_feature.dat', '../data/test_2.tsv', '../result/L2R_svm_200_8_feature.txt')