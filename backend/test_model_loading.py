from predict_image import predict_image
from predict_gas import predict_gas

print("Testing TFLite Image Model...")
print(predict_image("test.jpg"))

print("Testing Gas Model...")
print(predict_gas([0.56, 0.43]))
