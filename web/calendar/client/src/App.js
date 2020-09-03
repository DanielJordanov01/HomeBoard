import React from 'react';
import { Calendar, momentLocalizer } from 'react-big-calendar'
import moment from 'moment'
import Dialog from './components/Dialog/Dialog'
import "./App.css"
import 'bootstrap/dist/css/bootstrap.css';
import "react-big-calendar/lib/css/react-big-calendar.css";
import axios from 'axios'

const localizer = momentLocalizer(moment)

class App extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      events: [],
      event: '',
      isDialogOpen: false
    }
  }

  componentDidMount() {
    let events = []

    axios.get('http://127.0.0.1:5000/calendar/get/all')
    .then(res => {
      res.data.map(element => {
          events.push(element)
      });
      this.setState({events: events})
    })
  }

  addEvent = (e) => {
    this.toggleDialog()
    this.setState({event: e})
  }

  createEvent = (event) => {
    this.setState({
      events: [...this.state.events, event],
      isDialogOpen: false
    })
  }

  deleteEvent = (e) => {
    let eventsArr = [...this.state.events]

    eventsArr.map(ev => {
      if (ev.start === e.start && ev.end === e.end) {
        let id = eventsArr.indexOf(ev)
        eventsArr.splice(id, 1)
      }
    })

    axios({
            method: 'delete',
            headers: {'Access-Control-Allow-Origin': '*'},
            url: 'http://localhost:5000/calendar/delete/' + e['id'],
        })
    console.log(e['id'])

    this.setState({events: eventsArr})
  }

  toggleDialog = () => {
    this.setState({
      isDialogOpen: !this.state.isDialogOpen
    })
  }

  render() {
    return (
      <div>
        <Dialog createEvent={this.createEvent} show={this.state.isDialogOpen} onClose={this.toggleDialog} ev={this.state.event}/>
        <Calendar
          localizer={localizer}
          events={this.state.events}
          startAccessor="start"
          endAccessor="end" 
          style={{ height: 700 }}
          views={["month"]}
          selectable
          onSelectSlot={this.addEvent}
          onSelectEvent={this.deleteEvent}
        />
      </div>
    )
  }
}


export default App;
