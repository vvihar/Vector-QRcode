# qrcodegen

qrcodegen is a Python CLI package that generates QR codes in vector formats (PDF, EPS) and PNG from text input.

This package was created with the help of ChatGPT.

## Installation

You can install qrcodegen using pip:

```bash
pip install qrcodegen
```

## Usage

To generate a QR code, use the following command:

```bash
qrcodegen "your text here" -f <file_format> -o <output_file> -e <error_correction> -s <scale>
```

Replace `"your text here"` with the text you want to encode, `<file_format>` with the desired vector format (pdf, eps), `<output_file>` with the desired name of the output file, `<error_correction>` with the desired error correction level of the QR code (L, M, Q, H), and `<scale>` with the desired scale of the QR code (in integer).

For example, to generate a QR code in PDF format with the text "Hello World" and save it as "my_qrcode.pdf", run the following command:

```bash
qrcodegen "Hello World" -f pdf -o my_qrcode.pdf
```

## Options

- `-h`: show the help message.
- `-f`, `--format`: the desired vector format (pdf, eps) or png. Defaults to pdf.
- `-o`, `--output`: the desired name of the output file.
- `-e`, `--error`: the desired error correction level of the QR code (L, M, Q, H). Defaults to M.
- `-s`, `--scale`: the desired scale of the QR code. Defaults to 1.

## Dependencies

- reportlab

## License

This package is licensed under the MIT license.

## Acknowledgement

Most part of the package and its README were generated using ChatGPT, a large language model trained by OpenAI, based on the GPT-3.5 architecture.

QR Code is a registered trademark of DENSO WAVE.
