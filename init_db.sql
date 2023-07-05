/*
SQLyog Community v13.1.6 (64 bit)
MySQL - 5.7.9 : Database - metrostation1
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`metrostation1` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `metrostation1`;

/*Table structure for table `feedback` */

DROP TABLE IF EXISTS `feedback`;

CREATE TABLE `feedback` (
  `feedback_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `feedback` varchar(50) DEFAULT NULL,
  `date_time` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`feedback_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `feedback` */

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `login_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(30) DEFAULT NULL,
  `password` varchar(30) DEFAULT NULL,
  `user_type` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`login_id`)
) ENGINE=InnoDB AUTO_INCREMENT=55 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`login_id`,`username`,`password`,`user_type`) values 
(1,'admin','admin','admin'),
(2,'aluboat','aluboat','staffsboat'),
(3,'edaboat','edaboat','staffsboat'),
(4,'jlnboat','jlnboat','staffsboat'),
(5,'kadboat','kadboat','staffsboat'),
(6,'kakboat','kakboat','staffsboat'),
(7,'kalboat','kalboat','staffsboat'),
(8,'mahboat','mahboat','staffsboat'),
(9,'petboat','petboat','staffsboat'),
(10,'palboat','palboat','staffsboat'),
(11,'vytboat','vytboat','staffsboat'),
(12,'alumetro','alumetro','staffsmetro'),
(13,'edametro','edametro','staffsmetro'),
(14,'jlnmetro','jlnmetro','staffsmetro'),
(15,'kadmetro','kadmetro','staffsmetro'),
(16,'kakmetro','kakmetro','staffsmetro'),
(17,'kalmetro','kalmetro','staffsmetro'),
(18,'mahmetro','mahmetro','staffsmetro'),
(19,'petmetro','petmetro','staffsmetro'),
(20,'palmetro','palmetro','staffsmetro'),
(21,'vytmetro','vytmetro','staffsmetro'),
(22,'aluauto','aluauto','staffsauto'),
(23,'edaauto','edaauto','staffsauto'),
(24,'jlnauto','jlnauto','staffsauto'),
(25,'kadauto','kadauto','staffsauto'),
(26,'kakauto','kakauto','staffsauto'),
(27,'kalauto','kalauto','staffsauto'),
(28,'mahauto','mahauto','staffsauto'),
(29,'petauto','petauto','staffsauto'),
(30,'palauto','palauto','staffsauto'),
(31,'vytauto','vytauto','staffsauto'),
(32,'alucar','alucar','staffscar'),
(33,'edacar','edacar','staffscar'),
(34,'jlncar','jlncar','staffscar'),
(35,'kadcar','kadcar','staffscar'),
(36,'kakcar','kakcar','staffscar'),
(37,'kalcar','kalcar','staffscar'),
(38,'mahcar','mahcar','staffscar'),
(39,'petcar','petcar','staffscar'),
(40,'palcar','palcar','staffscar'),
(41,'vytcar','vytcar','staffscar'),
(42,'alubus','alubus','staffsbus'),
(43,'edabus','edabus','staffsbus'),
(44,'jlnbus','jlnbus','staffsbus'),
(45,'kadbus','kadbus','staffsbus'),
(46,'kakbus','kakbus','staffsbus'),
(47,'kalbus','kalbus','staffsbus'),
(48,'mahbus','mahbus','staffsbus'),
(49,'petbus','petbus','staffsbus'),
(50,'palbus','palbus','staffsbus'),
(51,'vytbus','vytbus','staffsbus'),
(52,'user','user','user'),
(53,'abc','abc','user'),
(54,'aaa','aaa','user');

/*Table structure for table `message` */

DROP TABLE IF EXISTS `message`;

CREATE TABLE `message` (
  `message_id` int(11) NOT NULL AUTO_INCREMENT,
  `sender_id` int(11) DEFAULT NULL,
  `sender_type` varchar(100) DEFAULT NULL,
  `receiver_id` int(11) DEFAULT NULL,
  `receiver_type` varchar(100) DEFAULT NULL,
  `message` varchar(100) DEFAULT NULL,
  `reply` varchar(100) DEFAULT NULL,
  `date_time` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`message_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `message` */

/*Table structure for table `payment` */

DROP TABLE IF EXISTS `payment`;

CREATE TABLE `payment` (
  `pay_id` int(11) NOT NULL AUTO_INCREMENT,
  `transaction_id` int(11) DEFAULT NULL,
  `amount` varchar(100) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`pay_id`)
) ENGINE=MyISAM AUTO_INCREMENT=77 DEFAULT CHARSET=latin1;

/*Data for the table `payment` */

insert  into `payment`(`pay_id`,`transaction_id`,`amount`,`date`) values 
(1,1,'0','2023-05-01'),
(2,1,'0','2023-05-01'),
(3,1,'0','2023-05-01'),
(4,2,'0','2023-05-01'),
(5,1,'0','2023-05-01'),
(6,1,'0','2023-05-01'),
(7,1,'0','2023-05-01'),
(8,1,'0','2023-05-01'),
(9,1,'0','2023-05-01'),
(10,1,'0','2023-05-03'),
(11,1,'0','2023-05-03'),
(12,1,'0','2023-05-03'),
(13,2,'0','2023-05-03'),
(14,3,'0','2023-05-03'),
(15,4,'0','2023-05-27'),
(16,5,'0','2023-05-27'),
(17,6,'0','2023-05-27'),
(18,7,'0','2023-05-27'),
(19,8,'0','2023-05-27'),
(20,9,'0','2023-05-27'),
(21,10,'0','2023-05-27'),
(22,11,'0','2023-05-29'),
(23,12,'0','2023-05-29'),
(24,13,'0','2023-05-29'),
(25,14,'0','2023-05-29'),
(26,15,'0','2023-05-29'),
(27,16,'0','2023-05-29'),
(28,17,'0','2023-05-29'),
(29,18,'0','2023-05-29'),
(30,19,'0','2023-05-29'),
(31,20,'0','2023-06-19'),
(32,21,'0','2023-06-19'),
(33,22,'0','2023-06-19'),
(34,1,'0','2023-06-19'),
(35,1,'0','2023-06-19'),
(36,2,'0','2023-06-19'),
(37,3,'0','2023-06-19'),
(38,4,'0','2023-06-19'),
(39,5,'0','2023-06-19'),
(40,6,'0','2023-06-19'),
(41,7,'0','2023-06-19'),
(42,8,'0','2023-06-19'),
(43,9,'0','2023-06-19'),
(44,10,'0','2023-06-19'),
(45,11,'0','2023-06-19'),
(46,12,'0','2023-06-20'),
(47,13,'0','2023-06-20'),
(48,14,'0','2023-06-20'),
(49,15,'0','2023-06-20'),
(50,16,'0','2023-06-20'),
(51,17,'0','2023-06-20'),
(52,18,'0','2023-06-20'),
(53,19,'0','2023-06-20'),
(54,20,'0','2023-06-20'),
(55,21,'0','2023-06-20'),
(56,22,'0','2023-06-20'),
(57,23,'0','2023-06-20'),
(58,24,'0','2023-06-20'),
(59,25,'0','2023-06-20'),
(60,26,'0','2023-06-20'),
(61,27,'0','2023-06-20'),
(62,28,'0','2023-06-20'),
(63,29,'0','2023-06-20'),
(64,30,'0','2023-06-20'),
(65,31,'0','2023-06-20'),
(66,32,'0','2023-06-20'),
(67,33,'0','2023-06-20'),
(68,34,'0','2023-06-20'),
(69,1,'0','2023-06-20'),
(70,2,'0','2023-06-20'),
(71,3,'0','2023-06-21'),
(72,4,'0','2023-06-21'),
(73,5,'0','2023-06-21'),
(74,6,'0','2023-06-21'),
(75,7,'0','2023-06-21'),
(76,8,'0','2023-06-21');

/*Table structure for table `request` */

DROP TABLE IF EXISTS `request`;

CREATE TABLE `request` (
  `request_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  `amount` varchar(100) DEFAULT NULL,
  `ftype` varchar(100) DEFAULT NULL,
  `fplace` varchar(100) DEFAULT NULL,
  `tplace` varchar(100) DEFAULT NULL,
  `totals` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`request_id`)
) ENGINE=MyISAM AUTO_INCREMENT=13 DEFAULT CHARSET=latin1;

/*Data for the table `request` */

insert  into `request`(`request_id`,`user_id`,`date`,`status`,`amount`,`ftype`,`fplace`,`tplace`,`totals`) values 
(1,1,'2023-06-20','0','0','0','kaloor','Palarivattom',''),
(2,1,'2023-06-20','0','0','0','kaloor','Palarivattom','58'),
(3,3,'2023-06-21','0','0','0','kaloor','Palarivattom',''),
(4,3,'2023-06-21','0','0','0','kaloor','Palarivattom','58'),
(5,3,'2023-06-21','0','0','0','kaloor','Palarivattom',''),
(6,3,'2023-06-21','0','0','0','kaloor','Palarivattom',''),
(7,3,'2023-06-21','0','0','0','kaloor','Palarivattom',''),
(8,3,'2023-06-21','0','8','0','kaloor','Palarivattom','58'),
(9,3,'2023-06-21','0','0','0','kaloor','Palarivattom',''),
(10,3,'2023-06-21','0','0','0','kaloor','Palarivattom',''),
(11,3,'2023-06-21','0','0','0','kaloor','Palarivattom',''),
(12,3,'2023-06-21','0','0','0','kaloor','Palarivattom','58');

/*Table structure for table `requestdetails` */

DROP TABLE IF EXISTS `requestdetails`;

CREATE TABLE `requestdetails` (
  `requestdetails_id` int(11) NOT NULL AUTO_INCREMENT,
  `request_id` int(11) DEFAULT NULL,
  `fplaces` varchar(100) DEFAULT NULL,
  `tplaces` varchar(100) DEFAULT NULL,
  `rates` varchar(100) DEFAULT NULL,
  `types` varchar(100) DEFAULT NULL,
  `amounts` varchar(100) DEFAULT NULL,
  `totals` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`requestdetails_id`)
) ENGINE=MyISAM AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;

/*Data for the table `requestdetails` */

insert  into `requestdetails`(`requestdetails_id`,`request_id`,`fplaces`,`tplaces`,`rates`,`types`,`amounts`,`totals`) values 
(1,2,'kaloor','jln','0','Metro','50','50'),
(2,2,'jln','Palarivattom','0','Metro','8','8'),
(3,4,'kaloor','jln','0','Metro','50','50'),
(4,4,'jln','Palarivattom','0','Metro','8','8'),
(5,8,'kaloor','jln','0','Metro','50','50'),
(6,8,'jln','Palarivattom','0','Metro','8','8'),
(7,12,'kaloor','jln','0','Metro','50','50'),
(8,12,'jln','Palarivattom','0','Metro','8','8');

/*Table structure for table `staffs` */

DROP TABLE IF EXISTS `staffs`;

CREATE TABLE `staffs` (
  `staff_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `station_id` int(11) DEFAULT NULL,
  `first_name` varchar(20) DEFAULT NULL,
  `image` varchar(1000) DEFAULT NULL,
  PRIMARY KEY (`staff_id`)
) ENGINE=InnoDB AUTO_INCREMENT=51 DEFAULT CHARSET=latin1;

/*Data for the table `staffs` */

insert  into `staffs`(`staff_id`,`login_id`,`station_id`,`first_name`,`image`) values 
(1,2,1,'aluboat','static/qr_code/f59f5d5b-5398-4dbd-9fd9-e6b9579e034b.png'),
(2,3,2,'edaboat','static/qr_code/4b5d07e9-6581-4134-96eb-e8e4614efdbf.png'),
(3,4,3,'jlnboat','static/qr_code/fd69f761-7db1-442e-aae8-7a66f30bf51a.png'),
(4,5,4,'kadboat','static/qr_code/30d9cef9-3d5f-4792-aaa5-15db237138d6.png'),
(5,6,5,'kakboat','static/qr_code/eb032eb4-a57a-4a3e-8d9d-5e5e59f712a3.png'),
(6,7,6,'kalboat','static/qr_code/87c6e2c2-4ec6-4ff1-988e-ef48bd914a76.png'),
(7,8,7,'mahboat','static/qr_code/faaa56f1-9677-4d71-babd-e2f30ccdf3a1.png'),
(8,9,8,'petboat','static/qr_code/126fc702-afa4-436e-b21d-fffe52b305b2.png'),
(9,10,9,'palboat','static/qr_code/dc745c0d-4733-43f2-ac94-af7c3ffc667c.png'),
(10,11,10,'vytboat','static/qr_code/12f890e3-8725-46cd-8ca2-6c361accb3fc.png'),
(11,12,1,'alumetro','static/qr_code/95a69ba0-ff30-44bd-8a2d-dc6d4f32a387.png'),
(12,13,2,'edametro','static/qr_code/063c7df4-f2e2-4e98-b438-562ac7941531.png'),
(13,14,3,'jlnmetro','static/qr_code/2a616748-4f68-45e4-b657-2f6212ad8b95.png'),
(14,15,4,'kadmetro','static/qr_code/c9963982-1b49-4be8-a39e-9a551d5bceef.png'),
(15,16,5,'kakmetro','static/qr_code/ec8544a5-8f28-42d5-8480-47a1b3b61e55.png'),
(16,17,6,'kalmetro','static/qr_code/d6bda96d-fa0d-4ca2-95a4-9e73a7c2a4eb.png'),
(17,18,7,'mahmetro','static/qr_code/750fa2aa-3117-4c1e-8da3-fed9af2e31bd.png'),
(18,19,8,'petmetro','static/qr_code/8ccab10c-4cb4-4842-9ba9-f0bebe3846d7.png'),
(19,20,9,'palmetro','static/qr_code/d85521a6-314e-468f-9f7f-1044f768fe74.png'),
(20,21,10,'vytmetro','static/qr_code/d2f9492c-ac3f-4952-9e8d-5fbef6fa236b.png'),
(21,22,1,'aluauto','static/qr_code/6d31e0b7-2915-4240-ab28-7a7b0d925107.png'),
(22,23,2,'edaauto','static/qr_code/42a34c47-ea25-4f81-8d2d-b0d7f5269d19.png'),
(23,24,3,'jlnauto','static/qr_code/4164ed96-9f4c-423b-ac2e-6fb67f0fc003.png'),
(24,25,4,'kadauto','static/qr_code/c6522428-00be-4041-8193-156700beb5b8.png'),
(25,26,5,'kakauto','static/qr_code/9eb02698-31e9-4bb2-9a11-718d0ecb884b.png'),
(26,27,6,'kalauto','static/qr_code/c7373ed2-f622-47d6-9f6c-18df0cc48172.png'),
(27,28,7,'mahauto','static/qr_code/9545a6fe-aded-430c-b642-bc5a96d84c77.png'),
(28,29,8,'petauto','static/qr_code/0d22b042-18fb-4980-9462-8b293ff08187.png'),
(29,30,9,'palauto','static/qr_code/ff6a0a52-53d9-4964-bc75-186c2f98a77d.png'),
(30,31,10,'vytauto','static/qr_code/59b52185-ffcd-4ff4-81f8-a4afce02f672.png'),
(31,32,1,'alucar','static/qr_code/35a34a23-0da4-4c29-b4d7-76821dbfcb80.png'),
(32,33,2,'edacar','static/qr_code/63470c6a-c337-4cab-9d41-cfce3c0beb2c.png'),
(33,34,3,'jlncar','static/qr_code/8bf75af9-380e-434e-bb13-4cf80a11a9cd.png'),
(34,35,4,'kadcar','static/qr_code/ae0854f6-9c85-46c9-8f24-8d1af282b8ce.png'),
(35,36,5,'kakcar','static/qr_code/0d7441df-a545-4a7d-9c4e-58f3df613943.png'),
(36,37,6,'kalcar','static/qr_code/f9e52d1d-785a-4161-8f99-6a24c6ba1a96.png'),
(37,38,7,'mahcar','static/qr_code/221b70f1-767f-4793-b4b1-17a77478a20e.png'),
(38,39,8,'petcar','static/qr_code/ae12ad59-8ca7-426c-8285-698bee4c38af.png'),
(39,40,9,'palcar','static/qr_code/c1dbd63c-5b66-491f-a0f1-d5d273cf114b.png'),
(40,41,10,'vytcar','static/qr_code/b82ffff4-f400-4e80-ac12-2cf75b352db8.png'),
(41,42,1,'alubus','static/qr_code/de41c0f9-c308-419c-9b90-f8876ea6dc65.png'),
(42,43,2,'edabus','static/qr_code/9e9bcbe3-d958-44ce-9e7b-7958165830e9.png'),
(43,44,3,'jlnbus','static/qr_code/3612a4e9-0919-4517-89af-3043e109fe45.png'),
(44,45,4,'kadbus','static/qr_code/66adaa12-a4a0-4919-b328-a30f202285d0.png'),
(45,46,5,'kakbus','static/qr_code/09e0aeb0-d045-4180-a25a-1a89924a2b51.png'),
(46,47,6,'kalbus','static/qr_code/be0c36e1-bc16-4ecf-9da7-01f8d7bf2760.png'),
(47,48,7,'mahbus','static/qr_code/d87e42a6-e7ec-49d0-80e9-6201aee4e2e1.png'),
(48,49,8,'petbus','static/qr_code/ff84148e-9866-4418-953e-7998ac84e627.png'),
(49,50,9,'palbus','static/qr_code/6f5284d8-6e5b-41d8-8e8c-45cfcd001ede.png'),
(50,51,10,'vytbus','static/qr_code/c11cc9ad-530b-45cc-bdc1-93044eeeae85.png');

/*Table structure for table `stations` */

DROP TABLE IF EXISTS `stations`;

CREATE TABLE `stations` (
  `station_id` int(11) NOT NULL AUTO_INCREMENT,
  `station_name` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`station_id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;

/*Data for the table `stations` */

insert  into `stations`(`station_id`,`station_name`) values 
(1,'Aluva'),
(2,'Edapally'),
(3,'JLN stadium'),
(4,'Kadavanthra'),
(5,'Kakkanad'),
(6,'Kaloor'),
(7,'Maharajas'),
(8,'Petta'),
(9,'Palarivattom'),
(10,'Vyttila');

/*Table structure for table `transaction` */

DROP TABLE IF EXISTS `transaction`;

CREATE TABLE `transaction` (
  `transaction_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `amount` decimal(10,0) DEFAULT NULL,
  `fromplace` varchar(1000) DEFAULT NULL,
  `toplace` varchar(1000) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  `travelstatus` varchar(100) DEFAULT NULL,
  `request_id` int(100) DEFAULT NULL,
  PRIMARY KEY (`transaction_id`)
) ENGINE=MyISAM AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;

/*Data for the table `transaction` */

insert  into `transaction`(`transaction_id`,`user_id`,`amount`,`fromplace`,`toplace`,`date`,`status`,`travelstatus`,`request_id`) values 
(1,1,50,'kaloor','','2023-06-20','out','complete',2),
(2,1,8,'jln','','2023-06-20','out','complete',2),
(3,3,50,'kaloor','','2023-06-21','out','complete',4),
(4,3,8,'jln','','2023-06-21','out','complete',4),
(6,3,50,'kaloor','','2023-06-21','out','complete',12),
(7,3,8,'jln','','2023-06-21','out','complete',12),
(8,3,13,'10.0013655','76.310081','2023-06-21','out','complete',0);

/*Table structure for table `users` */

DROP TABLE IF EXISTS `users`;

CREATE TABLE `users` (
  `user_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `first_name` varchar(20) DEFAULT NULL,
  `last_name` varchar(20) DEFAULT NULL,
  `email` varchar(40) DEFAULT NULL,
  `address` varchar(60) DEFAULT NULL,
  `phone` varchar(100) DEFAULT NULL,
  `place` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `users` */

insert  into `users`(`user_id`,`login_id`,`first_name`,`last_name`,`email`,`address`,`phone`,`place`) values 
(1,52,'Parvathi','Ambareesh','abc@gmail.com','ced','1234567894','Kochi'),
(2,53,'abc','abc','haj@gmail.com','bsjans','9567218421','bsusbs'),
(3,54,'aaa','qaa','aaa@gmail.com','vhbgyg','9532884212','vybg');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
