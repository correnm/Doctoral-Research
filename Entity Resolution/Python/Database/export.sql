BEGIN TRANSACTION;
CREATE TABLE "alumni" (
	`alumni_pk`	INTEGER,
	`first_name`	TEXT,
	`last_name`	TEXT,
	`student_type`	TEXT
);
INSERT INTO `alumni` VALUES ('1','Jessica','Totty','G');
INSERT INTO `alumni` VALUES ('2','Chelsea','Kelley','G');
INSERT INTO `alumni` VALUES ('3','Joe','Dobrota','G');
INSERT INTO `alumni` VALUES ('4','Mark','Stevenson','G');
INSERT INTO `alumni` VALUES ('5','Victoria','Walker','G');
INSERT INTO `alumni` VALUES ('6','Grace','Alegre','G');
INSERT INTO `alumni` VALUES ('7','Lena','Maslennikova','G');
INSERT INTO `alumni` VALUES ('8','Sean','Kirnan','G');
INSERT INTO `alumni` VALUES ('9','Kita','Graham','G');
INSERT INTO `alumni` VALUES ('10','Donnie','Staggs','G');
INSERT INTO `alumni` VALUES ('11','Jamie','Brennan','G');
INSERT INTO `alumni` VALUES ('12','Pamela','Lee','G');
INSERT INTO `alumni` VALUES ('13','Nathaniel','Richner','U');
INSERT INTO `alumni` VALUES ('14','Joshua','Mitchell','U');
INSERT INTO `alumni` VALUES ('15','Jacob','Affinito','U');
INSERT INTO `alumni` VALUES ('16','Augusta','Hayward','U');
INSERT INTO `alumni` VALUES ('17','Chad','Clukey','U');
INSERT INTO `alumni` VALUES ('18','Mike','Ackerman','U');
INSERT INTO `alumni` VALUES ('19','Bohdan','Smaha','G');
INSERT INTO `alumni` VALUES ('20','Kyle','Graham','G');
COMMIT;
