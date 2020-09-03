

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;


CREATE TABLE IF NOT EXISTS `all_messengers` (
  `name` varchar(100) NOT NULL,
  `img` mediumblob,
  `manufact` int(5) DEFAULT NULL,
  `upmax` int(1) DEFAULT NULL,
  `supos` int(1) DEFAULT NULL,
  `supvideo` int(1) DEFAULT NULL,
  `supvs` int(1) DEFAULT NULL,
  `supgc` int(1) DEFAULT NULL,
  PRIMARY KEY (`name`),
  KEY `manufact` (`manufact`),
  KEY `upmax` (`upmax`),
  KEY `supos` (`supos`),
  KEY `supvideo` (`supvideo`),
  KEY `supvs` (`supvs`),
  KEY `supgc` (`supgc`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `all_messengers`
--

INSERT INTO `all_messengers` (`name`, `img`, `manufact`, `upmax`, `supos`, `supvideo`, `supvs`, `supgc`) VALUES
('Psi', NULL, 0, 6, 0, 0, 0, 1),
('Riot.im', NULL, 8, 6, 0, 0, 1, 1),
('Signal', NULL, 7, 3, 0, 0, 1, 1),
('Skype', NULL, 6, 1, 0, 1, 1, 1),
('Telegram', NULL, 0, 0, 0, 1, 1, 1),
('Viber', NULL, 1, 2, 0, 1, 1, 1),
('VK', NULL, 9, 2, 0, 1, 1, 1),
('WeChat', NULL, 5, 3, 0, 1, 1, 1),
('WhatsApp', NULL, 2, 5, 0, 1, 0, 1),
('ТамТам', NULL, 3, 6, 0, 1, 2, 2);

-- --------------------------------------------------------

--
-- Table structure for table `manufactures`
--

CREATE TABLE IF NOT EXISTS `manufactures` (
  `manufactures_id` int(5) NOT NULL,
  `manufactures_title` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`manufactures_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `manufactures`
--

INSERT INTO `manufactures` (`manufactures_id`, `manufactures_title`) VALUES
(0, 'Telegram LLC'),
(1, 'Viber Media'),
(2, 'Facebook'),
(3, 'Mail.ru group'),
(4, 'The Psi team'),
(5, 'Tecent Holdings'),
(6, 'Microsoft'),
(7, 'Signal Messenger'),
(8, 'New Vector'),
(9, 'Mail.ru group'),
(10, 'nAn'),
(11, 'PY'),
(12, 'KKK'),
(13, 'LIKE'),
(14, 'ppp'),
(15, 'OOP'),
(16, 'KKK'),
(17, 'trash'),
(18, 'tru'),
(19, 'Shit'),
(20, 'feeeel'),
(21, 'clutch'),
(22, '0');

-- --------------------------------------------------------

--
-- Table structure for table `messages`
--

CREATE TABLE IF NOT EXISTS `messages` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user` text,
  `message` longtext,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `messenger_name`
--

CREATE TABLE IF NOT EXISTS `messenger_name` (
  `messenger_id` int(5) NOT NULL,
  `messenger_title` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`messenger_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `messenger_name`
--

INSERT INTO `messenger_name` (`messenger_id`, `messenger_title`) VALUES
(0, 'TELEGRAM'),
(1, 'VIBER'),
(2, 'WhatsApp'),
(3, 'ТамТам'),
(4, 'Psi'),
(5, 'WeChat'),
(6, 'Skype'),
(7, 'Signal'),
(8, 'Riot.im'),
(10, 'VK');

-- --------------------------------------------------------

--
-- Table structure for table `os_sup`
--

CREATE TABLE IF NOT EXISTS `os_sup` (
  `os_sup_id` int(1) NOT NULL,
  `os_sup_title` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`os_sup_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `os_sup`
--

INSERT INTO `os_sup` (`os_sup_id`, `os_sup_title`) VALUES
(0, 'Android/Ios/Windows/Mac/Ubuntu'),
(1, 'Android/Ios');

-- --------------------------------------------------------

--
-- Table structure for table `uploadmax`
--

CREATE TABLE IF NOT EXISTS `uploadmax` (
  `uploadmax_id` int(1) NOT NULL,
  `uploadmax_mb` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`uploadmax_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `uploadmax`
--

INSERT INTO `uploadmax` (`uploadmax_id`, `uploadmax_mb`) VALUES
(0, '1500мб'),
(1, '300мб'),
(2, '200мб'),
(3, '100мб'),
(4, '16 мб'),
(5, '2мб'),
(6, 'Неизвестно');

-- --------------------------------------------------------

--
-- Table structure for table `yesorno`
--

CREATE TABLE IF NOT EXISTS `yesorno` (
  `yesorno_id` int(1) NOT NULL,
  `yesorno_title` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`yesorno_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `yesorno`
--

INSERT INTO `yesorno` (`yesorno_id`, `yesorno_title`) VALUES
(0, 'Нету'),
(1, 'Есть'),
(2, 'Неизвестно');

--
-- Constraints for dumped tables
--

--
-- Constraints for table `all_messengers`
--
ALTER TABLE `all_messengers`
  ADD CONSTRAINT `all_messengers_ibfk_1` FOREIGN KEY (`manufact`) REFERENCES `manufactures` (`manufactures_id`),
  ADD CONSTRAINT `all_messengers_ibfk_2` FOREIGN KEY (`upmax`) REFERENCES `uploadmax` (`uploadmax_id`),
  ADD CONSTRAINT `all_messengers_ibfk_3` FOREIGN KEY (`supos`) REFERENCES `os_sup` (`os_sup_id`),
  ADD CONSTRAINT `all_messengers_ibfk_4` FOREIGN KEY (`supvideo`) REFERENCES `yesorno` (`yesorno_id`),
  ADD CONSTRAINT `all_messengers_ibfk_5` FOREIGN KEY (`supvs`) REFERENCES `yesorno` (`yesorno_id`),
  ADD CONSTRAINT `all_messengers_ibfk_6` FOREIGN KEY (`supgc`) REFERENCES `yesorno` (`yesorno_id`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
