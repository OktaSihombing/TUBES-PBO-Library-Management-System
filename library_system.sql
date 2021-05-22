-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Waktu pembuatan: 22 Bulan Mei 2021 pada 13.00
-- Versi server: 10.1.38-MariaDB
-- Versi PHP: 7.3.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `library_system`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `admin`
--

CREATE TABLE `admin` (
  `Admin_ID` int(10) NOT NULL,
  `Name` varchar(50) DEFAULT NULL,
  `Username` varchar(20) DEFAULT NULL,
  `password` varchar(20) DEFAULT NULL,
  `Address` varchar(50) DEFAULT NULL,
  `Phone` int(20) DEFAULT NULL,
  `Email` varchar(30) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data untuk tabel `admin`
--

INSERT INTO `admin` (`Admin_ID`, `Name`, `Username`, `password`, `Address`, `Phone`, `Email`) VALUES
(0, '', 'q', 'q', 'q', 0, 'q'),
(121212, 'Nama Lengkap', 'Username', 'Password', 'Alamat', 2134, 'a');

-- --------------------------------------------------------

--
-- Struktur dari tabel `borrowing`
--

CREATE TABLE `borrowing` (
  `subscriber_ID` int(10) DEFAULT NULL,
  `Borrow_Date` date DEFAULT NULL,
  `Item_ID` int(10) DEFAULT NULL,
  `Return_Date` date DEFAULT NULL,
  `Fee` int(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data untuk tabel `borrowing`
--

INSERT INTO `borrowing` (`subscriber_ID`, `Borrow_Date`, `Item_ID`, `Return_Date`, `Fee`) VALUES
(1213, '2021-05-19', 1, '2021-06-09', 0),
(1213, '2021-05-19', 9, '2021-06-09', 0),
(1213, '2021-05-19', 5, '2021-06-09', 0),
(1213, '2021-04-19', 1, '2021-04-19', 0),
(1213, '2021-03-19', 8, '2021-04-09', 0),
(1213, '2021-05-19', 2, '2021-08-19', 0),
(1213, '2021-05-19', 7, '2021-06-09', 0),
(1122, '2021-05-19', 4, '2021-08-19', NULL),
(1213, '2021-05-19', 9, '2021-06-09', 0),
(1213, '2021-05-19', 6, '2021-06-09', 0),
(1122, '2021-05-19', 2, '2021-08-19', NULL),
(1122, '2021-05-19', 5, '2021-08-19', 0),
(1213, '2021-05-19', 3, '2021-08-19', 0),
(1122, '2021-05-19', 5, '2021-06-09', 0),
(1213, '2021-05-19', 5, '2021-06-09', 0),
(1213, '2021-05-19', 6, '2021-06-09', 0),
(1213, '2021-05-19', 6, '2021-06-09', 0),
(1213, '2021-05-19', 6, '2021-08-19', 0),
(1213, '2021-05-19', 5, '2021-08-19', 0),
(1213, '2021-05-19', 3, '2021-08-19', NULL),
(1213, '2021-05-19', 9, '2021-08-19', 0),
(1213, '2021-05-19', 8, '2021-08-19', 0),
(1213, '2021-05-19', 4, '2021-08-19', NULL),
(1213, '2021-05-19', 1, '2021-08-19', 0),
(1122, '2021-05-19', 6, '2021-06-09', 0),
(1122, '2021-05-19', 3, '2021-06-09', NULL),
(1213, '2021-05-19', 8, '2021-08-19', 0),
(1122, '2021-05-19', 7, '2021-08-19', NULL),
(1213, '2021-05-20', 6, '2021-08-20', 0),
(1213, '2021-05-20', 2, '2021-08-20', NULL),
(0, '2021-05-20', 5, '2021-06-10', NULL),
(1213, '2021-05-20', 3, '2021-08-20', NULL),
(0, '2021-05-20', 8, '2021-06-10', NULL),
(1213, '2021-05-21', 0, '2021-08-21', NULL),
(1213, '2021-05-21', 0, '2021-08-21', NULL),
(1213, '2021-05-21', 0, '2021-08-21', NULL),
(1213, '2021-05-21', 0, '2021-08-21', NULL),
(1213, '2021-05-21', 0, '2021-08-21', NULL),
(1213, '2021-05-21', 5, '2021-08-21', NULL);

-- --------------------------------------------------------

--
-- Struktur dari tabel `borrowingsubscribers`
--

CREATE TABLE `borrowingsubscribers` (
  `Subscriber_ID` int(10) DEFAULT NULL,
  `Title_Book` varchar(50) DEFAULT NULL,
  `borrow_date` date DEFAULT NULL,
  `Item_ID` int(10) DEFAULT NULL,
  `return_Date` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data untuk tabel `borrowingsubscribers`
--

INSERT INTO `borrowingsubscribers` (`Subscriber_ID`, `Title_Book`, `borrow_date`, `Item_ID`, `return_Date`) VALUES
(1213, 'Spiderman', '2021-05-19', 3, '2021-08-19'),
(1213, 'Batman and Robin', '2021-05-19', 4, '2021-08-19'),
(1122, 'Spiderman', '2021-05-19', 3, '2021-06-09'),
(1122, 'Fisika Dasar', '2021-05-19', 7, '2021-08-19'),
(1213, 'Senja', '2021-05-20', 2, '2021-08-20'),
(0, 'Petang', '2021-05-20', 5, '2021-06-10'),
(1213, 'Spiderman', '2021-05-20', 3, '2021-08-20'),
(0, 'Malam', '2021-05-20', 8, '2021-06-10'),
(1213, 'Petang', '2021-05-21', 5, '2021-08-21');

-- --------------------------------------------------------

--
-- Struktur dari tabel `items`
--

CREATE TABLE `items` (
  `Item_ID` int(10) NOT NULL,
  `Library_ID` int(10) DEFAULT NULL,
  `Category` varchar(30) DEFAULT NULL,
  `Title` varchar(50) DEFAULT NULL,
  `Author` varchar(50) DEFAULT NULL,
  `Publisher` varchar(50) DEFAULT NULL,
  `Production_Year` int(5) DEFAULT NULL,
  `Copies` int(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data untuk tabel `items`
--

INSERT INTO `items` (`Item_ID`, `Library_ID`, `Category`, `Title`, `Author`, `Publisher`, `Production_Year`, `Copies`) VALUES
(1, 3, 'Book', 'Buku Teknik Mesin', 'Abdul Karim', 'Dua Serangkai', 2003, 100),
(2, 3, 'Novel', 'Senja', 'Anthony ', 'Puspa', 2010, 50),
(3, 3, 'Komik', 'Spiderman', 'Stan Lee', 'Marvel', 2000, 200),
(4, 2, 'Komik', 'Batman and Robin', 'Bob Kane', 'DC Comic', 1990, 200),
(5, 2, 'Novel', 'Petang', 'Deni Awan', 'Desaku', 2012, 150),
(6, 2, 'Book', 'Matematika Aljabar', 'Sandy Santoso', 'Sejahtera', 2014, 70),
(7, 1, 'Book', 'Fisika Dasar', 'Bedu Santoso', 'Wanami', 2006, 170),
(8, 1, 'Novel', 'Malam', 'Andi Bagus', 'Genjari', 2018, 190),
(9, 1, 'Comic', 'Iron Man', 'Jack KIrby', 'Marvel', 1968, 250),
(10, 1, 'Novel', 'Sunyi', 'Dwi Putra', 'Bahari', 2017, 106);

-- --------------------------------------------------------

--
-- Struktur dari tabel `library`
--

CREATE TABLE `library` (
  `ID` int(10) NOT NULL,
  `Nama` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data untuk tabel `library`
--

INSERT INTO `library` (`ID`, `Nama`) VALUES
(1, 'Main Campus Library'),
(2, 'Computer Science Library'),
(3, 'Engineering Library');

-- --------------------------------------------------------

--
-- Struktur dari tabel `subscribers`
--

CREATE TABLE `subscribers` (
  `Subscriber_ID` int(10) NOT NULL,
  `Type` varchar(10) DEFAULT NULL,
  `Name` varchar(50) DEFAULT NULL,
  `username` varchar(20) DEFAULT NULL,
  `password` varchar(20) DEFAULT NULL,
  `Address` varchar(50) DEFAULT NULL,
  `Phone` int(20) DEFAULT NULL,
  `Email` varchar(30) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data untuk tabel `subscribers`
--

INSERT INTO `subscribers` (`Subscriber_ID`, `Type`, `Name`, `username`, `password`, `Address`, `Phone`, `Email`) VALUES
(0, 'Regular', 'ezio', 'ezio', 'ezio', 'jl. mangga', 2147483647, 'ezio@gmail.com'),
(1122, 'Golden', 'samsul', 'samsul', '123', 'jl. km', 1212121212, 'qweqwad'),
(1213, 'Golden', 'Nama Lengkap', 'a', 'a', 'Alamat', 123, 'E-mail');

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`Admin_ID`);

--
-- Indeks untuk tabel `borrowing`
--
ALTER TABLE `borrowing`
  ADD KEY `subscriber_ID` (`subscriber_ID`);

--
-- Indeks untuk tabel `borrowingsubscribers`
--
ALTER TABLE `borrowingsubscribers`
  ADD KEY `Subscriber_ID` (`Subscriber_ID`),
  ADD KEY `Item_ID` (`Item_ID`);

--
-- Indeks untuk tabel `items`
--
ALTER TABLE `items`
  ADD PRIMARY KEY (`Item_ID`),
  ADD KEY `Library_ID` (`Library_ID`);

--
-- Indeks untuk tabel `library`
--
ALTER TABLE `library`
  ADD PRIMARY KEY (`ID`);

--
-- Indeks untuk tabel `subscribers`
--
ALTER TABLE `subscribers`
  ADD PRIMARY KEY (`Subscriber_ID`);

--
-- Ketidakleluasaan untuk tabel pelimpahan (Dumped Tables)
--

--
-- Ketidakleluasaan untuk tabel `borrowing`
--
ALTER TABLE `borrowing`
  ADD CONSTRAINT `borrowing_ibfk_1` FOREIGN KEY (`subscriber_ID`) REFERENCES `subscribers` (`Subscriber_ID`) ON UPDATE CASCADE;

--
-- Ketidakleluasaan untuk tabel `borrowingsubscribers`
--
ALTER TABLE `borrowingsubscribers`
  ADD CONSTRAINT `borrowingsubscribers_ibfk_1` FOREIGN KEY (`Subscriber_ID`) REFERENCES `borrowing` (`subscriber_ID`),
  ADD CONSTRAINT `borrowingsubscribers_ibfk_2` FOREIGN KEY (`Item_ID`) REFERENCES `items` (`Item_ID`) ON UPDATE CASCADE;

--
-- Ketidakleluasaan untuk tabel `items`
--
ALTER TABLE `items`
  ADD CONSTRAINT `items_ibfk_1` FOREIGN KEY (`Library_ID`) REFERENCES `library` (`ID`) ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
