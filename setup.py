"""
PDF 합치기 애플리케이션의 설치 스크립트
"""
from setuptools import setup, find_packages
import os

# README 파일 읽기
with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

# 버전 정보
VERSION = '1.0.0'

setup(
    name="pdf_merger",
    version=VERSION,
    author="reinhardt0926",
    author_email="reinhardt0926@gmail.com",
    description="PDF 파일을 손쉽게 병합하는 애플리케이션",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/reinhardt0926/pdf_merger",
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        'PyPDF2>=3.0.0',
    ],
    entry_points={
        'console_scripts': [
            'pdf_merger=pdf_src.main:main',
        ],
    },
    # package_data={
    #     'pdf_merger': ['resources/icons/*.ico'],
    # },
)