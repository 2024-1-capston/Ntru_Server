from flask import Flask, request, jsonify
import subprocess
import base64

app = Flask(__name__)

@app.route('/enc', methods=['POST'])
def encrypt():
    data = request.json
    text = data.get('text', '')

    encoded_text = base64.b64encode(text.encode()).decode()

    command = ['python3', 'NTRU.py', '-k', 'NTRU_key', '-eS', encoded_text, '-T']

    try:
        process = subprocess.run(command, check=True, stdout=subprocess.PIPE)
        output = process.stdout.decode('utf-8')
        return jsonify({'result': output[:-1]})
    except subprocess.CalledProcessError as e:
        return jsonify({'error': f'ntru.py 실행 중 오류 발생: {e}'})

@app.route('/dec', methods=['POST'])
def decrypt():
    data = request.json
    text = data.get('text', '')

    command = ['python3', 'NTRU.py', '-k', 'NTRU_key', '-T', '-dS', text,]

    try:
        process = subprocess.run(command, check=True, stdout=subprocess.PIPE)
        output = process.stdout.decode('utf-8')

        decoded_output = base64.b64decode(output.encode()).decode()

        return jsonify({'result': decoded_output})
    except subprocess.CalledProcessError as e:
        return jsonify({'error': f'ntru.py 실행 중 오류 발생: {e}'})

if __name__ == '__main__':
    app.run(host='0.0.0.0')
