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
-- Table structure for table `given_names`
--

DROP TABLE IF EXISTS `given_names`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `given_names` (
  `name_pk` int(11) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(45) NOT NULL,
  PRIMARY KEY (`name_pk`)
) ENGINE=InnoDB AUTO_INCREMENT=702 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `given_names`
--

LOCK TABLES `given_names` WRITE;
/*!40000 ALTER TABLE `given_names` DISABLE KEYS */;
INSERT INTO `given_names` VALUES (1,'aaron'),(2,'abel'),(3,'abednego'),(4,'abijah'),(5,'abigail'),(6,'abner'),(7,'abraham'),(8,'absalom'),(9,'adaline'),(10,'adam'),(11,'addy'),(12,'adelaide'),(13,'adela'),(14,'adelaide'),(15,'adelbert'),(16,'adeline'),(17,'adolphus'),(18,'adrian'),(19,'adrienne'),(20,'agatha'),(21,'agnes'),(22,'aileen'),(23,'alanson'),(24,'alastair'),(25,'alazama'),(26,'albert'),(27,'alberta'),(28,'aleva'),(29,'alexander'),(30,'alexandra'),(31,'alexandria'),(32,'alexandria'),(33,'alexis'),(34,'alfred'),(35,'alfreda'),(36,'algernon'),(37,'alicia'),(38,'alice'),(39,'aline'),(40,'alison'),(41,'almena'),(42,'almina'),(43,'alonzo'),(44,'alphinias'),(45,'almira'),(46,'alverta'),(47,'alyssa'),(48,'alzada'),(49,'amanda'),(50,'ambrose'),(51,'amelia'),(52,'amos'),(53,'anastasia'),(54,'andrea'),(55,'andrew'),(56,'angela'),(57,'angelina'),(58,'anna'),(59,'anne'),(60,'annie'),(61,'annette'),(62,'anselm'),(63,'anthony'),(64,'antoinette'),(65,'antonia'),(66,'appoline'),(67,'aquilla'),(68,'arabella'),(69,'araminta'),(70,'archibald'),(71,'ariadne'),(72,'arielle'),(73,'archilles'),(74,'aristotle'),(75,'arizona'),(76,'arlene'),(77,'armanda'),(78,'armilda'),(79,'arminda'),(80,'arminta'),(81,'arnold'),(82,'artelepsa'),(83,'artemus'),(84,'arthur'),(85,'arthusa'),(86,'arzada'),(87,'aubrey'),(88,'audrey'),(89,'augusta'),(90,'augustina'),(91,'augustine'),(92,'augustus'),(93,'aurelia'),(94,'avarilla'),(95,'barbara'),(96,'barbery'),(97,'barnabas'),(98,'bernard'),(99,'bartholomew'),(100,'barticus'),(101,'bazaleel'),(102,'beatrice'),(103,'bedelia'),(104,'belinda'),(105,'benedict'),(106,'benjamin'),(107,'bertram'),(108,'bertha'),(109,'bethena'),(110,'beverly'),(111,'bezaleel'),(112,'blanche'),(113,'boetius'),(114,'brenda'),(115,'bridget'),(116,'brian'),(117,'brittany'),(118,'caldonia'),(119,'caleb'),(120,'california'),(121,'calista'),(122,'calpurnia'),(123,'calvin'),(124,'cameron'),(125,'camille'),(126,'campbell'),(127,'candace'),(128,'carlotta'),(129,'carlton'),(130,'carmon'),(131,'carmellia'),(132,'caroline'),(133,'carolyn'),(134,'carthaette'),(135,'casper'),(136,'cassandra'),(137,'caswell'),(138,'catherine'),(139,'cathleen'),(140,'cecilia'),(141,'celeste'),(142,'celinda'),(143,'charity'),(144,'charles'),(145,'chick'),(146,'charlotte'),(147,'chauncey'),(148,'chesley'),(149,'chester'),(150,'chloe'),(151,'christian'),(152,'christine'),(153,'christopher'),(154,'cicely'),(155,'cinderella'),(156,'clara'),(157,'clarence'),(158,'clarinda'),(159,'clarissa'),(160,'claudia'),(161,'cleatus'),(162,'clementine'),(163,'clifford'),(164,'clifton'),(165,'cole'),(166,'columbus'),(167,'constance'),(168,'cordelia'),(169,'cory'),(170,'corey'),(171,'corinne'),(172,'cornelia'),(173,'cornelius'),(174,'courtney'),(175,'crystal'),(176,'cynthia'),(177,'cyrus'),(178,'daisy'),(179,'daniel'),(180,'danielle'),(181,'daphne'),(182,'david'),(183,'deanne'),(184,'deborah'),(185,'delbert'),(186,'deidre'),(187,'delia'),(188,'delilah'),(189,'dell'),(190,'della'),(191,'delores'),(192,'delpha'),(193,'delphine'),(194,'demaris'),(195,'demerias'),(196,'democrates'),(197,'denise'),(198,'deuteronomy'),(199,'diane'),(200,'diana'),(201,'dickson'),(202,'doctor'),(203,'dominic'),(204,'dorinda'),(205,'doris'),(206,'dorothea'),(207,'dorothy'),(208,'dotha'),(209,'douglas'),(210,'drusilla'),(211,'duncan'),(212,'ebenezer'),(213,'edith'),(214,'edmund'),(215,'edna'),(216,'edward'),(217,'edwina'),(218,'egbert'),(219,'eighta'),(220,'eileen'),(221,'elaine'),(222,'elbert'),(223,'elbertson'),(224,'eleanor'),(225,'leonora'),(226,'elena'),(227,'elias'),(228,'elijah'),(229,'eliphalel'),(230,'elisa'),(231,'elisha'),(232,'eliza'),(233,'elizabeth'),(234,'ella'),(235,'ellie'),(236,'ellen'),(237,'ellender'),(238,'elminie'),(239,'elmira'),(240,'elnora'),(241,'eloise'),(242,'elsie'),(243,'elwood'),(244,'elvira'),(245,'elysia'),(246,'emanuel'),(247,'emeline'),(248,'emil'),(249,'emily'),(250,'ephraim'),(251,'erasmus'),(252,'eric'),(253,'ernest'),(254,'earnest'),(255,'ernestine'),(256,'erwin'),(257,'essy'),(258,'eseneth'),(259,'estella'),(260,'esther'),(261,'eudicy'),(262,'eudora'),(263,'eudoris'),(264,'eugene'),(265,'eunice'),(266,'euphemia'),(267,'eurydice'),(268,'eustacia'),(269,'evangeline'),(270,'evelyn'),(271,'ezekiel'),(272,'ezideen'),(273,'experience'),(274,'faith'),(275,'fidelia'),(276,'felicia'),(277,'felicity'),(278,'ferdinand'),(279,'ferdinando'),(280,'florence'),(281,'floyd'),(282,'frances'),(283,'francis'),(284,'franklin'),(285,'frederick'),(286,'frederica'),(287,'gabriel'),(288,'gabrielle'),(289,'genevieve'),(290,'geoffrey'),(291,'george'),(292,'georgia'),(293,'gerald'),(294,'geraldine'),(295,'gerhardt'),(296,'gertrude'),(297,'gilbert'),(298,'gloria'),(299,'governor'),(300,'greenberry'),(301,'gretchen'),(302,'gregory'),(303,'griselda'),(304,'gustavus'),(305,'gwendolyn'),(306,'hamilton'),(307,'hannah'),(308,'heather'),(309,'herman'),(310,'harold'),(311,'harriet'),(312,'harry'),(313,'haseltine'),(314,'helen'),(315,'helena'),(316,'heloise'),(317,'henrietta'),(318,'henry'),(319,'herbert'),(320,'hester'),(321,'hezekiah'),(322,'honora'),(323,'horace'),(324,'hortense'),(325,'hosea'),(326,'howard'),(327,'hubert'),(328,'ian'),(329,'ignatius'),(330,'ignatzio'),(331,'immanuel'),(332,'india'),(333,'inez'),(334,'iona'),(335,'irene'),(336,'irvin'),(337,'irwin'),(338,'isaac'),(339,'isabelle'),(340,'isabella'),(341,'isadora'),(342,'isaiah'),(343,'isidore'),(344,'iva'),(345,'ivan'),(346,'jacob'),(347,'jacqueline'),(348,'jackson'),(349,'jahoda'),(350,'james'),(351,'jane'),(352,'jannett'),(353,'jasper'),(354,'jayme'),(355,'jean'),(356,'jeanette'),(357,'jedediah'),(358,'jeffrey'),(359,'jefferey'),(360,'jehu'),(361,'jemima'),(362,'jennet'),(363,'jennifer'),(364,'jeremiah'),(365,'jerita'),(366,'jessica'),(367,'jincy'),(368,'jinsy'),(369,'jessie'),(370,'joanna'),(371,'john'),(372,'johannes'),(373,'jonathan'),(374,'joseph'),(375,'josephine'),(376,'josetta'),(377,'joshua'),(378,'joyce'),(379,'juanita'),(380,'judah'),(381,'judith'),(382,'julia'),(383,'june'),(384,'justin'),(385,'karonhappuck'),(386,'katarina'),(387,'kathleen'),(388,'kayla'),(389,'kendra'),(390,'keziah'),(391,'kristel'),(392,'kristine'),(393,'kristopher'),(394,'lafayette'),(395,'laodicia'),(396,'lauren'),(397,'laurinda'),(398,'lauryn'),(399,'laveda'),(400,'laverne'),(401,'lavinia'),(402,'lavonia'),(403,'louvinia'),(404,'lawrence'),(405,'leanne'),(406,'lecurgus'),(407,'lemuel'),(408,'lena'),(409,'leonard'),(410,'leonidas'),(411,'leonore'),(412,'leonora'),(413,'leroy'),(414,'leslie'),(415,'letitia'),(416,'levicy'),(417,'levone'),(418,'lavonne'),(419,'lillian'),(420,'lincoln'),(421,'lionel'),(422,'littleberry'),(423,'lois'),(424,'loretta'),(425,'lorraine'),(426,'louis'),(427,'louise'),(428,'lucia'),(429,'lucias'),(430,'lucille'),(431,'lucina'),(432,'lucinda'),(433,'lucretia'),(434,'luella'),(435,'lunetta'),(436,'lurana'),(437,'mabel'),(438,'mac'),(439,'mack'),(440,'mackenzie'),(441,'madeline'),(442,'maud'),(443,'madison'),(444,'magdalena'),(445,'mahala'),(446,'malachi'),(447,'malcolm'),(448,'malinda'),(449,'manerva'),(450,'manoah'),(451,'manola'),(452,'manuel'),(453,'marcus'),(454,'margaret'),(455,'margarita'),(456,'mariah'),(457,'marie'),(458,'marion'),(459,'marian'),(460,'marilyn'),(461,'marissa'),(462,'marjorie'),(463,'marsha'),(464,'martha'),(465,'martine'),(466,'marvin'),(467,'mary'),(468,'marietta'),(469,'matthew'),(470,'mathilda'),(471,'matilda'),(472,'marguerite'),(473,'maureen'),(474,'maurice'),(475,'mavine'),(476,'mavery'),(477,'maxine'),(478,'may'),(479,'mckenna'),(480,'medora'),(481,'megan'),(482,'mehitabel'),(483,'melanie'),(484,'melchizedek'),(485,'melinda'),(486,'melissa'),(487,'mellony'),(488,'melody'),(489,'melvin'),(490,'melvina'),(491,'mercedes'),(492,'micajah'),(493,'michael'),(494,'michelle'),(495,'mildred'),(496,'millicent'),(497,'minerva'),(498,'miranda'),(499,'miriam'),(500,'mitchell'),(501,'mitzi'),(502,'monet'),(503,'monica'),(504,'monteleon'),(505,'montesque'),(506,'montgomery'),(507,'mortimer'),(508,'moses'),(509,'muriel'),(510,'myrtle'),(511,'nadine'),(512,'nancy'),(513,'nancy'),(514,'naomi'),(515,'napoleon'),(516,'natalie'),(517,'natasha'),(518,'nathaniel'),(519,'nelson'),(520,'nicholas'),(521,'nicodemus'),(522,'nicole'),(523,'nora'),(524,'nowell'),(525,'obadiah'),(526,'obedience'),(527,'octavia'),(528,'odell'),(529,'olive'),(530,'olivia'),(531,'oliver'),(532,'onicyphorous'),(533,'orilla'),(534,'orlando'),(535,'orphelia'),(536,'oswald'),(537,'otis'),(538,'pamela'),(539,'pandora'),(540,'parthenia'),(541,'patience'),(542,'patricia'),(543,'patrick'),(544,'paul'),(545,'pauline'),(546,'penelope'),(547,'percival'),(548,'peregrine'),(549,'permelia'),(550,'pernetta'),(551,'persephone'),(552,'petronella'),(553,'pheriba'),(554,'pheney'),(555,'philip'),(556,'philadelphia'),(557,'philander'),(558,'philipina'),(559,'philomena'),(560,'phoebe'),(561,'pinckney'),(562,'pleasant'),(563,'pocahontas'),(564,'posthuma'),(565,'prescott'),(566,'priscilla'),(567,'providence'),(568,'prudence'),(569,'rachel'),(570,'randolph'),(571,'raphael'),(572,'ramona'),(573,'raymond'),(574,'rebecca'),(575,'regina'),(576,'reginald'),(577,'reuben'),(578,'reynold'),(579,'rhoda'),(580,'rhodella'),(581,'rhyna'),(582,'richard'),(583,'robert'),(584,'roberta'),(585,'roderick'),(586,'roger'),(587,'roland'),(588,'ronald'),(589,'roscoe'),(590,'rosina'),(591,'roxane'),(592,'rudolph'),(593,'russell'),(594,'ryan'),(595,'sabrina'),(596,'salome'),(597,'salvador'),(598,'samantha'),(599,'samson'),(600,'sampson'),(601,'samuel'),(602,'samyra'),(603,'sandra'),(604,'sanford'),(605,'sarah'),(606,'sarilla'),(607,'serena'),(608,'savannah'),(609,'scott'),(610,'sebastian'),(611,'selma'),(612,'serena'),(613,'serilla'),(614,'shaina'),(615,'sharon'),(616,'sheila'),(617,'sheldon'),(618,'sheridan'),(619,'sidney'),(620,'sibbilla'),(621,'sigfrid'),(622,'sigfired'),(623,'sigismund'),(624,'silas'),(625,'silence'),(626,'silvester'),(627,'simeon'),(628,'socrates'),(629,'solomon'),(630,'sondra'),(631,'sophronia'),(632,'stephanie'),(633,'stephen'),(634,'submit'),(635,'sullivan'),(636,'susannah'),(637,'suzanne'),(638,'sybill'),(639,'sydney'),(640,'sylvanus'),(641,'sylvester'),(642,'tabitha'),(643,'tamarra'),(644,'tanafra'),(645,'tasha'),(646,'temperance'),(647,'terence'),(648,'teresa'),(649,'thaddeus'),(650,'theodora'),(651,'theodore'),(652,'theodosia'),(653,'theophilus'),(654,'theotha'),(655,'theresa'),(656,'thomas'),(657,'thomasa'),(658,'tiffany'),(659,'tilford'),(660,'timothy'),(661,'tobias'),(662,'tranquilla'),(663,'unice'),(664,'uriah'),(665,'ursula'),(666,'valentina'),(667,'valentine'),(668,'valerie'),(669,'vanburen'),(670,'vandalia'),(671,'vanessa'),(672,'vernisee'),(673,'veronica'),(674,'victor'),(675,'victoria'),(676,'vincent'),(677,'viola'),(678,'violetta'),(679,'virginia'),(680,'vivian'),(681,'waldo'),(682,'wallace'),(683,'walter'),(684,'webster'),(685,'wendy'),(686,'wilber'),(687,'wilfred'),(688,'wilhelmina'),(689,'william'),(690,'willis'),(691,'wilda'),(692,'wilma'),(693,'winfield'),(694,'winifred'),(695,'winton'),(696,'woodrow'),(697,'yeona'),(698,'yulan'),(699,'yvonne'),(700,'zachariah'),(701,'zedediah');
/*!40000 ALTER TABLE `given_names` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2015-04-11 19:15:19
