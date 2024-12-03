CREATE TYPE lahteet.SOURCE_KIND AS ENUM ('book', 'article', 'inproceedings');

CREATE TABLE lahteet.source (
    source_id SERIAL PRIMARY KEY,
    bibtex_key TEXT NOT NULL UNIQUE,
    kind lahteet.SOURCE_KIND NOT NULL,
    title TEXT NOT NULL,
    year INTEGER NOT NULL,
    author TEXT NOT NULL,
    note TEXT
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

CREATE TABLE lahteet.source_article (
    source_article_id SERIAL PRIMARY KEY,
    source_id INTEGER NOT NULL REFERENCES lahteet.source ON DELETE CASCADE,
    journal TEXT NOT NULL,
    volume INTEGER,
    number INTEGER,
    pages TEXT,
    month TEXT
);

CREATE TABLE lahteet.source_inproceedings (
    source_inproceedings_id SERIAL PRIMARY KEY,
    source_id INTEGER NOT NULL REFERENCES lahteet.source ON DELETE CASCADE,
    booktitle TEXT NOT NULL,
    editor TEXT,
    series TEXT,
    pages TEXT,
    address TEXT,
    month TEXT,
    organization TEXT,
    publisher TEXT,
    volume INTEGER
);

CREATE TABLE lahteet.tag (
    tag_id SERIAL PRIMARY KEY,
    source_id INTEGER NOT NULL REFERENCES lahteet.source ON DELETE CASCADE,
    name TEXT NOT NULL,
    UNIQUE(source_id, name)
);
