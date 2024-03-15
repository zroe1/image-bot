import os
from PIL import Image
from torchvision import transforms
import torch

folder_path = "test"

paths = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith("png")]

to_grey = transforms.Compose([
            transforms.Grayscale(num_output_channels=1),  # Convert to grayscale
            transforms.ToTensor(),  # Convert to tensor
])

all_imgs = []

for path in paths:
    img = Image.open(path).convert('RGB')
    img = to_grey(img)
    all_imgs.append(img)

all_imgs_tensor = torch.stack(all_imgs, dim=0)

torch.save(all_imgs_tensor, 'all_imgs.pt')
