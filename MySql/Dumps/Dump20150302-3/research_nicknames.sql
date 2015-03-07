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
-- Table structure for table `nicknames`
--

DROP TABLE IF EXISTS `nicknames`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `nicknames` (
  `name_pk` int(11) NOT NULL,
  `nickname` varchar(45) NOT NULL COMMENT 'store in lowercase',
  PRIMARY KEY (`name_pk`,`nickname`),
  KEY `nicknames_fk1_idx` (`name_pk`),
  CONSTRAINT `nicknames_fk1` FOREIGN KEY (`name_pk`) REFERENCES `given_names` (`name_pk`) ON DELETE CASCADE ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `nicknames`
--

LOCK TABLES `nicknames` WRITE;
/*!40000 ALTER TABLE `nicknames` DISABLE KEYS */;
INSERT INTO `nicknames` VALUES (1,'ron'),(2,'abe'),(3,'bedney'),(4,'ab'),(4,'bige'),(5,'ab'),(5,'abbie'),(5,'abby'),(5,'gail'),(6,'ab'),(6,'abbie'),(6,'abby'),(7,'abe'),(7,'abram'),(7,'bram'),(8,'ab'),(8,'abbie'),(8,'app'),(9,'ada'),(9,'adela'),(9,'aline'),(9,'edith'),(10,'ade'),(10,'edie'),(11,'ad'),(12,'ada'),(12,'addie'),(12,'adela'),(12,'adeline'),(12,'della'),(12,'heide'),(13,'della'),(14,'addie'),(15,'albert'),(15,'bert'),(15,'del'),(15,'delbert'),(16,'addie'),(16,'linney'),(17,'ado'),(17,'adolph'),(17,'dolph'),(18,'rian'),(19,'adrian'),(20,'addy'),(20,'ag'),(20,'aggie'),(20,'agnes'),(21,'aggy'),(21,'ann'),(21,'nancy'),(21,'nessie'),(22,'helen'),(23,'al'),(23,'lanson'),(24,'al'),(25,'ali'),(26,'al'),(26,'alberta'),(26,'bert'),(26,'bird'),(27,'abertina'),(27,'albert'),(27,'albertine'),(27,'allie'),(27,'bert'),(27,'bertie'),(28,'leve'),(28,'levy'),(29,'ala'),(29,'alec'),(29,'alex'),(29,'alexis'),(29,'andi'),(29,'ec'),(29,'lex'),(29,'sandra'),(29,'sandy'),(29,'xandra'),(30,'lexa'),(30,'xan'),(31,'alexander'),(31,'alla'),(31,'drina'),(31,'sandra'),(32,'alla'),(32,'elic'),(32,'ellie'),(33,'lexi'),(34,'al'),(34,'alf'),(34,'alfie'),(34,'alfreda'),(34,'fred'),(35,'alfred'),(35,'alfy'),(35,'frieda'),(36,'algy'),(37,'ally'),(38,'alcy'),(38,'alicia'),(38,'allie'),(38,'elsie'),(38,'lisa'),(39,'adeline'),(40,'ali'),(41,'allie'),(41,'mena'),(42,'minnie'),(43,'al'),(43,'alphonzo'),(43,'lon'),(43,'lonnie'),(43,'lonzo'),(44,'alphus'),(45,'myra'),(46,'vert'),(46,'virdie'),(47,'al'),(47,'ally'),(47,'lissia'),(48,'zada'),(49,'amy'),(49,'manda'),(49,'mandana'),(49,'mandy'),(50,'brose'),(51,'amy'),(51,'emily'),(51,'mel'),(51,'melia'),(51,'millie'),(52,'moses'),(53,'ana'),(53,'stacy'),(54,'andrew'),(54,'drea'),(54,'rea'),(55,'andrea'),(55,'andy'),(55,'ansey'),(55,'drew'),(56,'angel'),(56,'angelica'),(56,'angelina'),(56,'angeline'),(56,'angie'),(56,'jane'),(57,'lina'),(58,'ann'),(58,'anne'),(58,'annie'),(59,'ann'),(59,'annie'),(60,'ann'),(60,'anna'),(61,'anna'),(61,'nettie'),(62,'ance'),(62,'anse'),(62,'ansel'),(62,'selma'),(63,'antoinette'),(63,'antonia'),(63,'tony'),(64,'antonia'),(64,'net'),(64,'nettie'),(64,'tonie'),(65,'anthony'),(65,'antone'),(65,'nettie'),(66,'appie'),(66,'appy'),(67,'quil'),(67,'quillie'),(68,'ara'),(68,'bella'),(68,'belle'),(69,'armida'),(69,'middie'),(69,'minty'),(69,'ruminta'),(70,'archie'),(70,'baldie'),(71,'arie'),(72,'arie'),(73,'kill'),(73,'killis'),(74,'telly'),(75,'ona'),(75,'onie'),(76,'lena'),(77,'mandy'),(78,'milly'),(79,'mindie'),(80,'minite'),(80,'minnie'),(81,'arnie'),(82,'epsey'),(83,'art'),(84,'art'),(85,'thursa'),(86,'zaddi'),(87,'bree'),(88,'dee'),(89,'aggy'),(89,'augie'),(89,'gus'),(89,'guss'),(89,'gussie'),(90,'aggy'),(90,'augie'),(90,'augustus'),(90,'gus'),(90,'guss'),(90,'gussie'),(90,'ina'),(90,'tina'),(91,'aggy'),(91,'augie'),(91,'augustus'),(91,'gus'),(91,'guss'),(91,'gussie'),(91,'ina'),(91,'tina'),(92,'augusta'),(92,'gus'),(92,'gustie'),(92,'gustus'),(93,'aurilla'),(93,'ora'),(93,'orilla'),(93,'ree'),(93,'rilly'),(94,'rilla'),(95,'babs'),(95,'barb'),(95,'barbie'),(95,'barby'),(95,'bobbie'),(95,'bonnie'),(96,'barbara'),(97,'barney'),(98,'barney'),(98,'bernie'),(99,'bart'),(99,'bartel'),(99,'barth'),(99,'bat'),(100,'bart'),(101,'basil'),(102,'bea'),(102,'trisha'),(102,'trissy'),(102,'trixie'),(103,'bridgit'),(103,'delia'),(104,'bell'),(104,'belle'),(104,'linda'),(105,'bennett'),(106,'ben'),(106,'benjie'),(106,'bennie'),(106,'jamie'),(107,'bert'),(108,'bertie'),(109,'beth'),(109,'thaney'),(110,'bev'),(111,'zeely'),(112,'bea'),(113,'bo'),(114,'brandy'),(115,'biddy'),(115,'bridie'),(115,'brie'),(115,'delia'),(116,'bryan'),(116,'bryant'),(117,'britt'),(118,'calliedona'),(119,'cal'),(120,'callie'),(121,'kissy'),(122,'cally'),(123,'cal'),(124,'cam'),(125,'cammy'),(125,'millie'),(126,'cam'),(127,'candy'),(127,'dacey'),(128,'lottie'),(129,'carl'),(130,'cammie'),(130,'carm'),(130,'charm'),(131,'mellia'),(132,'caddie'),(132,'carol'),(132,'carrie'),(132,'cassie'),(132,'lena'),(132,'lynn'),(133,'caddie'),(133,'carol'),(133,'carrie'),(133,'cassie'),(133,'lena'),(133,'lynn'),(134,'etta'),(134,'etty'),(135,'jasper'),(136,'cass'),(136,'cassey'),(136,'cassie'),(136,'sandi'),(136,'sandra'),(137,'cass'),(138,'cathy'),(138,'karen'),(138,'katharine'),(138,'kathleen'),(138,'katie'),(138,'kay'),(138,'kit'),(138,'kittie'),(139,'catherine'),(140,'cecil'),(140,'celia'),(140,'cissy'),(141,'celia'),(141,'lessie'),(142,'linda'),(142,'lindy'),(142,'lynn'),(143,'chat'),(144,'buck'),(144,'carl'),(144,'chad'),(144,'charlie'),(145,'caroline'),(145,'charlotte'),(145,'chuck'),(146,'car'),(146,'carlotta'),(146,'charles'),(146,'letty'),(146,'lotta'),(146,'lottie'),(147,'chance'),(148,'chet'),(149,'chet'),(150,'clo'),(151,'chris'),(151,'christopher'),(151,'kit'),(152,'chris'),(152,'christiana'),(152,'christy'),(152,'crissy'),(152,'ina'),(152,'tina'),(152,'xina'),(153,'chris'),(153,'christian'),(153,'kester'),(153,'kit'),(154,'cilla'),(155,'arilla'),(155,'cindy'),(155,'rella'),(155,'rilla'),(156,'claire'),(156,'clarice'),(156,'clarissa'),(157,'clay'),(158,'clara'),(158,'clarence'),(158,'renee'),(159,'cissy'),(159,'clara'),(159,'clare'),(160,'claud'),(161,'cleat'),(162,'clem'),(162,'clement'),(163,'cliff'),(163,'ford'),(164,'cliff'),(165,'colie'),(166,'lum'),(167,'connie'),(167,'constant'),(168,'cordy'),(168,'delia'),(169,'coco'),(169,'cordy'),(169,'ree'),(170,'coco'),(170,'cordy'),(170,'ree'),(171,'cora'),(171,'ora'),(172,'conny'),(172,'cornelius'),(172,'corny'),(172,'neely'),(172,'nelle'),(172,'nelly'),(173,'cornelia'),(173,'neely'),(173,'neil'),(174,'corky'),(174,'court'),(174,'curt'),(175,'chris'),(175,'crys'),(175,'stal'),(175,'tal'),(176,'cindy'),(176,'sina'),(177,'cy'),(178,'margaret'),(179,'dan'),(179,'dank'),(179,'danny'),(180,'dani'),(180,'ellie'),(181,'daph'),(181,'daphie'),(182,'davy'),(182,'vida'),(183,'ann'),(183,'dee'),(184,'deb'),(184,'debbie'),(184,'debby'),(184,'debi'),(185,'bert'),(185,'del'),(186,'deedee'),(187,'cordelia'),(187,'delius'),(187,'fidelia'),(188,'dell'),(188,'della'),(188,'lil'),(188,'lila'),(189,'adela'),(189,'adelaide'),(189,'delilah'),(190,'adela'),(190,'adelaide'),(190,'delilah'),(191,'dee'),(191,'dodie'),(191,'lola'),(192,'philadelphia'),(193,'del'),(193,'delf'),(193,'delphi'),(194,'dea'),(194,'maris'),(194,'mary'),(195,'dea'),(195,'maris'),(195,'mary'),(196,'mock'),(197,'dennis'),(198,'duty'),(199,'di'),(199,'dicey'),(199,'didi'),(200,'di'),(200,'dicey'),(200,'didi'),(201,'dick'),(202,'namegivento'),(203,'dom'),(203,'nick'),(203,'nicky'),(204,'dora'),(204,'dorothea'),(205,'dora'),(206,'doda'),(206,'dora'),(207,'dee'),(207,'dolly'),(207,'dorothea'),(207,'dot'),(208,'dotty'),(209,'doug'),(210,'silla'),(211,'dunk'),(212,'eb'),(212,'eben'),(212,'eber'),(213,'dicey'),(213,'edie'),(214,'ed'),(214,'ned'),(214,'ted'),(215,'edny'),(216,'ed'),(216,'ned'),(216,'ted'),(217,'edwin'),(218,'bert'),(218,'burt'),(219,'athy'),(220,'helen'),(221,'helen'),(221,'lainie'),(222,'albert'),(223,'bert'),(223,'elbert'),(224,'elaine'),(224,'ella'),(224,'ellen'),(224,'helen'),(224,'lanna'),(225,'nell'),(225,'nellie'),(225,'nora'),(226,'helen'),(227,'eli'),(228,'eli'),(228,'lige'),(229,'life'),(230,'lisa'),(231,'eli'),(231,'ellis'),(231,'lish'),(232,'elizabeth'),(233,'bess'),(233,'bessie'),(233,'beth'),(233,'bethia'),(233,'betsy'),(233,'bette'),(233,'betty'),(233,'dicey'),(233,'elis'),(233,'elsie'),(233,'ibby'),(233,'libby'),(233,'liz'),(233,'liza'),(233,'lizabeth'),(233,'lizzie'),(233,'tess'),(234,'eleanor'),(234,'gabriella'),(234,'helen'),(234,'luella'),(235,'eleanor'),(235,'gabriella'),(235,'helen'),(235,'luella'),(236,'helen'),(236,'nell'),(236,'nellie'),(237,'ellen'),(237,'helen'),(237,'nellie'),(238,'minnie'),(239,'mira'),(240,'nora'),(241,'heloise'),(241,'louise'),(242,'alice'),(242,'elizabeth'),(243,'ells'),(243,'elly'),(244,'elvie'),(245,'lisa'),(246,'manny'),(246,'manuel'),(247,'emily'),(247,'emmer'),(247,'emmy'),(247,'lina'),(247,'millie'),(248,'emily'),(249,'emma'),(249,'emmie'),(249,'erma'),(250,'eph'),(251,'rasmus'),(251,'raze'),(252,'erica'),(252,'rick'),(252,'ricky'),(253,'ernestine'),(253,'ernie'),(254,'ernestine'),(254,'ernie'),(255,'erna'),(255,'ernest'),(255,'teeny'),(255,'tina'),(256,'irwin'),(257,'es'),(258,'senie'),(259,'essy'),(259,'stella'),(260,'essie'),(260,'hester'),(261,'dicey'),(262,'dora'),(263,'dosie'),(263,'dossie'),(264,'eugenia'),(264,'euy'),(264,'gene'),(264,'genie'),(264,'jenny'),(265,'nicie'),(266,'effie'),(266,'effy'),(267,'dicey'),(268,'stacia'),(268,'stacy'),(269,'ev'),(269,'evan'),(269,'vangie'),(270,'ev'),(270,'eve'),(270,'evelina'),(271,'ez'),(271,'zeke'),(272,'ez'),(273,'exie'),(274,'fay'),(275,'delia'),(275,'delius'),(276,'fel'),(276,'feli'),(276,'felix'),(277,'flick'),(277,'tick'),(278,'ferdie'),(278,'fred'),(279,'ferdie'),(279,'fred'),(279,'nando'),(280,'flo'),(280,'flora'),(280,'florrie'),(280,'floss'),(280,'flossie'),(281,'lloyd'),(282,'fan'),(282,'fanny'),(282,'fran'),(282,'france'),(282,'francis'),(282,'franie'),(282,'frankie'),(282,'franz'),(282,'sis'),(283,'frances'),(283,'frank'),(284,'frank'),(285,'derick'),(285,'fred'),(285,'freddie'),(285,'frederica'),(285,'fredric'),(285,'frish'),(285,'fritz'),(285,'rick'),(286,'frederick'),(287,'gabby'),(287,'gabe'),(287,'garbrielle'),(288,'ella'),(288,'gabbie'),(288,'gabriel'),(289,'gency'),(289,'jenny'),(289,'jinsey'),(290,'geoff'),(291,'georgiana'),(291,'jorge'),(292,'george'),(292,'georgiana'),(293,'geraldine'),(293,'gerry'),(293,'jerry'),(294,'deannie'),(294,'dina'),(294,'gerald'),(294,'gerri'),(294,'gerrie'),(294,'jerry'),(295,'gay'),(296,'gatty'),(296,'gertie'),(296,'trudy'),(297,'bert'),(297,'bertie'),(297,'gib'),(297,'gil'),(297,'wilber'),(298,'glory'),(299,'govie'),(300,'berry'),(300,'green'),(301,'margaret'),(302,'greg'),(303,'grissel'),(304,'gus'),(305,'genny'),(305,'gwen'),(305,'wendy'),(306,'ham'),(307,'anna'),(307,'hattie'),(307,'nan'),(307,'nanny'),(307,'susannah'),(308,'hetty'),(309,'dutch'),(309,'harman'),(310,'hal'),(310,'harry'),(311,'harry'),(311,'hattie'),(311,'hatty'),(312,'harold'),(312,'henry'),(313,'hassie'),(314,'aileen'),(314,'eileen'),(314,'elaine'),(314,'eleanor'),(314,'ellen'),(314,'lena'),(314,'nell'),(314,'nellie'),(315,'aileen'),(315,'eileen'),(315,'elaine'),(315,'eleanor'),(315,'ellen'),(315,'lena'),(315,'nell'),(315,'nellie'),(316,'eloise'),(316,'lois'),(317,'etta'),(317,'hank'),(317,'henry'),(317,'hetty'),(317,'nettie'),(317,'retta'),(318,'hal'),(318,'hank'),(318,'harry'),(318,'hen'),(318,'hence'),(319,'bert'),(319,'herb'),(320,'estherhessy'),(320,'hetty'),(321,'hez'),(321,'ki'),(321,'ky'),(322,'honey'),(322,'nora'),(322,'norah'),(322,'norry'),(323,'harry'),(323,'horatio'),(324,'harty'),(324,'tensey'),(325,'hosey'),(325,'hosie'),(326,'hal'),(326,'howie'),(327,'bert'),(327,'hugh'),(327,'hugo'),(328,'john'),(329,'iggy'),(329,'nace'),(330,'iggy'),(330,'nace'),(330,'naz'),(331,'emmanuel'),(331,'manuel'),(332,'indie'),(332,'indy'),(333,'agnes'),(334,'onnie'),(335,'rena'),(335,'rennie'),(336,'irving'),(337,'erwin'),(338,'ike'),(338,'zeke'),(339,'bella'),(339,'belle'),(339,'cybilla'),(339,'elizabeth'),(339,'ib'),(339,'issy'),(339,'nib'),(339,'sabe'),(339,'sabra'),(339,'sibella'),(339,'tibbie'),(340,'bella'),(340,'belle'),(340,'cybilla'),(340,'elizabeth'),(340,'ib'),(340,'issy'),(340,'nib'),(340,'sabe'),(340,'sabra'),(340,'sibella'),(340,'tibbie'),(341,'dora'),(341,'isidore'),(341,'issy'),(342,'zadie'),(342,'zay'),(343,'isadora'),(343,'izzy'),(344,'ivy'),(345,'john'),(346,'jake'),(347,'jack'),(347,'jackie'),(348,'jack'),(349,'hoda'),(349,'hodie'),(349,'hody'),(350,'jamie'),(350,'jeb'),(350,'jim'),(351,'janet'),(351,'janie'),(351,'jenny'),(351,'jessie'),(351,'jinsey'),(351,'joan'),(351,'joanna'),(352,'nettie'),(353,'casper'),(353,'jap'),(354,'jay'),(355,'jennie'),(355,'joanna'),(356,'jeanne'),(356,'nettie'),(357,'diah'),(357,'dyer'),(357,'jed'),(358,'jeff'),(359,'jeff'),(360,'gee'),(360,'hugh'),(361,'jemma'),(361,'mima'),(361,'mimi'),(362,'jenny'),(362,'jessie'),(363,'jan'),(363,'jenny'),(364,'jeremy'),(364,'jerry'),(365,'rita'),(366,'jess'),(366,'jesse'),(366,'jessie'),(366,'sica'),(367,'jane'),(368,'jane'),(369,'jane'),(369,'janet'),(369,'jess'),(370,'jane'),(370,'jean'),(370,'joan'),(370,'jody'),(370,'johanna'),(370,'john'),(371,'hans'),(371,'ian'),(371,'ivan'),(371,'jack'),(371,'jayhugh'),(371,'jean'),(371,'jehu'),(371,'jock'),(372,'johnjohnny'),(372,'jonathan'),(373,'john'),(373,'jon'),(373,'nat'),(373,'nathan'),(374,'joe'),(374,'joey'),(375,'jo'),(375,'joey'),(375,'joseie'),(375,'josey'),(376,'jettie'),(377,'josh'),(378,'joy'),(379,'nita'),(380,'jude'),(380,'juder'),(381,'juda'),(381,'jude'),(381,'judi'),(381,'judie'),(381,'judy'),(382,'jill'),(382,'jule'),(382,'julian'),(382,'julie'),(382,'juliet'),(382,'julius'),(383,'junius'),(384,'justina'),(384,'justus'),(385,'carrie'),(385,'happy'),(385,'karen'),(385,'karon'),(386,'catherine'),(386,'tina'),(387,'cathy'),(387,'karen'),(387,'katharine'),(387,'kathleen'),(387,'katie'),(387,'kay'),(387,'kit'),(387,'kittie'),(388,'kay'),(389,'kay'),(389,'kenj'),(389,'kenji'),(389,'kenny'),(390,'kezzie'),(390,'kezzy'),(390,'kid'),(390,'kizzy'),(391,'kris'),(392,'kissy'),(392,'kris'),(392,'krissy'),(393,'chris'),(393,'kris'),(394,'fate'),(394,'fayette'),(394,'leffie'),(394,'leffy'),(394,'left'),(395,'cenia'),(395,'dicy'),(396,'laurie'),(396,'ren'),(397,'laura'),(397,'lawrence'),(398,'laurie'),(399,'veda'),(400,'verna'),(400,'vernon'),(401,'vina'),(401,'viney'),(401,'vonnie'),(401,'wyncha'),(402,'vina'),(402,'viney'),(402,'vonnie'),(402,'wyncha'),(403,'vina'),(403,'viney'),(403,'vonnie'),(403,'wyncha'),(404,'larry'),(404,'lars'),(404,'laura'),(404,'laurence'),(404,'lawrie'),(404,'lon'),(404,'lorry'),(405,'annie'),(405,'lea'),(406,'curg'),(407,'lem'),(408,'leenlina'),(409,'leo'),(409,'leon'),(409,'leona'),(410,'lee'),(410,'leon'),(411,'elenor'),(411,'honor'),(411,'nora'),(412,'elenor'),(412,'honor'),(412,'nora'),(413,'lee'),(413,'roy'),(414,'les'),(414,'lester'),(415,'lettice'),(415,'lettie'),(415,'tish'),(415,'titia'),(416,'vicy'),(417,'von'),(418,'von'),(419,'lil'),(419,'lila'),(419,'lilly'),(419,'lolly'),(419,'odie'),(420,'link'),(421,'leon'),(422,'berry'),(422,'l.b.'),(422,'little'),(423,'heloise'),(423,'louise'),(424,'etta'),(424,'laura'),(424,'lorrie'),(424,'retta'),(425,'lorrie'),(426,'lewis'),(426,'lou'),(426,'louie'),(426,'louise'),(427,'eliza'),(427,'eloise'),(427,'issie'),(427,'lois'),(427,'lou'),(427,'louis'),(427,'lulu'),(428,'lucius'),(428,'lucy'),(429,'lucas'),(429,'luke'),(430,'ceall'),(430,'cille'),(430,'lucy'),(431,'sinah'),(432,'cindy'),(432,'lucy'),(433,'creasey'),(434,'ella'),(435,'nettie'),(436,'lura'),(437,'amabel'),(437,'mehitabel'),(438,'mc'),(439,'mac'),(439,'mc'),(440,'kenzy'),(440,'mac'),(440,'mack'),(441,'lena'),(441,'maddie'),(441,'madge'),(441,'maggie'),(441,'maud'),(441,'middy'),(442,'middy'),(443,'maddy'),(443,'mattie'),(444,'lena'),(444,'maggie'),(445,'haley'),(445,'huldah'),(446,'mally'),(447,'mac'),(447,'mal'),(447,'malc'),(448,'lindy'),(449,'eve'),(449,'minerva'),(449,'nerva'),(449,'nervie'),(450,'noah'),(451,'nonnie'),(452,'emanuel'),(452,'manny'),(453,'marcia'),(453,'mark'),(454,'daisy'),(454,'greta'),(454,'madge'),(454,'maggie'),(454,'maisie'),(454,'marge'),(454,'margo'),(454,'meg'),(454,'megan'),(454,'metta'),(454,'midge'),(454,'peggie'),(455,'daisy'),(455,'greta'),(455,'madge'),(455,'maggie'),(455,'maisie'),(455,'marge'),(455,'margo'),(455,'meg'),(455,'megan'),(455,'metta'),(455,'midge'),(455,'peggie'),(455,'rita'),(456,'maria'),(456,'mary'),(457,'mae'),(458,'mary'),(459,'marianna'),(459,'marion'),(460,'mary'),(461,'rissa'),(462,'madge'),(462,'marge'),(462,'margie'),(463,'marcie'),(463,'mary'),(464,'marnie'),(464,'mart'),(464,'marty'),(464,'mat'),(464,'mattie'),(464,'patsy'),(464,'patty'),(465,'tine'),(466,'marv'),(466,'merv'),(466,'mervyn'),(467,'mae'),(467,'mamie'),(467,'maria'),(467,'mariah'),(467,'marie'),(468,'mae'),(468,'mamie'),(468,'maria'),(468,'mariah'),(468,'marie'),(468,'marion'),(468,'mary'),(468,'maureen'),(468,'may'),(468,'mercy'),(468,'minnie'),(468,'mitzi'),(468,'mollie'),(468,'molly'),(468,'polly'),(469,'matt'),(469,'matthias'),(470,'patty'),(470,'tillie'),(471,'mat'),(471,'matty'),(471,'maud'),(471,'tilda'),(471,'tillie'),(472,'peggy'),(473,'mary'),(474,'maury'),(474,'morris'),(474,'mossie'),(475,'mave'),(476,'mave'),(477,'max'),(478,'mae'),(479,'ken'),(479,'kenna'),(479,'meaka'),(480,'dora'),(481,'meg'),(482,'hetty'),(482,'mabel'),(482,'mitty'),(483,'mellie'),(484,'dick'),(484,'zadock'),(485,'linda'),(485,'lindy'),(485,'mel'),(486,'alyssa'),(486,'lisa'),(486,'mel'),(486,'melissa'),(486,'milly'),(486,'missa'),(486,'missy'),(487,'mellia'),(488,'lodi'),(489,'mel'),(490,'vina'),(491,'merci'),(491,'mercy'),(491,'sadie'),(492,'cage'),(493,'mickey'),(493,'mike'),(493,'mitchell'),(494,'mickey'),(494,'shelly'),(495,'mell'),(495,'milly'),(495,'mimi'),(496,'milly'),(497,'mina'),(497,'minnie'),(497,'nerva'),(497,'nervie'),(498,'mandy'),(498,'mari'),(498,'mira'),(498,'randy'),(499,'mary'),(499,'mitzi'),(500,'michael'),(500,'mitch'),(501,'mary'),(502,'nettie'),(503,'monna'),(503,'monnie'),(504,'monte'),(505,'monty'),(506,'gum'),(506,'monty'),(507,'mort'),(508,'amos'),(508,'mose'),(508,'moss'),(509,'mur'),(510,'mert'),(510,'myrt'),(510,'myrti'),(511,'deedee'),(511,'nada'),(512,'alsoamalename'),(513,'agnes'),(513,'ann'),(513,'nan'),(513,'nance'),(513,'nannie'),(514,'omi'),(515,'leon'),(515,'nap'),(515,'poley'),(515,'pony'),(516,'nattie'),(516,'nettie'),(517,'nat'),(517,'tasha'),(518,'jonathan'),(518,'nat'),(518,'nate'),(518,'nathan'),(518,'natty'),(518,'tan'),(519,'nels'),(520,'nick'),(520,'nicky'),(521,'nick'),(522,'cole'),(522,'nikki'),(522,'nole'),(523,'nonie'),(524,'noel'),(525,'diah'),(525,'dyer'),(525,'obe'),(525,'obed'),(525,'obie'),(526,'beda'),(526,'beedy'),(526,'biddie'),(526,'obed'),(527,'tave'),(527,'tavia'),(528,'odo'),(529,'ollie'),(530,'livia'),(530,'olive'),(530,'oliver'),(531,'ollie'),(532,'cy'),(532,'cyphorus'),(532,'one'),(532,'osaforum'),(532,'osaforus'),(532,'syphorous'),(533,'ora'),(533,'rilly'),(534,'roland'),(535,'phelia'),(536,'ossy'),(536,'waldo'),(537,'ode'),(537,'ote'),(538,'pam'),(539,'dora'),(540,'parsuny'),(540,'pasoonie'),(540,'phenie'),(540,'teeny'),(541,'pat'),(541,'patty'),(542,'pat'),(542,'patrick'),(542,'patsy'),(542,'patty'),(542,'tricia'),(542,'trish'),(542,'trixie'),(543,'paddy'),(543,'pat'),(543,'patricia'),(543,'patsy'),(543,'pete'),(543,'peter'),(544,'paula'),(544,'pauline'),(544,'polly'),(545,'polly'),(546,'neppie'),(546,'penny'),(547,'perce'),(547,'percy'),(548,'perry'),(549,'mellie'),(549,'melly'),(549,'milly'),(550,'nettie'),(551,'seph'),(551,'sephy'),(552,'nellie'),(553,'ferbie'),(553,'pherbia'),(554,'josephine'),(555,'filip'),(555,'phil'),(555,'philippa'),(555,'phyllis'),(555,'pip'),(556,'delphia'),(557,'fie'),(558,'penie'),(558,'phoebe'),(559,'menaalmena'),(560,'fifi'),(561,'pink'),(562,'ples'),(563,'pokey'),(564,'humey'),(565,'pres'),(565,'scott'),(566,'cil'),(566,'cilla'),(566,'ciller'),(566,'prissy'),(566,'siller'),(567,'provy'),(568,'densy'),(568,'prudy'),(569,'rae'),(569,'raech'),(569,'ray'),(570,'dolph'),(570,'rafe'),(570,'randall'),(570,'randy'),(571,'raff'),(572,'mona'),(573,'ray'),(574,'becca'),(574,'beck'),(574,'beckie'),(574,'becky'),(574,'reba'),(575,'gina'),(575,'ray'),(576,'reg'),(576,'reggie'),(576,'rex'),(576,'reynold'),(577,'rube'),(577,'ruby'),(578,'reginald'),(579,'rodie'),(580,'della'),(581,'rhynie'),(582,'dick'),(582,'richie'),(582,'rick'),(582,'ritchie'),(583,'bob'),(583,'bobby'),(583,'dob'),(583,'dobbin'),(583,'rob'),(583,'roberta'),(583,'robin'),(583,'rupert'),(584,'bert'),(584,'bobbie'),(584,'robbie'),(584,'robert'),(585,'erick'),(585,'rickie'),(585,'rod'),(586,'hodge'),(586,'hodgekin'),(587,'orlando'),(587,'rowland'),(588,'ron'),(588,'ronnie'),(589,'ross'),(590,'sina'),(591,'rox'),(591,'roxie'),(592,'dolph'),(592,'rolf'),(592,'rollo'),(592,'rudy'),(593,'russ'),(594,'ry'),(595,'bri'),(595,'brina'),(595,'sabby'),(595,'sabra'),(596,'loomie'),(597,'sal'),(598,'mantha'),(598,'sam'),(598,'sammy'),(599,'sam'),(600,'sam'),(601,'sam'),(601,'sonny'),(602,'myra'),(603,'alexandra'),(603,'sandy'),(604,'sandy'),(605,'cera'),(605,'sadie'),(605,'sal'),(605,'sallie'),(605,'sara'),(605,'sukie'),(605,'surry'),(606,'silla'),(607,'rena'),(608,'anna'),(608,'vannie'),(609,'sceeter'),(609,'scottie'),(609,'scotty'),(609,'squat'),(610,'sebby'),(611,'anselm'),(612,'rena'),(613,'rilla'),(614,'sha'),(614,'shay'),(615,'sha'),(615,'shay'),(616,'cecilia'),(617,'shelly'),(618,'dan'),(618,'danny'),(619,'sid'),(620,'sibbell'),(620,'sibbie'),(620,'sybill'),(621,'sid'),(622,'sid'),(623,'sig'),(624,'si'),(625,'liley'),(626,'si'),(626,'sly'),(626,'syl'),(626,'vest'),(626,'vester'),(627,'sim'),(627,'simon'),(628,'crate'),(629,'sal'),(629,'salmon'),(629,'sol'),(629,'solly'),(629,'zolly'),(630,'dre'),(630,'sonnie'),(631,'frona'),(631,'fronia'),(631,'sophia'),(632,'annie'),(632,'steph'),(632,'stephen'),(632,'stephie'),(633,'step'),(633,'steve'),(633,'steven'),(633,'stevie'),(634,'mitty'),(635,'sully'),(636,'hannah'),(636,'sudy'),(636,'sue'),(636,'sukey'),(636,'susan'),(636,'susie'),(636,'suzanne'),(637,'sue'),(637,'suki'),(637,'susie'),(638,'sibbie'),(639,'sid'),(640,'sly'),(640,'syl'),(641,'si'),(641,'sly'),(641,'syl'),(641,'vest'),(641,'vester'),(642,'tabby'),(643,'tammy'),(644,'tanny'),(645,'tash'),(645,'tashie'),(646,'tempy'),(647,'terry'),(648,'terry'),(648,'tess'),(648,'tessie'),(648,'tyrza'),(649,'tad'),(649,'thad'),(650,'dora'),(651,'dorey'),(651,'ted'),(651,'theodora'),(651,'theotric'),(652,'dosia'),(652,'theo'),(652,'theodosius'),(653,'ophi'),(654,'otha'),(655,'terry'),(655,'tess'),(655,'tessie'),(655,'thursa'),(655,'ticy'),(655,'tracy'),(655,'trissy'),(656,'thom'),(656,'tom'),(657,'tamzine'),(658,'tiff'),(658,'tiffy'),(659,'tillie'),(660,'tim'),(661,'bias'),(661,'tobe'),(661,'toby'),(662,'quilla'),(662,'trannie'),(663,'eunice'),(663,'nicie'),(664,'ury'),(665,'sula'),(665,'sulie'),(666,'felty'),(666,'val'),(666,'vallie'),(667,'felty'),(667,'val'),(667,'vallie'),(668,'val'),(669,'buren'),(670,'vannie'),(671,'nessa'),(671,'van'),(671,'vannie'),(672,'nicey'),(673,'franky'),(673,'ronna'),(673,'ronnie'),(673,'vonnie'),(674,'vic'),(674,'vick'),(675,'toria'),(675,'torrie'),(675,'tory'),(675,'vicki'),(675,'victor'),(676,'vin'),(676,'vince'),(676,'vinnie'),(676,'vinny'),(677,'ola'),(677,'vi'),(678,'lettie'),(679,'ginger'),(679,'ginny'),(679,'jane'),(679,'jennie'),(679,'jenny'),(679,'jinie'),(679,'virgie'),(680,'vi'),(680,'viv'),(681,'oswald'),(682,'wallie'),(682,'wally'),(683,'wat'),(684,'webb'),(685,'wen'),(686,'wib'),(687,'fred'),(687,'willie'),(688,'billie'),(688,'helmie'),(688,'mina'),(688,'minnie'),(688,'wilhelm'),(688,'william'),(688,'willie'),(688,'wilma'),(689,'bill'),(689,'bud'),(689,'will'),(689,'willie'),(690,'bill'),(690,'willy'),(691,'willie'),(692,'billiewilhelm'),(692,'william'),(693,'field'),(693,'win'),(693,'winny'),(694,'freddie'),(694,'winnet'),(694,'winnie'),(695,'wint'),(696,'woody'),(697,'ona'),(697,'onie'),(698,'lan'),(698,'yul'),(699,'vonna'),(700,'zach'),(700,'zacharias'),(700,'zachary'),(700,'zeke'),(701,'zed');
/*!40000 ALTER TABLE `nicknames` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2015-03-02 22:00:52
