create table notes
(
    id            INTEGER not null
        constraint notes_pk
            primary key autoincrement,
    created_date  TEXT    not null,
    modified_date TEXT    not null,
    status_id     INTEGER not null
        constraint status
            references status (status_id)
            on update cascade on delete restrict,
    title         TEXT,
    description   TEXT
);

create unique index notes_id_uindex
    on notes (id);
<<<<<<< HEAD
=======

>>>>>>> origin/master
