CREATE DATABASE  IF NOT EXISTS `research` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `research`;
-- MySQL dump 10.13  Distrib 5.6.17, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: research
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
-- Table structure for table `affiliations`
--

DROP TABLE IF EXISTS `affiliations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `affiliations` (
  `affiliation_pk` int(10) NOT NULL AUTO_INCREMENT,
  `affiliation_name` varchar(200) NOT NULL,
  PRIMARY KEY (`affiliation_pk`),
  UNIQUE KEY `affiliation_name_UNIQUE` (`affiliation_name`)
) ENGINE=InnoDB AUTO_INCREMENT=288 DEFAULT CHARSET=utf8 COMMENT='Maintains the list of educational or employee affiliations';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `affiliations`
--

LOCK TABLES `affiliations` WRITE;
/*!40000 ALTER TABLE `affiliations` DISABLE KEYS */;
INSERT INTO `affiliations` VALUES (47,'Aberdeen College'),(37,'American University'),(161,'Arizona State University'),(156,'Art Institute of Atlanta'),(83,'Assumption College'),(63,'Bank Street College of Education'),(166,'Bethel University'),(97,'Boise State University'),(50,'Boston College Law School'),(75,'Bucknell University'),(125,'California State Polytechnic University-Pomona'),(153,'Central Michigan University'),(39,'Chapman University'),(137,'Charleston School of Law'),(124,'Claremont Graduate University - Peter F. Drucker and Masatoshi Ito Graduate School of Management'),(123,'Colorado Technical University'),(177,'Columbia Southern University'),(89,'Cornell University'),(93,'Darden Business School'),(72,'Duke University'),(65,'Edison Community College'),(103,'ESADE Business School'),(176,'Evangel University'),(142,'Fairleigh Dickinson University &#x2013; Vancouver'),(90,'Farmingdale State University of New York'),(79,'Florida Southern College'),(96,'Florida State University'),(151,'Fordham University'),(146,'Fort Lewis College'),(158,'Franklin Pierce College'),(141,'Franklin Pierce Law Center'),(135,'Full Sail University'),(178,'Geneva College'),(105,'Georg-Simon-Ohm-Fachhochschule N&#xfc;rnberg'),(59,'George Mason University School of Law'),(42,'Georgetown University'),(85,'Georgetown University Law Center'),(145,'Harvard Kennedy School of Government'),(169,'Harvard University'),(109,'Harvard University Graduate School of Design'),(147,'Harvard University Graduate School of Education'),(154,'Hastings College of the Law'),(172,'Hillsborough Community College'),(58,'Howard University'),(136,'Indiana University&#x2014;Purdue University Fort Wayne'),(45,'Iowa State University - College of Business'),(101,'John Carroll University'),(162,'King&#39;s College London, U. of London'),(92,'Kingston University'),(132,'Kolej Han Chiang'),(55,'Lehigh University'),(64,'Liberty University'),(91,'Liverpool Hope University'),(181,'Long Beach City College'),(74,'Los Angeles City College'),(106,'Macomb Community College'),(173,'Madison Area Technical College'),(122,'Mary Washington College'),(179,'Massachusetts Institute of Technology'),(99,'Michigan State University College of Law'),(76,'Middle Tennessee State University'),(128,'Moore College of Art and Design'),(127,'Mount Olive College'),(157,'National University &#39;Ivan Franko&#39; , Lviv'),(38,'Naval Postgraduate School'),(134,'New England College'),(73,'New Mexico State University'),(88,'New York University - Leonard N. Stern School of Business'),(167,'North Hennepin Community College'),(77,'Northeastern State University'),(67,'Northern Virginia Community College'),(41,'Northwestern University - Kellogg School of Management'),(44,'Old Dominion University'),(78,'Oral Roberts University'),(140,'Oregon State University'),(129,'Parsons School of Design'),(36,'Penn State University'),(112,'Point Loma Nazarene University'),(148,'Prescott College'),(53,'Regent University'),(170,'Ringling School of Art and Design'),(111,'Rutgers University'),(94,'Saint John&#39;s University - Peter J. Tobin College of Business'),(160,'Salem State College'),(115,'Sam Houston State University'),(113,'San Diego State University'),(33,'San Diego State University-California State University'),(117,'San Francisco State University'),(165,'Seattle Central Community College'),(52,'Southern California University of Health Sciences'),(40,'Southern Illinois University, Carbondale'),(62,'Spelman College'),(82,'State University of New York at Albany'),(130,'State University of New York at New Paltz'),(98,'SUNY Oswego'),(54,'Susquehanna University'),(57,'Syracuse University'),(155,'Temple University - Fox School of Business and Management'),(51,'Texas A&amp;M University'),(48,'Texas State University-San Marcos'),(107,'The American College'),(35,'The Ohio State University'),(175,'The University of Tennessee at Chattanooga'),(126,'Thunderbird School of Global Management'),(66,'Tidewater Community College'),(46,'UC Berkeley'),(102,'UC San Diego'),(104,'Universit&#xe0; degli Studi di Cagliari'),(180,'University of Alberta'),(120,'University of Arizona'),(131,'University of California, Berkeley'),(70,'University of California, Irvine'),(168,'University of California, Los Angeles'),(34,'University of California, San Diego'),(108,'University of California, Santa Barbara'),(114,'University of Colorado at Denver'),(149,'University of Colorado Boulder'),(100,'University of Detroit Mercy'),(56,'University of Hawaii at Manoa'),(49,'University of Houston Law Center'),(68,'University of Mary Washington'),(139,'University of Maryland College Park'),(69,'University of Maryland University College'),(143,'University of Massachusetts at Amherst - Isenberg School of Management'),(95,'University of Mississippi'),(116,'University of Nebraska-Lincoln'),(61,'University of North Carolina at Chapel Hill'),(133,'University of Phoenix'),(84,'University of San Diego'),(119,'University of San Francisco'),(87,'University of Scranton'),(80,'University of Southern Maine'),(60,'University of Virginia'),(164,'University of Washington'),(159,'University of Wisconsin-Oshkosh'),(152,'Vassar College'),(121,'Virginia Commonwealth University'),(163,'Virginia Commonwealth University - School of Business'),(86,'Wake Forest University School of Law'),(118,'Wayne State University'),(71,'Westmont College'),(174,'WGU Texas'),(81,'Wheaton College'),(150,'Whitman College'),(110,'Widener University School of Law'),(171,'Winona State University'),(138,'Winthrop University'),(144,'Yeshiva University');
/*!40000 ALTER TABLE `affiliations` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2015-03-07 17:04:08
