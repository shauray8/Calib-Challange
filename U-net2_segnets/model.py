import torch
import torch.nn as nn


# --------------- U square Net architecture here the research paper https://arxiv.org/pdf/2005.09007v2.pdf --------------- #

class Unet_square(nn.Module):
    def __init__(self):
        super(Unet_square, self).__init__()

        pass

    # --------------- I think this is the only function i'll need --------------- #

    def conv_blocks_BNR(self, some_more_stuff):
        pass

    def forward(self, z):
        pass


if __name__ == "__main__":
    ## Using U square net for segmentations 
    ## getting the data from comma's some repo
    model = Unet_square()