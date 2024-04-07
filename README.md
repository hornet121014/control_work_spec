# Итоговая контрольная работа #


## Информация о проекте##

Необходимо организовать систему учета для питомника в котором живут
домашние и вьючные животные.

## Как сдавать проект ##
Для сдачи проекта необходимо создать отдельный общедоступный
репозиторий(Github, gitlub, или Bitbucket). Разработку вести в этом
репозитории, использовать пул реквесты на изменения. Программа должна
запускаться и работать, ошибок при выполнении программы быть не должно.
Программа, может использоваться в различных системах, поэтому необходимо
разработать класс в виде конструктора

## Задание ##
1. Используя команду cat в терминале операционной системы Linux, создать
два файла Домашние животные (заполнив файл собаками, кошками,
хомяками) и Вьючные животными заполнив файл Лошадьми, верблюдами и
ослы), а затем объединить их. Просмотреть содержимое созданного файла.
Переименовать файл, дав ему новое имя (Друзья человека).

```shell
hornet@hornet-VirtualBox:~$ cat > pets
dog
cat
hamster
hornet@hornet-VirtualBox:~$ cat > pack_animals
horse
camel
donkey
hornet@hornet-VirtualBox:~$ cat pets pack_animals > union_animals
hornet@hornet-VirtualBox:~$ cat union_animals
dog
cat
hamster
horse
camel
donkey
hornet@hornet-VirtualBox:~$ mv union_animals human_friends
hornet@hornet-VirtualBox:~$
```

2. Создать директорию, переместить файл туда.

```shell
hornet@hornet-VirtualBox:~$ mkdir animal_nursery
hornet@hornet-VirtualBox:~$ mv human_friends animal_nursery/
hornet@hornet-VirtualBox:~$ ls animal_nursery/
human_friends
hornet@hornet-VirtualBox:~$
```

3. Подключить дополнительный репозиторий MySQL. Установить любой пакет
из этого репозитория.

```shell
hornet@hornet-VirtualBox:~$ wget https://dev.mysql.com/get/mysql-apt-config_0.8.24-1_all.deb
--2024-03-31 16:30:50--  https://dev.mysql.com/get/mysql-apt-config_0.8.24-1_all.deb
Распознаётся dev.mysql.com (dev.mysql.com)… 23.211.74.232, 2a02:2d8:3:9a9::2e31, 2a02:2d8:3:9a5::2e31
Подключение к dev.mysql.com (dev.mysql.com)|23.211.74.232|:443... соединение установлено.
HTTP-запрос отправлен. Ожидание ответа… 302 Moved Temporarily
Адрес: https://repo.mysql.com//mysql-apt-config_0.8.24-1_all.deb [переход]
--2024-03-31 16:30:51--  https://repo.mysql.com//mysql-apt-config_0.8.24-1_all.deb
Распознаётся repo.mysql.com (repo.mysql.com)… 104.81.113.179, 2a02:26f0:d8:98f::1d68, 2a02:26f0:d8:980::1d68
Подключение к repo.mysql.com (repo.mysql.com)|104.81.113.179|:443... соединение установлено.
HTTP-запрос отправлен. Ожидание ответа… 200 OK
Длина: 18048 (18K) [application/x-debian-package]
Сохранение в: ‘mysql-apt-config_0.8.24-1_all.deb’

mysql-apt-config_0.8.24-1_all.de 100%[========================================================>]  17,62K  --.-KB/s    за 0,001s

2024-03-31 16:30:51 (24,3 MB/s) - ‘mysql-apt-config_0.8.24-1_all.deb’ сохранён [18048/18048]

hornet@hornet-VirtualBox:~$ sudo dpkg -i mysql-apt-config_0.8.24-1_all.deb
(Чтение базы данных … на данный момент установлено 222159 файлов и каталогов.)
Подготовка к распаковке mysql-apt-config_0.8.24-1_all.deb …
Распаковывается mysql-apt-config (0.8.24-1) на замену (0.8.10-1) …
Настраивается пакет mysql-apt-config (0.8.24-1) …
Warning: apt-key should not be used in scripts (called from postinst maintainerscript of the package mysql-apt-config)
Warning: apt-key is deprecated. Manage keyring files in trusted.gpg.d instead (see apt-key(8)).
OK
hornet@hornet-VirtualBox:~$ sudo apt update
Пол:1 http://repo.mysql.com/apt/ubuntu jammy InRelease [20,2 kB]
Сущ:2 http://by.archive.ubuntu.com/ubuntu jammy InRelease
Пол:3 http://by.archive.ubuntu.com/ubuntu jammy-updates InRelease [119 kB]
Сущ:4 http://nginx.org/packages/ubuntu jammy InRelease
Сущ:5 http://by.archive.ubuntu.com/ubuntu jammy-backports InRelease
Сущ:6 https://download.docker.com/linux/ubuntu jammy InRelease
Пол:7 http://security.ubuntu.com/ubuntu jammy-security InRelease [110 kB]
Ошб:1 http://repo.mysql.com/apt/ubuntu jammy InRelease
  Следующие подписи не могут быть проверены, так как недоступен открытый ключ: NO_PUBKEY B7B3B788A8D3785C
Чтение списков пакетов… Готово
W: Ошибка GPG: http://repo.mysql.com/apt/ubuntu jammy InRelease: Следующие подписи не могут быть проверены, так как недоступен открытый ключ: NO_PUBKEY B7B3B788A8D3785C
E: Репозиторий «http://repo.mysql.com/apt/ubuntu jammy InRelease» не подписан.
N: Обновление из этого репозитория нельзя выполнить безопасным способом, поэтому по умолчанию он отключён.
N: Информацию о создании репозитория и настройках пользователя смотрите в справочной странице apt-secure(8).
N: Пропускается получение настроенного файла «nginx/binary-i386/Packages», так как репозиторий «http://nginx.org/packages/ubuntu jammy InRelease» не поддерживает архитектуру «i386»
hornet@hornet-VirtualBox:~$ sudo apt-get install mysql-server
Чтение списков пакетов… Готово
Построение дерева зависимостей… Готово
Чтение информации о состоянии… Готово
Уже установлен пакет mysql-server самой новой версии (8.0.36-0ubuntu0.22.04.1).
Обновлено 0 пакетов, установлено 0 новых пакетов, для удаления отмечено 0 пакетов, и 140 пакетов не обновлено.
hornet@hornet-VirtualBox:~$ systemctl status mysql
● mysql.service - MySQL Community Server
     Loaded: loaded (/lib/systemd/system/mysql.service; enabled; vendor preset: enabled)
     Active: active (running) since Sun 2024-03-31 14:47:00 +03; 1h 47min ago
   Main PID: 1231 (mysqld)
     Status: "Server is operational"
      Tasks: 37 (limit: 2260)
     Memory: 13.5M
        CPU: 50.598s
     CGroup: /system.slice/mysql.service
             └─1231 /usr/sbin/mysqld

мар 31 14:46:55 hornet-VirtualBox systemd[1]: Starting MySQL Community Server...
мар 31 14:47:00 hornet-VirtualBox systemd[1]: Started MySQL Community Server.

```
4. Установить и удалить deb-пакет с помощью dpkg.
```shell
hornet@hornet-VirtualBox:~$ apt download notepadqq
Пол:1 http://by.archive.ubuntu.com/ubuntu jammy/universe amd64 notepadqq amd64 2.0.0~beta1-3 [1 105 kB]
Получено 1 105 kB за 10с (108 kB/s)
hornet@hornet-VirtualBox:~$ sudo dpkg -i notepadqq_2.0.0~beta1-3_amd64.deb
Выбор ранее не выбранного пакета notepadqq.
(Чтение базы данных … на данный момент установлено 223084 файла и каталога.)
Подготовка к распаковке notepadqq_2.0.0~beta1-3_amd64.deb …
Распаковывается notepadqq (2.0.0~beta1-3) …
dpkg: зависимости пакетов не позволяют настроить пакет notepadqq:
 notepadqq зависит от libqt5core5a (>= 5.15.1), однако:
  Пакет libqt5core5a:amd64 не установлен.
 notepadqq зависит от libqt5gui5 (>= 5.8.0) | libqt5gui5-gles (>= 5.8.0), однако:
  Пакет libqt5gui5:amd64 не установлен.
  Пакет libqt5gui5-gles не установлен.
 notepadqq зависит от libqt5network5 (>= 5.0.2), однако:
  Пакет libqt5network5 не установлен.
 notepadqq зависит от libqt5printsupport5 (>= 5.0.2), однако:
  Пакет libqt5printsupport5 не установлен.
 notepadqq зависит от libqt5svg5 (>= 5.6.0~beta), однако:
  Пакет libqt5svg5 не установлен.
 notepadqq зависит от libqt5webchannel5 (>= 5.6.1), однако:
  Пакет libqt5webchannel5 не установлен.
 notepadqq зависит от libqt5webenginewidgets5 (>= 5.14.1), однако:
  Пакет libqt5webenginewidgets5 не установлен.
 notepadqq зависит от libqt5widgets5 (>= 5.11.0~rc1), однако:
  Пакет libqt5widgets5 не установлен.
 notepadqq зависит от libjs-highlight.js (>= 9.12), однако:
  Пакет libjs-highlight.js не установлен.
 notepadqq зависит от libjs-modernizr, однако:
  Пакет libjs-modernizr не установлен.
 notepadqq зависит от libjs-jquery (>= 2.1.1), однако:
  Пакет libjs-jquery не установлен.
 notepadqq зависит от libjs-requirejs (>= 2.3.5), однако:
  Пакет libjs-requirejs не установлен.
 notepadqq зависит от libjs-mathjax (>= 2.7.0), однако:
  Пакет libjs-mathjax не установлен.

dpkg: ошибка при обработке пакета notepadqq (--install):
 проблемы зависимостей — оставляем не настроенным
Обрабатываются триггеры для mailcap (3.70+nmu1ubuntu1) …
Обрабатываются триггеры для gnome-menus (3.36.0-1ubuntu3) …
Обрабатываются триггеры для desktop-file-utils (0.26-1ubuntu3) …
Обрабатываются триггеры для hicolor-icon-theme (0.17-2) …
Обрабатываются триггеры для man-db (2.10.2-1) …
При обработке следующих пакетов произошли ошибки:
 notepadqq
hornet@hornet-VirtualBox:~$ dpkg -l | grep notepadqq
iU  notepadqq                                  2.0.0~beta1-3                           amd64        Notepad++-like editor for Linux
hornet@hornet-VirtualBox:~$ sudo dpkg -r notepadqq
(Чтение базы данных … на данный момент установлен 223541 файл и каталог.)
Удаляется notepadqq (2.0.0~beta1-3) …
Обрабатываются триггеры для man-db (2.10.2-1) …
Обрабатываются триггеры для hicolor-icon-theme (0.17-2) …
Обрабатываются триггеры для mailcap (3.70+nmu1ubuntu1) …
Обрабатываются триггеры для gnome-menus (3.36.0-1ubuntu3) …
Обрабатываются триггеры для desktop-file-utils (0.26-1ubuntu3) …
hornet@hornet-VirtualBox:~$ dpkg -l | grep notepadqq
hornet@hornet-VirtualBox:~$ sudo apt-get autoremove
Чтение списков пакетов… Готово
Построение дерева зависимостей… Готово
Чтение информации о состоянии… Готово
Обновлено 0 пакетов, установлено 0 новых пакетов, для удаления отмечено 0 пакетов, и 140 пакетов не обновлено.
hornet@hornet-VirtualBox:~$
```

5. Выложить историю команд в терминале ubuntu

```shell
1461  cat > pets
1462  cat > pack_animals
1463  cat pets pack_animals > union_animals
1464  cat union_animals
1465  mv union_animals human_friends
1466  ls
1467  cat human_friends
1468  mkdir animal_nursery
1469  mv human_friends animal_nursery/
1470  ls animal_nursery/
1471  clear
1472  wget https://dev.mysql.com/get/mysql-apt-config_0.8.24-1_all.deb
1473  sudo dpkg -i mysql-apt-config_0.8.24-1_all.deb
1474  sudo apt update
1475  sudo apt-get install mysql-server
1476  systemctl status mysql
1477  apt download notepadqq
1478  sudo dpkg -i notepadqq_2.0.0~beta1-3_amd64.deb
1479  dpkg -l | grep notepadqq
1480  sudo dpkg -r notepadqq
1481  dpkg -l | grep notepadqq
1482  sudo apt-get autoremove
1483  history
```

6. Нарисовать диаграмму, в которой есть класс родительский класс, домашние
животные и вьючные животные, в составы которых в случае домашних
животных войдут классы: собаки, кошки, хомяки, а в класс вьючные животные
войдут: Лошади, верблюды и ослы).
<br><br>
![animals.jpg](animals.jpg)
<br><br>

7. В подключенном MySQL репозитории создать базу данных “Друзья
человека”

```mysql
CREATE DATABASE human_friends;
```

8. Создать таблицы с иерархией из диаграммы в БД

```shell
CREATE TABLE Animals (
    animals_id INT AUTO_INCREMENT PRIMARY KEY,
	animals_name VARCHAR(50)
);

CREATE TABLE Pets (
    pets_id INT AUTO_INCREMENT PRIMARY KEY,
    parent_id INT,
    pets_name VARCHAR(50),
    FOREIGN KEY (parent_id) REFERENCES Animals(animals_id) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE Pack_animals (
    pack_animals_id INT AUTO_INCREMENT PRIMARY KEY,
    parent_id INT,
    pack_animals_name VARCHAR(50),
    FOREIGN KEY (parent_id) REFERENCES Animals(animals_id) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE Dog (
    dog_id INT AUTO_INCREMENT PRIMARY KEY,
    kind_id INT,
    animal_name VARCHAR(50),
    animal_command VARCHAR(50),
    animal_birth DATE,
    FOREIGN KEY (kind_id) REFERENCES Pets(pets_id) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE Cat (
    cat_id INT AUTO_INCREMENT PRIMARY KEY,
    kind_id INT,
    animal_name VARCHAR(50),
    animal_command VARCHAR(50),
    animal_birth DATE,
    FOREIGN KEY (kind_id) REFERENCES Pets(pets_id) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE Hamster (
    hamster_id INT AUTO_INCREMENT PRIMARY KEY,
    kind_id INT,
    animal_name VARCHAR(50),
    animal_command VARCHAR(50),
    animal_birth DATE,
    FOREIGN KEY (kind_id) REFERENCES Pets(pets_id) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE Horse (
    horse_id INT AUTO_INCREMENT PRIMARY KEY,
    kind_id INT,
    animal_name VARCHAR(50),
    animal_command VARCHAR(50),
    animal_birth DATE,
    FOREIGN KEY (kind_id) REFERENCES Pack_animals(pack_animals_id) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE Camel (
    camel_id INT AUTO_INCREMENT PRIMARY KEY,
    kind_id INT,
    animal_name VARCHAR(50),
    animal_command VARCHAR(50),
    animal_birth DATE,
    FOREIGN KEY (kind_id) REFERENCES Pack_animals(pack_animals_id) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE Donkey (
    donkey_id INT AUTO_INCREMENT PRIMARY KEY,
    kind_id INT,
    animal_name VARCHAR(50),
    animal_command VARCHAR(50),
    animal_birth DATE,
    FOREIGN KEY (kind_id) REFERENCES Pack_animals(pack_animals_id) ON DELETE CASCADE ON UPDATE CASCADE
);
```

9. Заполнить низкоуровневые таблицы именами(животных), командами
которые они выполняют и датами рождения

```shell
INSERT INTO Animals (animals_name) VALUES 
('Pets'),
('Pack animals');

INSERT INTO Pets (parent_id, pets_name) VALUES 
(1, 'Dog'),
(1, 'Cat'),
(1, 'Hamster');

INSERT INTO Pack_animals (parent_id, pack_animals_name) VALUES 
(2, 'Horse'),
(2, 'Camel'),
(2, 'Donkey');

INSERT INTO Dog (kind_id, animal_name, animal_command, animal_birth) VALUES 
(1, 'Charlie', 'Roll over', '2021-09-21'),
(1, 'Buddy', 'Stay', '2017-11-04'),
(1, 'Luna', 'Voice', '2019-03-12'),
(1, 'Max', 'Apport', '2024-07-30'),
(1, 'Bailey', 'Sitdown', '2022-05-17');

INSERT INTO Cat (kind_id, animal_name, animal_command, animal_birth) VALUES
(2, 'Whiskers', 'Meow', '2019-08-14'),
(2, 'Smokey', 'Purr', '2022-12-02'),
(2, 'Mittens', 'Run', '2020-04-25'),
(2, 'Tiger', 'Stretch', '2023-10-07'),
(2, 'Shadow', 'Play', '2021-06-19');

INSERT INTO Hamster (kind_id, animal_name, animal_command, animal_birth) VALUES
(3, 'Nibbles', 'Running on wheel', '2024-01-05'),
(3, 'Cheeks', 'Burrowing', '2021-06-18'),
(3, 'Peanut', 'Exploring tubes', '2018-11-23'),
(3, 'Marshmallow', 'Sleep', '2023-09-10'),
(3, 'Cinnamon', 'Napping', '2022-03-27');

INSERT INTO Horse (kind_id, animal_name, animal_command, animal_birth) VALUES
(1, 'Thunder', 'Gallop', '2015-07-12'),
(1, 'Bella', 'Trot', '2021-04-28'),
(1, 'Spirit', 'Canter', '2023-02-03'),
(1, 'Shadowfax', 'Whinny', '2017-09-19'),
(1, 'Midnight', 'Run', '2021-11-25');

INSERT INTO Camel (kind_id, animal_name, animal_command, animal_birth) VALUES
(2, 'Sahara', 'Drinking', '2021-10-08'),
(2, 'Desert Rose', 'Walking', '2016-02-14'),
(2, 'Dune', 'Resting', '2018-04-30'),
(2, 'Nomad', 'Carrying cargo', '2019-08-22'),
(2, 'Mirage', 'Sleeping', '2024-01-17');

INSERT INTO Donkey (kind_id, animal_name, animal_command, animal_birth) VALUES
(3, 'Eeyore', 'Brake', '2023-05-10'),
(3, 'Burrito', 'Graze', '2017-02-15'),
(3, 'Jack', 'Carry load', '2019-11-20'),
(3, 'Jenny', 'Stand', '2016-08-25'),
(3, 'Pablo', 'Pull cart', '2020-03-30');
```

10. Удалив из таблицы верблюдов, т.к. верблюдов решили перевезти в другой
питомник на зимовку. Объединить таблицы лошади, и ослы в одну таблицу.

```shell
DELETE FROM Camel;

CREATE TABLE Ungulates (ungulates_id INT AUTO_INCREMENT PRIMARY KEY) AS
SELECT
    kind_id,
    animal_name AS ungulates_name,
    animal_command AS ungulates_command,
    animal_birth AS ungulates_birth
FROM Horse
UNION
SELECT
    kind_id,
    animal_name AS ungulates_name,
    animal_command AS ungulates_command,
    animal_birth AS ungulates_birth
FROM Donkey;
```

11. Создать новую таблицу “молодые животные” в которую попадут все
животные старше 1 года, но младше 3 лет и в отдельном столбце с точностью
до месяца подсчитать возраст животных в новой таблице

```shell
CREATE TABLE Young_animals (young_animals_id INT AUTO_INCREMENT PRIMARY KEY) AS
SELECT
	a.animals_name AS parent_class,
    p.pets_name AS type,
    animal_name AS name,
    animal_command AS command,
    TIMESTAMPDIFF(MONTH, animal_birth, CURDATE()) AS age_months
FROM Dog
JOIN Pets p ON kind_id = p.pets_id
JOIN Animals a ON p.parent_id = a.animals_id
WHERE TIMESTAMPDIFF(YEAR, animal_birth, CURDATE()) BETWEEN 1 AND 2
UNION
SELECT
	a.animals_name AS parent_class,
    p.pets_name AS type,
    animal_name AS name,
    animal_command AS command,
    TIMESTAMPDIFF(MONTH, animal_birth, CURDATE()) AS age_months
FROM Cat
JOIN Pets p ON kind_id = p.pets_id
JOIN Animals a ON p.parent_id = a.animals_id
WHERE TIMESTAMPDIFF(YEAR, animal_birth, CURDATE()) BETWEEN 1 AND 2
UNION
SELECT
	a.animals_name AS parent_class,
    p.pets_name AS type,
    animal_name AS name,
    animal_command AS command,
    TIMESTAMPDIFF(MONTH, animal_birth, CURDATE()) AS age_months
FROM Hamster
JOIN Pets p ON kind_id = p.pets_id
JOIN Animals a ON p.parent_id = a.animals_id
WHERE TIMESTAMPDIFF(YEAR, animal_birth, CURDATE()) BETWEEN 1 AND 2
UNION
SELECT
	a.animals_name AS parent_class,
    pa.pack_animals_name AS type,
    animal_name AS name,
    animal_command AS command,
    TIMESTAMPDIFF(MONTH, animal_birth, CURDATE()) AS age_months
FROM Horse
JOIN Pack_animals pa ON kind_id = pa.pack_animals_id
JOIN Animals a ON pa.parent_id = a.animals_id
WHERE TIMESTAMPDIFF(YEAR, animal_birth, CURDATE()) BETWEEN 1 AND 2
UNION
SELECT
	a.animals_name AS parent_class,
    pa.pack_animals_name AS type,
    animal_name AS name,
    animal_command AS command,
    TIMESTAMPDIFF(MONTH, animal_birth, CURDATE()) AS age_months
FROM Camel
JOIN Pack_animals pa ON kind_id = pa.pack_animals_id
JOIN Animals a ON pa.parent_id = a.animals_id
WHERE TIMESTAMPDIFF(YEAR, animal_birth, CURDATE()) BETWEEN 1 AND 2
UNION
SELECT
	a.animals_name AS parent_class,
    pa.pack_animals_name AS type,
    animal_name AS name,
    animal_command AS command,
    TIMESTAMPDIFF(MONTH, animal_birth, CURDATE()) AS age_months
FROM Donkey
JOIN Pack_animals pa ON kind_id = pa.pack_animals_id
JOIN Animals a ON pa.parent_id = a.animals_id
WHERE TIMESTAMPDIFF(YEAR, animal_birth, CURDATE()) BETWEEN 1 AND 2;
```

12. Объединить все таблицы в одну, при этом сохраняя поля, указывающие на
прошлую принадлежность к старым таблицам.

```shell
CREATE TABLE Union_animals (union_animals_id INT AUTO_INCREMENT PRIMARY KEY) AS
SELECT
	a.animals_name AS parent_class,
    p.pets_name AS type,
    animal_name AS name,
    animal_command AS command,
    animal_birth AS birth
FROM Dog
JOIN Pets p ON kind_id = p.pets_id
JOIN Animals a ON p.parent_id = a.animals_id
UNION
SELECT
	a.animals_name AS parent_class,
    p.pets_name AS type,
    animal_name AS name,
    animal_command AS command,
    animal_birth AS birth
FROM Cat
JOIN Pets p ON kind_id = p.pets_id
JOIN Animals a ON p.parent_id = a.animals_id
UNION
SELECT
	a.animals_name AS parent_class,
    p.pets_name AS type,
    animal_name AS name,
    animal_command AS command,
    animal_birth AS birth
FROM Hamster
JOIN Pets p ON kind_id = p.pets_id
JOIN Animals a ON p.parent_id = a.animals_id
UNION
SELECT
	a.animals_name AS parent_class,
    pa.pack_animals_name AS type,
    animal_name AS name,
    animal_command AS command,
    animal_birth AS birth
FROM Horse
JOIN Pack_animals pa ON kind_id = pa.pack_animals_id
JOIN Animals a ON pa.parent_id = a.animals_id
UNION
SELECT
	a.animals_name AS parent_class,
    pa.pack_animals_name AS type,
    animal_name AS name,
    animal_command AS command,
    animal_birth AS birth
FROM Camel
JOIN Pack_animals pa ON kind_id = pa.pack_animals_id
JOIN Animals a ON pa.parent_id = a.animals_id
UNION
SELECT
	a.animals_name AS parent_class,
    pa.pack_animals_name AS type,
    animal_name AS name,
    animal_command AS command,
    animal_birth AS birth
FROM Donkey
JOIN Pack_animals pa ON kind_id = pa.pack_animals_id
JOIN Animals a ON pa.parent_id = a.animals_id;
```

13. Создать класс с Инкапсуляцией методов и наследованием по диаграмме.

```python
class Animals:
    def __init__(self, animals_name):
        self.animals_name = animals_name

    def get_animals_name(self):
        return self.animals_name
```
```python
from animals.animals import Animals

class Pets(Animals):
    def __init__(self, animals_name, pets_name):
        super().__init__(animals_name)
        self.pets_name = pets_name
```
```python
from animals.animals import Animals

class PackAnimals(Animals):
    def __init__(self, animals_name, pack_animals_name):
        super().__init__(animals_name)
        self.pack_animals_name = pack_animals_name
```
```python
from animals.pets import Pets

class Dog(Pets):
    def __init__(self, animals_name, pets_name, animal_name, animal_command, animal_birth):
        super().__init__(animals_name, pets_name)
        self.animal_name = animal_name
        self.animal_command = animal_command
        self.animal_birth = animal_birth
```
```python
from animals.pets import Pets

class Cat(Pets):
    def __init__(self, animals_name, pets_name, animal_name, animal_command, animal_birth):
        super().__init__(animals_name, pets_name)
        self.animal_name = animal_name
        self.animal_command = animal_command
        self.animal_birth = animal_birth
```
```python
from animals.pets import Pets

class Hamster(Pets):
    def __init__(self, animals_name, pets_name, animal_name, animal_command, animal_birth):
        super().__init__(animals_name, pets_name)
        self.animal_name = animal_name
        self.animal_command = animal_command
        self.animal_birth = animal_birth
```
```python
from animals.pack_animals import PackAnimals

class Horse(PackAnimals):
    def __init__(self, animals_name, pack_animals_name, animal_name, animal_command, animal_birth):
        super().__init__(animals_name, pack_animals_name)
        self.animal_name = animal_name
        self.animal_command = animal_command
        self.animal_birth = animal_birth
```
```python
from animals.pack_animals import PackAnimals

class Camel(PackAnimals):
    def __init__(self, animals_name, pack_animals_name, animal_name, animal_command, animal_birth):
        super().__init__(animals_name, pack_animals_name)
        self.animal_name = animal_name
        self.animal_command = animal_command
        self.animal_birth = animal_birth
```
```python
from animals.pack_animals import PackAnimals

class Donkey(PackAnimals):
    def __init__(self, animals_name, pack_animals_name, animal_name, animal_command, animal_birth):
        super().__init__(animals_name, pack_animals_name)
        self.animal_name = animal_name
        self.animal_command = animal_command
        self.animal_birth = animal_birth
```

14. Написать программу, имитирующую работу реестра домашних животных.
В программе должен быть реализован следующий функционал:
    - Завести новое животное
    - определять животное в правильный класс
    - увидеть список команд, которое выполняет животное
    - обучить животное новым командам
    - Реализовать навигацию по меню
15. Создайте класс Счетчик, у которого есть метод add(), увеличивающий̆
значение внутренней̆int переменной̆на 1 при нажатие “Завести новое
животное” Сделайте так, чтобы с объектом такого типа можно было работать в
блоке try-with-resources. Нужно бросить исключение, если работа с объектом
типа счетчик была не в ресурсном try и/или ресурс остался открыт. Значение
считать в ресурсе try, если при заведения животного заполнены все поля.