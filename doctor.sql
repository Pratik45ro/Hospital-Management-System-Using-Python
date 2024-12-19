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
-- Table structure for table `doctor`
--

DROP TABLE IF EXISTS `doctor`;
CREATE TABLE IF NOT EXISTS `doctor` (
  `doc_id` int NOT NULL,
  `doc_pass` varchar(10) NOT NULL,
  `doc_name` varchar(50) DEFAULT NULL,
  `doc_specialist` varchar(50) DEFAULT NULL,
  `doc_exp` varchar(50) DEFAULT NULL,
  `doc_time` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`doc_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `doctor`
--

INSERT INTO `doctor` (`doc_id`, `doc_pass`, `doc_name`, `doc_specialist`, `doc_exp`, `doc_time`) VALUES
(101, 'Doc1', 'Vijay', 'Dentist', '20 Years', '10:00 AM to 04:00 PM'),
(102, 'Doc2', 'Ajay', 'Medicine', '10 Years', '10:00 AM to 01:00 PM'),
(103, 'Doc3', 'Karan', 'Orthopedic', '10 Years', '04:00 PM - 09:00 PM');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
