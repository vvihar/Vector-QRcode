from setuptools import setup

setup(
    name="qrcodegen",
    version="0.1",
    py_modules=["qrcodegen"],
    install_requires=["qrcode", "reportlab"],
    entry_points={"console_scripts": ["qrcodegen = qrcodegen:main"]},
    author="Gulmohar",
    description="A CLI tool for generating QR codes in vector formats",
    license="MIT",
    keywords="qrcode",
    url="https://github.com/vvihar/Vector-QRcode",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Utilities",
    ],
)
