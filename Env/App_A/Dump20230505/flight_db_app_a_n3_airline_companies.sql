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
-- Table structure for table `app_a_n3_airline_companies`
--

DROP TABLE IF EXISTS `app_a_n3_airline_companies`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `app_a_n3_airline_companies` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `Name` varchar(30) NOT NULL,
  `Country_id` bigint NOT NULL,
  `User_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `App_A_n3_airline_com_Country_id_b4506a10_fk_App_A_n6_` (`Country_id`),
  KEY `App_A_n3_airline_companies_User_id_c3b17495_fk_App_A_n1_users_id` (`User_id`),
  CONSTRAINT `App_A_n3_airline_com_Country_id_b4506a10_fk_App_A_n6_` FOREIGN KEY (`Country_id`) REFERENCES `app_a_n6_countries` (`id`),
  CONSTRAINT `App_A_n3_airline_companies_User_id_c3b17495_fk_App_A_n1_users_id` FOREIGN KEY (`User_id`) REFERENCES `app_a_n1_users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=hebrew;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app_a_n3_airline_companies`
--

LOCK TABLES `app_a_n3_airline_companies` WRITE;
/*!40000 ALTER TABLE `app_a_n3_airline_companies` DISABLE KEYS */;
INSERT INTO `app_a_n3_airline_companies` VALUES (1,'אלעל',1,3),(2,'Earoflot',2,4),(3,'Boing',4,5);
/*!40000 ALTER TABLE `app_a_n3_airline_companies` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-05-05 12:15:15
