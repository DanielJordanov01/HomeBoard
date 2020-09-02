import React from 'react';
import "./AddNote.css";

class AddNote extends React.Component {

    render() {
        return (
            <div className="addButton d-flex justify-content-center">
                <button onClick={this.props.toggleDialog} className="btn btn-light">+</button>
            </div>
        )
    }
}

export default AddNote