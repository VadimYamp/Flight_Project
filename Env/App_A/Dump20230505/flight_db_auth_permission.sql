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
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=101 DEFAULT CHARSET=hebrew;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (37,'Can add log entry',10,'add_logentry'),(38,'Can change log entry',10,'change_logentry'),(39,'Can delete log entry',10,'delete_logentry'),(40,'Can view log entry',10,'view_logentry'),(41,'Can add permission',11,'add_permission'),(42,'Can change permission',11,'change_permission'),(43,'Can delete permission',11,'delete_permission'),(44,'Can view permission',11,'view_permission'),(45,'Can add group',12,'add_group'),(46,'Can change group',12,'change_group'),(47,'Can delete group',12,'delete_group'),(48,'Can view group',12,'view_group'),(49,'Can add user',13,'add_user'),(50,'Can change user',13,'change_user'),(51,'Can delete user',13,'delete_user'),(52,'Can view user',13,'view_user'),(53,'Can add content type',14,'add_contenttype'),(54,'Can change content type',14,'change_contenttype'),(55,'Can delete content type',14,'delete_contenttype'),(56,'Can view content type',14,'view_contenttype'),(57,'Can add session',15,'add_session'),(58,'Can change session',15,'change_session'),(59,'Can delete session',15,'delete_session'),(60,'Can view session',15,'view_session'),(61,'Can add n5_ user_ roles',16,'add_n5_user_roles'),(62,'Can change n5_ user_ roles',16,'change_n5_user_roles'),(63,'Can delete n5_ user_ roles',16,'delete_n5_user_roles'),(64,'Can view n5_ user_ roles',16,'view_n5_user_roles'),(65,'Can add n7_ flights',17,'add_n7_flights'),(66,'Can change n7_ flights',17,'change_n7_flights'),(67,'Can delete n7_ flights',17,'delete_n7_flights'),(68,'Can view n7_ flights',17,'view_n7_flights'),(69,'Can add n3_ airline_ companies',18,'add_n3_airline_companies'),(70,'Can change n3_ airline_ companies',18,'change_n3_airline_companies'),(71,'Can delete n3_ airline_ companies',18,'delete_n3_airline_companies'),(72,'Can view n3_ airline_ companies',18,'view_n3_airline_companies'),(73,'Can add n8_ tickets',19,'add_n8_tickets'),(74,'Can change n8_ tickets',19,'change_n8_tickets'),(75,'Can delete n8_ tickets',19,'delete_n8_tickets'),(76,'Can view n8_ tickets',19,'view_n8_tickets'),(77,'Can add n2_ customers',20,'add_n2_customers'),(78,'Can change n2_ customers',20,'change_n2_customers'),(79,'Can delete n2_ customers',20,'delete_n2_customers'),(80,'Can view n2_ customers',20,'view_n2_customers'),(81,'Can add n6_ countries',21,'add_n6_countries'),(82,'Can change n6_ countries',21,'change_n6_countries'),(83,'Can delete n6_ countries',21,'delete_n6_countries'),(84,'Can view n6_ countries',21,'view_n6_countries'),(85,'Can add n1_ users',22,'add_n1_users'),(86,'Can change n1_ users',22,'change_n1_users'),(87,'Can delete n1_ users',22,'delete_n1_users'),(88,'Can view n1_ users',22,'view_n1_users'),(89,'Can add n4_ administrators',23,'add_n4_administrators'),(90,'Can change n4_ administrators',23,'change_n4_administrators'),(91,'Can delete n4_ administrators',23,'delete_n4_administrators'),(92,'Can view n4_ administrators',23,'view_n4_administrators'),(93,'Can add Token',24,'add_token'),(94,'Can change Token',24,'change_token'),(95,'Can delete Token',24,'delete_token'),(96,'Can view Token',24,'view_token'),(97,'Can add token',25,'add_tokenproxy'),(98,'Can change token',25,'change_tokenproxy'),(99,'Can delete token',25,'delete_tokenproxy'),(100,'Can view token',25,'view_tokenproxy');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
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
