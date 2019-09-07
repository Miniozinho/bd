CREATE TABLE `lista` (
  `idlista` int(11) NOT NULL AUTO_INCREMENT,
  `nome` varchar(45) NOT NULL,
  `data` varchar(10) NOT NULL,
  `prioridade` varchar(1) NOT NULL,
  `conclusao` varchar(3) DEFAULT '[ ]',
  PRIMARY KEY (`idlista`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci