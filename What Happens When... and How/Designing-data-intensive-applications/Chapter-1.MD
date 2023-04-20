## Chapter 1 - Reliable, Scalable, and Maintainable Applications

from *compute-intensive* to *data-intensive*
nowadays, CPU power is rarely a limiting factor for these applications
bigger problems are usually the amount of data, the complexity of data, and the speed at which it is changing

Ex. Typical data-intensive applications
1. **databases**: store data so that they, or another application can find it again later
2. **caches**: spped up reads by memorizing the result of expensive operation
3. **search indexes**: allow to search data by keyword or filter in various way
4. **stream processing**: send a message to another process, to be handled acynchronously
5. **batch processing**: perioically crunch a large amount of accumulated data

*Good abstraction! But reality is not that simple*

- there are many database systems with different characteristics, because different applications have different requirements
- there are various approaches to caching
- several ways of building search indexes
- ...

### Thinking About Data System

![Fig. 1-1](assets/fig.%201-1.png)
*One possible architecture for a data system that combines several components*

If you are designing a data system or service, a lot of tricky questions arise.
- How do you ensure that the data remains correct and complete, even when things go wrong internally?
- How do you provide consistently good performance to clients, even when parts of your system are degraded?
- How do you scale to handle an increase in load? What does a good API for the service look like?

There are many factors that may influence the design of a data system, including
- the skills and experience of the people involved
- legacy system dependencies
- the timescale for delivery
- your organization’s tolerance of different kinds of risk, regulatory constraints, etc.

we focus on three concerns that are important in most software systems:

***Reliability***

    The system should continue to work *correctly* (performing the correct function at the desired level of performance) even in the face of *adversity* (hardware or software faults, human error, ...)

***Scalability***

    As the system *grows* (in data volume, traffic volume or complexity), there should be reasonable ways of dealing with that growth.

***Maintainability***

    Over time, many different people will work on the system (engineering and operations, both maintaining current behavior and adapting the system to new use cases), and they should all be able to work on it *productively*

### Reliability

typical expectations:

- the application performs the function that the user expected
- it can tolerate the user making mistakes or using the software in unexpected ways
- its performance is good enough for the required use case, under the expected load and data volume
- the system prevents any unauthorized access and abuse

If all those things together mean "working correctly"
Roughly, *reliability* means "continuing to work correctly, even when things go wrong"

the things that can go wrong ared called *faluts*
systems that anticipate faults and can cope with them are called *fault-tolerant* or *resilient*

*ps. falut-tolerant means it can tolerate certain types of faults, not feasible to say it can tolerate every possible kind of faults.*


* **fault** is not the same as a **failure**

A *fault* is usually defined as one component of the system deviating from its spec.
A *failure* is when the system as a whole stops providing the required service to the user.

it's usually best to design fault-tolerance mechanisms that prevent faults from causing failures

* **The Netflix *Chaos Monkey***

in such fault-tolerant systems, it can make sense to *increase* the rate of faults by triggering them deliberately

ex.
by randomly killing individual processes without warning. many critical bugs are actually due to poor error handling.
by deliberately inducing faults, you ensure the fault-tolerance machinery is continually exercised and tested.

#### Hardware Faults

hard disks crash, faulty RAM, power grid has a blackout, someone unplugs the wrong network, cable, ...
all these things happen *all the time*

ex.
hard disks are reported as having a *mean time to failure (MTTF)* of about 10 to 50 years.
thus, on a storage cluster with 10,000 disks, we should expect on average one disk to die per day

first response is usually to add redundancy to the individual hardware components in order to reduce the failure rate of the system

ex. set up disks in a RAID configuration. have dual power supplies and hot-swappable CPUs for server. backup power for datacenter.

until recently, redundancy of hardware components was sufficient for most applications, since it makes total failure of a single machine fairly rare.

however, as data volumes and applications' computing demands have increased, more applications have begun using larger numbers of machines, which proportionally increases the rate of hardware faults. moreover, in some cloud platforms such as AWS it's fairly common for virtual machine instances to become unavailable without warning, as the platforms are designed to prioritize flexibility and elasticity over single-machine reliability

hence, there is a move toward ystems that can tolerate the loss of entire machines, by using software fault-tolerance techniques in preference or in addition to hardware redundancy

operational advantages:
a single-server system requires planned downtime if you need to reboot the machine to apply patches,
whereas a system that can tolerate machine failure can be patched one node at a time without downtime

#### Software Errors

systematic error within the system
- harder to anticipate
- correlated across nodes

they tend to cause many more system failures than uncorrelated hardware faults, ex.
- A software bug that causes every instance of an application server to crash when given a particular bad input.
- A runaway process that uses up some shared resource—CPU time, memory, disk space, or network bandwidth
- A service that the system depends on that slows down, becomes unresponsive, or starts returning corrupted responses
- Cascading failures

There is no quick solution to the problem of systematic faults in software. Lots of small things can help:
- carefully thinking about assumptions and interactions in the system
- thorough testing
- process isolation
- allowing processes to crash and restart
- measuring, monitoring, and analyzing system behavior in production

#### Human Errors

humans are known to be unreliable.
For example, one study of large internet services found that configuration errors by operators were the leading cause of outages, whereas hardware faults (servers or network) played a role in only 10–25% of outages

How do we make our systems reliable, in spite of unreliable humans?

- Design systems in a way that minimizes opportunities for error
  - well-designed abstractions, APIs, and admin interfaces make it easy to do “the right thing” and discourage “the wrong thing.”
  - However, if the interfaces are too restrictive people will work around them, negating their benefit, so this is a tricky balance to get right.
- Decouple the places where people make the most mistakes from the places where they can cause failures
  - In particular, provide fully featured non-production sandbox environments where people can explore and experiment safely, using real data, without affecting real users.
- Test thoroughly at all levels, from unit tests to whole-system integration tests and manual tests
  - Automated testing is widely used, well understood, and especially valuable for covering corner cases that rarely arise in normal operation
- Allow quick and easy recovery from human errors, to minimize the impact in the case of a failure
- Set up detailed and clear monitoring, such as performance metrics and error rates
  - In other engineering disciplines this is referred to as *telemetry*
- Implement good management practices and training

### Scalability

*Scalability* is the term we use to describe a system’s ability to cope with increased load.

discussing scalability means considering questions like:
- “If the system grows in a particular way, what are our options for coping with the growth?”
- “How can we add computing resources to handle the additional load?”

#### Describing Load

Load can be described with a few numbers which we call *load parameters*

let’s consider Twitter as an example, using data published in November 2012.

Two of Twitter’s main operations are:
1. *Post tweet*: A user can publish a new message to their followers (4.6k requests/sec on average, over 12k requests/sec at peak).
2. *Home timeline*: A user can view tweets posted by the people they follow (300k requests/sec).

Twitter’s scaling challenge is not primarily due to tweet volume, but due to *fan-out*—each user follows many people, and each user is followed by many people

There are broadly two ways of implementing these two operations:
1. Posting a tweet simply inserts the new tweet into a global collection of tweets.

  When a user requests their home timeline, look up all the people they follow, find all the tweets for each of those users, and merge them (sorted by time)
  ex.
  ```sql
  SELECT tweets.*, users.* FROM tweets
    JOIN users ON tweets.sender_id = users.id
    JOIN follows ON follows.followee_id = users.id
    WHERE follows.follower_id = current_user
  ```

![Fig. 1-2](assets/fig.%201-2.png)

2. Maintain a cache for each user's home timeline

like a mailbox of tweets for each recipient user. when a user *posts a tweet*, look up all the people who follow that user, and insert the new tweet into each of their home timeline caches. the request to read the home timeline is then cheap, because its result has been computed ahead of time

![Fig. 1-3](assets/fig.%201-3.png)

The first version of Twitter used approach 1, but the systems struggled to keep up with the load of home timeline queries, so the company switched to approach 2.

This works better because the average rate of published tweets is almost two orders of magnitude lower than the rate of home timeline reads, and so in this case it’s preferable to do more work at write time and less at read time

However, the downside of approach 2 is that posting a tweet now requires a lot of extra work.

```
On average, a tweet is delivered to about 75 followers, so 4.6k tweets per second become 345k writes per second to the home timeline caches

But this average hides the fact that the number of followers per user varies wildly, and some users have over 30 million followers.

Doing this in a timely manner—Twitter tries to deliver tweets to followers within five seconds—is a significant challenge.
```

now that approach 2 is robustly implemented, Twitter is moving to a hybrid of both approaches

Most users’ tweets continue to be fanned out to home timelines at the time when they are posted, but a small number of users with a very large number of followers (i.e., celebrities) are excepted from this fan-out.

Tweets from any celebrities that a user may follow are fetched separately and merged with that user’s home timeline when it is read, like in approach 1

This hybrid approach is able to deliver consistently good performance.

#### Describing Performance

what happens when the load increases? You can look at it in two ways:
- When you increase a load parameter and keep the system resources (CPU, mem‐ ory, network bandwidth, etc.) unchanged, how is the performance of your system affected?
- When you increase a load parameter, how much do you need to increase the resources if you want to keep performance unchanged?

Both questions require performance numbers

In a batch processing system such as Hadoop, we usually care about *throughput*—the number of records we can process per second, or the total time it takes to run a job on a dataset of a certain size.

In online systems, what’s usually more important is the service’s *response time*—that is, the time between a client sending a request and receiving a response.

**Latency and response time**

Latency and response time are often used synonymously, but they are not the same. 
```
The response time is what the client sees: besides the actual time to process the request (the service time), it includes network delays and queueing delays.
Latency is the duration that a request is waiting to be handled—during which it is *latent*, awaiting service
```

In practice, in a system handling a variety of requests, the response time can vary a lot. We therefore need to think of response time not as a single number, but as a *distribution* of values that you can measure.

![Fig. 1-4](assets/fig.%201-4.png)

each gray bar represents a request to a service, and its height shows how long that request took.

there are occasional *outliers* that take much longer. perhaps the slow requests are intrinsically more expensive.
but even in a scenario where you'd think all requests should take the same time, you get variation:
- random additional latency chould be introduced by a context switch to background process
- the loss of a network packet and TCP retransmission
- a garbage collection pause
- a page fault forcing a read from disk
- mechanical vibration in the server rack
- or many other causes...

It’s common to see the *average* response time of a service reported. (it is usually understood as the *arithmetic mean*: given n values, add up all the values, and divide by n.)
However, the mean is **not** a very good metric if you want to know your “typical” response time, because it doesn’t tell you how many users actually experienced that delay

Usually it is better to use *percentiles*.
If you take your list of response times and sort it from fastest to slowest, then the *median* is the halfway point: for example, if median response time is 200 ms, that means half requests return in less than 200 ms, and half requests take longer than that.

This makes the *median* a good metric if you want to know how long users typically have to wait. (also known as the *50th percentile*, and sometimes abbreviated as *p50*)

In order to figure out **how bad your outliers are**, you can look at higher percentiles: the *95th*, *99th*, and *99.9th* percentiles are common (abbreviated *p95*, *p99*, and *p999*).

They are the response time thresholds at which 95%, 99%, or 99.9% of requests are faster than that particular threshold. For example, if the 95th percentile response time is 1.5 seconds, that means 95 out of 100 requests take less than 1.5 seconds, and 5 out of 100 requests take 1.5 seconds or more

High percentiles of response times, also known as *tail latencies*, are important because they directly affect users’ experience of the service.

```
For example, Amazon describes response time requirements for internal services in terms of the 99.9th percentile, even though it only affects 1 in 1,000 requests. This is because the customers with the slowest requests are often those who have the most data on their accounts because they have made many purchases—that is, *they’re the most valuable customers*

Amazon has also observed that a 100 ms increase in response time reduces sales by 1%.
others report that a 1-second slowdown reduces a customer satisfaction metric by 16%.
```

On the other hand, optimizing the 99.99th percentile (the slowest 1 in 10,000 requests) was deemed too expensive and to not yield enough benefit for Amazon’s purposes.
Reducing response times at very high percentiles is difficult because they are easily affected by random events outside of your control, and the benefits are diminishing.


For example, percentiles are often used in *service level objectives* (**SLOs**) and *service level agreements* (**SLAs**), contracts that define the expected performance and availability of a service

An SLA may state that the service is considered to be up if it has a median response time of less than 200 ms and a 99th percentile under 1 s (if the response time is longer, it might as well be down), and the service may be required to be up at least 99.9% of the time. These metrics set expectations for clients of the service and allow customers to demand a refund if the SLA is not met.

Queueing delays often account for a large part of the response time at high percen‐ tiles. As a server can only process a small number of things in parallel (limited, for example, by its number of CPU cores), it only takes a small number of slow requests to hold up the processing of subsequent requests—an effect sometimes known as *head-of-line blocking*.

Even if those subsequent requests are fast to process on the server, the client will see a slow overall response time due to the time waiting for the prior request to complete. Due to this effect, it is important to measure response times on the client side.

```
High percentiles become especially important in backend services that are called mul‐ tiple times as part of serving a single end-user request. Even if you make the calls in parallel, the end-user request still needs to wait for the slowest of the parallel calls to complete. It takes just one slow call to make the entire end-user request slow, as illus‐ trated in Figure 1-5. Even if only a small percentage of backend calls are slow, the chance of getting a slow call increases if an end-user request requires multiple backend calls, and so a higher proportion of end-user requests end up being slow (an effect known as *tail latency amplification*)

The naïve implementation is to keep a list of response times for all requests within the time window and to sort that list every minute. If that is too inefficient for you, there are algorithms that can calculate a good approximation of percentiles at minimal CPU and memory cost, such as forward decay, t-digest, or HdrHistogram.

the right way of aggregating response time data is to add the histograms 
```

![Fig.1-5](assets/fig.%201-5.png)

#### Appraoches for Coping with Load

An architecture that is appropriate for one level of load is unlikely to cope with 10 times that load.
People often talk of a dichotomy between *scaling up* (vertical scaling, moving to a more powerful machine) and *scaling out* (horizontal scaling, distributing the load across multiple smaller machines). Distributing load across multiple machines is also known as a *shared-nothing* architecture.

In reality, good architectures usually involve a pragmatic mixture of approaches: for example, using several fairly powerful machines can still be simpler and cheaper than a large number of small virtual machines.

While distributing stateless services across multiple machines is fairly straightforward, taking stateful data systems from a single node to a distributed setup can introduce a lot of additional complexity.
For this reason, common wisdom until recently was to keep your database on a single node (scale up) until scaling cost or high-availability requirements forced you to make it distributed.

The architecture of systems that operate at large scale is usually highly specific to the application—there is no such thing as a generic, one-size-fits-all scalable architecture.
For example, a system that is designed to handle 100,000 requests per second, each 1 kB in size, looks very different from a system that is designed for 3 requests per minute, each 2 GB in size—even though the two systems have the same data throughput.

### Maintainability

It is well known that the majority of the cost of software is not in its initial develop‐ ment, but in its ongoing maintenance—fixing bugs, keeping its systems operational, investigating failures, adapting it to new platforms, modifying it for new use cases, repaying technical debt, and adding new features.

three design principles for software systems:

***Operability***:

Make it easy for operations teams to keep the system running smoothly.

***Simplicity***

Make it easy for new engineers to understand the system, by removing as much complexity as possible from the system. (Note this is not the same as simplicity of the user interface.)

***Evolvability***

Make it easy for engineers to make changes to the system in the future, adapting it for unanticipated use cases as requirements change. Also known as *extensibility*, *modifiability*, or *plasticity*.

#### Operability: Making Life Easy for Operations

*“good operations can often work around the limitations of bad (or incomplete) software, but good software cannot run reliably with bad operations”*

Operations teams are vital to keeping a software system running smoothly. A good operations team typically is responsible for the following, and more:

- Monitoring the health of the system and quickly restoring service if it goes into a bad state
- Tracking down the cause of problems, such as system failures or degraded performance
- Keeping software and platforms up to date, including security patches
- Keeping tabs on how different systems affect each other, so that a problematic change can be avoided before it causes damage
- Anticipating future problems and solving them before they occur (e.g., capacity planning)
- Establishing good practices and tools for deployment, configuration management, and more
- Performing complex maintenance tasks, such as moving an application from one platform to another
- Maintaining the security of the system as configuration changes are made
- Defining processes that make operations predictable and help keep the production environment stable
- Preserving the organization’s knowledge about the system, even as individual people come and go

Good operability means making routine tasks easy, allowing the operations team to focus their efforts on high-value activities.
Data systems can do various things to make routine tasks easy, including:

- Providing visibility into the runtime behavior and internals of the system, with good monitoring
- Providing good support for automation and integration with standard tools
- Avoiding dependency on individual machines (allowing machines to be taken down for maintenance while the system as a whole continues running uninterrupted)
- Providing good documentation and an easy-to-understand operational model (“If I do X, Y will happen”)
- Providing good default behavior, but also giving administrators the freedom to override defaults when needed
- Self-healing where appropriate, but also giving administrators manual control over the system state when needed
- Exhibiting predictable behavior, minimizing surprises

#### Simplicity: Managing Complexity

There are various possible symptoms of complexity:
- explosion of the state space
- tight coupling of modules
- tangled dependencies
- inconsistent naming and terminology
- hacks aimed at solving performance problems
- special-casing to work around issues elsewhere

When complexity makes maintenance hard, budgets and schedules are often overrun

when the system is harder for developers to understand and reason about, hidden assumptions, unintended consequences, and unexpected interactions are more easily overlooked. Conversely, reducing complexity greatly improves the maintainability of software, and thus simplicity should be a key goal for the systems we build.

Making a system simpler does not necessarily mean reducing its functionality; it can also mean removing *accidental complexity*.

* *Moseley and Marks define complex‐ ity as accidental if it is not inherent in the problem that the software solves (as seen by the users) but arises only from the implementation.*

One of the best tools we have for removing accidental complexity is *abstraction*.

- A good abstraction can hide a great deal of implementation detail behind a clean, simple-to-understand façade.
- A good abstraction can also be used for a wide range of different applications.

Not only is this reuse more efficient than reimplementing a similar thing multiple times, but it also leads to higher-quality software, as quality improvements in the abstracted component benefit all applications that use it.

Examples:

- high-level programming languages are abstractions that hide machine code, CPU registers, and syscalls.
- SQL is an abstraction that hides complex on-disk and in-memory data structures, concurrent requests from other clients, and inconsis‐ tencies after crashes

we are still using machine code; we are just not using it *directly*, because the programming language abstraction saves us from having to think about it.

#### Evolvability: Making Change Easy

In terms of organizational processes, *Agile* working patterns provide a framework for adapting to change. The Agile community has also developed technical tools and patterns that are helpful when developing software in a frequently changing environment, such as test-driven development (TDD) and refactoring.

The ease with which you can modify a data system, and adapt it to changing requirements, is closely linked to its simplicity and its abstractions: simple and easy-to-understand systems are usually easier to modify than complex ones.

But since this is such an important idea, we will use a different word to refer to agility on a data sys‐ tem level: *evolvability*

### Summary

An application has to meet various requirements in order to be useful

There are *functional requirements* (what it should do, such as allowing data to be stored, retrieved, searched, and processed in various ways), and some *nonfunctional requirements* (general properties like security, reliability, compliance, scalability, compatibility, and maintainability)

*Reliability* means making systems work correctly, even when faults occur.

Faults can be in hardware (typically random and uncorrelated), software (bugs are typically sys‐ tematic and hard to deal with), and humans (who inevitably make mistakes from time to time).

*Scalability* means having strategies for keeping performance good, even when load increases.

In order to discuss scalability, we first need ways of describing load and performance quantitatively.  In a scalable system, you can add processing capacity in order to remain reliable under high load.

*Maintainability* has many facets, but in essence it’s about making life better for the engineering and operations teams who need to work with the system. 

- Good abstractions can help reduce complexity and make the system easier to modify and adapt for new use cases.
- Good operability means having good visibility into the system’s health, and having effective ways of managing it.
