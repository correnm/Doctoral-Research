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
-- Table structure for table `linkedin_candidates`
--

DROP TABLE IF EXISTS `linkedin_candidates`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `linkedin_candidates` (
  `dataset_pk` int(10) NOT NULL,
  `linkedin_pk` int(10) NOT NULL,
  `position_no` int(10) NOT NULL COMMENT 'Identifies the location in the search results',
  PRIMARY KEY (`dataset_pk`,`linkedin_pk`,`position_no`),
  KEY `linkedin_candidates_fk1_idx` (`linkedin_pk`),
  CONSTRAINT `linkedin_candidates_fk1` FOREIGN KEY (`linkedin_pk`) REFERENCES `linkedin` (`linkedin_pk`) ON DELETE CASCADE ON UPDATE NO ACTION,
  CONSTRAINT `linkedin_candidates_fk2` FOREIGN KEY (`dataset_pk`) REFERENCES `people` (`dataset_pk`) ON DELETE CASCADE ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `linkedin_candidates`
--

LOCK TABLES `linkedin_candidates` WRITE;
/*!40000 ALTER TABLE `linkedin_candidates` DISABLE KEYS */;
INSERT INTO `linkedin_candidates` VALUES (19,67737,1),(1,67914,1),(1,67915,2),(2,68237,1),(2,68238,2),(3,68699,1),(3,68700,2),(3,68701,3),(4,69470,1),(4,69471,2),(4,69472,3),(4,69473,4),(4,69474,5),(4,69475,6),(4,69476,7),(4,69477,8),(4,69478,9),(4,69479,10),(4,69480,11),(4,69481,1),(4,69482,2),(4,69483,3),(4,69484,4),(4,69485,5),(6,72227,1),(6,72228,2),(5,72730,1),(5,72731,2),(5,72732,3),(5,72733,4),(5,72734,5),(5,72735,6),(5,72736,7),(5,72737,8),(5,72738,9),(5,72739,10),(5,72740,11),(5,72741,12),(5,72742,13),(5,72743,1),(5,72744,1),(5,72745,1),(5,72746,2),(5,72747,3),(5,72748,1),(5,72749,2),(5,72750,3),(5,72751,4),(5,72752,5),(5,72753,6),(5,72754,7),(5,72755,8),(5,72756,9),(5,72757,10),(5,72758,1),(5,72759,2),(5,72760,3),(7,76499,1),(8,76531,1),(9,76742,1),(9,76743,2),(10,76958,1),(11,77207,1),(11,77208,2),(11,77209,3),(11,77210,4),(11,77211,1),(11,77212,1),(11,77213,2),(11,77214,3),(11,77215,4),(11,77216,5),(12,78040,1),(12,78041,2),(12,78042,3),(12,78043,4),(12,78044,5),(12,78045,6),(12,78046,7),(12,78047,8),(12,78048,9),(12,78049,10),(12,78050,11),(12,78051,12),(12,78052,13),(12,78053,14),(12,78054,15),(12,78055,16),(12,78056,17),(12,78057,18),(12,78058,19),(12,78059,20),(12,78060,21),(12,78061,22),(12,78062,23),(12,78063,24),(12,78064,25),(12,78065,26),(12,78066,27),(12,78067,28),(12,78068,29),(12,78069,30),(12,78070,1),(12,78071,2),(12,78072,3),(12,78073,4),(12,78074,5),(12,78075,6),(12,78076,7),(13,82517,1),(14,82518,1),(14,82519,2),(14,82520,3),(14,82521,4),(14,82522,5),(14,82523,6),(14,82524,7),(14,82525,8),(14,82526,9),(14,82527,10),(14,82528,11),(14,82529,12),(14,82530,13),(14,82531,14),(14,82532,1),(14,82533,2),(14,82534,3),(14,82535,4),(14,82536,5),(14,82537,6),(15,84587,1),(16,84654,1),(16,84655,1),(17,84666,1),(18,84834,1),(18,84835,2),(18,84836,3),(18,84837,4),(18,84838,1),(18,84839,2),(18,84840,3),(18,84841,4),(18,84842,5),(18,84843,6),(18,84844,7),(18,84845,8),(18,84846,9),(18,84847,10),(18,84848,11),(18,84849,12),(18,84850,13),(18,84851,14),(18,84852,15),(18,84853,16),(20,88440,1),(20,88441,2),(20,88442,3),(20,88443,4),(20,88444,5),(20,88445,6),(20,88446,7),(20,88447,8),(21,88993,1),(22,89104,1),(22,89105,2),(22,89106,3),(22,89107,4),(22,89108,5),(22,89109,6),(22,89110,7),(22,89111,8),(22,89112,9),(22,89113,1),(22,89114,2),(22,89115,3),(22,89116,4),(22,89117,5),(22,89118,1),(22,89119,1),(22,89120,2),(22,89121,3),(22,89122,4),(22,89123,5),(22,89124,6),(22,89125,7),(22,89126,8),(22,89127,1),(22,89128,1),(22,89129,2),(22,89130,3),(22,89131,4),(23,91823,1),(23,91824,2),(24,92240,1),(24,92241,2),(24,92242,3),(24,92243,4),(24,92244,1),(24,92245,2),(24,92246,1),(24,92247,1),(24,92248,1),(24,92249,1),(25,92945,1);
/*!40000 ALTER TABLE `linkedin_candidates` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2015-04-05 12:05:37
