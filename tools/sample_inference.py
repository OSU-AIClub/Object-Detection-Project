import torch

model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

imgs = ['../sample_images/P4-FEB-iStock-1352165307.jpg'] # batch of images

results = model(imgs)

results.print()
results.show()

print("\nxyxy[0]") 
print(results.xyxy[0])


print("\npandas.xyxy[0]")
print(results.pandas().xyxy[0])