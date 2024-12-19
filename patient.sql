-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Mar 22, 2024 at 06:23 AM
-- Server version: 8.2.0
-- PHP Version: 8.2.13

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `clinic`
--

-- --------------------------------------------------------

--
-- Table structure for table `patient`
--

DROP TABLE IF EXISTS `patient`;
CREATE TABLE IF NOT EXISTS `patient` (
  `pat_id` int NOT NULL,
  `pat_pass` varchar(10) NOT NULL,
  `pat_name` varchar(50) DEFAULT NULL,
  `pat_email` varchar(50) DEFAULT NULL,
  `pat_contact` int DEFAULT NULL,
  `pat_height` varchar(10) DEFAULT NULL,
  `pat_weight` varchar(10) DEFAULT NULL,
  `pat_bg` varchar(10) DEFAULT NULL,
  `pat_add` varchar(50) DEFAULT NULL,
  `pat_dob` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`pat_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `patient`
--

INSERT INTO `patient` (`pat_id`, `pat_pass`, `pat_name`, `pat_email`, `pat_contact`, `pat_height`, `pat_weight`, `pat_bg`, `pat_add`, `pat_dob`) VALUES
(301, 'Pat1', 'Arjun', 'arjun121@gmail.com', 2147483647, '5.3 Feet', '60 Kg', 'O Positive', 'Bandra', '19 April 2004'),
(302, 'Pat2', 'Ramesh', 'ramesh23@gmail.com', 2147483647, '5.0 Feet', '67.3 Kg', 'A Positive', 'Lalbaug', '23 May 2000'),
(303, 'Pat3', 'Suresh', 'Suresh02@gmail.com', 2147483647, '6.0 Feet', '80 Kg', 'B Positive', 'Currey Road', '02 January 1996');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
