/*
If schema is used in sqlite3,
please run the following beforehand:

  PRAGMA foreign_keys = ON;

*/

CREATE TABLE artists (
  album_id INTEGER NOT NULL PRIMARY KEY,
  music_artist TEXT
  );

CREATE TABLE albums (
  song_name TEXT,
  track_num INTEGER,
  song_length INTEGER,
  album TEXT,
  album_id INTEGER,
  FOREIGN KEY(album_id) REFERENCES artists(album_id)
  );
