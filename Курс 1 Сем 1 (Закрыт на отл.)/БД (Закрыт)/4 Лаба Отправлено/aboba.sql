-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Хост: 127.0.0.1:3306
-- Время создания: Дек 11 2024 г., 20:03
-- Версия сервера: 9.1.0
-- Версия PHP: 8.3.14

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- База данных: `aboba`
--

-- --------------------------------------------------------

--
-- Структура таблицы `жанр`
--

DROP TABLE IF EXISTS `жанр`;
CREATE TABLE IF NOT EXISTS `жанр` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `Название` varchar(127) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Дамп данных таблицы `жанр`
--

INSERT INTO `жанр` (`ID`, `Название`) VALUES
(1, 'Комедия'),
(2, 'Романтика'),
(3, 'Детектив'),
(4, 'Хоррор'),
(5, 'Драма');

-- --------------------------------------------------------

--
-- Структура таблицы `фильм`
--

DROP TABLE IF EXISTS `фильм`;
CREATE TABLE IF NOT EXISTS `фильм` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `Название` varchar(127) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `Режиссёр` varchar(127) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `Время показа` time(6) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Дамп данных таблицы `фильм`
--

INSERT INTO `фильм` (`ID`, `Название`, `Режиссёр`, `Время показа`) VALUES
(1, 'Титаник', 'Джеймс Кэмерон', '03:15:00.000000'),
(2, 'Аватар', 'Джеймс Кэмерон', '02:42:00.000000'),
(3, 'Руки Вверх!', 'Аскар Узабаев', '01:40:00.000000'),
(4, 'Беляковы в отпуске', 'Александр Назаров', '01:33:00.000000'),
(5, 'Субстанция', 'Корали Фаржа', '02:21:00.000000'),
(6, 'Лунтик. Возвращение домой', 'Константин Бронзит', '01:18:00.000000'),
(7, 'Досье «Чёрная канарейка»', 'Пьер Морель', '01:41:00.000000'),
(8, 'Холоп из Парижа', 'Александр Шарло, Франк Манье', '01:49:00.000000'),
(9, 'Пчеловод', 'Дэвид Эйр', '01:45:00.000000'),
(10, 'Профессионал', 'Ханс Петтер Муланд', '01:52:00.000000');

-- --------------------------------------------------------

--
-- Структура таблицы `фильм_жанр`
--

DROP TABLE IF EXISTS `фильм_жанр`;
CREATE TABLE IF NOT EXISTS `фильм_жанр` (
  `Фильм_ID` int NOT NULL,
  `Жанр_ID` int NOT NULL,
  KEY `Фильм_ID` (`Фильм_ID`),
  KEY `Жанр_ID` (`Жанр_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Дамп данных таблицы `фильм_жанр`
--

INSERT INTO `фильм_жанр` (`Фильм_ID`, `Жанр_ID`) VALUES
(1, 5),
(1, 2),
(10, 3),
(10, 4),
(9, 1),
(4, 1),
(7, 4),
(6, 1),
(5, 4),
(8, 1),
(3, 3);

--
-- Ограничения внешнего ключа сохраненных таблиц
--

--
-- Ограничения внешнего ключа таблицы `фильм_жанр`
--
ALTER TABLE `фильм_жанр`
  ADD CONSTRAINT `фильм_жанр_ibfk_1` FOREIGN KEY (`Фильм_ID`) REFERENCES `фильм` (`ID`),
  ADD CONSTRAINT `фильм_жанр_ibfk_2` FOREIGN KEY (`Жанр_ID`) REFERENCES `жанр` (`ID`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
