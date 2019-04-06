CREATE TABLE artists (music_artist TEXT,
                      album TEXT);

CREATE TABLE albums (song_name TEXT,
                     track_num INTEGER,
                     song_length INTEGER,
                     FOREIGN KEY (album) REFERENCES artists(album));
