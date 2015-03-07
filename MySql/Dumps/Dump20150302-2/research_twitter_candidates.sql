CREATE DATABASE  IF NOT EXISTS `research` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `research`;
-- MySQL dump 10.13  Distrib 5.6.17, for Win64 (x86_64)
--
-- Host: localhost    Database: research
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
-- Table structure for table `twitter_candidates`
--

DROP TABLE IF EXISTS `twitter_candidates`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `twitter_candidates` (
  `dataset_pk` int(10) NOT NULL,
  `twitter_profile_pk` int(10) NOT NULL,
  PRIMARY KEY (`dataset_pk`,`twitter_profile_pk`),
  KEY `twitter_candidates_fk2_idx` (`twitter_profile_pk`),
  CONSTRAINT `twitter_candidates_fk1` FOREIGN KEY (`dataset_pk`) REFERENCES `people` (`dataset_pk`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `twitter_candidates_fk2` FOREIGN KEY (`twitter_profile_pk`) REFERENCES `twitter_profiles` (`twitter_profile_pk`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='Potential matches to the LinkedIn profile';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `twitter_candidates`
--

LOCK TABLES `twitter_candidates` WRITE;
/*!40000 ALTER TABLE `twitter_candidates` DISABLE KEYS */;
/*!40000 ALTER TABLE `twitter_candidates` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2015-03-02 21:57:57
