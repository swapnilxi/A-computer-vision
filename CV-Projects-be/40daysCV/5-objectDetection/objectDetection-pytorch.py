#object detection - udemy - Deep Learning and Computer Vision A-Z + Prizes
import torch
from torch.autograd import variable
import cv2
#legacy- nowaday people use torchvision.transforms
# torchvision does not need ssd package externally 
import torchvision
#from data import BaseTransform, VOC_CLASSES  as LabelMap
#from ssd import build_ssd
import imageio
import numpy

# Load a pre-trained SSD model from torchvision
model = torchvision.models.detection.ssd300_vgg16(pretrained=True)
model.eval()

#defining a function that will do the detection 
#net- neural network
def detect(frame, net, transform):
    # height and width of the frame
    height, width=frame.shape[0,1]
    # can be written as frame.shape[:2]
    # We apply the transformation to our frame.
    frame_t= transform(frame)[0]
    
    #converting to tensor 
    x= torch.from_numpy(frame_t).permute(2,0,1)
    #transform = torchvision.transforms.ToTensor()
    #img = transform(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    # If you're using torchvision.transforms.ToTensor(), then there's no need to manually permute
    # dimensions (permute(2, 0, 1)), because ToTensor() already does that for you. 
    x.unsqueeze(0) # in older version variable was needed 
    
    y= net(x)
    detections=y.data
    
    #normalizating the dimension
    
    