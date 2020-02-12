use league;


DROP TABLE match_subscription;
DROP TABLE match_status;
DROP TABLE matches;


create table matches(
    match_id int not null primary key,
    home_team varchar(50),
    visitor_team varchar(50),
    start_time DATETIME,
    day_date DATE,
    match_status int
);

create table match_status(
    match_id int not null primary key,
    home_team_score int default 0,
    visitor_team_score int  default 0,
    last_updated datetime,
    CHANGED BOOLEAN,
    FOREIGN KEY(match_id) REFERENCES matches(match_id)
);

create table match_subscription(
    user_id int not null, 
    match_id int not null,
    FOREIGN KEY(match_id) REFERENCES matches(match_id),
    CONSTRAINT PK_subscription PRIMARY KEY (match_id,user_id)
);


CREATE TABLE Teams(
	team_id INT,
	team_name VARCHAR(50) PRIMARY KEY,
	team_nickname VARCHAR(50),
	team_logo VARCHAR(100)
);


CREATE TABLE favorite_teams(
	team_name VARCHAR(50),
	user_id INT,
	FOREIGN KEY(team_name) REFERENCES Teams(team_name),
   CONSTRAINT PK_favorite PRIMARY KEY (team_name,user_id)
);


