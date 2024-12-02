import time
from multiprocessing import Pool


def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf-8') as file:
        while True:
            line = file.readline().strip()
            all_data.append(line)
            if not line:
                break


# Список название файлов
file_name = ['file 1.txt', 'file 2.txt', 'file 3.txt', 'file 4.txt']

# Линейное выполнение.
start_l = time.time()

for j in file_name:
    read_info(j)
end_l = time.time()
print(f'Время работы линейной функции:{end_l - start_l}')

# Мультипроцессорное выполнение:

if __name__ == '__main__':
    start_m = time.time()

    with Pool() as pool:
        results = map(read_info, file_name)

    end_m = time.time()

    print(f'Время работы мультипроцесса:{end_m - start_m}')
