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
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=hebrew;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('1f2q9fz0zfrd1ggr16ijvqgzu0k92voi','e30:1pud2L:17pE6yRd2NxFwq7Rgg5Dm1Ywdn6j_Nz9zRrl71FVQLc','2023-05-18 17:46:37.952511'),('6il0bqo26d29ra2mgzb88vrhwtcm1jvj','.eJyrVsqtjM9PylKyUoqujlHKzU9JzYlRslKIUXIsKIh31MszjC8tTi0qjlHSAYoVZIPkDEHMtMzUnJRiEBeozS8xNxWiKzgjsTTHNzEnOxGiIyCxuLg8vygFImtgYAhBEEnX3MTMHGR9DukgEb3k_FyIgqD8HLC5hrW1sUo6SiCXDAGH1gIAeUpnVg:1prgqO:_7pIy9kIEaNpOWlfNer4XcZuOIuJa-eCKsMPji2adaA','2023-05-10 15:14:08.748659'),('84mvczs3dk1j9zwug07hc447zqvbf8ua','.eJyrViotTi1SslKKro5Rys1PSc2JUbJSiFFyLCiId9TLM4wHSRfHKOkAxQqyQXJGIGZaZmpOSjGIC9Tml5ibCtHlkliWmRKcUZZYVALVE5BYXFyeX5QCkTcwMIIgiKRrbmJmDrJOh3SQiF5yfi5EQVB-Dthkw9raWKVaAPO5NJY:1ptXFw:8HuZh88CUMDgENLawy7K86mt6gzsY_PMi5uy9Pc-9E4','2023-05-15 17:24:08.230557'),('8quugedjear8g51cvyufyajhzv178z2l','e30:1pubFk:PqmgMHHiKuHq-_E6dU1qmKvTKkmc_iGJ5DVZvorZs0w','2023-05-18 15:52:20.500204'),('cq441ihwfnrxqkk9xbdqlo8oz4zz8gik','.eJxVjDsOwjAQBe_iGlnr_4aSnjNY3tiLA8iR4qRC3B0ipYD2zcx7iZi2tcatlyVOWZyFEqffjdL4KG0H-Z7abZbj3NZlIrkr8qBdXudcnpfD_TuoqddvzYOzNpHRxYEJGrMyzIDeF3KmeEB2BhJkFbTDEBAHogDeMTKaYJV4fwDAVjab:1pmCRJ:kGcRQeavU_EqQZYyYHjQODJ-aqlo1_osjkOcXodu1do','2023-04-25 11:45:33.964666'),('jbbd5yjqmm8z6iv8awv9kleeed8i63q4','.eJxVjDsOwjAQBe_iGlnr_4aSnjNY3tiLA8iR4qRC3B0ipYD2zcx7iZi2tcatlyVOWZyFEqffjdL4KG0H-Z7abZbj3NZlIrkr8qBdXudcnpfD_TuoqddvzYOzNpHRxYEJGrMyzIDeF3KmeEB2BhJkFbTDEBAHogDeMTKaYJV4fwDAVjab:1pefX0:zM3pbNJQB1qPm3mCcPrPTavSiWrpzadNhWh_Tu_tijg','2023-04-04 17:12:18.210540'),('kmzz621a3p8bixorqw3docv44rj2neaw','.eJxVjDsOwjAQBe_iGlnr_4aSnjNY3tiLA8iR4qRC3B0ipYD2zcx7iZi2tcatlyVOWZyFEqffjdL4KG0H-Z7abZbj3NZlIrkr8qBdXudcnpfD_TuoqddvzYOzNpHRxYEJGrMyzIDeF3KmeEB2BhJkFbTDEBAHogDeMTKaYJV4fwDAVjab:1pj10c:BLG4Boj-x2BIWfh0q5TPQGaZlJ3otfLdEJCku4JgLGQ','2023-04-16 16:56:50.765267'),('kqlnqi1zt91zdo7zje15tnoaw99ckfx7','.eJyrViotTi1SslKKro5Rys1PSc2JUbJSiFFyLCiId9TLM4wHSRfHKOkAxQqyQXKGIGZaZmpOSjGIC9Tml5ibCtEVnJFYmuObmJOdCNERkFhcXJ5flAKRNTAwhCCIpGtuYmYOsj6HdJCIXnJ-LkRBUH4O2FzD2tpYJR2l3Mr4_KSsIeDUWgBfqWdW:1prLhY:EnPN-29us4wZrlc72gQ7uFOMkiIs01BAfMo3bntyBuw','2023-05-09 16:39:36.156422'),('st331dphryyb8ilteefoivxuscicdtpp','e30:1psN0Q:gse3B3xUVVkhMepZF4Gpd2YgF1qpjVPEIZjzqu7ApWc','2023-05-12 12:15:18.606037'),('uhfvxpt70ko3doqswdfxwzjwbvx4dc5d','.eJxVjMsOwiAQRf-FtSG8JgWX7v0GMjOAVA0kpV0Z_12bdKHbe865LxFxW2vcRl7inMRZGHH63Qj5kdsO0h3brUvubV1mkrsiDzrktaf8vBzu30HFUb81AXqySQcHjidrYfLKGmSNwbDzCogDBlWSKRSCI2a0TnkLqIsHDeL9AdJ8N2k:1ppCHp:pNLU2ZERCF1eErf4N9VafOKSm11zM7T772jGKWNCaPo','2023-05-03 18:12:09.705829');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
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
