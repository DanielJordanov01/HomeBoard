class Note:

    def __init__(self, row_id, created_date, modified_date, status_id, title, description):
        self.id = row_id
        self.created_date = created_date
        self.modified_date = modified_date
        self.status_id = status_id
        self.title = title
        self.description = description

    @staticmethod
    def from_row(row):
        return Note(row[0], row[1], row[2], row[3], row[4], row[5])

    @staticmethod
    def from_rows(rows):
        notes = []

        for row in rows:
            notes.append(Note.from_row(row))

        return notes
