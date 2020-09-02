class Event:

    def __init__(self, row_id, start_date, end_date, status_id, event):
        self.id = row_id
        self.start_date = start_date
        self.end_date = end_date
        self.event = event
        self.status_id = status_id

    @staticmethod
    def from_row(row):
        return Event(row[0], row[1], row[2], row[3], row[4])

    @staticmethod
    def from_rows(rows):
        events = []

        for row in rows:
            events.append(Event.from_row(row))

        return events

