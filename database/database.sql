use league;


/*DROP TABLE match_subscription;*/
/*DROP TABLE match_status;*/
/*DROP TABLE matches;*/



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
    FOREIGN KEY(match_id) REFERENCES today_matches(match_id)
);

create table match_subscription(
    user_id int not null, 
    match_id int not null,
    FOREIGN KEY(match_id) REFERENCES today_matches(match_id),
    CONSTRAINT PK_subscription PRIMARY KEY (user_id,match_id)
);