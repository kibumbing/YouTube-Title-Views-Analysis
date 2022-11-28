import pandas as pd
pd.options.display.max_columns = 100
pd.options.display.max_rows = 100
from sortings import *
import time

if __name__ == '__main__':
    cdm_2019 = pd.read_csv("calmdownman_2019.csv")
    cdm_2020 = pd.read_csv("calmdownman_2020.csv")
    cdm_2021 = pd.read_csv("calmdownman_2021.csv")
    cdm_2022 = pd.read_csv("calmdownman_2022.csv")

    cdm_data = pd.concat([cdm_2019, cdm_2020, cdm_2021, cdm_2022], ignore_index=True)
    title = []
    views = []
    for i in range(len(cdm_data)):
        if cdm_data['views'][i] == '-':
            continue
        temp = '\"' + str(cdm_data['title'][i]) + '\"'
        title.append(temp)
        views.append(int(cdm_data['views'][i]))
    views_temp = views.copy()

    sorted_views = []
    start = time.time()
    sorted_views = bubble_sort(views)
    print(f"bubble sort:{time.time()-start}")
    start = time.time()
    sorted_views = selection_sort(views)
    print(f"selection sort:{time.time() - start}")
    start = time.time()
    sorted_views = insertion_sort(views)
    print(f"insertion sort:{time.time() - start}")
    start = time.time()
    sorted_views = merge_sort(views)
    print(f"merge_sort sort:{time.time() - start}")
    start = time.time()
    sorted_views = quick_sort(views)
    print(f"quick sort:{time.time() - start}")
    start = time.time()
    sorted_views = heap_sort(views)
    print(f"heap sort:{time.time() - start}")
    start = time.time()
    sorted_views = radix_sort(views)
    print(f"radix sort:{time.time() - start}")

    sorted_title = []
    for i in range(len(sorted_views)):
        for j in range(len(views_temp)):
            if sorted_views[i] == views_temp[j]:
                sorted_title.append(title[j])

    sorted_cdm = pd.DataFrame([sorted_title, sorted_views]).T
    sorted_cdm.columns = ['title', 'views']
    idx = -1
    for i in range(len(sorted_cdm)):
        if sorted_cdm['views'][i] > 1000000:
            sorted_cdm['views'][i] = 1
            if idx == -1:
                print(f"100만 이하: {i}개 (0~{i-1})")
                print(f"100만 초과: {len(sorted_cdm)-i}개 ({i}~{len(sorted_cdm)})")
                idx = i
        else:
            sorted_cdm['views'][i] = 0

    down_100 = sorted_cdm[:idx]
    down_100 = down_100.sample(frac=1).reset_index(drop=True)
    up_100 = sorted_cdm[idx:]
    up_100 = up_100.sample(frac=1).reset_index(drop=True)
    len_down = int(len(down_100)*0.8)
    len_up =int(len(up_100)*0.8)

    test_data = pd.concat([up_100[len_up:], down_100[len_down:]], ignore_index=True)
    test_data = test_data.sample(frac=1).reset_index(drop=True)
    test_data.to_csv('calmdownman_test.csv')

    train_data = pd.concat([up_100[:len_up].sample(n=len_down, replace=True), down_100[:len_down]],
                           ignore_index=True)
    train_data = train_data.sample(frac=1).reset_index(drop=True)
    train_data.to_csv('balanced_calmdownman_train.csv')

    train_data = pd.concat([up_100[:len_up].sample(n=len_down, replace=True), down_100[:len_down]],
                           ignore_index=True)
    train_data = train_data.sample(frac=1).reset_index(drop=True)
    train_data.to_csv('normal_calmdownman_train.csv')

    train_data = pd.concat([up_100[:len_up].sample(n=len_up//10), down_100[:len_down]],
                           ignore_index=True)
    train_data = train_data.sample(frac=1).reset_index(drop=True)
    train_data.to_csv('unbalanced_calmdownman_train.csv')