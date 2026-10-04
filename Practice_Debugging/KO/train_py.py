import torch.nn as nn


def train(model, train_loader, optimizer, epochs, device):
    criterion = nn.CrossEntropyLoss()
    for epoch in range(epochs):
        for X_batch, Y_batch in train_loader:
            X_batch = X_batch.to(device)
            Y_batch = Y_batch.to(device)

            output = model(X_batch)               # logits, (batch, 10)
            loss = criterion(output, Y_batch)

            optimizer.zero_grad()                 # 누적된 기울기를 지운다
            loss.backward()                       # autograd 가 기울기를 계산
            optimizer.step()                      # optimizer 가 파라미터를 갱신
