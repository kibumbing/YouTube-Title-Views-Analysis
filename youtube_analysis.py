import pandas as pd
pd.options.display.max_columns = 100
pd.options.display.max_rows = 100

df = pd.read_csv("calmdownman_2022_2.csv")

# print(KRvideo.head())
# print(KRvideo.info())

for i in range(len(df)):
    st = df['description'][i]
    st_2 = st.split()
    st_3 = []
    for word in st_2:
        if '식욕저하' in word:
            st_3.append('식욕저하 다이어트 먹방')
            break
        elif '일상재롱' in word:
            st_3.append('일상재롱 영상')
            break
        elif '쿡방' in word:
            st_3.append('쿡방')
            break
        elif '짧게' in word:
            st_3.append('짧게 한 게임들')
            break
        elif '이상형' in word:
            st_3.append('이상형 월드컵')
            break
        elif '특강' in word:
            st_3.append('특강')
            break
        elif '침터뷰' in word:
            st_3.append('침터뷰')
            break
        elif '물건' in word:
            st_3.append('물건사기 프로젝트 쇼핑맨')
            break
        elif '뱉은' in word:
            st_3.append('침착맨의 뱉은 말은 지킨다')
            break
        elif '리그' in word:
            st_3.append('리그 오브 레전드 게임영상')
            break
        elif '노래방' in word:
            st_3.append('노래방')
            break
        elif '쏘영' in word:
            st_3.append('쏘영이와 함께라면')
            break
        elif '설명회' in word:
            st_3.append('설명맨: 대충 설명하고 쉽게 설명하기')
            break
        elif '감상회' in word:
            st_3.append('(스포)감상회')
            break
        else:
            continue
    if (st_3 == []):
        st_3.append('기타')
    #print(st_3)

for i in range(len(df)):
    st = df['description'][i]
    st_2 = st.split()
    st_3 = []
    for word in st_2:
        if '#주호민' in word:
            st_3.append('주호민')
        elif '#김풍' in word:
            st_3.append('김풍')
        elif '#안될과학' in word:
            st_3.append('안될과학')
        elif '#통닭천사' in word:
            st_3.append('통닭천사')
        elif '#배도라지' in word:
            st_3.append('배도라지')
        elif '#' in word:
            st_3.append(word)
    print(st_3)
