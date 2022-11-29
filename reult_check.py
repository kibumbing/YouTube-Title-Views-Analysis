from torch.utils.data import Dataset, DataLoader
from kobert.utils import get_tokenizer
from kobert.pytorch_kobert import get_pytorch_kobert_model
from bert_model import *
import pandas as pd

cdm_test_data = pd.read_csv("calmdownman_test.csv")

max_len = 64
batch_size = 64

device = torch.device("cuda:1")
bertmodel, vocab = get_pytorch_kobert_model()

tokenizer = get_tokenizer()
tok = nlp.data.BERTSPTokenizer(tokenizer, vocab, lower=False)

# model = torch.load('normal_model.pt')
model = torch.load('unbalanced_model.pt')
# model = torch.load('balanced_model.pt')
# model = torch.load('balanced2_model.pt')

def predict(predict_sentence):
    data = [predict_sentence, '0']
    dataset_another = [data]

    another_test = BERTDataset(dataset_another, 0, 1, tok, max_len, True, False)
    test_dataloader = torch.utils.data.DataLoader(another_test, batch_size=batch_size, num_workers=5)

    model.eval()

    for batch_id, (token_ids, valid_length, segment_ids, label) in enumerate(test_dataloader):
        token_ids = token_ids.long().to(device)
        segment_ids = segment_ids.long().to(device)

        valid_length = valid_length
        label = label.long().to(device)

        out = model(token_ids, valid_length, segment_ids)

        for i in out:
            logits = i
            logits = logits.detach().cpu().numpy()

    return np.argmax(logits)

num = 0.0
num0 = 0.0
num1 = 0.0
for i in range(len(cdm_test_data)):
    result = predict(cdm_test_data['title'][i])
    if result== cdm_test_data['views'][i]:
        num += 1
        if result == 1:
            num1 += 1
        else:
            num0 += 1
print(f"0의 recall: {num0/num}")
print(f"1의 recall: {num1/num}")

num1_1 = 0.0
num0_1 = 0.0
num0 = 0.0
num1 = 0.0
for i in range(len(cdm_test_data)):
    result = predict(cdm_test_data['title'][i])
    if result==1:
        num1_1 += 1
        if result==cdm_test_data['views'][i]:
            num1 += 1
    else:
        num0_1 += 1
        if result==cdm_test_data['views'][i]:
            num0 += 1
print(f"0의 precision: {num0/num0_1}")
print(f"1의 precision: {num1/num1_1}")

#질문 무한반복하기! 0 입력시 종료
end = 1
while end == 1 :
    sentence = input("유튜브 영상의 제목을 입력하시오. : ")
    if sentence == 0 :
        break
    if predict(sentence) == 0:
        print("조회수가 100만 미만 입니다.")
    elif predict(sentence) == 1:
        print("조회수가 100만 이상입니다.")
    print("\n")