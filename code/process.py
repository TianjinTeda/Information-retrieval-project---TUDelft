def process_raw_data(input_path, output_path):
    with open(input_path, 'r', encoding='utf-8') as fr:
        with open(output_path, 'w', encoding='utf-8') as fw:
            line = fr.readline()[:-1]
            i = 1
            previous_qid = '1108939'
            r = 100
            while line != '':
                qid, pid, bm25, bm25_title, document_frequenct, title_frequency, url_frequency = line.split('\t')
                if qid != previous_qid:
                    i += 1
                    r = 100
                    print(i)
                #if float(bm25) != 0 and float(bm25_title) != 0:
                fw.write(str(r)+" qid:"+str(i)+" "+"1:"+bm25+" 2:"+bm25_title+" 3:"+document_frequenct+" 4:"+title_frequency+" 5:"+url_frequency+"\n")
                line = fr.readline()[:-1]
                previous_qid = qid
                r -= 1

def clean_data(input_path, output_path):
    pass


if __name__ == "__main__":
    process_raw_data("../data/test_correction.tsv", "../data/test_correction.dat")