import platform
from setuptools import setup, Extension
import numpy

CXX_ARGS = {
    "Darwin": ["-std=c++11", "-march=native", "-ftree-vectorize"],
    "Linux": ["-fopenmp", "-std=c++11", "-march=native", "-ftree-vectorize"],
    "Windows": ["/openmp", "/std:c++latest", "/arch:AVX2"]
}

setup(
    name="lapjv",
    description="Linear sum assignment problem solver using Jonker-Volgenant "
                "algorithm.",
    version="1.3.1",
    license="MIT",
    author="Vadim Markovtsev",
    author_email="vadim@sourced.tech",
    url="https://github.com/src-d/lapjv",
    download_url="https://github.com/src-d/lapjv",
    ext_modules=[Extension("lapjv",
                           sources=["python.cc"],
                           extra_compile_args=CXX_ARGS[platform.system()],
                           include_dirs=[numpy.get_include()])],
    install_requires=["numpy"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6"
    ]
)

# python3 setup.py bdist_wheel
# auditwheel repair -w dist dist/*
# twine upload dist/*manylinux*
