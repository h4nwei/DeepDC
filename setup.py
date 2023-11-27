from setuptools import setup, find_packages
with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='DeepDC_PyTorch',
    version='0.1.2',
    description='DeepDC: Deep Distance Correlation as a Perceptual Image Quality Evaluator',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=['DeepDC_PyTorch'],
    author='Hanwei ZHU',
    author_email='hanwei.zhu@outlook.com',
    install_requires=["torch>=1.0"],
    url='https://github.com/h4nwei/DeepDC',
    keywords = ['pytorch', 'similarity', 'VGG','texture','structure','metric'], 
    platforms = "python",
    license='MIT',
)

# python setup.py sdist bdist_wheel
# twine check dist/*
# twine upload dist/*