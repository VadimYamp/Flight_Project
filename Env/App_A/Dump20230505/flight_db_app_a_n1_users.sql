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
-- Table structure for table `app_a_n1_users`
--

DROP TABLE IF EXISTS `app_a_n1_users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `app_a_n1_users` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `Name` varchar(30) NOT NULL,
  `Password` varchar(30) NOT NULL,
  `Email` varchar(30) NOT NULL,
  `Role_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `App_A_n1_users_Role_id_0bd29c2e_fk_App_A_n5_user_roles_id` (`Role_id`),
  CONSTRAINT `App_A_n1_users_Role_id_0bd29c2e_fk_App_A_n5_user_roles_id` FOREIGN KEY (`Role_id`) REFERENCES `app_a_n5_user_roles` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=35 DEFAULT CHARSET=hebrew;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app_a_n1_users`
--

LOCK TABLES `app_a_n1_users` WRITE;
/*!40000 ALTER TABLE `app_a_n1_users` DISABLE KEYS */;
INSERT INTO `app_a_n1_users` VALUES (1,'ShaulMalka','001001001','ShaulM@gmail.com',1),(2,'DavidShvarts','002002002','DavidS@gmail.com',1),(3,'Elal','003003003','Elal@gmail.com',2),(4,'Eurofloat','004004004','Eurofloat@gmail.com',2),(5,'Boing','005005005','Boing@gmail.com',2),(6,'MosheAzulay','006006006','MosheA@gmail.com',3),(7,'AharonCohen','007007007','AharonC@gmail.com',3);
/*!40000 ALTER TABLE `app_a_n1_users` ENABLE KEYS */;
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
