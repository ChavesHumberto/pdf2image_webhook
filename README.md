# PDF to Image Webhook

This project provides a simple n8n-compatible webhook endpoint for converting PDF files to base64-encoded JPEG images. It is built using Flask and utilizes the `pdf2image` library for PDF processing.

## Overview

The webhook accepts POST requests containing PDF files and returns a JSON response with the base64-encoded image data and metadata. This functionality is useful for applications that need to convert PDF documents into images for display or further processing.

## Features

- Accepts PDF file uploads via a POST request.
- Converts each page of the PDF into JPEG images.
- Returns the first page as a base64-encoded JPEG image.
- Provides detailed error messages for invalid requests.

## Installation

To set up the project, clone the repository and install the required dependencies:

```bash
git clone <repository-url>
cd pdf2image-webhook
pip install -r requirements.txt
```

## Usage

Run the Flask application:

```bash
python src/app.py
```

The application will start listening on `http://localhost:5000`.

### Endpoint

- **POST /pdf-to-image**: Upload a PDF file to convert it to a base64-encoded JPEG image.

#### Request

- Content-Type: `multipart/form-data`
- Form field: `file` (the PDF file to upload)

#### Response

A successful response will return a JSON object containing:

- `success`: Boolean indicating the success of the operation.
- `image_base64`: Base64-encoded JPEG image data.
- `filename`: The name of the uploaded file.
- `pages_processed`: Number of pages processed (always 1 for this endpoint).
- `total_pages`: Total number of pages in the PDF.
- `image_size_bytes`: Size of the base64-encoded image in bytes.
- `message`: Success message.

### Error Handling

The API provides n8n-friendly error responses for various failure scenarios, including:

- No file part in the request.
- Invalid file type (only PDF files are supported).
- Empty file uploads.
- PDF files with no pages.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.