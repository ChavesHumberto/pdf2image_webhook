from flask import Flask, request, jsonify
from pdf2image import convert_from_bytes
import base64
import io

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 20 * 1024 * 1024  # 20MB

@app.route('/pdf-to-image', methods=['POST'])
def pdf_to_image():
    """
    n8n-compatible webhook endpoint for converting PDF files to base64-encoded JPEG images.
    Aceita apenas PDF enviado como binário (application/pdf).
    """
    if request.content_type != 'application/pdf':
        return jsonify({'success': False, 'error': 'Content-Type must be application/pdf'}), 400

    pdf_bytes = request.get_data()
    if not pdf_bytes:
        return jsonify({'success': False, 'error': 'No PDF data received'}), 400

    try:
        images = convert_from_bytes(pdf_bytes, dpi=200, fmt="jpeg")
        if not images:
            return jsonify({'success': False, 'error': 'No pages found'}), 400

        img_io = io.BytesIO()
        images[0].save(img_io, format='JPEG', quality=85, optimize=True)
        img_io.seek(0)
        img_base64 = base64.b64encode(img_io.read()).decode('utf-8')

        return jsonify({
            'success': True,
            'image_base64': img_base64,
            'pages_processed': 1,
            'total_pages': len(images)
        }), 200

    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

