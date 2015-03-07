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
  `first_name` varchar(30) DEFAULT NULL,
  `last_name` varchar(60) DEFAULT NULL,
  `student_type` varchar(15) DEFAULT NULL COMMENT 'Identifies the person as a (G)raduate or (U)ndergraduate student',
  `record_type` varchar(1) DEFAULT 'T' COMMENT 'Identifies the record as a (T)raining or (P)roduction record',
  `linkedin_public_profile` varchar(100) DEFAULT NULL,
  `twitter_account` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`dataset_pk`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `people`
--

LOCK TABLES `people` WRITE;
/*!40000 ALTER TABLE `people` DISABLE KEYS */;
INSERT INTO `people` VALUES (1,'Jessica','Totty','G','T','https://www.linkedin.com/pub/jessica-totty/5/786/964','JessicaTotty'),(2,'Chelsea','Kelley','G','T','https://www.linkedin.com/in/chelseakelley',NULL),(3,'Joe','Dobrota','G','T','https://www.linkedin.com/in/joedobrota',NULL),(4,'Mark','Stevenson','G','T','https://www.linkedin.com/pub/mark-l-stevenson/3/b05/674','StevensonEsq, msteve27'),(5,'Victoria','Walker','G','T','https://www.linkedin.com/in/victorialynnwalker',NULL),(6,'Grace','Alegre','G','T','https://www.linkedin.com/in/gracemalegre','gracemalegre'),(7,'Lena','Maslennikova','G','T','https://www.linkedin.com/pub/lena-maslennikova-dsl-mba/4/a4a/893','olenmas'),(8,'Sean','Kirnan','G','T','https://www.linkedin.com/pub/sean-kirnan/13/44a/352',NULL),(9,'Kita','Graham','G','T','https://www.linkedin.com/pub/kita-graham-m-a/25/6b0/490','kitagraham'),(10,'Donnie','Staggs','G','T','https://www.linkedin.com/pub/donnie-staggs/66/86a/816',NULL),(11,'Jamie','Brennan','G','T','https://www.linkedin.com/pub/jamie-brennan/71/a1/9b3',NULL),(12,'Pamela','Lee','G','T','https://www.linkedin.com/pub/pamela-lee/84/757/56b',NULL),(13,'Nathaniel','Richner','U','T','https://www.linkedin.com/pub/nathaniel-richner/2b/483/a81',NULL),(14,'Joshua','Mitchell','U','T','https://www.linkedin.com/pub/joshua-mitchell/44/a13/628',NULL),(15,'Jacob','Affinito','U','T','https://www.linkedin.com/in/jacobaffinito',NULL),(16,'Augusta','Hayward','U','T','https://www.linkedin.com/pub/augusta-hayward/10/969/760','auguhay50'),(17,'Chad','Clukey','U','T','https://www.linkedin.com/pub/chad-clukey/16/8b4/a16',NULL),(18,'Mike','Ackerman','U','T','https://www.linkedin.com/pub/mike-ackerman/39/a81/88a','mikeack'),(19,'Bohdan','Smaha','G','T','https://www.linkedin.com/in/bohdan','smaha '),(20,'Kyle','Graham','G','T','https://www.linkedin.com/in/kylejgraham','kylegra'),(21,'Marc','Santom','G','T','https://www.linkedin.com/pub/marc-santom/a/3a/618','heymoe3000'),(22,'Ella','Thompson','G','T','https://www.linkedin.com/pub/ella-thompson-ph-d/11/771/b68','EllaRThompson'),(23,'Jared','Beasley','G','T','https://www.linkedin.com/in/jaredcbeasley','JaredBeasley'),(24,'Patricia','Mercier','G','T','https://www.linkedin.com/pub/patricia-mercier/8/9b5/500','patrmer');
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

-- Dump completed on 2015-03-07 17:04:05
