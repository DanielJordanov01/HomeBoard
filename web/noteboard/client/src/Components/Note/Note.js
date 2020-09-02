import React from 'react';
import "./Note.css";
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faEdit } from '@fortawesome/free-solid-svg-icons';
import { faTrash } from '@fortawesome/free-solid-svg-icons';


function Note({title, description, id, delNote, editNote}) {

    const del = () => {
        delNote(id)
    }

    const edit = () => {
        editNote(id)
    }

    return (
        <div className="note">

            <div className="text-content">
                <h3>{title}</h3>
                <p>{description}</p>
            </div>
                        
            <div className="icons d-flex justify-content-center">

                <div className="note-button">
                    <FontAwesomeIcon onClick={edit} icon={faEdit}/>
                </div>

                <div className="note-button">   
                    <FontAwesomeIcon onClick={del} icon={faTrash}/>
                </div>

            </div>

        </div>
    )
}

export default Note 