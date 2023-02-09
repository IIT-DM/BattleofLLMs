import json
import torch
import torch.nn as nn
from torch.optim.lr_scheduler import StepLR
import random
from tqdm import tqdm
from transformers import GPT2LMHeadModel, GPT2Tokenizer

num_epochs = 8
supporting_texts = json.load(open('./supporting.json'))
refuting_texts = json.load(open('./refuting.json'))


split = 0.8

_prompt = '\n\n\nThe evidence supports the claim:\n'
train_list = [item + _prompt + 'Yes.' for item in supporting_texts]
train_list += [item + _prompt + 'Nope.' for item in refuting_texts]
random.shuffle(train_list)

json.dump(train_list, open('./train_list.json', 'w'))

train_list = json.load(open('./train_list.json'))

print(train_list[0])

def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

def batchify(data, n):
    len_dict = {}
    for item in data:
        length = item.shape[1]
        try:
            len_dict[length].append(item)
        except:
            len_dict[length] = [item]

    batch_chunks = []
    for k in len_dict.keys():
        vectors = len_dict[k]
        batch_chunks += chunks(vectors, n)

    batches = []
    for chunk in batch_chunks:
        inputs = torch.stack([item[0] for item in chunk])
        batches.append((inputs))

    return batches


tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
model = GPT2LMHeadModel.from_pretrained('gpt2')
model.cuda()
criterion = nn.BCEWithLogitsLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=2e-5)

_limit = 1024
data = []
total_skipped = 0
for item in train_list:
    tokens = tokenizer.encode(item, return_tensors='pt')
    if tokens.shape[1] > _limit:
        total_skipped += 1
        continue
    data.append(tokens)
print(f'Skipped {total_skipped} out of {len(train_list)}')

train_batches = batchify(data, 1)

def train(train_model, batches, optimizer, criterion):
    total_loss = 0.
    for i, batch in tqdm(enumerate(batches), total=len(batches)):
        model.train()
        inputs = batch
        optimizer.zero_grad()
        loss = train_model(inputs.cuda(), labels=inputs.cuda())[0]
        loss.backward()
        torch.nn.utils.clip_grad_norm_(train_model.parameters(), 0.5)
        optimizer.step()
        total_loss += loss.item()

    return total_loss / len(batches)


random.shuffle(train_batches)
scheduler = StepLR(optimizer, step_size=2, gamma=0.8)
for epoch in range(num_epochs):
    random.shuffle(train_batches)
    loss = train(model, train_batches, optimizer, criterion)
    print('Epoch:', epoch, 'Loss:', loss)
    torch.save({'epoch': epoch,
                'model_state_dict': model.state_dict()},
                'save_fever' + str(epoch))
    scheduler.step()
