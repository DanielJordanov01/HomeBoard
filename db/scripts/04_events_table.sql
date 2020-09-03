create table calendar_events
(
    id         INTEGER not null
        constraint calendar_events_pk
            primary key autoincrement,
    event      TEXT    not null,
    start_date TEXT    not null,
    end_date   TEXT    not null,
    status_id  INTEGER default 1 not null
        constraint calendar_events
            references status (status_id)
            on update cascade on delete restrict
);

create unique index calendar_events_id_uindex
    on calendar_events (id);
