CREATE DATABASE  IF NOT EXISTS `corren` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `corren`;
-- MySQL dump 10.13  Distrib 5.6.17, for Win64 (x86_64)
--
-- Host: localhost    Database: corren
-- ------------------------------------------------------
-- Server version	5.6.21-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `linkedin_affiliation`
--

DROP TABLE IF EXISTS `linkedin_affiliation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `linkedin_affiliation` (
  `affiliation_pk` int(10) NOT NULL AUTO_INCREMENT,
  `linkedin_pk` int(10) NOT NULL,
  `affiliation_name` varchar(100) NOT NULL,
  PRIMARY KEY (`affiliation_pk`),
  KEY `linkedin_affiliation_fk_idx` (`linkedin_pk`),
  CONSTRAINT `linkedin_affiliation_fk` FOREIGN KEY (`linkedin_pk`) REFERENCES `linkedin` (`linkedin_pk`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=204 DEFAULT CHARSET=utf8 COMMENT='Contains the educational affiliations for all linkedin public profiles';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `linkedin_affiliation`
--

LOCK TABLES `linkedin_affiliation` WRITE;
/*!40000 ALTER TABLE `linkedin_affiliation` DISABLE KEYS */;
INSERT INTO `linkedin_affiliation` VALUES (5,1115,'San Diego State University-California State University'),(6,1115,'University of California, San Diego'),(7,1115,'The Ohio State University'),(8,1115,'The Ohio State University'),(9,1117,'Penn State University'),(10,1117,'American University'),(11,1119,'Naval Postgraduate School'),(12,1119,'Chapman University'),(13,1119,'Southern Illinois University, Carbondale'),(14,1119,'Northwestern University - Kellogg School of Management'),(15,1119,'Georgetown University'),(16,1120,'Regent University School of Law'),(17,1120,'Old Dominion University'),(18,1121,'Iowa State University - College of Business'),(19,1122,'Georgetown University'),(20,1122,'UC Berkeley'),(21,1126,'Aberdeen College'),(22,1127,'Texas State University-San Marcos'),(23,1128,'University of Houston Law Center'),(24,1128,'Boston College Law School'),(25,1128,'Texas A&amp;M University'),(26,1135,'Southern California University of Health Sciences'),(27,1135,'Texas State University-San Marcos'),(28,1137,'Old Dominion University'),(29,1137,'Regent University'),(30,1137,'Susquehanna University'),(31,1138,'Lehigh University'),(32,1140,'Regent University'),(33,1140,'University of Hawaii at Manoa'),(34,1140,'University of Hawaii at Manoa'),(35,1141,'Syracuse University'),(36,1142,'Howard University'),(37,1143,'George Mason University School of Law'),(38,1143,'University of Virginia'),(39,1144,'University of North Carolina at Chapel Hill'),(40,1145,'Spelman College'),(41,1145,'Bank Street College of Education'),(42,1148,'Liberty University'),(43,1148,'Liberty University'),(44,1148,'Edison Community College'),(45,1152,'Tidewater Community College'),(46,1153,'Northern Virginia Community College'),(47,1153,'Northern Virginia Community College'),(48,1153,'University of Mary Washington'),(49,1155,'University of Maryland University College'),(50,1156,'University of California, Irvine'),(51,1156,'Westmont College'),(52,1157,'Duke University'),(53,1159,'New Mexico State University'),(54,1160,'Los Angeles City College'),(55,1166,'Regent University'),(56,1167,'Regent University'),(57,1167,'Bucknell University'),(58,1167,'Bucknell University'),(59,1169,'Regent University'),(60,1169,'Regent University'),(61,1169,'Middle Tennessee State University'),(62,1171,'Regent University'),(63,1171,'Regent University'),(64,1171,'Northeastern State University'),(65,1171,'Oral Roberts University'),(66,1171,'Oral Roberts University'),(67,1172,'Florida Southern College'),(68,1173,'University of Southern Maine'),(69,1173,'Wheaton College'),(70,1175,'State University of New York at Albany'),(71,1175,'Assumption College'),(72,1177,'University of San Diego'),(73,1178,'Georgetown University Law Center'),(74,1178,'Wake Forest University School of Law'),(75,1178,'University of Scranton'),(76,1179,'Duke University'),(77,1180,'New York University - Leonard N. Stern School of Business'),(78,1180,'Cornell University'),(79,1180,'Farmingdale State University of New York'),(80,1181,'The Ohio State University'),(81,1181,'The Ohio State University'),(82,1181,'Liverpool Hope University'),(83,1181,'Kingston University'),(84,1182,'Darden Business School'),(85,1184,'Saint John&#39;s University - Peter J. Tobin College of Business'),(86,1184,'Saint John&#39;s University - Peter J. Tobin College of Business'),(87,1185,'University of Mississippi'),(88,1187,'Florida State University'),(89,1188,'Boise State University'),(90,1191,'SUNY Oswego'),(91,1192,'State University of New York at Albany'),(92,1193,'Michigan State University College of Law'),(93,1193,'University of Detroit Mercy'),(94,1193,'John Carroll University'),(95,1194,'UC Berkeley'),(96,1194,'UC San Diego'),(97,1195,'Syracuse University'),(98,1197,'ESADE Business School'),(99,1197,'Universit&#xe0; degli Studi di Cagliari'),(100,1197,'Georg-Simon-Ohm-Fachhochschule N&#xfc;rnberg'),(101,1199,'Macomb Community College'),(102,1199,'Macomb Community College'),(103,1200,'The American College'),(104,1200,'University of California, Santa Barbara'),(105,1202,'Harvard University Graduate School of Design'),(106,1202,'Cornell University'),(107,1203,'University of California, San Diego'),(108,1204,'Widener University School of Law'),(109,1204,'Rutgers University'),(110,1206,'Point Loma Nazarene University'),(111,1206,'San Diego State University'),(112,1207,'University of Colorado at Denver'),(113,1207,'Sam Houston State University'),(114,1207,'University of Nebraska-Lincoln'),(115,1209,'San Francisco State University'),(116,1210,'George Mason University School of Law'),(117,1210,'Wayne State University'),(118,1210,'Wayne State University'),(119,1212,'University of San Francisco'),(120,1212,'University of Arizona'),(121,1213,'Virginia Commonwealth University'),(122,1213,'Mary Washington College'),(123,1215,'Colorado Technical University'),(124,1220,'Claremont Graduate University - Peter F. Drucker and Masatoshi Ito Graduate School of Management'),(125,1220,'California State Polytechnic University-Pomona'),(126,1221,'Thunderbird School of Global Management'),(127,1221,'University of San Diego'),(128,1222,'Mount Olive College'),(129,1222,'Mount Olive College'),(130,1224,'Moore College of Art and Design'),(131,1226,'Parsons School of Design'),(132,1226,'State University of New York at New Paltz'),(133,1227,'University of California, Berkeley'),(134,1229,'Kolej Han Chiang'),(135,1237,'University of Phoenix'),(136,1237,'University of Phoenix'),(137,1238,'New England College'),(138,1242,'Regent University'),(139,1246,'Full Sail University'),(140,1247,'Southern California University of Health Sciences'),(141,1247,'Indiana University&#x2014;Purdue University Fort Wayne'),(142,1248,'Charleston School of Law'),(143,1248,'Winthrop University'),(144,1250,'Full Sail University'),(145,1251,'University of Maryland College Park'),(146,1253,'Oregon State University'),(147,1256,'Regent University'),(148,1258,'Regent University'),(149,1259,'Franklin Pierce Law Center'),(150,1259,'Fairleigh Dickinson University &#x2013; Vancouver'),(151,1263,'University of Massachusetts at Amherst - Isenberg School of Management'),(152,1263,'Yeshiva University'),(153,1263,'Duke University'),(154,1264,'Harvard Kennedy School of Government'),(155,1264,'Fort Lewis College'),(156,1264,'Harvard University Graduate School of Education'),(157,1264,'Prescott College'),(158,1267,'University of Colorado Boulder'),(159,1268,'Whitman College'),(160,1271,'Fordham University'),(161,1271,'Vassar College'),(162,1273,'Central Michigan University'),(163,1274,'Hastings College of the Law'),(164,1274,'San Francisco State University'),(165,1275,'Temple University - Fox School of Business and Management'),(166,1275,'Penn State University'),(167,1277,'Regent University'),(168,1277,'Art Institute of Atlanta'),(169,1277,'National University &#39;Ivan Franko&#39; , Lviv'),(170,1278,'Franklin Pierce College'),(171,1279,'University of Wisconsin-Oshkosh'),(172,1280,'Salem State College'),(173,1282,'Texas A&amp;M University'),(174,1285,'Arizona State University'),(175,1289,'King&#39;s College London, U. of London'),(176,1289,'Regent University'),(177,1289,'Regent University'),(178,1289,'Virginia Commonwealth University - School of Business'),(179,1291,'University of Washington'),(180,1291,'Seattle Central Community College'),(181,1293,'Bethel University'),(182,1293,'North Hennepin Community College'),(183,1295,'University of California, Los Angeles'),(184,1295,'University of California, Santa Barbara'),(185,1297,'Harvard University'),(186,1302,'Ringling School of Art and Design'),(187,1303,'Naval Postgraduate School'),(188,1303,'Winona State University'),(189,1305,'Hillsborough Community College'),(190,1305,'Madison Area Technical College'),(191,1313,'University of California, San Diego'),(192,1314,'WGU Texas'),(193,1315,'The University of Tennessee at Chattanooga'),(194,1316,'Regent University'),(195,1316,'Regent University'),(196,1316,'Evangel University'),(197,1317,'Columbia Southern University'),(198,1318,'Regent University'),(199,1318,'Geneva College'),(200,1325,'Massachusetts Institute of Technology'),(201,1325,'Massachusetts Institute of Technology'),(202,1325,'University of Alberta'),(203,1326,'Long Beach City College');
/*!40000 ALTER TABLE `linkedin_affiliation` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2015-02-14 19:22:40
