CREATE TABLE `Asteroid_dataset` (
  `Object_Name` VARCHAR(255),
  `Mass` VARCHAR(255),
  `Distance_from_Earth` VARCHAR(255),
  `Diameter` VARCHAR(255)
);

CREATE TABLE `astronomical_data` (
  `Object_Type` VARCHAR(255),
  `Description` VARCHAR(255),
  `Example` VARCHAR(255)
);

CREATE TABLE `Black_Hole_dataset` (
  `Object_Name` VARCHAR(255),
  `Mass` VARCHAR(255),
  `Distance_from_Earth` VARCHAR(255),
  `Diameter` VARCHAR(255)
);

CREATE TABLE `Comet_dataset` (
  `Object_Name` VARCHAR(255),
  `Mass` VARCHAR(255),
  `Distance_from_Earth` VARCHAR(255),
  `Diameter` VARCHAR(255)
);

CREATE TABLE `constellationAbrev` (
  `constellationID` VARCHAR(255),
  `Con` VARCHAR(255),
  `ConstellationName` VARCHAR(255)
);

CREATE TABLE `constellations` (
  `constellationID` VARCHAR(255),
  `pageID` VARCHAR(255),
  `menuID` VARCHAR(255),
  `SubMenuID` VARCHAR(255),
  `ConstellationName` VARCHAR(255),
  `Declination` VARCHAR(255),
  `RightAscension` VARCHAR(255),
  `visableEn` VARCHAR(255),
  `visableCy` VARCHAR(255),
  `descriptionEn` VARCHAR(255),
  `descriptionCy` VARCHAR(255),
  `wikiURL` VARCHAR(255),
  `wikiDataURL` VARCHAR(255),
  `imageURL` VARCHAR(255),
  `Magnitude` VARCHAR(255),
  `soEn` VARCHAR(255),
  `soCy` VARCHAR(255),
  `asoEn` VARCHAR(255),
  `asoCy` VARCHAR(255),
  `bt1En` VARCHAR(255),
  `bt2En` VARCHAR(255),
  `bt3En` VARCHAR(255),
  `bt4En` VARCHAR(255),
  `bt5En` VARCHAR(255),
  `bt1Cy` VARCHAR(255),
  `bt2Cy` VARCHAR(255),
  `bt3Cy` VARCHAR(255),
  `bt4Cy` VARCHAR(255),
  `bt5Cy` VARCHAR(255),
  `bt1Image` VARCHAR(255),
  `bt1AltTextEn` VARCHAR(255),
  `bt1AltTextCy` VARCHAR(255),
  `bt2Image` VARCHAR(255),
  `bt2AltTextEn` VARCHAR(255),
  `bt2AltTextCy` VARCHAR(255),
  `bt3Image` VARCHAR(255),
  `bt3AltTextEn` VARCHAR(255),
  `bt3AltTextCy` VARCHAR(255),
  `bt4Image` VARCHAR(255),
  `bt4AltTextEn` VARCHAR(255),
  `bt4AltTextCy` VARCHAR(255)
);

CREATE TABLE `constellationsByArea_clean00` (
  `Rank` VARCHAR(255),
  `Abbrev.` VARCHAR(255),
  `Constellation` VARCHAR(255),
  `Solid angle ("Area") (sq. deg.) ` VARCHAR(255),
  `Solid angle (millisteradians)` VARCHAR(255),
  `Per­cent­age` VARCHAR(255),
  `Right ascension (hours & mins) ` VARCHAR(255),
  `Decli­nation (degs & mins) ` VARCHAR(255),
  `Quad ` VARCHAR(255)
);

CREATE TABLE `constellationStars` (
  `starID` VARCHAR(255),
  `constelleationID` VARCHAR(255),
  `Name` VARCHAR(255),
  `B` VARCHAR(255),
  `F` VARCHAR(255),
  `G` VARCHAR(255),
  `Var` VARCHAR(255),
  `HD` VARCHAR(255),
  `HIP` VARCHAR(255),
  `RA` VARCHAR(255),
  `Declination` VARCHAR(255),
  `visMag` VARCHAR(255),
  `abs mag` VARCHAR(255),
  `DistLy` VARCHAR(255),
  `SpClass` VARCHAR(255),
  `Notes` VARCHAR(255)
);

CREATE TABLE `constellations_clean00` (
  `Constellation` VARCHAR(255),
  `AbreviationIAU` VARCHAR(255),
  `AbreviationNASA` VARCHAR(255),
  `Genitive` VARCHAR(255),
  `Origin` VARCHAR(255),
  `Meaning` VARCHAR(255),
  `Brightesstar` VARCHAR(255)
);

CREATE TABLE `Galaxy_dataset` (
  `Object_Name` VARCHAR(255),
  `Mass` VARCHAR(255),
  `Distance_from_Earth` VARCHAR(255),
  `Diameter` VARCHAR(255)
);

CREATE TABLE `messierConstellationTypes` (
  `constellationID` VARCHAR(255),
  `Con` VARCHAR(255),
  `Constellation Name` VARCHAR(255)
);

CREATE TABLE `messierObjectAbrev` (
  `messierID` VARCHAR(255),
  `Con` VARCHAR(255)
);

CREATE TABLE `messierObjects` (
  `messierID` VARCHAR(255),
  `NGC` VARCHAR(255),
  `Type` VARCHAR(255),
  `Mag` VARCHAR(255),
  `Size` VARCHAR(255),
  `DistanceLy` VARCHAR(255),
  `RA` VARCHAR(255),
  `Declination` VARCHAR(255),
  `Con` VARCHAR(255),
  `Viewing Season` VARCHAR(255),
  `CommonName` VARCHAR(255),
  `DescriptionEn` VARCHAR(255),
  `DescriptionCy` VARCHAR(255)
);

CREATE TABLE `messierObjectsTable` (
  `messierID` VARCHAR(255),
  `NGC` VARCHAR(255),
  `CommonName` VARCHAR(255),
  `objecType` VARCHAR(255),
  `Distance` VARCHAR(255),
  `Constellation` VARCHAR(255),
  `aparentMag` VARCHAR(255),
  `RA` VARCHAR(255),
  `Declination` VARCHAR(255)
);

CREATE TABLE `messierTable` (
  `constellationID` VARCHAR(255),
  `pageID` VARCHAR(255),
  `menuID` VARCHAR(255),
  `SubMenuID` VARCHAR(255),
  `ConstellationName` VARCHAR(255),
  `Declination` VARCHAR(255),
  `RightAscension` VARCHAR(255),
  `visableEn` VARCHAR(255),
  `visableCy` VARCHAR(255),
  `descriptionEn` VARCHAR(255),
  `descriptionCy` VARCHAR(255),
  `wikiURL` VARCHAR(255),
  `imageURL` VARCHAR(255),
  `Magnitude` VARCHAR(255),
  `soEn` VARCHAR(255),
  `soCy` VARCHAR(255),
  `asoEn` VARCHAR(255),
  `asoCy` VARCHAR(255),
  `bt1En` VARCHAR(255),
  `bt2En` VARCHAR(255),
  `bt3En` VARCHAR(255),
  `bt4En` VARCHAR(255),
  `bt5En` VARCHAR(255),
  `bt1Cy` VARCHAR(255),
  `bt2Cy` VARCHAR(255),
  `bt3Cy` VARCHAR(255),
  `bt4Cy` VARCHAR(255),
  `bt5Cy` VARCHAR(255),
  `bt1Image` VARCHAR(255),
  `bt1AltTextEn` VARCHAR(255),
  `bt1AltTextCy` VARCHAR(255),
  `bt2Image` VARCHAR(255),
  `bt2AltTextEn` VARCHAR(255),
  `bt2AltTextCy` VARCHAR(255),
  `bt3Image` VARCHAR(255),
  `bt3AltTextEn` VARCHAR(255),
  `bt3AltTextCy` VARCHAR(255),
  `bt4Image` VARCHAR(255),
  `bt4AltTextEn` VARCHAR(255),
  `bt4AltTextCy` VARCHAR(255)
);

CREATE TABLE `Nebula_dataset` (
  `Object_Name` VARCHAR(255),
  `Mass` VARCHAR(255),
  `Distance_from_Earth` VARCHAR(255),
  `Diameter` VARCHAR(255)
);

CREATE TABLE `Planet_dataset` (
  `Object_Name` VARCHAR(255),
  `Mass` VARCHAR(255),
  `Distance_from_Earth` VARCHAR(255),
  `Diameter` VARCHAR(255)
);

CREATE TABLE `Quasar_dataset` (
  `Object_Name` VARCHAR(255),
  `Mass` VARCHAR(255),
  `Distance_from_Earth` VARCHAR(255),
  `Diameter` VARCHAR(255)
);

CREATE TABLE `starByConstellation` (
  `constellation` VARCHAR(255),
  `wikiURL` VARCHAR(255)
);

CREATE TABLE `Star_dataset` (
  `Object_Name` VARCHAR(255),
  `Mass` VARCHAR(255),
  `Distance_from_Earth` VARCHAR(255),
  `Diameter` VARCHAR(255)
);

CREATE TABLE `tables_list` (
  `ID` VARCHAR(255),
  `Table` VARCHAR(255),
  `Fields` VARCHAR(255)
);

CREATE TABLE `types` (
  `Type` VARCHAR(255),
  `descriptionEn` VARCHAR(255),
  `descriptionCy` VARCHAR(255)
);

