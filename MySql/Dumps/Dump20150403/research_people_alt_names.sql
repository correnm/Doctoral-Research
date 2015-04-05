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
) ENGINE=InnoDB AUTO_INCREMENT=360 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `people_alt_names`
--

LOCK TABLES `people_alt_names` WRITE;
/*!40000 ALTER TABLE `people_alt_names` DISABLE KEYS */;
INSERT INTO `people_alt_names` VALUES (253,19,'bohdan','smaha','O'),(279,1,'jessica','totty','O'),(280,1,'jess','totty','A'),(281,1,'jesse','totty','A'),(282,1,'jessie','totty','A'),(283,1,'sica','totty','A'),(284,2,'chelsea','kelley','O'),(285,3,'joe','dobrota','O'),(286,3,'joseph','dobrota','A'),(287,4,'mark','stevenson','O'),(288,4,'marcus','stevenson','A'),(289,6,'grace','alegre','O'),(290,5,'victoria','walker','O'),(291,5,'toria','walker','A'),(292,5,'torrie','walker','A'),(293,5,'tory','walker','A'),(294,5,'vicki','walker','A'),(295,5,'victor','walker','A'),(296,7,'lena','maslennikova','O'),(297,7,'leenlina','maslennikova','A'),(298,7,'arlene','maslennikova','A'),(299,7,'caroline','maslennikova','A'),(300,7,'carolyn','maslennikova','A'),(301,7,'helen','maslennikova','A'),(302,7,'helena','maslennikova','A'),(303,7,'madeline','maslennikova','A'),(304,7,'magdalena','maslennikova','A'),(305,8,'sean','kirnan','O'),(306,9,'kita','graham','O'),(307,10,'donnie','staggs','O'),(308,11,'jamie','brennan','O'),(309,11,'benjamin','brennan','A'),(310,11,'james','brennan','A'),(311,12,'pamela','lee','O'),(312,12,'pam','lee','A'),(313,13,'nathaniel','richner','O'),(314,13,'jonathan','richner','A'),(315,13,'nat','richner','A'),(316,13,'nate','richner','A'),(317,13,'nathan','richner','A'),(318,13,'natty','richner','A'),(319,13,'tan','richner','A'),(320,14,'joshua','mitchell','O'),(321,14,'josh','mitchell','A'),(322,15,'jacob','affinito','O'),(323,15,'jake','affinito','A'),(324,16,'augusta','hayward','O'),(325,16,'aggy','hayward','A'),(326,16,'augie','hayward','A'),(327,16,'gus','hayward','A'),(328,16,'guss','hayward','A'),(329,16,'gussie','hayward','A'),(330,16,'augustus','hayward','A'),(331,17,'chad','clukey','O'),(332,17,'charles','clukey','A'),(333,18,'mike','ackerman','O'),(334,18,'michael','ackerman','A'),(335,20,'kyle','graham','O'),(336,21,'marc','santom','O'),(337,22,'ella','thompson','O'),(338,22,'eleanor','thompson','A'),(339,22,'gabriella','thompson','A'),(340,22,'helen','thompson','A'),(341,22,'luella','thompson','A'),(342,22,'gabrielle','thompson','A'),(343,23,'jared','beasley','O'),(344,24,'patricia','mercier','O'),(345,24,'pat','mercier','A'),(346,24,'patrick','mercier','A'),(347,24,'patsy','mercier','A'),(348,24,'patty','mercier','A'),(349,24,'tricia','mercier','A'),(350,24,'trish','mercier','A'),(351,24,'trixie','mercier','A'),(352,25,'christine','habrle','O'),(353,25,'chris','habrle','A'),(354,25,'christiana','habrle','A'),(355,25,'christy','habrle','A'),(356,25,'crissy','habrle','A'),(357,25,'ina','habrle','A'),(358,25,'tina','habrle','A'),(359,25,'xina','habrle','A');
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

-- Dump completed on 2015-04-03 15:27:01
