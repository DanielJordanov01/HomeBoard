create table status
(
    id        INTEGER not null
        constraint status_pk
            primary key autoincrement,
    status    TEXT    not null,
    status_id INTEGER not null
);

create unique index status_id_uindex
    on status (id);

create unique index status_status_id_uindex
    on status (status_id);

create unique index status_status_uindex
    on status (status);

