create database league;
use league;

create table match_status(
    match_id int not null primary key,
    team_one_score int,
    team_two_score int,
    last_updated datetime,
    start_time datetime
);

create table match_subscription(
    user_id int not null, 
    match_id int not null,
    FOREIGN KEY(match_id) REFERENCES match_status(match_id),
    CONSTRAINT PK_subscription PRIMARY KEY (user_id,match_id)
);