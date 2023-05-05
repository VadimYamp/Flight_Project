-- MySQL dump 10.13  Distrib 8.0.31, for Win64 (x86_64)
--
-- Host: localhost    Database: flight_db
-- ------------------------------------------------------
-- Server version	8.0.31

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `app_a_n6_countries`
--

DROP TABLE IF EXISTS `app_a_n6_countries`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `app_a_n6_countries` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `Name` varchar(30) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=38 DEFAULT CHARSET=hebrew;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app_a_n6_countries`
--

LOCK TABLES `app_a_n6_countries` WRITE;
/*!40000 ALTER TABLE `app_a_n6_countries` DISABLE KEYS */;
INSERT INTO `app_a_n6_countries` VALUES (1,'ישראל'),(2,'רוסיה'),(3,'אוקראינה'),(4,'ארצות-הברית'),(5,'קנדה'),(6,'ברזיל'),(7,'ארגנטינה'),(8,'לבנון'),(9,'סוריה'),(10,'איראן'),(11,'ירדן'),(12,'ערב הסעודית'),(13,'צ\'כיה'),(14,'בולגריה'),(15,'הונגריה'),(16,'אוסטרליה'),(17,'גרמניה'),(18,'בלגיה'),(19,'איטליה'),(20,'טורקיה'),(21,'צרפת'),(22,'ספרד'),(23,'שוויץ'),(24,'ליטא'),(25,'פולין'),(26,'נורבגיה'),(27,'שוודיה'),(28,'מקסיקו'),(29,'מרוקו'),(30,'טוניס'),(31,'הודו'),(32,'יפן'),(33,'סין'),(34,'קוריאה'),(35,'יוון'),(36,'מצרים'),(37,'קפריסין');
/*!40000 ALTER TABLE `app_a_n6_countries` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-05-05 12:15:14
