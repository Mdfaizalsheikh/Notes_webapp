from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

notes = [
    {'id': 1, 'title': 'Note 1', 'content': 'This is note 1 content.'},
    {'id': 2, 'title': 'Note 2', 'content': 'This is note 2 content.'}
]
next_id = 3


@app.route('/')
def index():
    return render_template('index.html', notes=notes)


@app.route('/add', methods=['POST'])
def add_note():
    global next_id
    title = request.form['title']
    content = request.form['content']
    note = {'id': next_id, 'title': title, 'content': content}
    notes.append(note)
    next_id += 1
    return redirect(url_for('index'))

@app.route('/delete/<int:note_id>')
def delete_note(note_id):
    global notes
    notes = [note for note in notes if note['id'] != note_id]
    return redirect(url_for('index'))

@app.route('/edit/<int:note_id>')
def edit_note_form(note_id):
    note = next((note for note in notes if note['id'] == note_id), None)
    if note:
        return render_template('edit.html', note=note)
    return redirect(url_for('index'))


@app.route('/update/<int:note_id>', methods=['POST'])
def update_note(note_id):
    title = request.form['title']
    content = request.form['content']
    for note in notes:
        if note['id'] == note_id:
            note['title'] = title
            note['content'] = content
            break
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
