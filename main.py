import torch
import numpy as np

# check numpy version
print("numpy: ", np.__version__)

# check torch version
print("torch: ", torch.__version__)

# check torch with gpu or not
print("torch cuda: ", torch.cuda.is_available())
