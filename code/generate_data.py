import random


def sampling(input_path, output_path, num_of_sample, probability):
    with open(input_path, 'r', encoding='utf-8') as fr:
        with open(output_path, 'w', encoding='utf-8') as fw:
            count = 0
            line = fr.readline()
            while line != '':
                number = random.random()
                if number < probability:
                    count += 1
                    fw.write(line)
                    print(count)
                if count == num_of_sample:
                    break
                line = fr.readline()


if __name__ == "__main__":
    sampling('../data/queries.doctrain.tsv', '../data/train.tsv', 500, 0.2)