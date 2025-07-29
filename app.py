from flask import Flask, render_template, request, jsonify, send_from_directory
import os
import json
from werkzeug.utils import secure_filename

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
KEY_FILE = 'key.txt'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'mp4', 'mp3', 'pdf', 'txt', 'Images2'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def allowed_file(filename):
    return True  # Autoriser tous les fichiers

@app.route('/delete', methods=['POST'])
def delete_file():
    data = request.get_json()
    filename = data.get('filename')
    if not filename:
        return jsonify({'success': False, 'message': 'Nom de fichier manquant'}), 400
    file_path = os.path.join(UPLOAD_FOLDER, filename)
    print(f"Suppression demandée pour : {file_path}")
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"Fichier supprimé : {file_path}")
        return jsonify({'success': True})
    else:
        print(f"Fichier introuvable : {file_path}")
        return jsonify({'success': False, 'message': 'Fichier introuvable'}), 404
from flask import Flask, render_template, request, jsonify, send_from_directory
import os
import json
from werkzeug.utils import secure_filename

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
KEY_FILE = 'key.txt'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'mp4', 'mp3', 'pdf', 'txt', 'Images2'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def allowed_file(filename):
    return True  # Autoriser tous les fichiers

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check_key')
def check_key():
    return jsonify({'key_exists': os.path.exists(KEY_FILE) and os.path.getsize(KEY_FILE) > 0})

@app.route('/save_key', methods=['POST'])
def save_key():
    data = request.get_json()
    key = data.get('key')
    if not key:
        return jsonify({'success': False}), 400
    with open(KEY_FILE, 'w', encoding='utf-8') as f:
        f.write(key)
    return jsonify({'success': True})

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return jsonify({'success': False, 'message': 'No file part'})
    file = request.files['file']
    if file.filename == '':
        return jsonify({'success': False, 'message': 'No selected file'})
    if file:
        # Utiliser secure_filename pour garantir la cohérence avec la suppression
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return jsonify({'success': True})
    return jsonify({'success': False, 'message': 'Invalid file'})

@app.route('/playlist')
def playlist():
    files = [f for f in os.listdir(UPLOAD_FOLDER) if os.path.isfile(os.path.join(UPLOAD_FOLDER, f))]
    return jsonify({'files': files})

@app.route('/download/<filename>')
def download(filename):
    return send_from_directory(UPLOAD_FOLDER, filename, as_attachment=True)

# Dummy encryption/decryption for demonstration
def encrypt_file(filename):
    # Rename file to .Images2
    src = os.path.join(UPLOAD_FOLDER, filename)
    if not os.path.exists(src):
        return False, 'File not found'
    if filename.endswith('.Images2'):
        return False, 'Déjà chiffré'
    dst = src + '.Images2'
    os.rename(src, dst)
    return True, None

def decrypt_file(filename):
    # Remove .Images2 extension
    src = os.path.join(UPLOAD_FOLDER, filename)
    if not os.path.exists(src):
        return False, 'File not found'
    if not filename.endswith('.Images2'):
        return False, 'Pas un fichier chiffré'
    dst = src[:-8]
    os.rename(src, dst)
    return True, None

@app.route('/encrypt', methods=['POST'])
def encrypt():
    data = request.get_json()
    filename = data.get('filename')
    if not filename:
        return jsonify({'success': False, 'message': 'Nom de fichier manquant'})
    success, message = encrypt_file(filename)
    return jsonify({'success': success, 'message': message})

@app.route('/decrypt', methods=['POST'])
def decrypt():
    data = request.get_json()
    filename = data.get('filename')
    if not filename:
        return jsonify({'success': False, 'message': 'Nom de fichier manquant'})
    success, message = decrypt_file(filename)
    return jsonify({'success': success, 'message': message})

if __name__ == '__main__':
    app.run(debug=True)
