PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE students(
        id integer primary key autoincrement,
        name text not null,
        sex text not null,
        age int not null,
        note text,
        update_time text);
INSERT INTO students VALUES(1,'Mick','boy',20,'','2019-02-24 15:33:52');
INSERT INTO students VALUES(2,'Mick','boy',20,'','2019-02-24 15:33:55');
INSERT INTO students VALUES(3,'Mick','boy',20,'','2019-02-24 15:33:56');
INSERT INTO students VALUES(4,'Mick','boy',20,'','2019-02-24 15:33:57');
INSERT INTO students VALUES(5,'Mick','boy',20,'','2019-02-24 15:33:58');
INSERT INTO students VALUES(6,'Mick','boy',20,'','2019-02-24 15:33:58');
INSERT INTO students VALUES(7,'Mick','boy',20,'','2019-02-24 15:35:10');
INSERT INTO students VALUES(8,'Mick','boy',20,'','2019-02-24 15:35:15');
INSERT INTO students VALUES(9,'Mick','boy',20,'','2019-02-24 15:55:00');
INSERT INTO students VALUES(10,'Mick','boy',20,'','2019-02-24 15:56:32');
INSERT INTO students VALUES(11,'Mick','boy',20,'','2019-02-24 15:58:58');
INSERT INTO students VALUES(12,'Mick','boy',20,'','2019-02-24 15:59:15');
INSERT INTO students VALUES(13,'Mick','boy',20,'','2019-02-24 16:00:07');
INSERT INTO students VALUES(14,'Mick','boy',20,'','2019-02-24 16:00:16');
INSERT INTO students VALUES(15,'Mick','boy',20,'','2019-02-24 16:09:48');
INSERT INTO students VALUES(16,'Mick','boy',20,'','2019-02-24 16:10:36');
DELETE FROM sqlite_sequence;
INSERT INTO sqlite_sequence VALUES('students',16);
COMMIT;
