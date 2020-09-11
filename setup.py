from setuptools import setup, find_packages

setup(
    name='efficientdet',
    version='0.0.1',
    description='The pytorch re-implement of the official efficientdet.',
    python_requires='>=3.7',
    install_requires=[
        'numpy',
        'tqdm',
        'opencv-python',
        'tensorboard',
        'tensorboardX',
        'pyyaml',
        'webcolors',
        'torch==1.4.0',
        'torchvision==0.5.0'
    ]
)
