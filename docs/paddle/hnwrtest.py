# 导入图像读取第三方库
# import matplotlib.image as mpimg
# import matplotlib.pyplot as plt
# import cv2
#加载飞桨和相关类库
import paddle.fluid as fluid
from paddle.fluid.dygraph.nn import Linear
import numpy as np
from PIL import Image

# # 读取图像
# img1 = cv2.imread('./work/example_0.png')
# example = mpimg.imread('./work/example_0.png')
# # 显示图像
# plt.imshow(example)
# plt.show()
# im = Image.open('./work/example_0.png').convert('L')
# print(np.array(im).shape)
# im = im.resize((28, 28), Image.ANTIALIAS)
# plt.imshow(im)
# plt.show()
# print(np.array(im).shape)

# 定义mnist数据识别网络结构，同房价预测网络
class MNIST(fluid.dygraph.Layer):
    def __init__(self):
        super(MNIST, self).__init__()
        
        # 定义一层全连接层，输出维度是1，激活函数为None，即不使用激活函数
        self.fc = Linear(input_dim=784, output_dim=1, act=None)
        
    # 定义网络结构的前向计算过程
    def forward(self, inputs):
        outputs = self.fc(inputs)
        return outputs

# 读取一张本地的样例图片，转变成模型输入的格式
def load_image(img_path):
    # 从img_path中读取图像，并转为灰度图
    im = Image.open(img_path).convert('L')
    print(np.array(im))
    im = im.resize((28, 28), Image.ANTIALIAS)
    im = np.array(im).reshape(1, -1).astype(np.float32)
    # 图像归一化，保持和数据集的数据范围一致
    im = 1 - im / 127.5
    return im

# 定义预测过程
with fluid.dygraph.guard():
    model = MNIST()
    params_file_path = 'mnist'
    img_path = './work/example_0.png'
# 加载模型参数
    model_dict, _ = fluid.load_dygraph("mnist")
    model.load_dict(model_dict)
# 灌入数据
    model.eval()
    tensor_img = load_image(img_path)
    result = model(fluid.dygraph.to_variable(tensor_img))
#  预测输出取整，即为预测的数字，打印结果
    print("本次预测的数字是", result.numpy().astype('int32'))