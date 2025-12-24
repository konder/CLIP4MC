from setuptools import setup, find_packages

setup(
    name='clip4mc',
    version='0.1.0',
    description='CLIP4MC: Reinforcement Learning Friendly Vision-Language Model for Minecraft',
    author='PKU-RL',
    url='https://github.com/konder/clip4mc',
    packages=find_packages(),
    python_requires='>=3.9',
    install_requires=[
        'torch>=1.10.0',
        'x-transformers==0.27.1',
        'einops',
        'pyyaml',
    ],
)

