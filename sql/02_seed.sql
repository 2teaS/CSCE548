USE csce548_watchlist;

-- USERS (10)
INSERT INTO users (username, email) VALUES
('alex','alex@example.com'),
('blake','blake@example.com'),
('casey','casey@example.com'),
('drew','drew@example.com'),
('emma','emma@example.com'),
('frank','frank@example.com'),
('gwen','gwen@example.com'),
('hayden','hayden@example.com'),
('iris','iris@example.com'),
('jordan','jordan@example.com');

-- MOVIES (20)
INSERT INTO movies (title, release_year, runtime_minutes, genre) VALUES
('The Matrix',1999,136,'Sci-Fi'),
('Inception',2010,148,'Sci-Fi'),
('Interstellar',2014,169,'Sci-Fi'),
('The Dark Knight',2008,152,'Action'),
('Parasite',2019,132,'Thriller'),
('Spirited Away',2001,125,'Animation'),
('The Godfather',1972,175,'Crime'),
('Pulp Fiction',1994,154,'Crime'),
('Fight Club',1999,139,'Drama'),
('The Shawshank Redemption',1994,142,'Drama'),
('Whiplash',2014,107,'Drama'),
('Get Out',2017,104,'Horror'),
('Arrival',2016,116,'Sci-Fi'),
('Toy Story',1995,81,'Animation'),
('The Social Network',2010,120,'Drama'),
('Mad Max: Fury Road',2015,120,'Action'),
('La La Land',2016,128,'Musical'),
('The Grand Budapest Hotel',2014,99,'Comedy'),
('Knives Out',2019,130,'Mystery'),
('Dune',2021,155,'Sci-Fi');

-- LISTS (10) (one per user for easy demo)
INSERT INTO lists (user_id, name, description, is_public) VALUES
(1,'Watchlist','Stuff I want to watch',TRUE),
(2,'Top Picks','My favorites',FALSE),
(3,'Weekend Movies','For the weekend',TRUE),
(4,'Sci-Fi Queue','Sci-fi marathon',FALSE),
(5,'Animation','Animated films',TRUE),
(6,'Thrillers','Edge of seat',FALSE),
(7,'Classics','Must-see classics',TRUE),
(8,'Rewatch','Movies to rewatch',FALSE),
(9,'Date Night','Easy wins',TRUE),
(10,'Awards','Award winners',FALSE);

-- LIST ITEMS (20) (2 items per list)
-- Note: WATCHED items must have watched_on date.
INSERT INTO list_items (list_id, movie_id, status, watched_on, notes) VALUES
(1,1,'WATCHED','2026-01-12','Still holds up'),
(1,2,'PLANNED',NULL,''),
(2,4,'WATCHED','2026-01-05','Amazing'),
(2,10,'PLANNED',NULL,''),
(3,19,'WATCHING',NULL,''),
(3,5,'PLANNED',NULL,''),
(4,3,'PLANNED',NULL,''),
(4,13,'WATCHED','2026-01-20','Great atmosphere'),
(5,6,'WATCHED','2026-01-02','Beautiful'),
(5,14,'PLANNED',NULL,''),
(6,12,'WATCHED','2026-01-18','Creepy'),
(6,5,'PLANNED',NULL,''),
(7,7,'PLANNED',NULL,''),
(7,8,'WATCHED','2026-01-08','Iconic'),
(8,9,'WATCHED','2026-01-10','Rewatching soon'),
(8,16,'PLANNED',NULL,''),
(9,17,'PLANNED',NULL,''),
(9,18,'WATCHED','2026-01-25','Fun'),
(10,11,'WATCHED','2026-01-03','Incredible'),
(10,20,'PLANNED',NULL,'');

-- RATINGS (10)
INSERT INTO ratings (user_id, movie_id, stars, review) VALUES
(1,1,5,'Classic sci-fi.'),
(2,4,5,'Best superhero movie.'),
(3,5,5,'So well made.'),
(4,3,4,'A little long but great.'),
(5,6,5,'Masterpiece.'),
(6,12,4,'Smart horror.'),
(7,7,5,'Legendary.'),
(8,16,4,'Nonstop action.'),
(9,18,4,'Stylish and funny.'),
(10,11,5,'Intense and rewarding.');

