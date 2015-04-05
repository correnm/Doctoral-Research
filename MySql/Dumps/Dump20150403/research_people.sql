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
-- Table structure for table `people`
--

DROP TABLE IF EXISTS `people`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `people` (
  `dataset_pk` int(10) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(60) NOT NULL,
  `student_type` varchar(15) DEFAULT NULL COMMENT 'Identifies the person as a (G)raduate or (U)ndergraduate student',
  `record_type` varchar(1) DEFAULT 'T' COMMENT 'Identifies the record as a (T)raining or (P)roduction record',
  `middle_name` varchar(30) DEFAULT NULL,
  `linkedin1` varchar(250) DEFAULT NULL,
  `linkedin2` varchar(250) DEFAULT NULL,
  `twitter1` varchar(25) DEFAULT NULL,
  `twitter 2` varchar(25) DEFAULT NULL,
  PRIMARY KEY (`dataset_pk`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `people`
--

LOCK TABLES `people` WRITE;
/*!40000 ALTER TABLE `people` DISABLE KEYS */;
INSERT INTO `people` VALUES (1,'Jessica','Totty','G','T',NULL,'http://www.linkedin.com/pub/jessica-totty/5/786/964/en',NULL,'JessicaTotty',NULL),(2,'Chelsea','Kelley','G','T',NULL,'https://www.linkedin.com/in/chelseakelley',NULL,NULL,NULL),(3,'Joe','Dobrota','G','T',NULL,'https://www.linkedin.com/in/joedobrota',NULL,'joedobrota',NULL),(4,'Mark','Stevenson','G','T',NULL,'https://www.linkedin.com/pub/mark-l-stevenson/3/b05/674',NULL,'msteve27','StevensonEsq'),(5,'Victoria','Walker','G','T',NULL,'https://www.linkedin.com/in/victorialynnwalker',NULL,'viwalker',NULL),(6,'Grace','Alegre','G','T',NULL,'https://www.linkedin.com/in/gracemalegre',NULL,'gracemalegre',NULL),(7,'Lena','Maslennikova','G','T',NULL,'https://www.linkedin.com/pub/lena-maslennikova-dsl-mba/4/a4a/893',NULL,'olenmas',NULL),(8,'Sean','Kirnan','G','T',NULL,NULL,NULL,NULL,NULL),(9,'Kita','Graham','G','T',NULL,NULL,NULL,NULL,NULL),(10,'Donnie','Staggs','G','T',NULL,NULL,NULL,NULL,NULL),(11,'Jamie','Brennan','G','T',NULL,NULL,NULL,NULL,NULL),(12,'Pamela','Lee','G','T',NULL,NULL,NULL,NULL,NULL),(13,'Nathaniel','Richner','U','T',NULL,NULL,NULL,NULL,NULL),(14,'Joshua','Mitchell','U','T',NULL,NULL,NULL,NULL,NULL),(15,'Jacob','Affinito','U','T',NULL,NULL,NULL,NULL,NULL),(16,'Augusta','Hayward','U','T',NULL,NULL,NULL,NULL,NULL),(17,'Chad','Clukey','U','T',NULL,NULL,NULL,NULL,NULL),(18,'Mike','Ackerman','U','T',NULL,NULL,NULL,NULL,NULL),(19,'Bohdan','Smaha','G','T',NULL,NULL,NULL,NULL,NULL),(20,'Kyle','Graham','G','T',NULL,NULL,NULL,NULL,NULL),(21,'Marc','Santom','G','T',NULL,NULL,NULL,NULL,NULL),(22,'Ella','Thompson','G','T',NULL,NULL,NULL,NULL,NULL),(23,'Jared','Beasley','G','T',NULL,NULL,NULL,NULL,NULL),(24,'Patricia','Mercier','G','T',NULL,NULL,NULL,NULL,NULL),(25,'Christine','Habrle','G','T',NULL,NULL,NULL,NULL,NULL);
/*!40000 ALTER TABLE `people` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2015-04-03 15:26:59
