# app.py
from flask import Flask, request, send_file
import tempfile

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        f1 = request.files['file1']
        f2 = request.files['file2']
        # Example processing: concatenate files
        tmp = tempfile.NamedTemporaryFile(delete=False)
        tmp.write(f1.read())
        tmp.write(b'\n---\n')
        tmp.write(f2.read())
        tmp.flush()
        return send_file(tmp.name, as_attachment=True, download_name='output.txt')
    return '''
    <form method="post" enctype="multipart/form-data">
      File 1: <input type="file" name="file1"><br>
      File 2: <input type="file" name="file2"><br>
      <input type="submit" value="Process">
    </form>
    '''

if __name__ == '__main__':
    app.run()
