from setuptools import setup

setup(
    name='okama',
    version='0.8',
    license='MIT',
    description='Modern Portfolio Theory (MPT) Python package',
    author='Sergey Kikevich',
    author_email='sergey@rostsber.ru',
    url='https://okama.io/',
    download_url='https://github.com/mbk-dev/okama/archive/v0.8.tar.gz',
    keywords=['finance', 'investments', 'efficient frontier', 'python'],
    packages=['okama', 'tests'],
    package_data={'tests': ['*.csv']},
    install_requires=['pytest',
                      'pandas',
                      'requests',
                      'numpy',
                      'scipy',
                      'psycopg2',
                      'urllib3',
                      'matplotlib',
                      'setuptools'],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers, End Users/Desktop, Financial and Insurance Industry, Science/Research",
        "Topic :: Scientific/Engineering :: Mathematics",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7'
)
