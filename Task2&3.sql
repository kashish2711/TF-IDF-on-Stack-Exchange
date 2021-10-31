## Creating Table

CREATE TABLE IF NOT EXISTS STACK_POSTS
(
Id int, PostTypeId tinyint, 
AcceptedAnswerId int, CreationDate timestamp, 
Score int, ViewCount int, 
Body string, OwnerUserId int, 
OwnerDisplayName varchar(40), LastEditorUserId int, 
LastEditorDisplayName varchar(40), LastEditDate timestamp, 
LastActivityDate timestamp, Title varchar (250), 
Tags varchar (250), AnswerCount int, 
CommentCount int, FavoriteCount int, 
ClosedDate timestamp, CommunityOwnedDate timestamp, 
ContentLicense varchar (12)
) 
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.OpenCSVSerde'
TBLPROPERTIES("SKIP.HEADER.LINE.COUNT"="1");

## Loading Data

LOAD DATA INPATH 
“gs://dataproc-staging-europe-west2-434500979019-mtxch6f3/google-cloud-dataproc-metainfo/ca675-assgn1/DataSet.csv” 
INTO TABLE STACK_POSTS;

## Creating a View

CREATE VIEW IF NOT EXISTS STACK_POSTS_VIEW as 
select cast(Id as int) as Id, cast(PostTypeId as tinyint) as PostTypeId, 
AcceptedAnswerId, CreationDate, cast(Score as int) as Score, 
cast(ViewCount as int) as ViewCount, Body, 
cast(OwnerUserId as int) as OwnerUserId, OwnerDisplayName as DisplayName,
LastEditorUserId, LastEditorDisplayName , LastEditDate , LastActivityDate , 
Title , Tags , AnswerCount , CommentCount , FavoriteCount , 
ClosedDate , CommunityOwnedDate , ContentLicense 
from STACK_POSTS;

## Query 1

SELECT SCORE, OWNERUSERID, TITLE FROM STACK_POSTS_VIEW ORDER BY SCORE DESC LIMIT 10;

## Query 2

SELECT OWNERUSERID, SUM(SCORE) AS SCORE FROM STACK_POSTS_VIEW WHERE OWNERUSERID IS NOT NULL GROUP BY OWNERUSERID ORDER BY SCORE DESC LIMIT 10;

## Query 3

SELECT COUNT(DISTINCT OWNERUSERID) FROM STACK_POSTS_VIEW WHERE UPPER(BODY) LIKE '%CLOUD%' OR UPPER(TITLE) LIKE '%CLOUD%';
