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
-- Table structure for table `app_a_n7_flights`
--

DROP TABLE IF EXISTS `app_a_n7_flights`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `app_a_n7_flights` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `Begin_DateTime` datetime(6) NOT NULL,
  `End_DateTime` datetime(6) NOT NULL,
  `Q_Tickets` int NOT NULL,
  `Company_id` bigint NOT NULL,
  `Dest_id` bigint NOT NULL,
  `Origin_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `App_A_n7_flights_Company_id_a28df8f1_fk_App_A_n3_` (`Company_id`),
  KEY `App_A_n7_flights_Dest_id_a20fa18d_fk_App_A_n6_countries_id` (`Dest_id`),
  KEY `App_A_n7_flights_Origin_id_66fb800f_fk_App_A_n6_countries_id` (`Origin_id`),
  CONSTRAINT `App_A_n7_flights_Company_id_a28df8f1_fk_App_A_n3_` FOREIGN KEY (`Company_id`) REFERENCES `app_a_n3_airline_companies` (`id`),
  CONSTRAINT `App_A_n7_flights_Dest_id_a20fa18d_fk_App_A_n6_countries_id` FOREIGN KEY (`Dest_id`) REFERENCES `app_a_n6_countries` (`id`),
  CONSTRAINT `App_A_n7_flights_Origin_id_66fb800f_fk_App_A_n6_countries_id` FOREIGN KEY (`Origin_id`) REFERENCES `app_a_n6_countries` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=hebrew;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app_a_n7_flights`
--

LOCK TABLES `app_a_n7_flights` WRITE;
/*!40000 ALTER TABLE `app_a_n7_flights` DISABLE KEYS */;
INSERT INTO `app_a_n7_flights` VALUES (1,'2023-09-01 06:00:00.000000','2023-09-01 09:00:00.000000',300,1,3,1),(2,'2023-09-08 14:00:00.000000','2023-09-08 17:00:00.000000',300,1,1,3);
/*!40000 ALTER TABLE `app_a_n7_flights` ENABLE KEYS */;
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
