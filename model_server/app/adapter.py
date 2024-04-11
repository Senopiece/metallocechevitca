from torch import nn


class Adapter(nn.Module):
    def __init__(self):
        super().__init__()
        self.body = nn.Sequential(
            nn.Linear(512, 2048),
            nn.ReLU(),
            nn.Linear(2048, 512),
        )
        self.loss = nn.CosineEmbeddingLoss(margin=.0)

    def forward(self, x):
        return x + self.body(x)
