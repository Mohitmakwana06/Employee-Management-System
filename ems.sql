-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 21, 2024 at 05:01 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `ems`
--

-- --------------------------------------------------------

--
-- Table structure for table `emp_salary`
--

CREATE TABLE `emp_salary` (
  `e_code` int(11) NOT NULL,
  `designation` text NOT NULL,
  `name` text NOT NULL,
  `age` text NOT NULL,
  `gender` text NOT NULL,
  `email` text NOT NULL,
  `hr_location` text NOT NULL,
  `doj` date NOT NULL,
  `dob` date NOT NULL,
  `experience` text NOT NULL,
  `proof_id` text NOT NULL,
  `contact_no` text NOT NULL,
  `status` text NOT NULL,
  `address` text NOT NULL,
  `month` text NOT NULL,
  `year` text NOT NULL,
  `basic_salary` int(11) NOT NULL,
  `total_days` int(11) NOT NULL,
  `absent_days` int(11) NOT NULL,
  `medical` int(11) NOT NULL,
  `pf` int(11) NOT NULL,
  `convence` int(11) NOT NULL,
  `net_salary` text NOT NULL,
  `salary_receipt` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `emp_salary`
--
ALTER TABLE `emp_salary`
  ADD PRIMARY KEY (`e_code`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `emp_salary`
--
ALTER TABLE `emp_salary`
  MODIFY `e_code` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=102;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
