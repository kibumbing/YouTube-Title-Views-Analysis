youtube title views analysis

논문
https://github.com/kibumbing/youtube-title-views-analysis/blob/main/%EC%A0%95%EB%A0%AC%20%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98%EC%9D%84%20%EA%B8%B0%EB%B0%98%ED%95%9C%20%EC%9E%90%EC%97%B0%EC%96%B4%20%EC%B2%98%EB%A6%AC%EC%97%90%EC%84%9C%EC%9D%98%20%EB%B6%88%EA%B7%A0%ED%98%95%20%EB%8D%B0%EC%9D%B4%ED%84%B0%20%EC%A1%B0%EC%A0%95.pdf

사용자 메뉴얼

1. get_data.py
- YouTube API를 통해 유튜버 침착맨의 2019-2022 사이의 동영상 데이터 수집
- 읽어들일 동영상 리스트의index를 변경해 가며 각 년도의 동영상 데이터 수집

2. data_preprocessing.py
- 수집한 데이터를 전처리
- 수집한 데이터를 concat하고 각종 알고리즘을 사용하여 정렬
- 정렬한 데이터를 기준에 따라 학습 데이터와 테스트 데이터로 split
- 기준 1)upsampling 2)downsampling 3)default 4)imbalanced
- Feature: title(String)
- Label: views(0,1)

3. youtube_classification.py
- KoBERT를 사용하여 학습 데이터 학습 및 모델 저장
- 정확도 확인

4. result.py
- recall, precision 확인
- 임의의 유튜브 title을 입력하여 모델 출력 확인
