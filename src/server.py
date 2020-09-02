import json
from flask_cors import CORS
from notes import Note
from events import Event
from db_operations import connect_db, get_all_notes, get_note, create_note, edit_note, remove_note, \
                                      get_all_events, get_event, create_event, edit_event, remove_event
from flask import Flask, jsonify, abort, request

DATABASE = '../db/homeboard.db'
app = Flask(__name__)
CORS(app)

cors = CORS(app, resources={
    r"/*": {
        "origins": "http://localhost:3000"
    }
})


@app.route('/board/get/all')
def get_notes():
    try:
        conn = connect_db(DATABASE)
        rows = get_all_notes(conn)
        return jsonify([vars(note) for note in Note.from_rows(rows)])
    except Exception:
        abort(500)


@app.route('/board/get/<int:row_id>')
def updated_note(row_id):
    try:
        conn = connect_db(DATABASE)
        row = get_note(conn, row_id)
        return jsonify(vars(Note.from_row(row)))
    except Exception:
        abort(500)


@app.route('/board/create', methods=['POST'])
def insert_note():
    conn = connect_db(DATABASE)
    data = request.data
    note = json.loads(data.decode('utf-8'))
    create_note(conn, ''.join(note['noteTitle']), ''.join(note['noteDescription']))
    return jsonify('note created')


@app.route('/board/update/<int:row_id>', methods=['PUT'])
def update_note(row_id):
    try:
        conn = connect_db(DATABASE)
        data = request.data
        updated_note = json.loads(data.decode('utf-8'))
        edit_note(conn, row_id, ''.join(updated_note['noteTitle']), ''.join(updated_note['noteDescription']))
        return jsonify(success=True)
    except Exception:
        abort(500)


@app.route('/board/delete/<int:row_id>', methods=['DELETE'])
def delete_note(row_id):
    try:
        conn = connect_db(DATABASE)
        remove_note(conn, row_id)
        return jsonify(success=True)
    except Exception:
        abort(500)


@app.route('/calendar/get/all')
def get_events():
    try:
        conn = connect_db(DATABASE)
        rows = get_all_events(conn)
        return jsonify([vars(event) for event in Event.from_rows(rows)])
    except Exception:
        abort(500)


@app.route('/calendar/get/<int:row_id>')
def event(row_id):
    try:
        conn = connect_db(DATABASE)
        row = get_event(conn, row_id)
        return jsonify(vars(Event.from_row(row)))
    except Exception:
        abort(500)


@app.route('/calendar/create', methods=['POST'])
def insert_event():
    try:
        data = request.data
        conn = connect_db(DATABASE)
        note = json.loads(data.decode('utf-8'))
        create_event(conn, '2020-03-02', '2020-0303', 'test event')
        return jsonify('event created')
    except:
        abort(500)


@app.route('/calendar/update/<int:row_id>', methods=['PUT'])
def update_event(row_id):
    try:
        conn = connect_db(DATABASE)
        edit_event(conn, row_id, '2020-03-04', '2020-03-05', 'edited')
        return jsonify(success=True)
    except Exception:
        abort(500)


@app.route('/calendar/delete/<int:row_id>', methods=['DELETE'])
def delete_event(row_id):
    try:
        conn = connect_db(DATABASE)
        remove_event(conn, row_id)
        return jsonify(success=True)
    except Exception:
        abort(500)


if __name__ == '__main__':
    app.run()
