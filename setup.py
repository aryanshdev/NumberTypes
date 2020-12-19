import setuptools

with open('README.md','r') as f:
    long_description = f.read()

setuptools.setup(
    name = 'NumberTypes',
    version='0.01',
    author = 'Aryansh Gupta (AryanshDev)',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    author_email = 'Aryanshappmaker@gmail.com',
    description = 'Python Module to identify type of a number quickly and easily',
    py_modules = ["numbertypes"],
    package_dir = {'':'src'},
    license='MIT',
    python_requires = '>=3.1',
    keywords=['numbers','helper','number types','number type','math']
)