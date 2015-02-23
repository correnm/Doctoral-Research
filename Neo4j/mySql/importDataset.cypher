//create PEOPLE from the dataset
USING PERIODIC COMMIT
LOAD CSV WITH HEADERS FROM 'file:///C:/Users/Corren/Documents/Neo4j/mySql/dataset.csv' as row
CREATE (:People {dataset_pk: row.dataset_pk,	
first_name: row.first_name,	 
last_name: row.last_name,
linkedin_public_profile: row.linkedin_public_profile, 
twitter_account: row.twitter_account});

//create alternative names
USING PERIODIC COMMIT
LOAD CSV WITH HEADERS FROM 'file:///C:/Users/Corren/Documents/Neo4j/MySql/dataset_alt_names.csv' as row
CREATE (:PeopleNames {
alt_name_pk: row.alt_name_pk,
dataset_pk: row.dataset_pk,	
first_name: row.first_name,	 
last_name: row.last_name,
name_type: row.name_type});

//create linkedin public profiles
USING PERIODIC COMMIT
LOAD CSV WITH HEADERS FROM 'file:///C:/Users/Corren/Documents/Neo4j/mySql/linkedin.csv' as row
CREATE (:Linkedin {
linkedin_pk: row.linkedin_pk,
dataset_pk: row.dataset_pk,	
full_name: row.full_name,	 
title: row.title,
url: row.url,
search_name: row.search_name,
search_engine: row.search_engine});

//create linkedin people also viewed
USING PERIODIC COMMIT
LOAD CSV WITH HEADERS FROM 'file:///C:/Users/Corren/Documents/Neo4j/mySql/linkedin_pav.csv' as row
CREATE (:Linkedin_PAV{
pav_pk: row.pav_pk,
linkedin_pk: row.linkedin_pk,
full_name: row.full_name,	 
degree: row.degree,
title: row.title,
url: row.url,
parent_pav_pk: row.parent_pav_pk});

//create linkedin affiliation
USING PERIODIC COMMIT
LOAD CSV WITH HEADERS FROM 'file:///C:/Users/Corren/Documents/Neo4j/mySql/linkedin_affiliation.csv' as row
CREATE (:Linkedin_Affiliation{
affiliation_pk: row.affiliation_pk,
linkedin_pk: row.linkedin_pk,
affiliation_name: row.affiliation_name});


// Add indexes so searches are fast
CREATE INDEX ON :People(dataset_pk);
CREATE INDEX ON :PeopleNames(dataset_pk);
CREATE INDEX ON :Linkedin(dataset_pk);
CREATE INDEX on :Linkedin(linkedin_pk);
CREATE INDEX ON :Linkedin_PAV(linkedin_pk);
CREATE INDEX ON :Linkedin_PAV(pav_pk);
CREATE INDEX ON :Linkedin_PAV(parent_pav_pk);
CREATE INDEX ON :Linkedin_PAV(degree);
CREATE INDEX on :Linkedin_Affiliation(linkedin_pk);

//relationships
MATCH (a:People), (b:PeopleNames)
WHERE a.dataset_pk = b.dataset_pk
MERGE (a)-[r:KNOWN_AS]->(b)
RETURN r;

MATCH (a:People), (b:Linkedin)
WHERE a.dataset_pk = b.dataset_pk
MERGE (a)-[r:LINKED_IN]->(b)
RETURN r;

MATCH (a:Linkedin),(b:Linkedin_PAV)
WHERE a.linkedin_pk = b.linkedin_pk
MERGE (a)-[r:ALSO_VIEWED]->(b)
RETURN r;

MATCH (a:Linkedin),(b:Linkedin_PAV)
WHERE a.linkedin_pk = b.linkedin_pk
and b.degree='1'
MERGE (a)-[r:FIRST_DEGREE]->(b)
RETURN r;

MATCH (a:Linkedin),(b:Linkedin_Affiliation)
WHERE a.linkedin_pk = b.linkedin_pk
MERGE (a)-[r:ATTENDED]->(b)
RETURN r;

MATCH (a:Linkedin_PAV),(b:Linkedin_PAV)
where a.pav_pk = b.parent_pav_pk
and a.degree='1'
and b.degree='2'
MERGE (a)-[r:SECOND_DEGREE]->(b)
return r;

MATCH (a:Linkedin_PAV),(b:Linkedin_PAV)
where a.pav_pk = b.parent_pav_pk
and a.degree='2'
and b.degree='3'
MERGE (a)-[r:THIRD_DEGREE]->(b)
return r;