import os
from PIL import Image
from torchvision import transforms
import matplotlib.pyplot as plt

folder_path = "test"

paths = [os.path.join(folder_path, f) for f in os.listdir(folder_path)]

to_grey = transforms.Compose([
            transforms.Grayscale(num_output_channels=1),  # Convert to grayscale
            transforms.ToTensor(),  # Convert to tensor
])

img = Image.open(paths[6]).convert('RGB')
print(to_grey(img))

plt.imshow(to_grey(img).squeeze(), cmap='gray')
plt.show()