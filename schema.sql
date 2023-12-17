CREATE TABLE `ElementsToProcess` (
`id` int NOT NULL AUTO_INCREMENT,
`idBulk` int NOT NULL,
`retries` int DEFAULT NULL,
`status` int NOT NULL,
`name` varchar(100) NOT NULL,
PRIMARY KEY (`id`),
KEY `ElementsToProcess_idBulk_IDX` (`idBulk`,`status`) USING BTREE,
KEY `ElementsToProcess_status_IDX` (`status`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=142812 DEFAULT CHARSET=utf8mb4
COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO ElementsToProcess (idBulk, retries, status, name) VALUES (1, 0, 20, 'Element 1');
INSERT INTO ElementsToProcess (idBulk, retries, status, name) VALUES (1, 1, 20, 'Element 2');
INSERT INTO ElementsToProcess (idBulk, retries, status, name) VALUES (2, 2, 20, 'Element 3');
INSERT INTO ElementsToProcess (idBulk, retries, status, name) VALUES (2, 0, 20, 'Element 4');
INSERT INTO ElementsToProcess (idBulk, retries, status, name) VALUES (3, 0, 60, 'Element 5');
INSERT INTO ElementsToProcess (idBulk, retries, status, name) VALUES (3, 1, 60, 'Element 6');
INSERT INTO ElementsToProcess (idBulk, retries, status, name) VALUES (4, 2, 60, 'Element 7');
INSERT INTO ElementsToProcess (idBulk, retries, status, name) VALUES (5, 0, 80, 'Element 8');
INSERT INTO ElementsToProcess (idBulk, retries, status, name) VALUES (5, 1, 80, 'Element 9');
INSERT INTO ElementsToProcess (idBulk, retries, status, name) VALUES (6, 0, 100, 'Element 10');