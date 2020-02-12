use league;



create table today_matches(
    match_id int not null primary key,
    team_one varchar(50),
    team_two varchar(50),
    start_time datetime
);

create table match_status(
    match_id int not null primary key,
    team_one_score int default 0,
    team_two_score int  default 0,
    last_updated datetime,
    FOREIGN KEY(match_id) REFERENCES today_matches(match_id)
);

create table match_subscription(
    user_id int not null, 
    match_id int not null,
    FOREIGN KEY(match_id) REFERENCES today_matches(match_id),
    CONSTRAINT PK_subscription PRIMARY KEY (user_id,match_id)
);