# 2209_youtube-title-views-analysis
Algorithm project

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
