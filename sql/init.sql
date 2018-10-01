
create table channels (
    Id serial PRIMARY KEY,
    TelegramId bigint UNIQUE not null,
    Name varchar(500),
    ShortName varchar(500),
    LastSyncTime timestamp,
    LastReadMessageId bigint,
    Active bool default true
);

create table messages (
    Id serial PRIMARY KEY,
    TelegramId bigint UNIQUE not null,
    Message text,
    AdditionalData text,
    ChannelId integer REFERENCES channels (Id),
    UNIQUE(TelegramId, ChannelId)
);