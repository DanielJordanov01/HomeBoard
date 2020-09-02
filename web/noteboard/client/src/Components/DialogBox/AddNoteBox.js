import React from 'react'
import "./AddNoteBox.css"

class DialogBox extends React.Component {
    state = {
        title: '',
        description: ''
    }

    onChange = (e) => {
        e.preventDefault()
        this.setState({
        [e.target.name]: e.target.value
    })
    }

    onSubmit = (e) => {
        e.preventDefault();
        this.props.addNote(this.state.title, this.state.description)
        this.setState({title: '', description: ''})
    }


    onSubmitEdit = (e) => {
        e.preventDefault();
        this.props.editNote(this.props.id, this.state.description, this.state.title, true, true)
        this.setState({title: '', description: ''})
        setTimeout(() => window.location.reload(true), 500);
    }

    render() {
        if(!this.props.show) {
            return null
        }
    
        return (
            <form onSubmit={ this.props.editMode ? this.onSubmitEdit : this.onSubmit} className="dialog-box d-flex flex-column align-items-center">
                <input id="title" className="form-control" placeholder="Title" type="text" name="title" value={this.state.title} onChange={this.onChange}/>
                <textarea className="form-control" placeholder="Description" name="description" value={this.state.description} onChange={this.onChange}></textarea>
                <div className="buttons">
                    <input type="submit" className="btn btn-light"/>
                    <button onClick={this.props.onClose} className="btn btn-light">Close</button>
                </div>
            </form>
        )
    }
   
}

export default DialogBox
