import argparse

from reportlab.graphics import renderPDF, renderPM
from reportlab.graphics.barcode.qr import QrCodeWidget
from reportlab.graphics.shapes import Drawing


def generate_qr_code(
    text, file_format="pdf", scale=1, error="M", file_name=None
):
    qr_code_w = QrCodeWidget(text, barLevel=error)
    qr_code_drawing = Drawing(0, 0, transform=[scale, 0, 0, scale, 0, 0])
    qr_code_drawing.add(qr_code_w)
    # limit the paper size to just the QR code
    qr_code_drawing.width = qr_code_w.barWidth * scale
    qr_code_drawing.height = qr_code_w.barHeight * scale

    if file_name is None:
        file_name = f"{text.replace(' ', '_').replace('/','_')}.{file_format}"
    if file_format == "pdf":
        renderPDF.drawToFile(qr_code_drawing, file_name)
    elif file_format == "eps":
        renderPM.drawToFile(qr_code_drawing, file_name, "EPS")
    elif file_format == "png":
        renderPM.drawToFile(qr_code_drawing, file_name, "PNG")

    print(f"{file_format.upper()} file saved as {file_name}")


def main():
    parser = argparse.ArgumentParser(
        description="Generate QR Code in Vector Format"
    )
    parser.add_argument(
        "text", type=str, help="Input Text for QR Code Generation"
    )
    parser.add_argument(
        "-f",
        "--format",
        type=str,
        default="pdf",
        choices=["pdf", "eps", "png"],
        help="Output File Format (PDF, EPS, PNG)",
    )
    parser.add_argument(
        "-s", "--scale", type=float, default=1, help="QR Code Scale Factor"
    )
    parser.add_argument(
        "-e",
        "--error",
        type=str,
        default="M",
        choices=["L", "M", "Q", "H"],
        help="Error Correction Level",
    )
    parser.add_argument("-o", "--output", type=str, help="Output File Name")

    args = parser.parse_args()
    generate_qr_code(
        args.text, args.format, args.scale, args.error, args.output
    )


if __name__ == "__main__":
    main()
