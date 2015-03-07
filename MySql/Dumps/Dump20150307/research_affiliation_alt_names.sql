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
-- Table structure for table `affiliation_alt_names`
--

DROP TABLE IF EXISTS `affiliation_alt_names`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `affiliation_alt_names` (
  `affiliation_alt_pk` int(10) NOT NULL AUTO_INCREMENT,
  `affiliation_pk` int(10) NOT NULL,
  `affiliation_name` varchar(200) NOT NULL,
  PRIMARY KEY (`affiliation_alt_pk`),
  UNIQUE KEY `affiliation_name_UNIQUE` (`affiliation_name`),
  KEY `affiliation_alt_fk_idx` (`affiliation_pk`),
  CONSTRAINT `affiliation_alt_fk` FOREIGN KEY (`affiliation_pk`) REFERENCES `affiliations` (`affiliation_pk`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COMMENT='Contains a list of variations that are acceptable for the primary affiliation name (e.g., Old Dominion University -> ODU)';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `affiliation_alt_names`
--

LOCK TABLES `affiliation_alt_names` WRITE;
/*!40000 ALTER TABLE `affiliation_alt_names` DISABLE KEYS */;
INSERT INTO `affiliation_alt_names` VALUES (1,53,'Regent University School of Law');
/*!40000 ALTER TABLE `affiliation_alt_names` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2015-03-07 17:04:07
