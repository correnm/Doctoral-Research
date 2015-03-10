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
-- Table structure for table `twitter_followers`
--

DROP TABLE IF EXISTS `twitter_followers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `twitter_followers` (
  `twitter_profile_pk` int(10) NOT NULL,
  `follower_twitter_profile_pk` int(10) NOT NULL,
  PRIMARY KEY (`twitter_profile_pk`,`follower_twitter_profile_pk`),
  KEY `twitter_followers_fk2_idx` (`follower_twitter_profile_pk`),
  CONSTRAINT `twitter_followers_fk1` FOREIGN KEY (`twitter_profile_pk`) REFERENCES `twitter_profiles` (`twitter_profile_pk`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `twitter_followers_fk2` FOREIGN KEY (`follower_twitter_profile_pk`) REFERENCES `twitter_profiles` (`twitter_profile_pk`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='List of followers to a particular twitter account. Can be a recursive relationship.';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `twitter_followers`
--

LOCK TABLES `twitter_followers` WRITE;
/*!40000 ALTER TABLE `twitter_followers` DISABLE KEYS */;
INSERT INTO `twitter_followers` VALUES (51,176),(51,177),(51,178),(51,179),(51,180),(51,181),(51,182),(51,183),(51,184),(51,185),(51,186),(51,187),(51,188),(51,189),(51,190),(51,191),(51,192),(51,193),(51,194),(51,195),(144,196),(144,197),(144,198),(144,199),(144,200),(144,201),(144,202),(144,203),(144,204),(144,205),(144,206),(144,207),(144,208),(144,209),(144,210),(144,211),(144,212),(144,213),(144,214),(144,215),(144,216),(144,217),(144,218),(144,219);
/*!40000 ALTER TABLE `twitter_followers` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2015-03-09 22:58:28