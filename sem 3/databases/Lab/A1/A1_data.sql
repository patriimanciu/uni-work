USE Music;
GO


INSERT INTO Users (Username, Email, PasswordHash, DateCreated)
VALUES 
    ('queen_bey', 'emily.queenbey@yahoo.com', 'hash_beyhive456', '2024-01-02'),
    ('drizzy_fanatic', 'mike.rapgod@gmail.com', 'hash_drake789', '2024-01-03'),
    ('rolling_in_deep', 'sarah.deepdiver@yahoo.com', 'hash_adele987', '2024-01-04'),
    ('johnsmith', 'john.smith@gmail.com', 'hash_john123', '2024-01-01'),
    ('emily_jones', 'emily.jones@yahoo.com', 'hash_emily456', '2024-01-02'),
    ('michael_brown', 'michael.brown@gmail.com', 'hash_michael789', '2024-01-03'),
    ('sarah_miller', 'sarah.miller@yahoo.com', 'hash_sarah987', '2024-01-04'),
    ('daniel_jackson', 'daniel.jackson@gmail.com', 'hash_daniel654', '2024-01-05'),
    ('laura_wilson', 'laura.wilson@yahoo.com', 'hash_laura321', '2024-01-06'),
    ('alex_kim', 'alex.kim@gmail.com', 'hash_alex111', '2024-01-07'),
    ('jessica_lee', 'jessica.lee@yahoo.com', 'hash_jessica222', '2024-01-08'),
    ('kevin_clark', 'kevin.clark@gmail.com', 'hash_kevin333', '2024-01-09'),
    ('olivia_martin', 'olivia.martin@yahoo.com', 'hash_olivia444', '2024-01-10');


INSERT INTO Artists (ArtistName, Bio, DateAdded) 
VALUES
    ('The Beatles', 'Legendary British rock band from Liverpool, formed in 1960.', '2024-01-01'),
    ('Beyoncé', 'American singer, songwriter, and actress, regarded as one of the greatest entertainers of all time.', '2024-01-02'),
    ('Drake', 'Canadian rapper, singer, and actor known for blending hip hop, R&B, and pop genres.', '2024-01-03'),
    ('Adele', 'English singer-songwriter known for her powerful voice and emotive ballads.', '2024-01-04'),
    ('Ed Sheeran', 'English singer-songwriter known for his acoustic pop and folk influences.', '2024-01-05'),
    ('Taylor Swift', 'American singer-songwriter who shifted from country to pop and indie-folk genres.', '2024-01-06'),
    ('Kanye West', 'American rapper, record producer, and fashion designer known for pushing the boundaries of hip-hop.', '2024-01-07'),
    ('Billie Eilish', 'American singer-songwriter who rose to prominence with her unique sound blending pop, electropop, and alternative.', '2024-01-08'),
    ('Rihanna', 'Barbadian singer, actress, and businesswoman known for her versatility in pop and R&B.', '2024-01-09'),
    ('Bruno Mars', 'American singer-songwriter and performer known for his wide range of musical styles from pop to funk and R&B.', '2024-01-10'),
    ('The Weeknd', 'Canadian singer, songwriter, and producer known for his dark wave and pop sound.', '2024-01-11'),
    ('Ariana Grande', 'American pop singer and actress with a powerful voice and a career that spans from TV to chart-topping hits.', '2024-01-12'),
    ('Post Malone', 'American rapper and singer known for his genre-blending music that spans hip-hop, rock, and pop.', '2024-01-14'),
    ('Dua Lipa', 'English singer-songwriter known for her dance-pop and electro-pop hits.', '2024-01-15'),
    ('BTS', 'South Korean boy band known for their global influence, blending pop, hip hop, and R&B.', '2024-01-16'),
    ('BLACKPINK', 'Popular South Korean girl group known for their mix of K-pop, EDM, and hip hop.', '2024-01-17'),
    ('EXO', 'South Korean-Chinese boy band known for their unique blend of pop, R&B, and hip hop.', '2024-01-18'),
    ('TWICE', 'South Korean girl group famous for their catchy pop songs and synchronized choreography.', '2024-01-19'),
    ('Stray Kids', 'South Korean boy group known for their self-produced music and experimental style in K-pop and hip hop.', '2024-01-20');


INSERT INTO Genre (GenreName)
VALUES
    ('Pop'),
    ('Rock'),
    ('Hip-Hop'),
    ('R&B'),
    ('K-Pop');


INSERT INTO Albums (AlbumName, ReleaseDate, ArtistID, GenreID)
VALUES 
    ('Abbey Road', '1969-09-26', 1020, 1007),
    ('Sgt. Peppers Lonely Hearts Club Band', '1967-05-26',1020, 1007),
    ('Revolver', '1966-08-05',1020, 1007),
    ('Lemonade', '2016-04-23',1021, 1009),
    ('4', '2011-06-24',1021, 1009),
    ('Beyoncé', '2013-12-13',1021, 1006),
    ('Take Care', '2011-11-15',1022, 1008),
    ('Nothing Was the Same', '2013-09-24',1022, 1008),
    ('Scorpion', '2018-06-29',1022, 1008),
    ('21', '2011-01-24',1023, 1006),
    ('25', '2015-11-20',1023, 1006),
    ('30', '2021-11-19',1023, 1006),
    ('÷ (Divide)', '2017-03-03',1024, 1006),
    ('x (Multiply)', '2014-06-20',1024, 1006),
    ('= (Equals)', '2021-10-29',1024, 1006),
    ('1989', '2014-10-27',1025, 1006),
    ('Red', '2012-10-22',1025, 1006),
    ('Folklore', '2020-07-24',1025, 1006),
    ('The College Dropout', '2004-02-10', 1026, 1008),
    ('My Beautiful Dark Twisted Fantasy', '2010-11-22', 1026, 1008),
    ('Ye', '2018-06-01', 1026, 1008),
    ('When We All Fall Asleep, Where Do We Go?', '2019-03-29', 1027, 1006),
    ('Happier Than Ever', '2021-07-30', 1027, 1006),
    ('Anti', '2016-01-28', 1028, 1009),
    ('Loud', '2010-11-12', 1028, 1006),
    ('Good Girl Gone Bad', '2007-05-31', 1028, 1006),
    ('Doo-Wops & Hooligans', '2010-10-05', 1029, 1006),
    ('24K Magic', '2016-11-18', 1029, 1009),
    ('Unorthodox Jukebox', '2012-12-07', 1029, 1006),
    ('After Hours', '2020-03-20', 1030, 1009),
    ('Starboy', '2016-11-25', 1030, 1006),
    ('Beauty Behind the Madness', '2015-08-28', 1030, 1009),
    ('Thank U, Next', '2019-02-08', 1031, 1006),
    ('Positions', '2020-10-30', 1031, 1006),
    ('Sweetener', '2018-08-17', 1031, 1006),
    ('Hollywoods Bleeding', '2019-09-06', 1032, 1008),
    ('Beerbongs & Bentleys', '2018-04-27', 1032, 1008),
    ('Stoney', '2016-12-09', 1032, 1008),
    ('Future Nostalgia', '2020-03-27', 1033, 1006),
    ('Dua Lipa', '2017-06-02', 1033, 1006),
    ('Map of the Soul: 7', '2020-02-21', 1034, 1010),
    ('BE', '2020-11-20', 1034, 1010),
    ('Love Yourself: Tear', '2018-05-18', 1034, 1010),
    ('The Album', '2020-10-02', 1035, 1010),
    ('Square Up', '2018-06-15', 1035, 1010),
    ('Don’t Mess Up My Tempo', '2018-11-02', 1036, 1010),
    ('EXODUS', '2015-03-30', 1036, 1010),
    ('Eyes Wide Open', '2020-10-26', 1037, 1010),
    ('Fancy You', '2019-04-22', 1037, 1010),
    ('NOEASY', '2021-08-23', 1038, 1010),
    ('IN生 (IN LIFE)', '2020-09-14', 1038, 1010);

INSERT INTO Tracks (TrackName, Duration, AlbumId)
VALUES 
    ('Come Together', 259, 52),   -- Track from Abbey Road
    ('Something', 182, 52),        -- Track from Abbey Road
    ('Hey Jude', 431, 54),         -- Revolver by The Beatles
    ('Single Ladies', 238, 55),    -- Lemonade by Beyoncé
    ('Halo', 264, 55),             -- Lemonade by Beyoncé
    ('Drunk In Love', 272, 57),    -- Beyoncé by Beyoncé
    ('Take Care', 313, 58),        -- Take Care by Drake
    ('Marvins Room', 265, 58),     -- Take Care by Drake
    ('God’s Plan', 198, 59),       -- Nothing Was the Same by Drake
    ('One Dance', 182, 59),        -- Nothing Was the Same by Drake
    ('Someone Like You', 285, 61), -- 21 by Adele
    ('Rolling In The Deep', 228, 61), -- 21 by Adele
    ('Perfect', 263, 64),         -- ÷ (Divide) by Ed Sheeran
    ('Shape of You', 233, 64),    -- ÷ (Divide) by Ed Sheeran
    ('Bad Guy', 194, 73),         -- When We All Fall Asleep by Billie Eilish
    ('Bury A Friend', 239, 73),   -- When We All Fall Asleep by Billie Eilish
    ('Diamonds', 238, 75),        -- Anti by Rihanna
    ('Work', 214, 75),            -- Anti by Rihanna
    ('Uptown Funk', 269, 80),     -- Unorthodox Jukebox by Bruno Mars
    ('Locked Out of Heaven', 223, 80), -- Unorthodox Jukebox by Bruno Mars
    ('Blinding Lights', 201, 81), -- After Hours by The Weeknd
    ('Save Your Tears', 215, 81), -- After Hours by The Weeknd
    ('Rockstar', 355, 87),        -- Hollywood's Bleeding by Post Malone
    ('Circles', 229, 87),         -- Hollywood's Bleeding by Post Malone
    ('Levitating', 203, 90),      -- Future Nostalgia by Dua Lipa
    ('Physical', 230, 90),        -- Future Nostalgia by Dua Lipa
    ('Dynamite', 198, 92),        -- Map of the Soul: 7 by BTS
    ('Boy With Luv', 243, 92),    -- Map of the Soul: 7 by BTS
    ('How You Like That', 210, 95), -- The Album by BLACKPINK
    ('Lovesick Girls', 210, 92);  -- The Album by BLACKPINK

INSERT INTO Playlists (PlaylistName, UserId)
VALUES 
    ('Beatles Classics', 2017),    -- Playlist for rolling_in_deep 
    ('Drake Vibes', 2019),         -- Playlist for emily_jones
    ('Adele Hits', 2017),          -- Playlist for rolling_in_deep 
    ('Beyoncé Essentials', 2018),  -- Playlist for johnsmith 
    ('Chill with Ed', 2019),       -- Playlist for emily_jones 
    ('Post Malone Favorites', 2020), -- Playlist for michael_brown 
    ('Pop Hits', 2021),            -- Playlist for sarah_miller 
    ('Weekend Vibes', 2022),       -- Playlist for daniel_jackson 
    ('Rihanna All Day', 2023),     -- Playlist for laura_wilson
    ('Indie Pop Gems', 2024),     -- Playlist for alex_kim 
    ('Rock Anthems', 2025),       -- Playlist for jessica_lee
    ('K-Pop Essentials', 2026);   -- Playlist for kevin_clark


INSERT INTO Playlist_Tracks (PlaylistID, TrackID)
VALUES  
    -- Beatles Classics (rolling_in_deep)
    (1, 1), -- Come Together
    (1, 2), -- Something
    (1, 3), -- Hey Jude
    
    -- Drake Vibes (emily_jones)
    (2, 7), -- Take Care
    (2, 9), -- God's Plan
    (2, 10), -- One Dance
    
    -- Adele Hits (rolling_in_deep)
    (3, 11), -- Someone Like You
    (3, 12), -- Rolling In The Deep
    
    -- Beyoncé Essentials (johnsmith)
    (4, 4), -- Single Ladies
    (4, 5), -- Halo
    (4, 6), -- Drunk In Love

    -- Chill with Ed (emily_jones)
    (5, 13), -- Perfect
    (5, 14), -- Shape of You
    
    -- Pop Hits (sarah_miller)
    (7, 19), -- Uptown Funk
    (7, 20), -- Locked Out of Heaven
    (7, 21), -- Blinding Lights
    (7, 22), -- Save Your Tears
    (7, 15),
    (7, 14),
    
    -- Weekend Vibes (daniel_jackson)
    (8, 25), -- Levitating
    (8, 26), -- Physical
    
    -- Rihanna All Day (laura_wilson)
    (9, 17), -- Diamonds
    (9, 18), -- Work
    
    -- Indie Pop Gems (alex_kim)
    (10, 27), -- Dynamite
    (10, 28), -- Boy With Luv
    
    -- Rock Anthems (jessica_lee)
    (11, 29), -- How You Like That
    (11, 30), -- Lovesick Girls
    
    -- K-Pop Essentials (kevin_clark)
    (12, 29), -- How You Like That
    (12, 30); -- Lovesick Girls


INSERT INTO User_Favorites (UserID, TrackID)
VALUES 
    (2017, 1),    -- rolling_in_deep likes "Come Together" from Abbey Road
    (2017, 2),    -- rolling_in_deep likes "Something" from Abbey Road
    (2018, 7),    -- johnsmith likes "Take Care" from Take Care
    (2018, 8),    -- johnsmith likes "Marvins Room" from Take Care
    (2019, 11),   -- emily_jones likes "Someone Like You" from 21
    (2019, 12),   -- emily_jones likes "Rolling In The Deep" from 21
    (2020, 4),    -- michael_brown likes "Single Ladies" from Lemonade
    (2020, 5),    -- michael_brown likes "Halo" from Lemonade
    (2021, 12),   -- sarah_miller likes "Shape of You" from ÷ (Divide)
    (2021, 13),   -- sarah_miller likes "Perfect" from ÷ (Divide)
    (2022, 17),   -- daniel_jackson likes "Diamonds" from Anti
    (2022, 18),   -- daniel_jackson likes "Work" from Anti
    (2023, 21),   -- laura_wilson likes "Blinding Lights" from After Hours
    (2023, 22),   -- laura_wilson likes "Save Your Tears" from After Hours
    (2024, 19),   -- alex_kim likes "Uptown Funk" from Unorthodox Jukebox
    (2024, 20),   -- alex_kim likes "Locked Out of Heaven" from Unorthodox Jukebox
    (2025, 23),   -- jessica_lee likes "Rockstar" from Hollywoods Bleeding
    (2025, 24),   -- jessica_lee likes "Circles" from Hollywoods Bleeding
    (2026, 25),   -- kevin_clark likes "Levitating" from Future Nostalgia
    (2026, 26),   -- kevin_clark likes "Physical" from Future Nostalgia
    (2027, 27),   -- olivia_martin likes "Dynamite" from Map of the Soul: 7
    (2027, 28),   -- olivia_martin likes "Boy With Luv" from Map of the Soul: 7
    (2017, 29),   -- rolling_in_deep likes "How You Like That" from The Album
    (2017, 30),   -- rolling_in_deep likes "Lovesick Girls" from The Album
    (2027, 12),   -- olivia_martin likes "Shape of You" from ÷ (Divide)
    (2021, 28),   -- sarah_miller likes "Boy With Luv" from Map of the Soul: 7
    (2021, 11),   -- sarah_miller likes "Someone Like You" from 21
    (2027, 11);   -- olivia_martin likes "Someone Like You" from 21
    

-- Violation of referential integrity 
INSERT INTO Albums (AlbumName, ReleaseDate, ArtistID, GenreID)
    VALUES ('Fake Album', '2023-01-01', 9999, 1006);

-- Updates
UPDATE Users
SET Email = 'emily.jones_UPDATED@yahoo.com'
WHERE Username = 'emily_jones' AND Email LIKE '%yahoo.com';

UPDATE Albums
SET ReleaseDate = '2021-11-20'
WHERE AlbumName = 'After Hours' AND ReleaseDate IS NOT NULL AND ReleaseDate BETWEEN '2020-01-01' AND '2023-12-31';

UPDATE Artists
SET Bio = 'UPDATE: Canadian rapper and singer, recognized for his versatility and influence in contemporary music.'
WHERE ArtistName = 'Drake';

-- Deletes
DELETE FROM Users
WHERE Username = 'queen_bey' OR Email = 'mike.rapgod@gmail.com';

DELETE FROM Albums
WHERE AlbumName = 'Starboy'