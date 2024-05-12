from flask import Flask, render_template, request, redirect
import csv

app =Flask(__name__)
app.config['ALLOWED_EXTENSIONS'] = {'csv'}
app.config['UPLOAD_FOLDER'] = 'upload'

#create a new function to store the new data
def save_to_csv(data, filename):
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = data[0].keys() if data else []
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in data:
            writer.writer(row)

def allowed_file(filename):
    return '.' in filename and filename.rsplit ('.' , 1)[1].lower() in app.config['ALLOWED EXTENSIONS']


@app.route('/')
def index():
    return render_template('upload.html')

@app.route('/upload', method=['POST'])
def upload():
    if 'file' not in request.files:
        return redirect(request.url)
    
    file = request.file[ 'file']

    if file.filename == '' or not allowed_file(file.filename):
        return redirect(request.url)

    if file:
        data = []
        csv_reader = csv.DictReader(file.read(). decode(' utf-8').splitlines())
        for row in csv_reader:
            print(row)
            data.append(row)
            save_to_csv(data, os.path.join(app.config('uploaded_data.csv')))

    return 'file upload successful'

#running the app
if __name__ == '__main__':
    app.run(port=8080, debug=True)