import React from 'react'
import axios from 'axios'
import "./Dialog.css"

class Dialog extends React.Component {
    state = {
        data: ''
    }

    onChange = (e) => {
        e.preventDefault()
        this.setState({
        [e.target.name]: e.target.value
    })
    }

    onSubmitAdd = (e) => {
        e.preventDefault();
        let event = {}
        
        if (this.state.data !== '') {
            event = {
                'title': this.state.data,
                'start': this.props.ev.start,
                'end': this.props.ev.end,
                'id': 127
            }
        }

        axios({
            method: 'post',
            headers: {'Access-Control-Allow-Origin': '*'},
            url: 'http://localhost:5000/calendar/create',
            data: event
        })

        this.props.createEvent(event)
        this.setState({data: ''})
    }

    render() {
        if(!this.props.show) {
            return null
        }
    
        return (
            <form onSubmit={this.onSubmitAdd} className="dialog-box d-flex flex-column align-items-center">
                <input id="title" className="form-control" placeholder="Event" type="text" name="data" value={this.state.data} onChange={this.onChange}/>
                <div className="buttons">
                    <input type="submit" className="btn btn-light"/>
                    <button onClick={this.props.onClose} className="btn btn-light">Close</button>
                </div>
            </form>
        )
    }
   
}

export default Dialog
