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
-- Table structure for table `linkedin_affiliation`
--

DROP TABLE IF EXISTS `linkedin_affiliation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `linkedin_affiliation` (
  `linkedin_affiliation_pk` int(10) NOT NULL AUTO_INCREMENT,
  `linkedin_pk` int(10) NOT NULL,
  `affiliation_name` varchar(100) NOT NULL,
  `affiliation_type` varchar(3) DEFAULT NULL COMMENT '(EDU)cation, (EMP)loyer',
  `affiliation_pk` int(10) DEFAULT NULL,
  PRIMARY KEY (`linkedin_affiliation_pk`),
  KEY `linkedin_affiliation_fk1_idx` (`linkedin_pk`),
  KEY `linkedin_affiliation_fk2_idx` (`affiliation_pk`),
  CONSTRAINT `linkedin_affiliation_fk1` FOREIGN KEY (`linkedin_pk`) REFERENCES `linkedin` (`linkedin_pk`) ON DELETE CASCADE ON UPDATE NO ACTION,
  CONSTRAINT `linkedin_affiliation_fk2` FOREIGN KEY (`affiliation_pk`) REFERENCES `affiliations` (`affiliation_pk`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=671 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `linkedin_affiliation`
--

LOCK TABLES `linkedin_affiliation` WRITE;
/*!40000 ALTER TABLE `linkedin_affiliation` DISABLE KEYS */;
INSERT INTO `linkedin_affiliation` VALUES (480,67737,'Regent University',NULL,53),(481,67737,'Art Institute of Atlanta',NULL,156),(482,67737,'National University &#39;Ivan Franko&#39; , Lviv',NULL,157),(483,68237,'Southern California University of Health Sciences',NULL,52),(484,68237,'Texas State University-San Marcos',NULL,48),(485,68699,'Old Dominion University',NULL,44),(486,68699,'Regent University',NULL,53),(487,68699,'Susquehanna University',NULL,54),(488,68700,'Lehigh University',NULL,55),(489,69472,'Naval Postgraduate School',NULL,38),(490,69472,'Chapman University',NULL,39),(491,69472,'Southern Illinois University, Carbondale',NULL,40),(492,69472,'Northwestern University - Kellogg School of Management',NULL,41),(493,69472,'Georgetown University',NULL,42),(494,69473,'Penn State University',NULL,36),(495,69473,'American University',NULL,37),(496,69475,'Regent University School of Law',NULL,53),(497,69475,'Old Dominion University',NULL,44),(498,69476,'Iowa State University - College of Business',NULL,45),(499,69477,'Georgetown University',NULL,42),(500,69477,'UC Berkeley',NULL,46),(501,69481,'University of Houston Law Center',NULL,49),(502,69481,'Boston College Law School',NULL,50),(503,69481,'Texas A&amp;M University',NULL,51),(504,69471,'University of Iowa',NULL,NULL),(505,69471,'Loras College',NULL,NULL),(506,72730,'Regent University',NULL,53),(507,72730,'University of Hawaii at Manoa',NULL,56),(508,72730,'University of Hawaii at Manoa',NULL,56),(509,72731,'Spelman College',NULL,62),(510,72731,'Bank Street College of Education',NULL,63),(511,72732,'George Mason University School of Law',NULL,59),(512,72732,'University of Virginia',NULL,60),(513,72733,'Howard University',NULL,58),(514,72733,'Howard University',NULL,58),(515,72734,'Syracuse University',NULL,57),(516,72735,'University of North Carolina at Chapel Hill',NULL,61),(517,72737,'Liberty University',NULL,64),(518,72737,'Liberty University',NULL,64),(519,72737,'Edison Community College',NULL,65),(520,72738,'University of Colorado Boulder',NULL,149),(521,72738,'University of Colorado Boulder',NULL,149),(522,72739,'Tidewater Community College',NULL,66),(523,72742,'Northern Virginia Community College',NULL,67),(524,72742,'Northern Virginia Community College',NULL,67),(525,72742,'University of Mary Washington',NULL,68),(526,72744,'University of Maryland University College',NULL,69),(527,72745,'University of California, Irvine',NULL,70),(528,72745,'Westmont College',NULL,71),(529,72746,'Duke University',NULL,72),(530,72747,'The Ohio State University',NULL,35),(531,72748,'University of New Hampshire',NULL,NULL),(532,72748,'University of Maryland College Park',NULL,139),(533,72749,'University of Minnesota - Carlson School of Management',NULL,NULL),(534,72749,'University of Wisconsin-Madison',NULL,NULL),(535,72750,'Southwest College of Naturopathic Medicine &amp; Health Sciences',NULL,NULL),(536,72751,'Rochester Community and Technical College',NULL,NULL),(537,72757,'New Mexico State University',NULL,73),(538,72760,'Los Angeles City College',NULL,74),(539,76499,'Regent University',NULL,53),(540,76531,'Regent University',NULL,53),(541,76531,'Bucknell University',NULL,75),(542,76531,'Bucknell University',NULL,75),(543,76743,'Regent University',NULL,53),(544,76743,'Regent University',NULL,53),(545,76743,'Middle Tennessee State University',NULL,76),(546,76958,'Regent University',NULL,53),(547,76958,'Regent University',NULL,53),(548,76958,'Northeastern State University',NULL,77),(549,76958,'Oral Roberts University',NULL,78),(550,76958,'Oral Roberts University',NULL,78),(551,77216,'The Ohio State University',NULL,35),(552,77216,'The Ohio State University',NULL,35),(553,77216,'Liverpool Hope University',NULL,91),(554,77216,'Kingston University',NULL,92),(555,77207,'Florida Southern College',NULL,79),(556,77208,'University of Southern Maine',NULL,80),(557,77208,'Wheaton College',NULL,81),(558,77211,'Columbia University - Graduate School of Architecture, Planning and Preservation',NULL,NULL),(559,77211,'Bowdoin College',NULL,NULL),(560,77211,'Columbia University - Graduate School of Architecture, Planning and Preservation',NULL,NULL),(561,77212,'University of San Diego',NULL,84),(562,77213,'Duke University',NULL,72),(563,77214,'New York University - Leonard N. Stern School of Business',NULL,88),(564,77214,'Cornell University',NULL,89),(565,77214,'Farmingdale State University of New York',NULL,90),(566,77215,'Georgetown University Law Center',NULL,85),(567,77215,'Wake Forest University School of Law',NULL,86),(568,77215,'University of Scranton',NULL,87),(569,78040,'Widener University School of Law',NULL,110),(570,78040,'Rutgers University',NULL,111),(571,78041,'Saint Mary&#39;s College of California',NULL,NULL),(572,78043,'University of California, San Diego',NULL,34),(573,78044,'Point Loma Nazarene University',NULL,112),(574,78044,'San Diego State University',NULL,113),(575,78045,'University of Colorado at Denver',NULL,114),(576,78045,'Sam Houston State University',NULL,115),(577,78045,'University of Nebraska-Lincoln',NULL,116),(578,78046,'Virginia Commonwealth University',NULL,121),(579,78046,'Mary Washington College',NULL,122),(580,78049,'San Francisco State University',NULL,117),(581,78050,'University of San Francisco',NULL,119),(582,78050,'University of Arizona',NULL,120),(583,78051,'Colorado Technical University',NULL,123),(584,78059,'Claremont Graduate University - Peter F. Drucker and Masatoshi Ito Graduate School of Management',NULL,124),(585,78059,'California State Polytechnic University-Pomona',NULL,125),(586,78060,'Parsons School of Design',NULL,129),(587,78060,'State University of New York at New Paltz',NULL,130),(588,78061,'University of California, Berkeley',NULL,131),(589,78062,'California State University-Northridge',NULL,NULL),(590,78063,'Kolej Han Chiang',NULL,132),(591,78064,'Moore College of Art and Design',NULL,128),(592,78065,'University of Phoenix',NULL,133),(593,78070,'University of Phoenix',NULL,133),(594,78070,'University of Phoenix',NULL,133),(595,78073,'Rollins College',NULL,NULL),(596,78074,'New England College',NULL,134),(597,82517,'Regent University',NULL,53),(598,82517,'Regent University ',NULL,53),(599,82531,'Full Sail University',NULL,135),(600,82532,'University of Maryland College Park',NULL,139),(601,82533,'Oregon State University',NULL,140),(602,82521,'Southern California University of Health Sciences',NULL,52),(603,82521,'Indiana University&#x2014;Purdue University Fort Wayne',NULL,136),(604,82525,'Full Sail University',NULL,135),(605,82526,'Charleston School of Law',NULL,137),(606,82526,'Winthrop University',NULL,138),(607,82527,'Brookdale Community College',NULL,NULL),(608,82527,'Lackawanna College',NULL,NULL),(609,84587,'Regent University',NULL,53),(610,84666,'Regent University',NULL,53),(611,84834,'Franklin Pierce Law Center',NULL,141),(612,84834,'Fairleigh Dickinson University &#x2013; Vancouver',NULL,142),(613,84838,'University of Massachusetts at Amherst - Isenberg School of Management',NULL,143),(614,84838,'Yeshiva University',NULL,144),(615,84838,'Duke University',NULL,72),(616,84841,'University of Colorado Boulder',NULL,149),(617,84842,'Harvard Kennedy School of Government',NULL,145),(618,84842,'Fort Lewis College',NULL,146),(619,84842,'Harvard University Graduate School of Education',NULL,147),(620,84842,'Prescott College',NULL,148),(621,84843,'Whitman College',NULL,150),(622,84845,'Fordham University',NULL,151),(623,84845,'Vassar College',NULL,152),(624,84848,'Central Michigan University',NULL,153),(625,84849,'Hastings College of the Law',NULL,154),(626,84849,'San Francisco State University',NULL,117),(627,84850,'Temple University - Fox School of Business and Management',NULL,155),(628,84850,'Penn State University',NULL,36),(629,88440,'Regent University',NULL,53),(630,88440,'Regent University',NULL,53),(631,88440,'Lakeland Community College',NULL,NULL),(632,88441,'University of Wisconsin-Oshkosh',NULL,159),(633,88442,'Texas A&amp;M University',NULL,51),(634,88443,'Royal College of Art',NULL,NULL),(635,88443,'Edinburgh College of Art',NULL,NULL),(636,88446,'Arizona State University',NULL,161),(637,88993,'Regent University',NULL,53),(638,88993,'Geneva College',NULL,178),(639,89104,'King&#39;s College London, U. of London',NULL,162),(640,89104,'Regent University',NULL,53),(641,89104,'Regent University',NULL,53),(642,89104,'Virginia Commonwealth University - School of Business',NULL,163),(643,89108,'University of Washington',NULL,164),(644,89108,'Seattle Central Community College',NULL,165),(645,89110,'Bethel University',NULL,166),(646,89110,'North Hennepin Community College',NULL,167),(647,89111,'University of California, Los Angeles',NULL,168),(648,89111,'University of California, Santa Barbara',NULL,108),(649,89113,'Harvard University',NULL,169),(650,89118,'Ringling School of Art and Design',NULL,170),(651,89119,'Naval Postgraduate School',NULL,38),(652,89119,'Winona State University',NULL,171),(653,89120,'The Johns Hopkins University',NULL,NULL),(654,89120,'Trinity University',NULL,NULL),(655,89122,'Hillsborough Community College',NULL,172),(656,89122,'Madison Area Technical College',NULL,173),(657,89128,'Georgetown University',NULL,42),(658,89130,'University of California, San Diego',NULL,34),(659,89131,'WGU Texas',NULL,174),(660,91824,'Regent University',NULL,53),(661,91824,'Regent University',NULL,53),(662,91824,'Evangel University',NULL,176),(663,91823,'The University of Tennessee at Chattanooga',NULL,175),(664,92240,'Regent University',NULL,53),(665,92246,'Massachusetts Institute of Technology',NULL,179),(666,92246,'Massachusetts Institute of Technology',NULL,179),(667,92246,'University of Alberta',NULL,180),(668,92247,'Long Beach City College',NULL,181),(669,92945,'Regent University',NULL,53),(670,92945,'University of Minnesota-Twin Cities',NULL,NULL);
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

-- Dump completed on 2015-04-05 12:05:36
