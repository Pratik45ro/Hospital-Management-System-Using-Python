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
-- Table structure for table `appointment`
--

DROP TABLE IF EXISTS `appointment`;
CREATE TABLE IF NOT EXISTS `appointment` (
  `Patient_name` varchar(20) DEFAULT NULL,
  `Patient_id` int DEFAULT NULL,
  `Doctor_name` varchar(20) DEFAULT NULL,
  `Doctor_ID` int DEFAULT NULL,
  `Doctor_specialist` varchar(20) DEFAULT NULL,
  `Doctor_experience` varchar(20) DEFAULT NULL,
  `Doctor_Timing` varchar(20) DEFAULT NULL,
  `Appointment_id` int NOT NULL,
  PRIMARY KEY (`Appointment_id`),
  KEY `Patient_id` (`Patient_id`),
  KEY `Doctor_ID` (`Doctor_ID`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `appointment`
--

INSERT INTO `appointment` (`Patient_name`, `Patient_id`, `Doctor_name`, `Doctor_ID`, `Doctor_specialist`, `Doctor_experience`, `Doctor_Timing`, `Appointment_id`) VALUES
('Ramesh', 302, 'Karan', 103, 'Orthopedic', '10 Years', '04:00 PM - 05:00 PM', 501);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
