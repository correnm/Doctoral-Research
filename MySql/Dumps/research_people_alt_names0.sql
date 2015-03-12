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
-- Table structure for table `people_alt_names`
--

DROP TABLE IF EXISTS `people_alt_names`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `people_alt_names` (
  `alt_name_pk` int(10) NOT NULL AUTO_INCREMENT,
  `dataset_pk` int(10) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(60) NOT NULL,
  `name_type` varchar(1) NOT NULL DEFAULT 'O' COMMENT 'Valid values are (O)riginal or (A)lias',
  PRIMARY KEY (`alt_name_pk`),
  KEY `people_alt_names_fk1_idx` (`dataset_pk`),
  CONSTRAINT `people_alt_names_fk1` FOREIGN KEY (`dataset_pk`) REFERENCES `people` (`dataset_pk`) ON DELETE CASCADE ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=135 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `people_alt_names`
--

LOCK TABLES `people_alt_names` WRITE;
/*!40000 ALTER TABLE `people_alt_names` DISABLE KEYS */;
INSERT INTO `people_alt_names` VALUES (13,1,'jessica','totty','O'),(14,1,'jess','totty','A'),(15,1,'jesse','totty','A'),(16,1,'jessie','totty','A'),(17,1,'sica','totty','A'),(18,2,'chelsea','kelley','O'),(19,3,'joe','dobrota','O'),(20,3,'joseph','dobrota','A'),(21,4,'mark','stevenson','O'),(22,4,'marcus','stevenson','A'),(23,5,'victoria','walker','O'),(24,5,'toria','walker','A'),(25,5,'torrie','walker','A'),(26,5,'tory','walker','A'),(27,5,'vicki','walker','A'),(28,5,'victor','walker','A'),(29,6,'grace','alegre','O'),(30,7,'lena','maslennikova','O'),(31,7,'leenlina','maslennikova','A'),(32,7,'arlene','maslennikova','A'),(33,7,'caroline','maslennikova','A'),(34,7,'carolyn','maslennikova','A'),(35,7,'helen','maslennikova','A'),(36,7,'helena','maslennikova','A'),(37,7,'madeline','maslennikova','A'),(38,7,'magdalena','maslennikova','A'),(39,8,'sean','kirnan','O'),(40,9,'kita','graham','O'),(41,10,'donnie','staggs','O'),(42,11,'jamie','brennan','O'),(43,11,'benjamin','brennan','A'),(44,11,'james','brennan','A'),(45,12,'pamela','lee','O'),(46,12,'pam','lee','A'),(47,13,'nathaniel','richner','O'),(48,13,'jonathan','richner','A'),(49,13,'nat','richner','A'),(50,13,'nate','richner','A'),(51,13,'nathan','richner','A'),(52,13,'natty','richner','A'),(53,13,'tan','richner','A'),(54,14,'joshua','mitchell','O'),(55,14,'josh','mitchell','A'),(56,15,'jacob','affinito','O'),(57,15,'jake','affinito','A'),(58,16,'augusta','hayward','O'),(59,16,'aggy','hayward','A'),(60,16,'augie','hayward','A'),(61,16,'gus','hayward','A'),(62,16,'guss','hayward','A'),(63,16,'gussie','hayward','A'),(64,16,'augustus','hayward','A'),(65,17,'chad','clukey','O'),(66,17,'charles','clukey','A'),(67,18,'mike','ackerman','O'),(68,18,'michael','ackerman','A'),(69,19,'bohdan','smaha','O'),(70,20,'kyle','graham','O'),(71,21,'marc','santom','O'),(72,22,'ella','thompson','O'),(73,22,'eleanor','thompson','A'),(74,22,'gabriella','thompson','A'),(75,22,'helen','thompson','A'),(76,22,'luella','thompson','A'),(77,22,'gabrielle','thompson','A'),(78,23,'jared','beasley','O'),(79,24,'patricia','mercier','O'),(80,24,'pat','mercier','A'),(81,24,'patrick','mercier','A'),(82,24,'patsy','mercier','A'),(83,24,'patty','mercier','A'),(84,24,'tricia','mercier','A'),(85,24,'trish','mercier','A'),(86,24,'trixie','mercier','A'),(127,25,'christine','habrle','O'),(128,25,'chris','habrle','A'),(129,25,'christiana','habrle','A'),(130,25,'christy','habrle','A'),(131,25,'crissy','habrle','A'),(132,25,'ina','habrle','A'),(133,25,'tina','habrle','A'),(134,25,'xina','habrle','A');
/*!40000 ALTER TABLE `people_alt_names` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2015-03-11 22:07:52
