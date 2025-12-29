-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Waktu pembuatan: 29 Des 2025 pada 00.14
-- Versi server: 10.4.32-MariaDB
-- Versi PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `siff_db`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `films`
--

CREATE TABLE `films` (
  `id` int(11) NOT NULL,
  `judul` varchar(100) NOT NULL,
  `sutradara` varchar(100) NOT NULL,
  `genre` varchar(50) NOT NULL,
  `tahun` int(11) NOT NULL,
  `durasi_menit` int(11) NOT NULL,
  `diinput_oleh` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `films`
--

INSERT INTO `films` (`id`, `judul`, `sutradara`, `genre`, `tahun`, `durasi_menit`, `diinput_oleh`) VALUES
(1, 'Laskar Pelangi', 'Riri Riza', 'Drama', 2008, 125, 1),
(2, 'The Raid', 'Gareth Evans', 'Action', 2011, 101, 1),
(3, 'Ada Apa Dengan Cinta 2', 'Riri Riza', 'Romance', 2016, 123, 2),
(4, 'Pengabdi Setan', 'Joko Anwar', 'Horror', 2017, 107, 1),
(5, 'Marlina Si Pembunuh', 'Mouly Surya', 'Thriller', 2017, 93, 2),
(6, 'Dilan 1990', 'Fajar Bustomi', 'Romance', 2018, 110, 1),
(7, 'Gundala', 'Joko Anwar', 'Action', 2019, 123, 1),
(8, 'Impetigore', 'Joko Anwar', 'Horror', 2019, 106, 2),
(9, 'Nanti Kita Cerita', 'Angga Sasongko', 'Drama', 2020, 121, 1),
(10, 'Penyalin Cahaya', 'Wregas Bhanuteja', 'Misteri', 2021, 130, 2),
(11, 'KKN Desa Penari', 'Awi Suryadi', 'Horror', 2022, 130, 1),
(12, 'Ngeri-Ngeri Sedap', 'Bene Dion', 'Komedi', 2022, 114, 2),
(13, 'Mencuri Raden Saleh', 'Angga Sasongko', 'Action', 2022, 154, 1),
(14, 'Miracle in Cell No.7', 'Hanung Bramantyo', 'Drama', 2022, 145, 1),
(15, 'Sri Asih', 'Upi Avianto', 'Action', 2022, 135, 2),
(16, 'Qodrat', 'Charles Gozali', 'Horror', 2022, 102, 1),
(17, 'Sewu Dino', 'Kimo Stamboel', 'Horror', 2023, 121, 2),
(18, 'Buya Hamka', 'Fajar Bustomi', 'Biografi', 2023, 129, 1),
(19, 'Petualangan Sherina 2', 'Riri Riza', 'Musikal', 2023, 126, 2),
(20, 'Budi Pekerti', 'Wregas Bhanuteja', 'Drama', 2023, 111, 1),
(21, 'Sore', 'Yandi Laurens', 'Romance', 2025, 120, 1),
(22, 'Cek Toko Sebelah', 'Raditya Dika', 'Komedi', 2022, 150, 2);

-- --------------------------------------------------------

--
-- Struktur dari tabel `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `username` varchar(50) NOT NULL,
  `password` varchar(255) NOT NULL,
  `role` enum('admin','juri') NOT NULL,
  `nama_lengkap` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `users`
--

INSERT INTO `users` (`id`, `username`, `password`, `role`, `nama_lengkap`) VALUES
(1, 'admin', 'scrypt:32768:8:1$mTzY80eVUJxkn5EQ$81f4304ecc4be6371337dc6bc7bef28b7ff46cdfc9f5eef2051dcf8d42d89ba1ec81fb42f4e5aff682137f48c6584190423b501e6b4713d3ea7946663d354391', 'admin', 'Panitia Inti'),
(2, 'juri', 'scrypt:32768:8:1$GxDqHOml9ISf2o58$aacbc63bc7d47108547ca424378710e71291574e4477c275af91d9e53073861c919c6fc7153a1c82872f0ba68eaccb6001130a9bfbb101a0384ffd3fab1c9f60', 'juri', 'Dewan Juri'),
(3, 'edbro', 'scrypt:32768:8:1$n4U5uAVaNjlq3x9y$51b822a44fec4d654a1aef6dd29f89679719e59ed2bd8403479bb9bf6d53000d99fa1df13d5d56b31d252ebb7696c44ee3e3424067a0065d7e9bcbe8e02e72d3', 'juri', 'Edi Brokoli');

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `films`
--
ALTER TABLE `films`
  ADD PRIMARY KEY (`id`),
  ADD KEY `diinput_oleh` (`diinput_oleh`);

--
-- Indeks untuk tabel `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- AUTO_INCREMENT untuk tabel yang dibuang
--

--
-- AUTO_INCREMENT untuk tabel `films`
--
ALTER TABLE `films`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=23;

--
-- AUTO_INCREMENT untuk tabel `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- Ketidakleluasaan untuk tabel pelimpahan (Dumped Tables)
--

--
-- Ketidakleluasaan untuk tabel `films`
--
ALTER TABLE `films`
  ADD CONSTRAINT `films_ibfk_1` FOREIGN KEY (`diinput_oleh`) REFERENCES `users` (`id`) ON DELETE SET NULL;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
