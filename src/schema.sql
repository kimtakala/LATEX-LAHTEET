CREATE TYPE SOURCE_KIND AS ENUM ('book');

CREATE TABLE lahteet.source (
    source_id SERIAL PRIMARY KEY,
    bibtex_key TEXT NOT NULL UNIQUE,
    kind SOURCE_KIND NOT NULL,
    title TEXT NOT NULL,
    year INTEGER NOT NULL,
    author TEXT NOT NULL
);

CREATE TABLE lahteet.source_book (
    source_book_id SERIAL PRIMARY KEY,
    source_id INTEGER NOT NULL REFERENCES lahteet.source ON DELETE CASCADE,
    publisher TEXT NOT NULL,
    editor TEXT, 
    volume INTEGER,
    number INTEGER,
    series TEXT,
    address TEXT,
    edition TEXT,
    month TEXT,
    note TEXT
);
