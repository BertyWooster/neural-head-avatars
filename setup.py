from setuptools import setup, find_packages

setup(
    name="nha",
    version="0.1.0",
    packages=find_packages(),
    python_requires=">=3.9",
    install_requires=[
        "ConfigArgParse",
        "numpy==1.21",
        "torch==1.12.0",
        "torchvision==0.13.0",
        "pytorch3d==0.7.1",
        "matplotlib",
        "tensorboard",
        "scipy",
        "opencv-python",
        "chumpy",
        "face-alignment",
        "face-detection-tflite",
        "pytorch-lightning==1.2.4"
        "lpips",
        "pytorch_msssim",
        "cpbd@git+https://github.com/wl2776/python-cpbd.git",
        "scikit-learn",
        "torchscope@git+https://github.com/Tramac/torchscope.git",
        "jupyter"
    ],
)
