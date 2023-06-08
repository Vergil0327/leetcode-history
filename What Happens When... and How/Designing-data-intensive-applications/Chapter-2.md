## Data Models and Query Languages

Most applications are built by layering one data model on top of another. For each layer, the key question is: how is it represented in terms of the next-lower layer? For example:

1. As an application developer, you look at the real world (in which there are peo‐ ple, organizations, goods, actions, money flows, sensors, etc.) and model it in terms of objects or data structures, and APIs that manipulate those data struc‐ tures. Those structures are often specific to your application.
2. When you want to store those data structures, you express them in terms of a general-purpose data model, such as JSON or XML documents, tables in a rela‐ tional database, or a graph model.
3. The engineers who built your database software decided on a way of representing that JSON/XML/relational/graph data in terms of bytes in memory, on disk, or on a network. The representation may allow the data to be queried, searched, manipulated, and processed in various ways.
4. On yet lower levels, hardware engineers have figured out how to represent bytes in terms of electrical currents, pulses of light, magnetic fields, and more.

In a complex application there may be more intermediary levels, such as APIs built upon APIs, but the basic idea is still the same: each layer hides the complexity of the layers below it by providing a clean data model. 

### Relational Model Versus Document Model

The best-known data model today is probably that of SQL, based on the relational model proposed by Edgar Codd in 1970: data is organized into relations (called *tables* in SQL), where each relation is an unordered collection of *tuples* (rows in SQL).

### The Birth of NoSQL

in the 2010s, NoSQL is the latest attempt to overthrow the relational model’s dominance. The name “NoSQL” is unfortunate, since it doesn’t actually refer to any particular technology—it was originally intended simply as a catchy Twitter hashtag for a meetup on open source, distributed, nonrelational databases in 2009.

A number of interesting database systems are now associated with the #NoSQL hashtag, and it has been retroactively reinterpreted as *Not Only SQL*.

There are several driving forces behind the adoption of NoSQL databases, including:

- A need for greater scalability than relational databases can easily achieve, including very large datasets or very high write throughput
- A widespread preference for free and open source software over commercial database products
- Specialized query operations that are not well supported by the relational model
- Frustration with the restrictiveness of relational schemas, and a desire for a more
dynamic and expressive data model

Different applications have different requirements. It therefore seems likely that in the foreseeable future, relational databases will continue to be used alongside a broad variety of nonrelational datastores—an idea that is sometimes called *polyglot persistence*.

### The Object-Relational Mismatch

Most application development today is done in object-oriented programming lan‐ guages, which leads to a common criticism of the SQL data model: if data is stored in relational tables, an awkward translation layer is required between the objects in the application code and the database model of tables, rows, and columns. The disconnect between the models is sometimes called an *impedance mismatch*.


### Many-to-One and Many-to-Many Relationships

Whether you store an ID or a text string is a question of duplication
When you use an ID, the information that is meaningful to humans (such as the word Philanthropy) is stored in only one place, and everything that refers to it uses an ID (which only has meaning within the database). When you store the text directly, you are duplicating the human-meaningful information in every record that uses it.

The advantage of using an ID is that because it has no meaning to humans, it never needs to change: the ID can remain the same, even if the information it identifies changes. Anything that is meaningful to humans may need to change sometime in the future—and if that information is duplicated, all the redundant copies need to be updated. That incurs write overheads, and risks inconsistencies.

Removing such duplication is the key idea behind *normalization* in databases.

### Are Document Databases Repeating History?

While many-to-many relationships and joins are routinely used in relational databases, document databases and NoSQL reopened the debate on how best to represent such relationships in a database

document databases worked well for one-to-many relationships, but it made many-to-many relationships difficult, and it didn’t support joins. Developers had to decide whether to duplicate (denormalize) data or to manually resolve references from one record to another.

Various solutions were proposed to solve the limitations of the hierarchical model. The two most prominent were the *relational model* (which became SQL, and took over the world) and the *network model* (which initially had a large following but eventually faded into obscurity).

Since the problem that the two models were solving is still so relevant today, it’s worth briefly revisiting this debate in today’s light.

#### The network model

it is also known as the *CODASYL model*.

The CODASYL model was a generalization of the hierarchical model. In the tree structure of the hierarchical model, every record has exactly one parent; in the network model, a record could have multiple parents.

For example, there could be one record for the "Greater Seattle Area" region, and every user who lived in that region could be linked to it. This allowed **many-to-one** and **many-to-many** relationships to be modeled.

The links between records in the network model were not foreign keys, but more like pointers in a programming language. The only way of accessing a record was to follow a path from a root record along these chains of links. This was called an *access path*.

A query in CODASYL was performed by moving a cursor through the database by iterating over lists of records and following access paths. If a record had multiple parents (i.e., multiple incoming pointers from other records), the application code had to keep track of all the various relationships.

Although manual access path selection was able to make the most efficient use of the very limited hardware capabilities in the 1970s (such as tape drives, whose seeks are extremely slow), the problem was that they made the code for querying and updating the database complicated and inflexible.

With both the hierarchical and the network model, if you didn’t have a path to the data you wanted, you were in a difficult situation. You could change the access paths, but then you had to go through a lot of handwritten database query code and rewrite it to handle the new access paths. It was difficult to make changes to an application’s data model.

#### The relational model

A relation (table) is simply a collection of tuples (rows), and that’s it.
- no labyrinthine nested structures
- no complicated access paths to follow if you want to look at the data

In a relational database, the query optimizer automatically decides which parts of the query to execute in which order, and which indexes to use. Those choices are effectively the “access path,” but the big difference is that they are made automatically by the query optimizer, not by the application developer

#### Comparison to document databases

Document databases reverted back to the hierarchical model in one aspect: storing nested records within their parent record rather than in a separate table.

when it comes to representing many-to-one and many-to-many relationships, relational and document databases are not fundamentally different: in both cases, the related item is referenced by a unique identifier, which is called a *foreign key* in the relational model and a *document reference* in the document model

### Relational Versus Document Databases Today

The main arguments in favor of the document data model are schema flexibility, better performance due to locality, and that for some applications it is closer to the data structures used by the application.

The relational model counters by providing better support for joins, and many-to-one and many-to-many relationships.

#### Which data model leads to simpler application code?

If the data in your application has a document-like structure (i.e., a tree of one-to-many relationships, where typically the entire tree is loaded at once), then it’s probably a good idea to use a document model. The relational technique of *shredding* (splitting a document-like structure into multiple tables) can lead to cumbersome schemas and unnecessarily complicated application code.

The document model has limitations:
- you cannot refer directly to a nes‐ ted item within a document, but instead you need to say something like “the second item in the list of positions for user 251” (much like an access path in the hierarchical model). However, as long as documents are not too deeply nested, that is not usually a problem.
- The poor support for joins in document databases may or may not be a problem, depending on the application.
  - if your application does use many-to-many relationships, the document model becomes less appealing. It’s possible to reduce the need for joins by denormal‐ izing, but then the application code needs to do additional work to keep the denormalized data consistent.
  - Joins can be emulated in application code by making multiple requests to the database, but that also moves complexity into the application and is usually slower than a join performed by specialized code inside the database.
  - In such cases, using a document model can lead to significantly more complex application code and worse performance

#### Schema flexibility in the document model

Most document databases, and the JSON support in relational databases, do not enforce any schema on the data in documents.

Document databases are sometimes called *schemaless*, but that’s misleading, as the code that reads the data usually assumes some kind of structure—i.e., there is an implicit schema, but it is not enforced by the database.

A more accurate term is *schema-on-read* (the structure of the data is implicit, and only interpreted when the data is read), in contrast with *schema-on-write* (the traditional approach of relational forms to it)

- schema-on-read is similar to dynamic (runtime) type checking in programming languages
- schema-on-write is similar to static (compile-time) type checking

The difference between the approaches is particularly noticeable in situations where an application wants to change the format of its data.

For example, say you are cur‐ rently storing each user’s full name in one field, and you instead want to store the first name and last name separately:

document database
```
if (user && user.name && !user.first_name) {
  // Documents written before Dec 8, 2013 don't have first_name
  user.first_name = user.name.split(" ")[0];
}
```

"statically typed" database
```sql
-- perform a *migration*
ALTER TABLE users ADD COLUMN first_name text;
UPDATE users SET first_name = split_part(name, ' ', 1); -- PostgreSQL
UPDATE users SET first_name = substring_index(name, ' ', 1); -- MySQL
```

Schema changes have a bad reputation of being slow and requiring downtime. This reputation is not entirely deserved:

- most relational database systems execute the ALTER TABLE statement in a few milliseconds.
- MySQL is a notable exception. it copies the entire table on ALTER TABLE, which can mean minutes or even hours of downtime when altering a large table

**work around**
Running the UPDATE statement on a large table is likely to be slow on any database, since every row needs to be rewritten. If that is not acceptable, the application can leave first_name set to its default of NULL and fill it in at read time, like it would with a document database.

The schema-on-read approach is advantageous if the items in the collection don’t all have the same structure for some reason (i.e., the data is heterogeneous)

- There are many different types of objects, and it is not practical to put each type of object in its own table.
- The structure of the data is determined by external systems over which you have no control and which may change at any time.

#### Data locality for queries

A document is usually stored as a single continuous string, encoded as JSON, XML, or a binary variant thereof (such as MongoDB’s BSON). If your application often needs to access the entire document (for example, to render it on a web page), there is a performance advantage to this *storage locality*.

If data is split across multiple tables, multiple index lookups are required to retrieve it all, which may require more disk seeks and take more time.

The locality advantage only applies if you need large parts of the document at the same time. The database typically needs to load the entire document, even if you access only a small portion of it, which can be wasteful on large documents.

On updates to a document, the entire document usually needs to be rewritten—only modifications that don’t change the encoded size of a document can easily be per‐ formed in place

For these reasons, it is generally recommended that you keep documents fairly small and avoid writes that increase the size of a document. These performance limitations significantly reduce the set of situations in which document databases are useful.

It’s worth pointing out that the idea of grouping related data together for locality is not limited to the document model. For example, Google’s Spanner database offers the same locality properties in a relational data model, by allowing the schema to declare that a table’s rows should be interleaved (nested) within a parent table. Oracle allows the same, using a feature called *multi-table index cluster tables*

The *column-family* concept in the Bigtable data model (used in Cassandra and HBase) has a similar purpose of managing locality

#### Convergence of document and relational databases

Most relational database systems (other than MySQL) have supported XML since the mid-2000s. This includes functions to make local modifications to XML documents and the ability to index and query inside XML documents, which allows applications to use data models very similar to what they would do when using a document database.

PostgreSQL since version 9.3, MySQL since version 5.7, and IBM DB2 since ver‐ sion 10.5 also have a similar level of support for JSON documents. Given the popularity of JSON for web APIs, it is likely that other relational databases will follow in their footsteps and add JSON support.

On the document database side, RethinkDB supports relational-like joins in its query language, and some MongoDB drivers automatically resolve database references (effectively performing a client-side join, although this is likely to be slower than a join performed in the database since it requires additional network round-trips and is less optimized).

It seems that relational and document databases are becoming more similar over time, and that is a good thing: the data models complement each other.

### Query Languages for Data

An imperative language tells the computer to perform certain operations in a certain order. You can imagine stepping through the code line by line, evaluating conditions, updating variables, and deciding whether to go around the loop one more time.

In a declarative query language, like SQL or relational algebra, you just specify the pattern of the data you want—what conditions the results must meet, and how you want the data to be transformed (e.g., sorted, grouped, and aggregated)—but not how to achieve that goal. It is up to the database system’s query optimizer to decide which indexes and which join methods to use, and in which order to execute various parts of the query.

A declarative query language is attractive because it is typically more concise and eas‐ ier to work with than an imperative API. But more importantly, it also hides imple‐ mentation details of the database engine, which makes it possible for the database system to introduce performance improvements without requiring any changes to queries.

declarative languages often lend themselves to parallel execution. Imperative code is very hard to parallelize across multiple cores and multiple machines, because it specifies instructions that must be performed in a particular order. Declarative languages have a better chance of getting faster in parallel execution because they specify only the pattern of the results, not the algorithm that is used to determine the results. The database is free to use a parallel implementation of the query language, if appropriate

### MapReduce Querying

*MapReduce* is a programming model for processing large amounts of data in bulk across many machines, popularized by Google.

MapReduce is neither a declarative query language nor a fully imperative query API, but somewhere in between: the logic of the query is expressed with snippets of code, which are called repeatedly by the processing framework.

It is based on the **map** (also known as **collect**) and **reduce** (also known as **fold** or **inject**) functions that exist in many functional programming languages.

To give an example:

imagine you are a marine biologist, and you add an observation record to your database every time you see animals in the ocean. Now you want to generate a report saying how many sharks you have sighted per month.

- In PostgreSQL you might express that query like this:

```sql
SELECT date_trunc('month', observation_timestamp) AS observation_month,
       sum(num_animals) AS total_animals
FROM observations
WHERE family = 'Sharks'
GROUP BY observation_month;
```

- Expressed with MongoDB’s MapReduce feature as follows:

```js
db.observations.mapReduce(
  function map() { // step 2
    const year = this.observationTimestamp.getFullYear()
    const month = this.observationTimestamp.getMonth() + 1
    emit(`${year}-${month}`, this.numAnimals) // step 3
  },
  function reduce(key, values) { // step 4
    return values.reduce((accu, curr) => accu+curr, 0) // step 5
  },
  {
    query: { family: 'Sharks' }, // step 1
    out: 'monthlySharkReport' // step 6
  }
)
```

1. The filter to consider only shark species can be specified declaratively (this is a MongoDB-specific extension to MapReduce).
2. The JavaScript function **map** is called once for every document that matches query, with **this** set to the document object.
3. The **map** function emits a key (ex. '2013-12' in this example) and a value (the mumber of animals in that observation)
4. The key-value pairs emitted by **map** are grouped by key. For all key-value pairs with the same key, the **reduce** function is called once
5. The **reduce** function adds up the number of animals from all observations in a particular month
6. The final output is written to the collection **monthlySharkReport**


The **map** and **reduce** functions must be pure functions, which means they only use the data that is passed to them as input, they cannot perform additional database queries, and they must not have any side effects. These restrictions allow the database to run the functions any‐ where, in any order, and rerun them on failure.

MapReduce is a fairly low-level programming model for distributed execution on a cluster of machines. Higher-level query languages like SQL can be implemented as a pipeline of MapReduce operations (see Chapter 10), but there are also many distributed implementations of SQL that don’t use MapReduce.

Note there is nothing in SQL that constrains it to running on a single machine, and MapReduce doesn’t have a monopoly on distributed query execution.

A usability problem with MapReduce is that you have to write two carefully coordinated JavaScript functions, which is often harder than writing a single query. Moreover, a declarative query language offers more opportunities for a query optimizer to improve the performance of a query.

For these reasons, MongoDB 2.2 added support for a declarative query language called the *aggregation pipeline*.

for example:
```js
db.observations.aggregate([
  { $match: { family: 'Sharks' } },
  { $group: { 
    _id: {
      year: { $year: '$observationTimestamp' }
      month: { $month: '$observationTimestamp' }
    }
    totalAnimals: { $sum: '$numAnimals' }
  }}
])
```

## Graph-Like Data Models

many-to-many relationships are an important distinguishing feature between different data models.

If your application has mostly one-to-many relationships (tree-structured data) or no relationships between records, the document model is appropriate.

But what if many-to-many relationships are very common in your data? The relational model can handle simple cases of many-to-many relationships, but as the connections within your data become more complex, it becomes more natural to start modeling your data as a graph.

A graph consists of two kinds of objects:
  1. *vertices* (also known as *nodes* or *entities*)
  2. *edges* (also known as *relationships* or *arcs*)

For examples:
- *Social graphs*
  - vertices: people
  - edges: relation between people
- *The web graphs*
  - vertices: web pages
  - edges: links to other pages
- *Road or rail networks*
  - vertices: junctions
  - edges: roads or railway lines between them

![Fig. 2-5](assets/fig.%202-5.png)

### Property Graphs

*property graph* model (implemented by Neo4j, Titan, and InfiniteGraph)

In the property graph model, each vertex consists of:
- A unique identifier
- A set of outgoing edges
- A set of incoming edges
- A collection of proerties (key-value pairs)

Each edge consists of:
- A unique identifier
- The vertex at which the edge starts (the *tail vertex*)
- The vertex at which the edge ends (the *head vertex*)
- A label to describe the kind of relationship between the two vertices
- A collection of properties (key-value pairs)

*Example Representing a property graph using a relational schema*

The head and tail vertex are stored for each edge; if you want the set of incoming or outgoing edges for a vertex, you can query the edges table by **head_vertex** or **tail_vertex**, respectively.

```sql
CREATE TABLE vertices (
  vertex_id  integer PRIMARY KEY,
  properties json
)

CREATE TABLE edges (
  edge_id     integer PRIMARY KEY,
  tail_vertex integer REFERENCES vertices (vertex_id),
  head_vertex integer REFERENCES vertices (vertex_id),
  label       text,
  properties  json
)

CREATE INDEX edges_tails ON edges (tail_vertex);
CREATE INDEX edges_heads ON edges (head_vertex);
```

Some important aspects of this model are:
1. Any vertex can have an edge connecting it withany other vertex. There is no schema that restricts which kinkds of things can or cannot be associated
2. Given any vertex, you can effectively find both its incoming and its outgoing edges, and thus *traverse* the graph——i.e., follow a path through a chain of vertices——both forward and backward.
3. By using different labels for different kinds of relationships, you can store several different kinds of information in a single graph, while still maintaining a clean model.

Those features give graphs a great deal of flexibility for data modeling.
Graphs are good for evolvability: as you add features to your application, a graph can easily be extended to accommodate changes in your application’s data structures.


### The Cypher Query Language

*Cypher* is a declarative query language for property graphs, created for the Neo4j graph database.

**Example 2-3** shows the Cypher query to insert the lefthand portion of Figure 2-5 into a graph database.
Each vertex is given a symbolic name like USA or Idaho, and other parts of the query can use those names to create edges between the vertices, using an arrow notation: (Idaho) -[:WITHIN]-> (USA) creates an edge labeled WITHIN, with Idaho as the tail node and USA as the head node

```sql
-- Example 2-3. A subset of the data in Figure 2-5, represented as a Cypher query
CREATE
  (NAmerica:Location {name:'North America', type:'continent'}),
  (USA:Location      {name:'United States', type:'country'  }),
  (Idaho:Location    {name:'Idaho',         type:'state'    }),
  (Lucy:Person       {name:'Lucy' }),
  (Idaho) -[:WITHIN]->  (USA)  -[:WITHIN]-> (NAmerica),
  (Lucy)  -[:BORN_IN]-> (Idaho)
```

What if we want to find *the names of all the people who emigrated from the United States to Europe*?
To be more precise, here we want to find all the vertices that have a BORN_IN edge to a location within the US, and also a LIVING_IN edge to a location within Europe, and return the name property of each of those vertices.

```sql
--# The same arrow notation is used in a MATCH clause to find patterns in the graph:
--# (person) -[:BORN_IN]-> () matches any two vertices that are related by an edge labeled BORN_IN.
--# The tail vertex of that edge is bound to the variable person, and the head vertex is left unnamed
-- Example 2-4. Cypher query to find people who emigrated from the US to Europe

MATCH
    (person) -[:BORN_IN]->  () -[:WITHIN*0..]-> (us:Location {name:'United States'}),
    (person) -[:LIVES_IN]-> () -[:WITHIN*0..]-> (eu:Location {name:'Europe'})
RETURN person.name
```

The query can be read as follows:
    
    Find any vertex (call it person) that meets both of the following conditions:
    
      1. person has an outgoing BORN_IN edge to some vertex. From that vertex, you can follow a chain of outgoing WITHIN edges until eventually you reach a vertex of type Location, whose name property is equal to "United States".
      
      2. That same person vertex also has an outgoing LIVES_IN edge. Following that edge, and then a chain of outgoing WITHIN edges, you eventually reach a vertex of type Location, whose name property is equal to "Europe".
    
    For each such person vertex, return the name property.

There are several possible ways of executing the query. The description given here suggests that you start by scanning all the people in the database, examine each person’s birthplace and residence, and return only those people who meet the criteria.
```
有很多方式能實現這個查詢. 這裡的敘述建議你從搜尋所有資料庫裡的`people`資料，然後看每個人的出生地(birthplace)及居留地(residence)，然後返回那些滿足條件的人名
```

But equivalently, you could start with the two Location vertices and work backward. If there is an index on the name property, you can probably efficiently find the two vertices representing the US and Europe. Then you can proceed to find all locations (states, regions, cities, etc.) in the US and Europe respectively by following all incom‐ ing WITHIN edges. Finally, you can look for people who can be found through an incoming BORN_IN or LIVES_IN edge at one of the location vertices.
```
但同樣地，你也可以從**Location**連接的兩個節點反找回來，如果存在著`name`的索引，你很可能可以很高效率地找出兩個代表US及Erope的節點，然後你可以再藉由incoming edge **WITHIN**來繼續個別找出US跟Europe的每個位置，像是州、區、市鎮
最後再透過**BORN_IN**或**LIVES_IN**等incoming edge在這些位置中找出符合條件的人
```

As is typical for a declarative query language, you don’t need to specify such execution details when writing the query: the query optimizer automatically chooses the strategy that is predicted to be the most efficient, so you can get on with writing the rest of your application.
如同一般的宣告式語言，你不需要為了查詢而詳細寫出所有細節，query optimizer會自動地選擇最佳策略來搜索，所以你可以繼續完成主程式的其他的部分

### Graph Queries in SQL

Example 2-2 suggested that graph data can be represented in a relational database. But if we put graph data in a relational structure, can we also query it using SQL?
```
Example 2-2暗示graph data可以用關聯式資料庫來儲存表示
但如果我們真的將graph data以關聯式結構儲存，我們能用SQL來進行查詢嗎?
```

The answer is yes, but with some difficulty. In a relational database, you usually know in advance which joins you need in your query. In a graph query, you may need to traverse a variable number of edges before you find the vertex you’re looking for—that is, the number of joins is not fixed in advance.

In our example, that happens in the () -[:WITHIN*0..]-> () rule in the Cypher query.

A person’s LIVES_IN edge may point at any kind of location: a street, a city, a district, a region, a state, etc. A city may be WITHIN a region, a region WITHIN a state, a state WITHIN a country, etc. The LIVES_IN edge may point directly at the location vertex you’re looking for, or it may be several levels removed in the location hierarchy.

In Cypher, :WITHIN*0.. expresses that fact very concisely: it means “follow a WITHIN edge, zero or more times.” It is like the * operator in a regular expression.

Since SQL:1999, this idea of variable-length traversal paths in a query can be expressed using something called recursive common table expressions (the WITH RECURSIVE syntax).

Example 2-5 shows the same query—finding the names of people who emigrated from the US to Europe—expressed in SQL using this technique (supported in PostgreSQL, IBM DB2, Oracle, and SQL Server).
However, the syntax is very clumsy in comparison to Cypher.

```sql
-- Example 2-5. The same query as Example 2-4, expressed in SQL using recursive common table expressions
WITH RECURSIVE
    -- in_usa is the set of vertex IDs of all locations within the United States
    in_usa(vertex_id) AS (
            SELECT vertex_id FROM vertices WHERE properties->>'name' = 'United States' -- 1.
        UNION
            SELECT edges.tail_vertex FROM edges -- 2.
            JOIN in_usa ON edges.head_vertex = in_usa.vertex_id
            WHERE edges.label = 'within'
    ),
  
    -- in_europe is the set of vertex IDs of all locations within Europe
    in_europe(vertex_id) AS (
            SELECT vertex_id FROM vertices WHERE properties->>'name' = 'Europe' -- 3.
        UNION
            SELECT edges.tail_vertex FROM edges
            JOIN in_europe ON edges.head_vertex = in_europe.vertex_id
            WHERE edges.label = 'within'
    ),

    -- born_in_usa is the set of vertex IDs of all people born in the US
    born_in_usa(vertex_id) AS ( -- 4.
        SELECT edges.tail_vertex FROM edges
        JOIN in_usa ON edges.head_vertex = in_usa.vertex_id
        WHERE edges.label = 'born_in'
    ),

    -- lives_in_europe is the set of vertex IDs of all people living in Europe
    lives_in_europe(vertex_id) AS ( -- 5.
        SELECT edges.tail_vertex FROM edges
        JOIN in_europe ON edges.head_vertex = in_europe.vertex_id
        WHERE edges.label = 'lives_in'
    )

SELECT vertices.properties->>'name'
FROM vertices
-- join to find those people who were both born in the US *and* live in Europe
JOIN born_in_usa ON vertices.vertex_id = born_in_usa.vertex_id -- 6.
JOIN lives_in_europe ON vertices.vertex_id = lives_in_europe.vertex_id;
```

1. First find the vertex whose **name** property has the value "United States", and make it the first element of the set of vertices **in_usa**.

2. Follow all incoming **wthin** edges from vertices in the set **in_usa**, and add them to the same set, until all incoming **within** edges have been visited.

3. Do the same starting with the vertex whose **name** property has the value "Europe", and build up th eset of vertices **in_europe**

4. For each of the vertices in the set **in_usa**, follow incoming **born_in** edges to find people who were borin in some place within the Unites States

5. Similarly, for each of the vertices in the set **in_europe**, follow incoming **lives_in** edges to find people who live in Europe.

6. Finally, intersect the set of people born in the USA with the set of people living in Europe, by joining them.

If the same query can be written in 4 lines in one query language but requires 29 lines in another, that just shows that different data models are designed to satisfy different use cases. It’s important to pick a data model that is suitable for your application.


### Triple-Stores and SPARQL

The triple-store model is mostly equivalent to the property graph model, using different words to describe the same ideas.
It is nevertheless worth discussing, because there are various tools and languages for triple-stores that can be valuable additions to your toolbox for building applications.

In a triple-store, all information is stored in the form of very simple three-part statements:
`(*subject*, *predicate*, *object*)`.

For example, in the triple (*Jim*, *likes*, *bananas*), *Jim* is the subject, *likes* is the predicate (verb), and *bananas* is the object.

The subject of a triple is equivalent to a vertex in a graph. The object is one of two things:

1. A value in a primitive datatype, such as a string or a number.
   - In that case, the predicate and object of the triple are equivalent to the key and value of a property on the subject vertex.
   - For example, (*lucy*, *age*, *33*) is like a vertex lucy with properties {"age":33}.

2. Another vertex in the graph.
   - In that case, the predicate is an edge in the graph, the subject is the tail vertex, and the object is the head vertex.
   - For example, in (*lucy*, *marriedTo*, *alain*) the subject and object *lucy* and *alain* are both vertices, and the predicate *marriedTo* is the label of the edge that connects them.

Example 2-6 shows the same data as in Example 2-3, written as triples in a format called *Turtle*, a subset of *Notation3 (N3)*

*Example 2-6. A subset of the data in Figure 2-5, represented as Turtle triples*

```
@prefix : <urn:example:>.
_:lucy     a       :Person.
_:lucy     :name   "Lucy".
_:lucy     :bornIn _:idaho.
_:idaho    a       :Location.
_:idaho    :name   "Idaho".
_:idaho    :type   "state".
_:idaho    :within _:usa.
_:usa      a       :Location.
_:usa      :name   "United States".
_:usa      :type   "country".
_:usa      :within _:namerica.
_:namerica a       :Location.
_:namerica :name   "North America".
_:namerica :type   "continent".
```

In this example, vertices of the graph are written as _:*someName*. The name doesn’t mean anything outside of this file; it exists only because we otherwise wouldn’t know which triples refer to the same vertex.
When the predicate represents an edge, the object is a vertex, as in _:idaho :within _:usa.
When the predicate is a property, the object is a string literal, as in _:usa :name "United States".

It’s quite repetitive to repeat the same subject over and over again, but fortunately you can use semicolons to say multiple things about the same subject. This makes the Turtle format quite nice and readable: see Example 2-7.

*Example 2-7. A more concise way of writing the data in Example 2-6*

```
@prefix : <urn:example:>.
_:lucy     a   :Person;    :name "Lucy";           :bornIn _:idaho.
_:idaho    a   :Location;  :name "Idaho";          :type "state";    :within  _:usa.
_:usa      a   :Location;  :name "United States";  :type "country";  :within  _:namerica.
_:namerica a   :Location;  :name "North America";  :type "continent".
```

#### The semantic web

The semantic web is fundamentally a simple and reasonable idea:

> websites already publish information as text and pictures for humans to read, so why don’t they also publish information as machine-readable data for computers to read?

The Resource Description Framework (RDF) was intended as a mechanism for different websites to publish data in a consistent format, allowing data from different websites to be automatically combined into a web of data—a kind of internet-wide “database of everything.”

Unfortunately, the semantic web was overhyped in the early 2000s but so far hasn’t shown any sign of being realized in practice, which has made many people cynical about it.


However, if you look past those failings, there is also a lot of good work that has come out of the semantic web project. Triples can be a good internal data model for applications, even if you have no interest in publishing RDF data on the semantic web.

#### The RDF data model

![Fig. 2-7](assets/fig.%202-7.png)

The Turtle language we used in Fig 2-7 is a human-readable format for RDF data.
Sometimes RDF is also written in an XML format, which does the same thing much more verbosely—see Fig 2-8.
Turtle/N3 is preferable as it is much easier on the eyes, and tools like Apache Jena can automatically convert between different RDF formats if necessary.

![Fig. 2-8. The data expressed using RDF/XML syntax](assets/fig.%202-8.png)

RDF has a few quirks due to the fact that it is designed for internet-wide data exchange. The subject, predicate, and object of a triple are often URIs. For example, a predicate might be an URI such as <http://my-company.com/namespace#within> or <http://my-company.com/namespace#lives_in>, rather than just WITHIN or LIVES_IN. The reasoning behind this design is that you should be able to combine your data with someone else’s data, and if they attach a different meaning to the word within or lives_in, you won’t get a conflict because their predicates are actually <http://other.org/foo#within> and <http://other.org/foo#lives_in>.

The URL <http://my-company.com/namespace> doesn’t necessarily need to resolve to anything—from RDF’s point of view, it is simply a namespace.
To avoid potential confusion with http:// URLs, the examples in this section use non-resolvable URIs such as urn:example:within. Fortunately, you can just specify this prefix once at the top of the file, and then forget about it.


#### The SPARQL query language

*SPARQL* is a query language for triple-stores using the RDF data model. (It is an acronym for SPARQL Protocol and RDF Query Language, pronounced “sparkle.”)

It predates Cypher, and since Cypher’s pattern matching is borrowed from SPARQL, they look quite similar
The same query as before—finding people who have moved from the US to Europe— is even more concise in SPARQL than it is in Cypher 


Example 2-9. The query expressed in SPARQL
```sql
PREFIX : <urn:example:>

SELECT ?personName WHERE {
  ?person :name ?personName
  ?person :bornIn / :within* / :name "United States".
  ?person :livesIn / :within* / :name "Europe".
}
```

The structure is very similar. The following two expressions are equivalent (variables start with a question mark in SPARQL):

```sql
(person) -[:BORN_IN]-> () -[:WITHIN*0..]-> (location) -- # Cypher
?person :bornIn / :within* ?location. -- # SPARQL
```

Because RDF doesn't distinguish between properties and edges but just use predicates for both, you can use the same syntax for matching properties.
In the folloing expression, the variable **usa** is bound to any vertex that has a **name** property whose value is the string "United States":

```
(usa {name:'United States'}) # Cypher
?usa :name "United States".  # SPARQL
```

SPARQL is a nice query language—even if the semantic web never happens, it can be a powerful tool for applications to use internally.

#### The Foundation: Datalog

*Datalog* is a much older language than SPARQL or Cypher, having been studied extensively by academics in the 1980s.
It is less well known among software engineers, but it is nevertheless important, because it provides the foundation that later query languages build upon.

In practice, Datalog is used in a few data systems: for example, it is the query language of Datomic, and Cascalog is a Datalog implementation for querying large datasets in Hadoop.

Datalog's data model is similar to the triple-store model, generalized a bit. Instead of writing a triple as (*subject*, *predicate*, *object*), we write it as *predicate*(subect, object).

Example 2-10. A subset of data represented as Datalog facts

```
name(namerica, 'North America').
type(namerica, continent).

name(usa, 'United States').
type(usa, country).
within(usa, namerica).

name(idaho, 'Idaho').
type(idaho, state).
within(idaho, usa).

name(lucy, 'Lucy').
born_in(lucy, idaho).
```

Now that we have defined the data, we can write the same query as before:

Example 2-11 query expressed in Datalog
```
within_recursive(Location, Name) :- name(Location, Name). /* Rule 1 */

within_recursive(Location, Name) :- within(Location, Via), /* Rule 2 */
                                    within_recursive(Via, Name).

migrated(Name, BornIn, LivingIn) :- name(Person, Name), /* Rule 3 */
                                    born_in(Person, BornLoc),
                                    within_recursive(BornLoc, BornIn),
                                    lives_in(Person, LivingLoc),
                                    within_recursive(LivingLoc, LivingIn).

?- migrated(Who, 'United States', 'Europe').
/* Who = 'Lucy'. */
```

Cypher ans SPARQL jump in right away with **SELECT**, but Datalog takes a small step at a time. We define *rules* that tell the database about new predicates: here we define two predicates, **within_recursive** and **migrated**. These predicates aren't triples stored in the database, but instead they are derived from data or from other rules.
Rules can refer to other rules, just like functions can call other functions or recursively call themselves. Like this, complex queries can be built up a small piece at a time.

In rules, words that start with an uppercase letter are variables, and predicates are matched like inCypher and SPARQL. For example, **name(Location, Name)** matches the triple **name(namerica, 'North America')** with variable bindings **Location = namerica** and **Name = 'North America'**.

A rule applies if the system can find a match for all predicates on the righhand side of the **:-** operator. When the rule applies, it's as though the lefthand side of the **:-** was added to the database (with variables replaced by the values thay matched).

One possible way of applying the rules is thus:

1. **name(namerica, 'North America')** exists in the database, so rule 1 applies. It generates **within_recursive(namerica, 'North America')**.
2. **within(usa, namerica)** exists in the database and the previous step generated **within_recursive(namerica, 'North America')**, so rule 2 applies. It generates **within_recursive(usa, 'North America')**.
3. **within(idaho, usa)** exists in the database and the previous step generated **within_recursive(usa, 'North America')**, so rule 2 applies. It generates **within_recursive(idaho, 'North America')**.

By repeated application of rules 1 and 2, th **within_recursive** predicate can tell us all the locations in North America (or any other location name) contained in our database. This process is illustrated in Below

*Determining that Idaho is in North America, using the Datalog rules from example 2-11 (above this section)*
![Figure 2-6](assets/fig.%202-6.png)

Now rule 3 can find people who were born in some loation **BornIn** and live in some location **LivingIn**. By querying with **BornIn = 'United States'** and **LivingIn = 'Europe'**, and leaving the person as a variable **Who**, weask the Datalog system to find out which values can appear for the variable **Who**. So, finally we get the same answer as in the earlier Cypher and SPARQL queries.

The Datalog approach requires a different kind of thinking to the other query language discussed in this chapter, but it's a very powerful approach, because rules can be combined and reused in different queries. It's less convenient for simple one-off queries, but it can cope better if your data is complex.

## Summary

Data models are a huge subject, and in this chapter we have taken a quick look at a broad variety of different models. We didn't have space to go into all the details of each model, but hopefully the overview has been enough to whet your appetite to find out more about the model that best fits your application's requirements.

Historically, data started out being represented as one big tree (the hierarchical model), but that wasn't good for representing many-to-many relationships, so the relational model was invented to solve that problem. More recently, developers found that some applications don't fit well  in the relational model either. New nonrelational "NoSQL" datastores have diverged in two main directions:

1. *Document databases* target use cases where data comes in self-contained documents and relationships between one document and another are rare.
2. *Graph databases* go in the opposite direction, targeting use cases where anything is potentially related to everything.

All three models (document, relational, and graph) are widely used today, and each is good in its respective domain. One model can be emulated in terms of another model-for example, graph data can be represented in a relational database-but the result is often awkward. That's why we have different systems for different purposes, not a single one-size-fits-all solution.

One thing that document and graph databses have in common is that they typically don'tenforce a schema for the data they store, which can make it easier to adapt applications to changing requirements. However, your application most likely still assumes that data has a certain structure; it's just a question of whether the schema is explicit (enforced on write) or implicit (handled on read).

Each data model comes with its own query language or framework, and we discussed several examples: SQL, MapReduce, MongoDB's aggregation pipeline, Cypher, SPARQL, and Datalog. We also touched on CSS and XSL/XPath, which aren't database query languages but have interesting parallels.

Although we have covered a lot of ground, there are still many data models left unmentioned. To give just a few brief examples:

- Researchers working with genome data often need to perform *sequence-similarity searches*, which means taking one very long string (representing a DNA molecule) and matching it against a large database of strings that are similar, but not identical. None of the databses described here can handle this kind of usage, which is why researchers have written specialized genome database software like GenBank.
- Paritcle physicists have been doing Big Data-style large-scale data analysis for decades, and projects like the Large Hadron Collider (LHC) now work with hundreds of petabytes! At such a scale custom solutions are required to stop the hardware cost from spiraling out of control.
- *Full-text search* is arguably a kind of data model that is frequently used alongside databases. Information retrieval is a large specialist subject that we won't cover in great detail in this book, but we'll touch on search indexes in Chapter 3 and Part III.

---------------------------------------

