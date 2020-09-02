import React, {Component} from 'react';
import './App.css';
import "./Components/Title/Title";
import "./Components/Note/Note";
import AddNote from "./Components/AddNote/AddNote"
import Title from './Components/Title/Title';
import Note from './Components/Note/Note';
import DialogBox from './Components/DialogBox/AddNoteBox'
import 'bootstrap/dist/css/bootstrap.css';

class App extends Component {
  constructor(props) {
    super(props);

    this.state = {
      isDialogOpen: false,
      editMode: false,
      notes: [],
      id: 0
    }
  }

  getAllNotes() {
    const axios = require('axios')
    let notes = []

    const config = {
      headers: {'Access-Control-Allow-Origin': '*'},
    }

    axios.get('http://127.0.0.1:5000/board/get/all', config)
    .then(res => {
      res.data.map(element => {
          notes.push(element)
      });
      this.setState({notes: notes})
    })
  }

  componentDidMount() {
    this.getAllNotes();
  }

  toggleDialog = () => {
    this.setState({
      isDialogOpen: !this.state.isDialogOpen
    })
  }

  addNote = (title, description, dialogStatus) => {
    const axios = require('axios')

    let note = {
      noteTitle: title,
      noteDescription: description
    }

    axios({
      method: 'post',
      headers: {'Access-Control-Allow-Origin': '*'},
      url: 'http://localhost:5000/board/create',
      data: note
    })

    this.setState({
      isDialogOpen: dialogStatus,
      id: this.state.notes.length + 1
    })

    setTimeout(() => window.location.reload(true), 500);
  }

  deleteNote = (id) => {
    const axios = require('axios')

    axios({
      method: 'delete',
      headers: {'Access-Control-Allow-Origin': '*'},
      url: 'http://localhost:5000/board/delete/' + id,
    })

    setTimeout(() => window.location.reload(true), 500);
  }

  editNote = (id, description, title, editMode, dialogStatus) => {

    const axios = require('axios')

    let updatedNote = {
      noteTitle: title,
      noteDescription: description
    }

    axios({
      method: 'put',
      headers: {'Access-Control-Allow-Origin': '*'},
      url: 'http://localhost:5000/board/update/' + id,
      data: updatedNote
    })

    this.setState({
      isDialogOpen: !dialogStatus,
      editMode: !editMode,
      id: id
    })
  }

  render() {
    return (
      <div className="App">
        <Title/>
        <div className="container d-flex justify-content-center flex-wrap">
          <DialogBox addNote={this.addNote} show={this.state.isDialogOpen} onClose={this.toggleDialog} editNote={this.editNote} editMode={this.state.editMode} id={this.state.id} />
          {this.state.notes.map((note) => (
            <Note title={note.title} description={note.title} key={note.id} id={note.id} delNote={this.deleteNote} editNote={this.editNote}/>
          ))}
        </div>
        <AddNote toggleDialog={this.toggleDialog}/>
      </div>
    );
  }
}

export default App;